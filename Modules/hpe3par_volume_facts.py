#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Avinash Jalumuru <avinash.jalumuru@hpe.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: hpe3par_volume_facts
short_description: Gather facts of the HPE3PAR Storage volumes
description:
    - This module gather facts about volume(s) of the 3PAR storage array.
version_added: 0.1
author:
    - Avinash Jalumuru
notes:
    - Tested on HPE 3PAR 7200 (3.2.2)
requirements:
  - "3PAR OS - 3.2.2 MU6, 3.3.1 MU1"
  - "Ansible - 2.4"
  - "hpe3par_sdk 1.0.0"
  - "WSAPI service should be enabled on the 3PAR storage array."
options:
   name:
     description:
     - Name of the matching volume
     - If set, facts of specific volume is returned.
     required: False
'''

EXAMPLES = """
    - name: Gather facts of 3PAR volume with name 'existing-volume'
      hpe3par_volume_facts:
        api_url: rest_api_url
        username: 3par_username
        password: 3par_password
        name: existing-volume
        register: facts

    - name: Gather facts of the available 3PAR volume
      hpe3par_volume_facts:
        api_url: rest_api_url
        username: 3par_username
        password: 3par_password
        register: facts
"""

RETURN = """
volumes:
    description: returns the array of 3PAR volumes
    type: list
count:
    description: Number of Virtual Volumes
    returned: always
    type: int
"""

from ansible.module_utils.basic import AnsibleModule

try:
    from hpe3parclient.client import HPE3ParClient
    from hpe3parclient.exceptions import HTTPNotFound
except ImportError:
    HPE3ParClient = None

try:
    from hpe3par_sdk import client
except ImportError:
    client = None

provisionType = {
        1: 'full',
        2: 'tpvv',
        3: 'snp',
        4: 'peer',
        5: 'unknown',
        6: 'tdvv',
        7: 'dds'
    }

def getPolicyJson(policy):
    if not policy:
        return None

    virtual_policy = dict()
    virtual_policy['staleSS'] = policy.stale_ss
    virtual_policy['oneHost'] = policy.one_host
    virtual_policy['zeroDetect'] = policy.zero_detect
    virtual_policy['system'] = policy.system
    virtual_policy['caching'] = policy.caching
    virtual_policy['fsvc'] = policy.fsvc
    virtual_policy['hostDIF'] = policy.host_dif

    return virtual_policy

def getCapEfficiencyJson(cap):
    if not cap:
        return None

    virtual_cap = dict()
    virtual_cap['compaction'] = cap.compaction
    virtual_cap['compression'] = cap.compression
    virtual_cap['dataReduction'] = cap.data_reduction
    virtual_cap['overProvisioning'] = cap.over_provisioning
    virtual_cap['deduplication'] = cap.deduplication

    return virtual_cap

def getSpaceJson(space):
    if not space:
        return None

    virtual_space = dict()
    virtual_space['reservedMiB'] = space.reserved_MiB
    virtual_space['rawReservedMiB'] = space.raw_reserved_MiB
    virtual_space['usedMiB'] = space.used_MiB
    virtual_space['freeMiB'] = space.free_MiB
    return virtual_space

def getVolumeInfo(volume):
    if not volume:
        return None

    volumes = dict()

    volumes['additionalStates'] = volume.additional_states
    volumes['adminSpace'] = getSpaceJson(volume.admin_space)
    volumes['baseId'] = volume.base_id
    volumes['comment'] = volume.comment
    volumes['capacityEfficiency'] = getCapEfficiencyJson(volume.capacity_efficiency)
    volumes['copyOf'] = volume.copy_of
    volumes['copyType'] = volume.copy_type
    volumes['creationTime8601'] = volume.creation_time8601
    volumes['creationTimeSec'] = volume.creation_time_sec
    volumes['degradedStates'] = volume.degraded_states
    volumes['domain'] = volume.domain
    volumes['expirationTime8601'] = volume.expiration_time8601
    volumes['expirationTimeSec'] = volume.expiration_time_sec
    volumes['failedStates'] = volume.failed_states
    volumes['compressionState'] = volume.compression_state
    volumes['deduplicationState'] = volume.deduplication_state
    volumes['id'] = volume.id
    volumes['links'] = volume.links
    volumes['name'] = volume.name
    volumes['parentId'] = volume.parent_id
    volumes['physParentId'] = volume.phys_parent_id
    volumes['policies'] = getPolicyJson(volume.policies)
    volumes['provisioningType'] = provisionType.get(volume.provisioning_type)
    volumes['readOnly'] = volume.read_only
    volumes['retentionTime8601'] = volume.retention_time8601
    volumes['retentionTimeSec'] = volume.retention_time_sec
    volumes['roChildId'] = volume.ro_child_id
    volumes['rwChildId'] = volume.rw_child_id
    volumes['hostWriteMiB'] = volume.host_write_mib
    volumes['totalUsedMiB'] = volume.total_used_mib
    volumes['totalReservedMiB'] = volume.total_reserved_mib
    volumes['sizeMiB'] = volume.size_mib
    volumes['snapCPG'] = volume.snap_cpg
    volumes['snapshotSpace'] = getSpaceJson(volume.snapshot_space)
    volumes['ssSpcAllocLimitPct'] = volume.ss_spc_alloc_limit_pct
    volumes['ssSpcAllocWarningPct'] = volume.ss_spc_alloc_warning_pct
    volumes['state'] = volume.state
    volumes['userCPG'] = volume.user_cpg
    volumes['userSpace'] = getSpaceJson(volume.user_space)
    volumes['usrSpcAllocLimitPct'] = volume.usr_spc_alloc_limit_pct
    volumes['usrSpcAllocWarningPct'] = volume.usr_spc_alloc_warning_pct
    volumes['uuid'] = volume.uuid
    volumes['sharedParentID'] = volume.shared_parent_id
    volumes['udid'] = volume.udid
    volumes['wwn'] = volume.wwn
    return volumes

def main():

    argument_spec = {
        "storage_system_ip":       { "required": True, "type": "str"},
        "storage_system_username": { "required": True, "type": "str", "no_log": True},
        "storage_system_password": { "required": True, "type": "str", "no_log": True},
        "name":                    { "required": False, "type": "str"}
    }

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    if client is None:
        module.fail_json(msg='the python hpe3par_sdk module is required')
    if HPE3ParClient is None:
        module.fail_json(msg='the python python-3parclient module is required')

    storage_system_ip = module.params["storage_system_ip"]
    storage_system_username = module.params["storage_system_username"]
    storage_system_password = module.params["storage_system_password"]

    wsapi_url = 'https://%s:8080/api/v1' % storage_system_ip
    client_obj = client.HPE3ParClient(wsapi_url)
    client_obj.login(storage_system_username, storage_system_password)

    try:

        result = dict()
        result['changed'] = False

        count = 0
        volumes = list()

        name = module.params.get('name')
        if not name:
            dbVolumes = client_obj.getVolumes()
            for volume in dbVolumes:
               volumes.extend([getVolumeInfo(volume)])
               count += 1
        else:
            try:
               dbVolumes = client_obj.getVolume(name)
               volumes = [getVolumeInfo(dbVolumes)]
               count = 1
            except HTTPNotFound as e:
               count = 0

        result['volumes'] = volumes
        result['count'] = count

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=str(e))
    finally:
        client_obj.logout()

if __name__ == '__main__':
    main()
