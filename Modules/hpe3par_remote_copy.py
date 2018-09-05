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

def modify_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            local_user_cpg,
            local_snap_cpg,
            targets,
            unset_user_cpg,
            unset_snap_cpg
            ):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Remote Copy Group modify failed. Storage system username or password is null",
            {})
    if remote_copy_group_name is None:
        return (False, False, "Remote Copy Group modify failed. Remote Copy Group name is null", {})

    if len(remote_copy_group_name) < 1 or len(remote_copy_group_name) > 31:
        return (False, False, "Remote Copy Group modify failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if client_obj.remoteCopyGroupExists(remote_copy_group_name):
            optional = {
                'localUserCPG': local_user_cpg,
                'localSnapCPG': local_snap_cpg,
                'targets': targets,
                'unsetUserCPG': unset_user_cpg,
                'unsetSnapCPG': unset_snap_cpg
            }
            client_obj.modifyRemoteCopyGroup(remote_copy_group_name, optional)
        else:
            return (True, False, "Remote Copy Group not present", {})
    except Exception as e:
        return (False, False, "Remote Copy Group modify failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Modify Remote Copy Group %s successfully." % remote_copy_group_name, {})

def add_volume_to_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            volume_name,
            targets,
            snapshot_name,
            volume_auto_creation,
            skip_initial_sync,
            different_secondary_wwn
            ):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Add volume to Remote Copy Group failed. Storage system username or password is null",
            {})
    if remote_copy_group_name is None:
        return (False, False, "Add volume to Remote Copy Group failed. Remote Copy Group name is null", {})
    if len(remote_copy_group_name) < 1 or len(remote_copy_group_name) > 31:
        return (False, False, "Add volume to Remote Copy Group failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {})
    if volume_name is None:
        return (False, False, "Add volume to Remote Copy Group failed. Volume name is null", {})
    if len(volume_name) < 1 or len(volume_name) > 31:
        return (False, False, "Add volume to Remote Copy Group failed. Volume name must be atleast 1 character and not more than 31 characters", {})
    if snapshot_name and volume_auto_creation:
        return (False, False, "Add volume to Remote Copy Group failed. volumeAutoCreation cannot be true if snapshot name is given", {})
    if snapshot_name and skip_initial_sync:
        return (False, False, "Add volume to Remote Copy Group failed. skipInitialSync cannot be true if snapshot name is given", {})
    if not snapshot_name and different_secondary_wwn:
        return (False, False, "Add volume to Remote Copy Group failed. skipInitialSync cannot be true if snapshot name is not given", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if client_obj.remoteCopyGroupExists(remote_copy_group_name):
            if not client_obj.remoteCopyGroupVolumeExists(remote_copy_group_name, volume_name):
                optional = {
                    'snapshotName': snapshot_name,
                    'volumeAutoCreation': volume_auto_creation,
                    'skipInitialSync': skip_initial_sync,
                    'differentSecondaryWWN': different_secondary_wwn
                }
                client_obj.addVolumeToRemoteCopyGroup(remote_copy_group_name, volume_name, targets, optional)
            else:
                return (True, False, "Volume %s already present in Remote Copy Group %s" % (volume_name, remote_copy_group_name), {})
        else:
            return (False, False, "Remote Copy Group not present", {})
    except Exception as e:
        return (False, False, "Remote Copy Group modify failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Volume %s added to Remote Copy Group %s successfully." % (volume_name, remote_copy_group_name), {})

def remove_volume_from_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            volume_name,
            keep_snap,
            remove_secondary_volume
            ):
    if remote_copy_group_name is None:
        return (False, False, "Remove volume from Remote Copy Group failed. Remote Copy Group name is null", {})
    if len(remote_copy_group_name) < 1 or len(remote_copy_group_name) > 31:
        return (False, False, "Remove volume from Remote Copy Group failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {})
    if volume_name is None:
        return (False, False, "Remove volume from Remote Copy Group failed. Volume name is null", {})
    if len(volume_name) < 1 or len(volume_name) > 31:
        return (False, False, "Remove volume from Remote Copy Group failed. Volume name must be atleast 1 character and not more than 31 characters", {})
    if keep_snap and remove_secondary_volume:
        return (False, False, "Remove volume from Remote Copy Group failed. keepSnap and removeSecondaryVolume cannot both be true", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if client_obj.remoteCopyGroupExists(remote_copy_group_name):
            if client_obj.remoteCopyGroupVolumeExists(remote_copy_group_name, volume_name):
                optional = {
                    'keepSnap': keep_snap
                }
                client_obj.removeVolumeFromRemoteCopyGroup(remote_copy_group_name, volume_name, optional, remove_secondary_volume)
            else:
                return (True, False, "Volume %s is not present in Remote Copy Group %s" % (volume_name, remote_copy_group_name), {})
        else:
            return (False, False, "Remote Copy Group not present", {})
    except Exception as e:
        return (False, False, "Remove volume from Remote Copy Group failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Volume %s removed from Remote Copy Group %s successfully." % (volume_name, remote_copy_group_name), {})

def start_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            skip_initial_sync,
            target_name,
            starting_snapshots,
			wait_for_task_to_end
            ):
    if remote_copy_group_name is None:
        return (False, False, "Start Remote Copy Group failed. Remote Copy Group name is null", {})
    if len(remote_copy_group_name) < 1 or len(remote_copy_group_name) > 31:
        return (False, False, "Start Remote Copy Group failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if client_obj.remoteCopyGroupExists(remote_copy_group_name):
            optional = {
                'skipInitialSync': skip_initial_sync,
                'targetName': target_name,
                'startingSnapshots': starting_snapshots
            }
            response = client_obj.startRemoteCopy(remote_copy_group_name, optional)
            # Task will not be created if the remote copy is already started
			if 'tasks' in response.keys():
				if wait_for_task_to_end:
					tasks = []
					for task in response['tasks']:
						client_obj.waitForTaskToEnd(task['task_id'])
				else:
					return (True, True, "Remote copy group %s starting." % remote_copy_group_name, {})
			else:
				return (True, False, "Remote Copy already started", {})
        else:
            return (False, False, "Remote Copy Group not present", {})
    except Exception as e:
        return (False, False, "Start Remote Copy Group failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Remote copy group %s started successfully." % remote_copy_group_name, {})

def stop_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            no_snapshot,
            target_name
            ):
    if remote_copy_group_name is None:
        return (False, False, "Stop Remote Copy Group failed. Remote Copy Group name is null", {})
    if len(remote_copy_group_name) < 1 or len(remote_copy_group_name) > 31:
        return (False, False, "Stop Remote Copy Group failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if client_obj.remoteCopyGroupExists(remote_copy_group_name):
            optional = {
                'noSnapshot': no_snapshot,
                'targetName': target_name
            }
            client_obj.stopRemoteCopy(remote_copy_group_name, optional)
        else:
            return (False, False, "Remote Copy Group not present", {})
    except Exception as e:
        return (False, False, "Stop Remote Copy Group failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Remote copy group %s stopped successfully." % remote_copy_group_name, {})

def synchronize_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            no_resync_snapshot,
            target_name,
            full_sync,
            wait_for_task_to_end
            ):
    if remote_copy_group_name is None:
        return (False, False, "Synchronize Remote Copy Group failed. Remote Copy Group name is null", {})
    if len(remote_copy_group_name) < 1 or len(remote_copy_group_name) > 31:
        return (False, False, "Synchronize Remote Copy Group failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if client_obj.remoteCopyGroupExists(remote_copy_group_name):
            optional = {
                'noResyncSnapshot': no_resync_snapshot,
                'targetName': target_name,
                'fullSync': full_sync
            }
            task = client_obj.synchronizeRemoteCopyGroup(remote_copy_group_name, optional)
            if wait_for_task_to_end:
                client_obj.waitForTaskToEnd(task.task_id)
        else:
            return (False, False, "Remote Copy Group not present", {})
    except Exception as e:
        return (False, False, "Synchronize Remote Copy Group failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Remote copy group %s resynchronized successfully." % remote_copy_group_name, {})

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
            return (True, False, "Remote Copy Group is already present", {})
    except Exception as e:
        return (False, False, "Remote Copy Group delete failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Deleted Remote Copy Group %s successfully." % remote_copy_group_name, {})

def recover_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            recovery_action,
            target_name,
            skip_start,
            skip_sync,
            discard_new_data,
            skip_promote,
            no_snapshot,
            stop_groups,
            local_groups_direction,
            wait_for_task_to_end
            ):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Remote Copy Group delete failed. Storage system username or password is null",
            {})
    if remote_copy_group_name is None:
        return (False, False, "Remote Copy Recover delete failed. Remote Copy Group name is null", {})
    if len(remote_copy_group_name) < 1 or len(remote_copy_group_name) > 31:
        return (False, False, "Remote Copy Group Recover failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {})
    if recovery_action is None:
        return (False, False, "Remote Copy Recover delete failed. recovery action is null", {})
    if skip_start and (recovery_action != 'FAILOVER_GROUP' or recovery_action != 'RESTORE_GROUP' or recovery_action != 'RECOVER_GROUP'):
        return (False, False, "Remote Copy Group Recover failed. skipStart can only be true if recovery action is either 'FAILOVER_GROUP', 'RESTORE_GROUP' or 'RECOVER_GROUP'", {})
    if skip_sync and (recovery_action != 'FAILOVER_GROUP' or recovery_action != 'RESTORE_GROUP'):
        return (False, False, "Remote Copy Group Recover failed. skipSync can only be true if recovery action is either 'FAILOVER_GROUP', 'RESTORE_GROUP' or 'RECOVER_GROUP'", {})
    if discard_new_data and recovery_action != 'FAILOVER_GROUP':
        return (False, False, "Remote Copy Group Recover failed. discardNewData can only be true if recovery action is 'FAILOVER_GROUP'", {})
    if skip_promote and (recovery_action != 'FAILOVER_GROUP' or recovery_action != 'REVERSE_GROUP'):
        return (False, False, "Remote Copy Group Recover failed. skipPromote can only be true if recovery action is either 'FAILOVER_GROUP' or 'REVERSE_GROUP'", {})
    if no_snapshot and (recovery_action != 'FAILOVER_GROUP' or recovery_action != 'REVERSE_GROUP' or recovery_action != 'RESTORE_GROUP'):
        return (False, False, "Remote Copy Group Recover failed. noSnapshot can only be true if recovery action is either 'FAILOVER_GROUP', 'RESTORE_GROUP' or 'REVERSE_GROUP'", {})
    if stop_groups and recovery_action != 'REVERSE_GROUP':
        return (False, False, "Remote Copy Group Recover failed. stopGroups can only be true if recovery action is 'REVERSE_GROUP'", {})
    if local_groups_direction and recovery_action != 'REVERSE_GROUP':
        return (False, False, "Remote Copy Group Recover failed. localGroupDirection can only be true if recovery action is 'REVERSE_GROUP'", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if client_obj.remoteCopyGroupExists(remote_copy_group_name):
            optional = {
                'targetName': target_name,
                'skipStart': skip_start,
                'skipSync': skip_sync,
                'discardNewData': discard_new_data,
                'skipPromote': skip_promote,
                'noSnapshot':no_snapshot,
                'stopGroups': stop_groups,
                'localGroupDirection': local_groups_direction
            }
            recovery_action_enum = getattr(client.HPE3ParClient, recovery_action)
            tasks = client_obj.recoverRemoteCopyGroupFromDisaster(remote_copy_group_name, recovery_action_enum, optional)
            if wait_for_task_to_end:
                for task in tasks:
                    client_obj.waitForTaskToEnd(task.task_id)
        else:
            return (True, False, "Remote Copy Group is not present", {})
    except Exception as e:
        return (False, False, "Remote Copy Group recovery failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Recovered Remote Copy Group %s successfully." % remote_copy_group_name, {})


def main():
    fields = {
        "state": {
            "required": True,
            "choices": ['present', 'absent', 'modify', 'add_volume', 'remove_volume', 'start', 'stop', 'synchronize', 'recover'],
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
        },
        "unset_user_cpg": {
            "type": "bool",
            "default": False
        },
        "unset_snap_cpg": {
            "type": "bool",
            "default": False
        },
        "snapshot_name": {
            "type": "string"
        },
        "volume_auto_creation": {
            "type": "bool",
            "default": False
        },
        "skip_initial_sync": {
            "type": "bool",
            "default": False
        },
        "different_secondary_wwn": {
            "type": "bool",
            "default": False
        },
        "remove_secondary_volume": {
            "type": "bool",
            "default": False
        },
        "target_name": {
            "type": "str"
        },
        "starting_snapshots": {
            "type": "list"
        },
        "no_snapshot": {
            "type": "bool",
            "default": False
        },
        "no_resync_snapshot": {
            "type": "bool",
            "default": False
        },
        "full_sync": {
            "type": "bool",
            "default": False
        },
        "recovery_action": {
            "choices": ['REVERSE_GROUP', 'FAILOVER_GROUP', 'SWITCHOVER_GROUP', 'RECOVER_GROUP', 'RESTORE_GROUP', 'OVERRIDE_GROUP', 'CLX_DR'],
            "type": 'str'
        },
        "skip_start": {
            "type": "bool",
            "default": False
        },
        "skip_sync": {
            "type": "bool",
            "default": False
        },
        "discard_new_data": {
            "type": "bool",
            "default": False
        },
        "skip_promote": {
            "type": "bool",
            "default": False
        },
        "stop_groups": {
            "type": "bool",
            "default": False
        },
        "local_groups_direction": {
            "type": "bool",
            "default": False
        },
        "volume_name": {
            "type": "str"
        },
        "wait_for_task_to_end": {
            "type": "bool",
            "defualt": False
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
    unset_user_cpg = module.params["unset_user_cpg"]
    unset_snap_cpg = module.params["unset_snap_cpg"]
    snapshot_name = module.params["snapshot_name"]
    volume_auto_creation = module.params["volume_auto_creation"]
    skip_initial_sync = module.params["skip_initial_sync"]
    different_secondary_wwn = module.params["different_secondary_wwn"]
    remove_secondary_volume = module.params["remove_secondary_volume"]
    target_name = module.params["target_name"]
    starting_snapshots = module.params["starting_snapshots"]
    no_snapshot = module.params["no_snapshot"]
    no_resync_snapshot = module.params["no_resync_snapshot"]
    full_sync = module.params["full_sync"]
    recovery_action = module.params["recovery_action"]
    volume_name = module.params["volume_name"]
    skip_start = module.params["skip_start"]
    skip_sync = module.params["skip_sync"]
    wait_for_task_to_end = module.params["wait_for_task_to_end"]
    discard_new_data = module.params["discard_new_data"]
    skip_promote = module.params["skip_promote"]
    stop_groups = module.params["stop_groups"]
    local_groups_direction = module.params["local_groups_direction"]

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
    elif module.params["state"] == "absent":
        return_status, changed, msg, issue_attr_dict = delete_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            keep_snap
        )
    elif module.params["state"] == "modify":
        return_status, changed, msg, issue_attr_dict = modify_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            local_user_cpg,
            local_snap_cpg,
            targets,
            unset_user_cpg,
            unset_snap_cpg
        )
    elif module.params["state"] == "add_volume":
        return_status, changed, msg, issue_attr_dict = add_volume_to_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            volume_name,
            targets,
            snapshot_name,
            volume_auto_creation,
            skip_initial_sync,
            different_secondary_wwn
        )
    elif module.params["state"] == "remove_volume":
        return_status, changed, msg, issue_attr_dict = remove_volume_from_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            volume_name,
            keep_snap,
            remove_secondary_volume
        )
    elif module.params["state"] == "start":
        return_status, changed, msg, issue_attr_dict = start_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            skip_initial_sync,
            target_name,
            starting_snapshots,
            wait_for_task_to_end
        )
    elif module.params["state"] == "stop":
        return_status, changed, msg, issue_attr_dict = stop_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            no_snapshot,
            target_name
        )
    elif module.params["state"] == "synchronize":
        return_status, changed, msg, issue_attr_dict = synchronize_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            no_resync_snapshot,
            target_name,
            full_sync,
            wait_for_task_to_end
        )
    elif module.params["state"] == "recover":
        return_status, changed, msg, issue_attr_dict = recover_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            recovery_action,
            target_name,
            skip_start,
            skip_sync,
            discard_new_data,
            skip_promote,
            no_snapshot,
            stop_groups,
            local_groups_direction,
            wait_for_task_to_end
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
