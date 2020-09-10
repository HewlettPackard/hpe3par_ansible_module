#!/usr/bin/python

# (C) Copyright 2018 Hewlett Packard Enterprise Development LP
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of version 3 of the GNU General Public License as
# published by the Free Software Foundation.  Alternatively, at your
# choice, you may also redistribute it and/or modify it under the terms
# of the Apache License, version 2.0, available at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <https://www.gnu.org/licenses/>

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = r'''
---
author: "Hewlett Packard Enterprise (ecostor@groups.ext.hpe.com)"
description: "On HPE 3PAR and PRIMERA - Get Volume Facts"
module: hpe3par_volume_facts
options:
  volume_name:
    description:
      - "Name of the Volume."
    required: true
  storage_system_ip:
    description:
      - "The storage system IP address."
    required: true
  storage_system_password:
    description:
      - "The storage system password."
    required: true
  storage_system_username:
    description:
      - "The storage system user name."
    required: true

requirements:
  - "3PAR OS - 3.2.2 MU6, 3.3.1 MU1"
  - "Ansible - 2.4"
  - "hpe3par_sdk 1.0.0"
  - "WSAPI service should be enabled on the 3PAR and PRIMERA storage array."
short_description: "Manage HPE 3PAR and PRIMERA volume"
version_added: "2.4"
'''

EXAMPLES = r'''
    - name: Get facts about all volumes"
      hpe3par_volume_facts:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"
        state=present
        volume_name="{{ volume_name }}"

    - name: Get facts about a volume by name"
      hpe3par_volume_facts:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"
        state=modify
        volume_name="{{ volume_name }}"
'''

