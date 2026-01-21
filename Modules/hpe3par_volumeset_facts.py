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
description: "On HPE 3PAR and PRIMERA - Get Volume Set Facts"
module: hpe3par_volumeset_facts
options:
  volumeset_name:
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
      hpe3par_volumeset_facts:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"
        state=present
        volumeset_name="{{ volumeset_name }}"

    - name: Get facts about a volume by name"
      hpe3par_volumeset_facts:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"
        state=modify
        volumeset_name="{{ volumeset_name }}"
'''

RETURN = r'''
volume_sets:
    description: The list of volume sets.
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


def get_volumesets(client_obj, storage_system_username, storage_system_password, volumeset_name):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            "Storage system username or password is null",
            {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if volumeset_name:
            if client_obj.volumeSetExists(volumeset_name):
                volumeset_obj_list = [client_obj.getVolumeSet(volumeset_name)]
            else:
                return (
                    False,
                    "volume set does not exists",
                    {})
        else:
            volumeset_obj_list = client_obj.getVolumeSets()
    except Exception as e:
        return (False, "execution error | %s" % e, {})
    finally:
        client_obj.logout()

    volumeset_json_list = []
    for currVolumeSet in volumeset_obj_list:
        jsonVolumeSet = {}
        jsonVolumeSet['id'] = currVolumeSet.id
        jsonVolumeSet['uuid'] = currVolumeSet.uuid
        jsonVolumeSet['name'] = currVolumeSet.name
        jsonVolumeSet['comment'] = currVolumeSet.comment
        jsonVolumeSet['domain'] = currVolumeSet.domain
        jsonVolumeSet['flash_cache_policy'] = currVolumeSet.flash_cache_policy
        jsonVolumeSet['qos_enabled'] = currVolumeSet.qos_enabled
        jsonVolumeSet['setmembers'] = currVolumeSet.setmembers
        volumeset_json_list.append(jsonVolumeSet)

    ansible_facts = {}
    ansible_facts['volume_sets'] = volumeset_json_list
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
        "volumeset_name": {
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
    volumeset_name = module.params["volumeset_name"]

    port_number = client.HPE3ParClient.getPortNumber(
        storage_system_ip, storage_system_username, storage_system_password)
    wsapi_url = 'https://%s:%s/api/v1' % (storage_system_ip, port_number)
    client_obj = client.HPE3ParClient(wsapi_url)

    return_status, msg, ansible_facts = get_volumesets(
            client_obj, storage_system_username, storage_system_password,
            volumeset_name)

    if return_status:
        module.exit_json(changed=False, ansible_facts=ansible_facts)
    else:
        module.fail_json(msg=msg)


if __name__ == '__main__':
    main()
