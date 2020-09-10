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
author: "Hewlett Packard Enterprise (ecostor@groups.ext.hpe.com )"
description: "On HPE 3PAR and PRIMERA - Get HostSet Facts"
module: hpe3par_hostset_facts
options:
  hostset_name:
    description:
      - "Name of the host set."
    required: false
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
short_description: "Manage HPE 3PAR and PRIMERA Host Set"
version_added: "2.4"
'''

EXAMPLES = r'''
    - name: Get facts about all hostsets
      hpe3par_hostset_facts:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"
        state=present
        hostset_name="{{ hostset_name }}"
        setmembers="{{ add_host_setmembers }}"

    - name: Get facts about an hostset by name
      hpe3par_hostset_facts:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"
        state=add_hosts
        hostset_name="{{ hostset_name }}"
        setmembers="{{ add_host_setmembers2 }}"
'''

RETURN = r'''
hostsets:
    description: The list of hostsets.
    returned: Always, but can be null.
    type: list
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from hpe3par_sdk import client
except ImportError:
    client = None

def get_hostsets (client_obj, storage_system_username, storage_system_password, hostset_name):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            "Storage system username or password is null",
            {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if hostset_name:
            if client_obj.hostSetExists(hostset_name):
                hostset_obj_list = [client_obj.getHostSet(hostset_name)]
            else:
                return (
                    False,
                    "hostset does not exists",
                    {})
        else:
            hostset_obj_list = client_obj.getHostSets()
    except Exception as e:
        return (False, "execution error | %s" % e, {})
    finally:
        client_obj.logout()

    hostset_json_list = []
    for currHostSet in hostset_obj_list:
        jsonHostSet = {}
        jsonHostSet['id'] = currHostSet.id
        jsonHostSet['uuid'] = currHostSet.uuid
        jsonHostSet['name'] = currHostSet.name
        jsonHostSet['domain'] = currHostSet.domain
        jsonHostSet['comment'] = currHostSet.comment
        jsonHostSet['setmembers'] = currHostSet.setmembers
        hostset_json_list.append(jsonHostSet)

    ansible_facts = {}
    ansible_facts['hostsets'] = hostset_json_list
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
        "hostset_name": {
            "type": "str"
        },
    }
    module = AnsibleModule(argument_spec=fields)

    if client is None:
        module.fail_json(msg='the python hpe3par_sdk module is required')

    storage_system_ip = module.params["storage_system_ip"]
    storage_system_username = module.params["storage_system_username"]
    storage_system_password = module.params["storage_system_password"]
    hostset_name = module.params["hostset_name"]

    port_number = client.HPE3ParClient.getPortNumber(
        storage_system_ip, storage_system_username, storage_system_password)
    wsapi_url = 'https://%s:%s/api/v1' % (storage_system_ip, port_number)
    client_obj = client.HPE3ParClient(wsapi_url)

    return_status, msg, ansible_facts = get_hostsets(
            client_obj, storage_system_username, storage_system_password,
            hostset_name)

    if return_status:
        module.exit_json(changed=False, ansible_facts=ansible_facts)
    else:
        module.fail_json(msg=msg)

if __name__ == '__main__':
    main()