RETURN = r'''
volumes:
    description: The list of volumes.
    returned: Always, but can be null.
    type: list
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from hpe3parclient.client import HPE3ParClient
except ImportError:
    HPE3ParClient = None
try:
    from hpe3par_sdk import client
except ImportError:
    client = None

def getCapacityJson(capacity):
    if not capacity:
        return None

    capacityInfo = dict()
    capacityInfo['compaction'] = capacity.compaction
    capacityInfo['compression']  = capacity.compression
    capacityInfo['data_reduction']  = capacity.data_reduction
    capacityInfo['deduplication'] = capacity.deduplication
    capacityInfo['over_provisioning'] = capacity.over_provisioning
    return capacityInfo

def getSpaceJson(space):
    if not space:
        return None

    spaceInfo = dict()
    spaceInfo['free_MiB'] = space.free_MiB
    spaceInfo['raw_reserved_MiB']  = space.raw_reserved_MiB
    spaceInfo['reserved_MiB']  = space.reserved_MiB
    spaceInfo['used_MiB'] = space.used_MiB
    return spaceInfo

def getPolicyJson(policy):
    if not policy:
        return None

    policyInfo = dict()
    policyInfo['caching'] = policy.caching
    policyInfo['fsvc']  = policy.fsvc
    policyInfo['host_dif']  = policy.host_dif
    policyInfo['one_host'] = policy.one_host
    policyInfo['stale_ss'] = policy.stale_ss
    policyInfo['system'] = policy.system
    policyInfo['zero_detect'] = policy.zero_detect
    return policyInfo

def get_volumes(client_obj, storage_system_username, storage_system_password, volume_name):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            "Storage system username or password is null",
            {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if volume_name:
            if client_obj.volumeExists(volume_name):
                volume_obj_list = [client_obj.getVolume(volume_name)]
            else:
                return (
                    False,
                    "volume does not exists",
                    {})
        else:
            volume_obj_list = client_obj.getVolumes()
    except Exception as e:
        return (False, "execution error | %s" % e, {})
    finally:
        client_obj.logout()

    volume_json_list = []
    for currVolume in volume_obj_list:
        jsonVolume = {}
        jsonVolume['id'] = currVolume.id
        jsonVolume['uuid'] = currVolume.uuid
        jsonVolume['wwn'] = currVolume.wwn
        jsonVolume['name'] = currVolume.name
        jsonVolume['additional_states'] = currVolume.additional_states
        jsonVolume['admin_space'] = getSpaceJson(currVolume.admin_space)
        jsonVolume['base_id'] = currVolume.base_id
        jsonVolume['capacity_efficiency'] = getCapacityJson(currVolume.capacity_efficiency)
        jsonVolume['comment'] = currVolume.comment
        jsonVolume['compression_state'] = currVolume.compression_state
        jsonVolume['copy_of'] = currVolume.copy_of
        jsonVolume['copy_type'] = currVolume.copy_type
        jsonVolume['creation_time8601'] = currVolume.creation_time8601
        jsonVolume['creation_time_sec'] = currVolume.creation_time_sec
        jsonVolume['deduplication_state'] = currVolume.deduplication_state
        jsonVolume['domain'] = currVolume.domain
        jsonVolume['expiration_time8601'] = currVolume.expiration_time8601
        jsonVolume['expiration_time_sec'] = currVolume.expiration_time_sec
        jsonVolume['failed_states'] = currVolume.failed_states
        jsonVolume['host_write_mib'] = currVolume.host_write_mib
        jsonVolume['links'] = currVolume.links
        jsonVolume['parent_id'] = currVolume.parent_id
        jsonVolume['phys_parent_id'] = currVolume.phys_parent_id
        jsonVolume['policies'] = getPolicyJson(currVolume.policies)
        jsonVolume['provisioning_type'] = currVolume.provisioning_type
        jsonVolume['read_only'] = currVolume.read_only
        jsonVolume['retention_time8601'] = currVolume.retention_time8601
        jsonVolume['retention_time_sec'] = currVolume.retention_time_sec
        jsonVolume['ro_child_id'] = currVolume.ro_child_id
        jsonVolume['rw_child_id'] = currVolume.rw_child_id
        jsonVolume['shared_parent_id'] = currVolume.shared_parent_id
        jsonVolume['size_mib'] = currVolume.size_mib
        jsonVolume['snap_cpg'] = currVolume.snap_cpg
        jsonVolume['snapshot_space'] = getSpaceJson(currVolume.snapshot_space)
        jsonVolume['ss_spc_alloc_limit_pct'] = currVolume.ss_spc_alloc_limit_pct
        jsonVolume['ss_spc_alloc_warning_pct'] = currVolume.ss_spc_alloc_warning_pct
        jsonVolume['state'] = currVolume.state
        jsonVolume['total_reserved_mib'] = currVolume.total_reserved_mib
        jsonVolume['total_used_mib'] = currVolume.total_used_mib
        jsonVolume['udid'] = currVolume.udid
        jsonVolume['user_cpg'] = currVolume.user_cpg
        jsonVolume['user_space'] = getSpaceJson(currVolume.user_space)
        jsonVolume['usr_spc_alloc_limit_pct'] = currVolume.usr_spc_alloc_limit_pct
        jsonVolume['usr_spc_alloc_warning_pct'] = currVolume.usr_spc_alloc_warning_pct
        volume_json_list.append(jsonVolume)

    ansible_facts = {}
    ansible_facts['volumes'] = volume_json_list
    return (True, "", ansible_facts)


def main():
    fields = {
        "storage_system_ip": {
            "required": True,
            "type": "str"
        },
        "storage_system_username": {
            "required": True,
            "type": "str",
            "no_log": True
        },
        "storage_system_password": {
            "required": True,
            "type": "str",
            "no_log": True
        },
        "volume_name": {
            "type": "str"
        },
    }

    module = AnsibleModule(argument_spec=fields)

    if client is None:
        module.fail_json(msg='the python hpe3par_sdk module is required')

    ansible_facts = {}

    storage_system_ip = module.params["storage_system_ip"]
    storage_system_username = module.params["storage_system_username"]
    storage_system_password = module.params["storage_system_password"]
    volume_name = module.params["volume_name"]

    port_number = client.HPE3ParClient.getPortNumber(
        storage_system_ip, storage_system_username, storage_system_password)
    wsapi_url = 'https://%s:%s/api/v1' % (storage_system_ip, port_number)
    client_obj = client.HPE3ParClient(wsapi_url)

    return_status, msg, ansible_facts = get_volumes(
            client_obj, storage_system_username, storage_system_password,
            volume_name)

    if return_status:
        module.exit_json(changed=False, ansible_facts=ansible_facts)
    else:
        module.fail_json(msg=msg)


if __name__ == '__main__':
    main()
