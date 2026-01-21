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
module: hpe3par_cpg_facts
short_description: Gather facts of the HPE3PAR CPGs
description:
    - This module gather facts about cpg(s) of the 3PAR storage array.
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
     - Name of the matching cpg
     - If set, facts of specific cpg are returned.
     required: False
'''

EXAMPLES = """
    - name: Gather facts of 3PAR cpg with name 'existing-cpg'
      hpe3par_cpg_facts:
        storage_system_ip: rest_api_url
        storage_system_username: 3par_username
        storage_system_password: 3par_password
        name: existing-cpg
        register: facts

    - name: Gather facts of the available 3PAR cpg
      hpe3par_cpg_facts:
        storage_system_ip: rest_api_url
        storage_system_username: 3par_username
        storage_system_password: 3par_password
        register: facts
"""

RETURN = """
cpgs:
    description: returns the array of 3PAR cpg(s)
    type: list
count:
    description: Number of CPGs
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

def getPrivateSpaceJson(privateSpace):
    if not privateSpace:
        return None

    privateSpaceJson = dict()
    privateSpaceJson['base'] = privateSpace.base
    privateSpaceJson['rawBase']  = privateSpace.raw_base
    privateSpaceJson['snapshot'] = privateSpace.snapshot
    privateSpaceJson['rawSnapshot'] = privateSpace.raw_snapshot

    return privateSpaceJson

def getLDLayoutJson(layout):
    if not layout:
        return None

    layoutJson = dict()
    layoutJson['RAIDType'] = layout.raidtype
    layoutJson['setSize']  = layout.set_size
    layoutJson['HA'] = layout.ha
    layoutJson['chunkletPosPref'] = layout.chunklet_pos_pref

def getGrowthParamJson(growthParams):
    if not growthParams:
        return None

    growthParamJson = dict()
    growthParamJson['warningMiB']   = growthParams.warning_MiB
    growthParamJson['incrementMiB'] = growthParams.increment_MiB
    growthParamJson['limitMiB'] = growthParams.limit_MiB
    growthParamJson['LDLayout'] = getLDLayoutJson(growthParams.ld_layout)

    return growthParamJson

def getUsageJson(usage):
    if not usage:
        return None

    usageInfo = dict()
    usageInfo['totalMiB'] = usage.total_MiB
    usageInfo['usedMiB']  = usage.used_MiB
    usageInfo['rawUsedMiB']  = usage.raw_used_MiB
    usageInfo['rawTotalMiB'] = usage.raw_total_MiB
    return usageInfo

def getCPGInfo(cpg):

    if not cpg:
        return None

    cpgInfo = dict()

    cpgInfo['id']                = cpg.id
    cpgInfo['uuid']              = cpg.uuid
    cpgInfo['name']              = cpg.name
    cpgInfo['state']             = cpg.state
    cpgInfo['domain']            = cpg.domain
    cpgInfo['warningPct']        = cpg.warning_pct
    cpgInfo['numTPVVs']          = cpg.num_tpvvs
    cpgInfo['numFPVVs']          = cpg.num_fpvvs
    cpgInfo['numTDVVs']          = cpg.num_tdvvs
    cpgInfo['UsrUsage']          = getUsageJson(cpg.usr_usage)
    cpgInfo['SAUsage']           = getUsageJson(cpg.sausage)
    cpgInfo['SDUsage']           = getUsageJson(cpg.sdusage)
    cpgInfo['failedStates']      = cpg.failed_states
    cpgInfo['degradedStates']    = cpg.degraded_states
    cpgInfo['additionalStates']  = cpg.additional_states
    cpgInfo['dedupCapable']      = cpg.dedup_capable
    cpgInfo['sharedSpaceMiB']    = cpg.shared_space_MiB
    cpgInfo['freeSpaceMiB']      = cpg.free_space_MiB
    cpgInfo['totalSpaceMiB']     = cpg.total_space_MiB
    cpgInfo['rawSharedSpaceMiB'] = cpg.raw_shared_space_MiB
    cpgInfo['rawFreeSpaceMiB']   = cpg.raw_free_space_MiB
    cpgInfo['rawTotalSpaceMiB']  = cpg.raw_total_space_MiB
    cpgInfo['tdvvVersion']       = cpg.tdvv_version
    cpgInfo['ddsRsvdMiB']        = cpg.dds_rsvd_MiB

    return cpgInfo

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
        cpgs = list()

        name = module.params.get('name')
        if not name:
            dbCPGs = client_obj.getCPGs()
            for cpg in dbCPGs:
               cpgs.extend([getCPGInfo(cpg)])
               count += 1
        else:
            try:
               dbCPG = client_obj.getCPG(name)
               cpg = [getCPGInfo(dbCPG)]
               count = 1
            except HTTPNotFound as e:
               count = 0

        result['cpgs'] = cpgs
        result['count'] = count

        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=str(e))
    finally:
        client_obj.logout()

if __name__ == '__main__':
    main()
