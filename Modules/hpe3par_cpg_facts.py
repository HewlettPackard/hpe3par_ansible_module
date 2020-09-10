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
# with this program. If not, see <https://www.gnu.org/licenses/>

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = r'''
---
author: "Hewlett Packard Enterprise (ecostor@groups.ext.hpe.com)"
description:
  - "On HPE 3PAR and PRIMERA - Get CPG Facts"
module: hpe3par_cpg_facts
options:
  cpg_name:
    description:
      - "Name of the CPG."
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

short_description: "Manage HPE 3PAR and PRIMERA CPG"
version_added: "2.6"
'''


EXAMPLES = r'''
    - name: Get facts about all CPGs
      hpe3par_cpg_facts:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"

    - name: Get facts about a CPG by name
      hpe3par_cpg_facts:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"
        cpg_name="{{ cpg_name }}"
'''

RETURN = r'''
cpgs:
    description: The list of CPGs.
    returned: Always, but can be null.
    type: list
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from hpe3par_sdk import client
except ImportError:
    client = None

def convert_to_binary_multiple(size, size_unit):
    size_mib = 0
    if size_unit == 'GiB':
        size_mib = size * 1024
    elif size_unit == 'TiB':
        size_mib = size * 1048576
    elif size_unit == 'MiB':
        size_mib = size
    return int(size_mib)

def getUsageJson(usage):
    if not usage:
        return None

    usageInfo = dict()
    usageInfo['totalMiB'] = usage.total_MiB
    usageInfo['usedMiB']  = usage.used_MiB
    usageInfo['rawUsedMiB']  = usage.raw_used_MiB
    usageInfo['rawTotalMiB'] = usage.raw_total_MiB
    return usageInfo

def get_cpgs(client_obj, storage_system_username, storage_system_password, cpg_name):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            "Storage system username or password is null",
            {})

    try:
        client_obj.login(storage_system_username, storage_system_password)
        if cpg_name:
            if client_obj.cpgExists(cpg_name):
                cpg_obj_list = [client_obj.getCPG(cpg_name)]
            else:
                return (
                    False,
                    "cpg does not exists",
                    {})
        else:
            cpg_obj_list = client_obj.getCPGs()
    except Exception as e:
        return (False, "execution error | %s" % e, {})
    finally:
        client_obj.logout()

    cpg_json_list = []
    for currCpg in cpg_obj_list:
        jsonCpg = {}
        jsonCpg['id'] = currCpg.id
        jsonCpg['uuid'] = currCpg.uuid
        jsonCpg['name'] = currCpg.name
        jsonCpg['state'] = currCpg.state
        jsonCpg['domain'] = currCpg.domain
        jsonCpg['warningPct'] = currCpg.warning_pct
        jsonCpg['numTPVVs'] = currCpg.num_tpvvs
        jsonCpg['numFPVVs'] = currCpg.num_fpvvs
        jsonCpg['numTDVVs'] = currCpg.num_tdvvs
        jsonCpg['UsrUsage'] = getUsageJson(currCpg.usr_usage)
        jsonCpg['SAUsage'] = getUsageJson(currCpg.sausage)
        jsonCpg['SDUsage'] = getUsageJson(currCpg.sdusage)
        jsonCpg['failedStates'] = currCpg.failed_states
        jsonCpg['degradedStates'] = currCpg.degraded_states
        jsonCpg['additionalStates'] = currCpg.additional_states
        jsonCpg['dedupCapable'] = currCpg.dedup_capable
        jsonCpg['sharedSpaceMiB'] = currCpg.shared_space_MiB
        jsonCpg['freeSpaceMiB'] = currCpg.free_space_MiB
        jsonCpg['totalSpaceMiB'] = currCpg.total_space_MiB
        jsonCpg['rawSharedSpaceMiB'] = currCpg.raw_shared_space_MiB
        jsonCpg['rawFreeSpaceMiB'] = currCpg.raw_free_space_MiB
        jsonCpg['rawTotalSpaceMiB'] = currCpg.raw_total_space_MiB
        jsonCpg['tdvvVersion'] = currCpg.tdvv_version
        jsonCpg['ddsRsvdMiB'] = currCpg.dds_rsvd_MiB
        cpg_json_list.append(jsonCpg)

    ansible_facts = {}
    ansible_facts['cpgs'] = cpg_json_list
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
        "cpg_name": {
            "type": "str"
        }
    }

    module = AnsibleModule(argument_spec=fields)

    if client is None:
        module.fail_json(msg='the python hpe3par_sdk module is required')

    storage_system_ip = module.params["storage_system_ip"]
    storage_system_username = module.params["storage_system_username"]
    storage_system_password = module.params["storage_system_password"]
    cpg_name = module.params["cpg_name"]

    port_number = client.HPE3ParClient.getPortNumber(
        storage_system_ip, storage_system_username, storage_system_password)
    wsapi_url = 'https://%s:%s/api/v1' % (storage_system_ip, port_number)
    client_obj = client.HPE3ParClient(wsapi_url)

    return_status, msg, ansible_facts = get_cpgs(
            client_obj, storage_system_username, storage_system_password,
            cpg_name)

    if return_status:
        module.exit_json(changed=False, ansible_facts=ansible_facts)
    else:
        module.fail_json(msg=msg)


if __name__ == '__main__':
    main()
