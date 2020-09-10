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
description: "On HPE 3PAR and PRIMERA - Get Host Facts"
module: hpe3par_host_facts
options:
  host_name:
    description:
      - "Name of the Host."
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
short_description: "Manage HPE 3PAR and PRIMERA Host"
version_added: "2.4"
'''

EXAMPLES = r'''
    - name: Get facts about all hosts"
      hpe3par_host_facts:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"
        state=present
        host_name="{{ host_name }}"

    - name: Get facts about an hosts by name"
      hpe3par_host_facts:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"
        state=modify
        host_name="{{ host_name }}"
'''

RETURN = r'''
hosts:
    description: The list of hosts.
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

def get_hosts (client_obj, storage_system_username, storage_system_password, host_name):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            "Storage system username or password is null",
            {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if host_name:
            if client_obj.hostExists(host_name):
                host_obj_list = [client_obj.getHost(host_name)]
            else:
                return (
                    False,
                    "host does not exists",
                    {})
        else:
            host_obj_list = client_obj.getHosts()
    except Exception as e:
        return (False, "execution error | %s" % e, {})
    finally:
        client_obj.logout()

    host_json_list = []
    for currHost in host_obj_list:
        jsonHost = {}
        jsonHost['id'] = currHost.id
        jsonHost['name'] = currHost.name
        jsonHost['persona'] = currHost.persona
        jsonHost['domain'] = currHost.domain
        jsonHost['fcpaths'] = []
        for currFCPath in currHost.fcpaths:
            jsonFCPath = {}
            jsonFCPath['driver_version'] = currFCPath.driver_version
            jsonFCPath['firmware_version'] = currFCPath.firmware_version
            jsonFCPath['host_speed'] = currFCPath.host_speed
            jsonFCPath['model'] = currFCPath.model
            jsonFCPath['vendor'] = currFCPath.vendor
            jsonFCPath['wwn'] = currFCPath.wwn
            jsonHost['fcpaths'].append(jsonFCPath)
        jsonHost['initiator_chap_enabled'] = currHost.initiator_chap_enabled
        jsonHost['initiator_chap_name'] = currHost.initiator_chap_name
        jsonHost['initiator_encrypted_chap_secret'] = currHost.initiator_encrypted_chap_secret
        jsonHost['iscsi_paths'] = currHost.iscsi_paths
        jsonHost['target_chap_enabled'] = currHost.target_chap_enabled
        jsonHost['target_chap_name'] = currHost.target_chap_name
        jsonHost['target_encrypted_chap_secret'] = currHost.target_encrypted_chap_secret
        host_json_list.append(jsonHost)

    ansible_facts = {}
    ansible_facts['hosts'] = host_json_list
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
        "host_name": {
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
    host_name = module.params["host_name"]

    port_number = client.HPE3ParClient.getPortNumber(
        storage_system_ip, storage_system_username, storage_system_password)
    wsapi_url = 'https://%s:%s/api/v1' % (storage_system_ip, port_number)
    client_obj = client.HPE3ParClient(wsapi_url)

    return_status, msg, ansible_facts = get_hosts(
            client_obj, storage_system_username, storage_system_password,
            host_name)

    if return_status:
        module.exit_json(changed=False, ansible_facts=ansible_facts)
    else:
        module.fail_json(msg=msg)


if __name__ == '__main__':
    main()
