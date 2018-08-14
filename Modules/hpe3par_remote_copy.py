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

########################################################
#                                                      #
#       TODO: Placeholder for documentation            #
#                                                      #
########################################################

from ansible.module_utils.basic import AnsibleModule
try:
    from hpe3par_sdk import client
except ImportError:
    client = None

def create_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            domain,
            targets,
            local_user_cpg,
            local_snap_cpg
            ):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Remote Copy Group create failed. Storage system username or password is null",
            {})
    if remote_copy_group_name is None:
        return (False, False, "Remote Copy Group create failed. Remote Copy Group name is null", {})
    if len(remote_copy_group_name) < 1 or len(remote_copy_group_name) > 31:
        return (False, False, "Remote Copy Group create failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {})
    if (not local_user_cpg and local_snap_cpg) or (local_user_cpg and not local_snap_cpg):
        return (False, False, "Either both local_user_cpg and local_snap_cpg must be present, or none of them must be present", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if not client_obj.remoteCopyGroupExists(remote_copy_group_name):
            optional = {
                'domain': domain,
                'localUserCPG': local_user_cpg,
                'localSnapCPG': local_snap_cpg
            }
            client_obj.createRemoteCopyGroup(remote_copy_group_name, targets, optional)
        else:
            return (True, False, "Remote Copy Group already present", {})
    except Exception as e:
        return (False, False, "Remote Copy Group creation failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Created Remote Copy Group %s successfully." % remote_copy_group_name, {})


def delete_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            keep_snap
            ):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Remote Copy Group delete failed. Storage system username or password is null",
            {})
    if remote_copy_group_name is None:
        return (False, False, "Remote Copy Group delete failed. Remote Copy Group name is null", {})
    if len(remote_copy_group_name) < 1 or len(remote_copy_group_name) > 31:
        return (False, False, "Remote Copy Group delete failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if client_obj.remoteCopyGroupExists(remote_copy_group_name):
            client_obj.removeRemoteCopyGroup(remote_copy_group_name, keep_snap)
        else:
            return (True, False, "Remote Copy Group not present", {})
    except Exception as e:
        return (False, False, "Remote Copy Group delete failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Deleted Remote Copy Group %s successfully." % remote_copy_group_name, {})

def main():
    fields = {
        "state": {
            "required": True,
            "choices": ['present', 'absent'],
            "type": 'str'
        },
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
        "remote_copy_group_name": {
            "required": True,
            "type": "str"
        },
        "domain": {
            "type": "str"
        },
        "targets": {
            "type": "list"
        },
        "local_user_cpg": {
            "type": "string"
        },
        "local_snap_cpg": {
            "type": "string"
        },
        "keep_snap": {
            "type": "bool",
            "default": False
        }
    }
    module = AnsibleModule(argument_spec=fields)

    if client is None:
        module.fail_json(msg='the python hpe3par_sdk module is required')

    storage_system_ip = module.params["storage_system_ip"]
    storage_system_username = module.params["storage_system_username"]
    storage_system_password = module.params["storage_system_password"]
    remote_copy_group_name = module.params["remote_copy_group_name"]
    domain = module.params["domain"]
    targets = module.params["targets"]
    local_user_cpg = module.params["local_user_cpg"]
    local_snap_cpg = module.params["local_snap_cpg"]
    keep_snap = module.params["keep_snap"]

    wsapi_url = 'https://%s:8080/api/v1' % storage_system_ip
    client_obj = client.HPE3ParClient(wsapi_url)

    # States
    if module.params["state"] == "present":
        return_status, changed, msg, issue_attr_dict = create_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            domain,
            targets,
            local_user_cpg,
            local_snap_cpg
        )
    if module.params["state"] == "absent":
        return_status, changed, msg, issue_attr_dict = delete_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            keep_snap
        )

    if return_status:
        if issue_attr_dict:
            module.exit_json(changed=changed, msg=msg, issue=issue_attr_dict)
        else:
            module.exit_json(changed=changed, msg=msg)
    else:
        module.fail_json(msg=msg)


if __name__ == '__main__':
    main()
