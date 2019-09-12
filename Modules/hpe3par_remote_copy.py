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
author: "Arshad Ansari(arshad.alam.ansari@hpe.com)"
description: "On HPE 3PAR and PRIMERA - Create Remote Copy Group - Modify Remote
 Copy Group - Add Volumes to Remote Copy Group - Remove Volumes from Remote
 Copy Group -Synchronize Remote Copy Group - Delete Remote Copy Group
 - Admit Remote Copy Link - Dismiss Remote Copy Link - Start Remote Copy Group
 - Stop Remote Copy Group - Admit Remote Copy Target - Dismiss Remote Copy Target
 - Start Remote Copy Service - Remote Copy Status"
module: hpe3par_remote_copy
options:
  remote_copy_group_name:
    description:
      - "Specifies the name of the Remote Copy group to create.\n
       Used with state[s] - present, absent, modify, add_volume,\n
       remove_volume, start, stop, synchronize, admit_target,\n
       dismiss_target, remote_copy_status"
  domain:
    description:
      - "Specifies the domain in which to create the Remote Copy group.\n
       Used with state[s] - present"
  remote_copy_targets:
    description:
      - "Specifies the attributes of the target of the Remote Copy group.\n
       Attributes are target_name, target_mode, user_cpg, snap_cpg.\n
       Used with state[s] - present"
  admit_volume_targets:
    description:
      - "Specify at least one pair of target_name and sec_volume_name.\n
       Attributes are target_name, sec_volume_name.\n
       Used with state[s] - add_volume"
  modify_targets:
    description:
      - "Specifies the attributes of the target of the Remote Copy group.\n
       Attributes are target_name, remote_user_cpg, remote_snap_cpg,\n
       sync_period, rm_sync_period, target_mode, snap_frequency,
       rm_snap_frequency, policies.\n
       Used with state[s] - modify"
  local_user_cpg:
    description:
      - "Specifies the local user CPG used for auto-created volumes.\n
       Used with state[s] - present, modify"
  local_snap_cpg:
    description:
      - "Specifies the local snap CPG used for auto-created volumes.\n
       Used with state[s] - present, modify"
  keep_snap:
    default: false
    description:
      - "Enables (true) or disables (false) retention \n of the local volume
       resynchronization snapshot.\n
       Used with state[s] - absent, remove_volume"
    type: bool
  unset_user_cpg:
    default: false
    description:
      - "Enables (true) or disables (false) setting the localUserCPG
       and \n remoteUserCPG of the Remote Copy group.\n
       Used with state[s] - modify"
    type: bool
  unset_snap_cpg:
    default: false
    description:
      - "Enables (true) or disables (false) setting the \n localSnapCPG
       and remoteSnapCPG of the Remote Copy group.\n
       Used with state[s] - modify"
    type: bool
  snapshot_name:
    description:
      - "The optional read-only snapshotName is a starting snapshot
       when \n the group is started without performing a full
       resynchronization. \n Instead, for synchronized groups, the volume
       synchronizes deltas \n between this snapshotName and the base volume.
       For periodic groups, \n the volume synchronizes deltas between this
       snapshotName and a snapshot of the base.\n
       Used with state[s] - add_volume"
  volume_auto_creation:
    default: false
    description:
      - "If volumeAutoCreation is set to true, \n the secondary volumes
       should be created automatically \n on the target using the CPG.
       associated with the Remote Copy group on that target.
       This cannot be set to true if the snapshot name is specified.\n
       Used with state[s] - add_volume"
    type: bool
  skip_initial_sync:
    default: false
    description:
      - "If skipInitialSync is set to true, the volume
       should skip the initial sync. \n This is for the
       admission of volumes that have been presynced
       with the target volume. \n This cannot be set to
       true if the snapshot name is specified.\n
       Used with state[s] - add_volume, start"
    type: bool
  different_secondary_wwn:
    default: false
    description:
      - "Setting differentSecondaryWWN to true, \n ensures that
       the system uses a different WWN on the secondary volume.
       Defaults to false. Use with volumeAutoCreation only.\n
       Used with state[s] - add_volume"
    type: bool
  remove_secondary_volume:
    default: false
    description:
      - "Enables (true) or disables (false) deletion of the
       remote volume on the secondary array from the system.
       Defaults to false. Do not use with keepSnap.\n
       Used with state[s] - remove_volume"
    type: bool
  target_name:
    description:
      - "Specifies the target name associated with the Remote Copy
       group to be created.\n
       Used with state[s] - start, stop, synchronize, admit_link,
       dismiss_link, admit_target, dismiss_target"
  starting_snapshots:
    description:
      - "When used, you must specify all the volumes inthe group.
       While specifying the pair, the starting snapshot is optional.
       When not used, the system performs a full resynchronization of
       the volume.\n
       Used with state[s] - start"
  no_snapshot:
    default: false
    description:
      - "If true, this option turns off creation of snapshots in
       synchronous and periodic modes, and deletes the current
       synchronization snapshots.\n
       Used with state[s] - stop"
    type: bool
  no_resync_snapshot:
    default: false
    description:
      - "Enables (true) or disables (false) saving the resynchronization
       snapshot. Applicable only to Remote Copy groups in asychronous
       periodic mode.\n
       Used with state[s] - synchronize"
    type: bool
  full_sync:
    default: false
    description:
      - "Enables (true) or disables (false) forcing a full synchronization
       of the Remote Copy group, even if the volumes are already
       synchronized. Applies only to volume groups in synchronous mode, and
       can be used to resynchronize volumes that have become inconsistent.\n
       Used with state[s] - synchronize"
    type: bool
  volume_name:
    description:
      - "Specifies the name of the existing virtual volume to
       be admitted to an existing Remote Copy group.\n
       Used with state[s] - add_volume, remove_volume"
  source_port:
    description:
      - "node:slot:port Specifies the node, slot, and port of
       the Ethernet port on the local system Ethernet port on the
       local system.\n
       Used with state[s] - admit_link, dismiss_link"
  target_port_wwn_or_ip:
    description:
      - "IP/WWN address of the peer port on the target system.\n
       Used with state[s] - admit_link, dismiss_link"
  target_mode:
    choices:
      - sync
      - periodic
      - async
    description:
      - "Specifies the mode of the target as either synchronous (sync),
       asynchronous periodic (periodic), or asynchronous streaming (async).\n
       Used with state[s] - admit_target"
  local_remote_volume_pair_list:
    description:
      - "Is a list of dictionaries, where each dictionary contains source and
       target volumes pairs i.e. [{'sourceVolumeName':'secondary_vv1',
       'targetVolumeName':'secondary_vv2'}, ..].\n
       Used with state[s] - admit_target"
  state:
    choices:
      - present
      - absent
      - modify
      - add_volume
      - remove_volume
      - start
      - stop
      - synchronize
      - admit_link
      - dismiss_link
      - admit_target
      - dismiss_target
      - start_rcopy
      - remote_copy_status
    description:
      - "Whether the specified Remote Copy Group should exist or not. State
       also provides actions to modify Remote copy Group ,add/remove volumes,
       start/stop/synchronize remote copy group, Add/remove remote
       copy link, start remote copy services, admit/dismiss target.\n"
    required: true
  storage_system_ip:
    description:
      - "The storage system IP address.\n"
    required: true
  storage_system_password:
    description:
      - "The storage system password.\n"
    required: true
  storage_system_username:
    description:
      - "The storage system user name.\n"
    required: true

requirements:
  - "3PAR OS - 3.2.2 MU6, 3.3.1 MU1"
  - "Ansible - 2.4"
  - "hpe3par_sdk 1.0.0"
  - "WSAPI service should be enabled on the 3PAR and PRIMERA storage array."
short_description: "Manage HPE 3PAR and PRIMERA Remote Copy"
version_added: "2.4"
'''

EXAMPLES = r'''
- hosts: localhost
  tasks:
  - name: Load Storage System Vars
    include_vars: 'properties/storage_system_properties.yml'

  - name: Create volume on source
    hpe3par_volume:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: present
      volume_name: demo_volume_1
      size: 1024
      size_unit: MiB
      cpg: FC_r1
      snap_cpg: FC_r1

  - name: Create volume on source
    hpe3par_volume:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: present
      volume_name: demo_volume_2
      size: 1024
      size_unit: MiB
      cpg: FC_r1
      snap_cpg: FC_r1     

  - name: Create volume on target
    hpe3par_volume:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: present
      volume_name: demo_volume_1
      size: 1024
      size_unit: MiB
      cpg: FC_r1
      snap_cpg: FC_r1     

  - name: Create volume on target
    hpe3par_volume:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: present
      volume_name: demo_volume_2
      size: 1024
      size_unit: MiB
      cpg: FC_r1
      snap_cpg: FC_r1           

  - name: Create volume on target2
    hpe3par_volume:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: present
      volume_name: demo_volume_1
      size: 1024
      size_unit: MiB
      cpg: FC_r1
      snap_cpg: FC_r1

  - name: Create volume on target2
    hpe3par_volume:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: present
      volume_name: demo_volume_2
      size: 1024
      size_unit: MiB
      cpg: FC_r1
      snap_cpg: FC_r1

  - name: Create Remote Copy Group test_rcg
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: present
      remote_copy_group_name: test_rcg
      remote_copy_targets:
      - target_name: target_array_name
        target_mode: sync
       
  - name: Add volume to remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: add_volume
      remote_copy_group_name: test_rcg
      volume_name: demo_volume_1
      admit_volume_targets:
      - target_name: target_array_name
        sec_volume_name: demo_volume_1
        
  - name: Add volume to remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: add_volume
      remote_copy_group_name: test_rcg
      volume_name: demo_volume_2
      admit_volume_targets:
      - target_name: target_array_name
        sec_volume_name: demo_volume_2

  - name: admit Remote Copy target
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: admit_target
      remote_copy_group_name: test_rcg
      target_name: target_array_name
      local_remote_volume_pair_list:
      - sourceVolumeName: source_volume_1
        targetVolumeName: target_volume_1
      - sourceVolumeName: source_volume_2
        targetVolumeName: target_volume_2
      target_mode: periodic

  - name: remote copy group status
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: remote_copy_status
      remote_copy_group_name: test_rcg
    register: result

  - debug:
      msg: "{{ result.output.remote_copy_sync_status}}"


  - name: dismiss Remote Copy target
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: dismiss_target
      remote_copy_group_name: test_rcg
      target_name: target_array_name

  - name: Modify Remote Copy Group test_rcg
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: modify
      remote_copy_group_name: test_rcg
      local_user_cpg: "FC_r1"
      local_snap_cpg: "FC_r6"
      unset_user_cpg: false
      unset_snap_cpg: false
      modify_targets:
      - target_name: target_array_name
        remote_user_cpg: "FC_r1"
        remote_snap_cpg: "FC_r6"
        
  - name: Start remote copy
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      remote_copy_group_name: test_rcg
      state: start
      
  - name: Stop remote copy
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      remote_copy_group_name: test_rcg
      state: stop
      
  - name: Remove volume from remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: remove_volume
      remote_copy_group_name: test_rcg
      volume_name: demo_volume_1
        
  - name: Remove volume from remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: remove_volume
      remote_copy_group_name: test_rcg
      volume_name: demo_volume_2
        
  - name: Remove Remote Copy Group test_rcg
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: absent 
      remote_copy_group_name: test_rcg

  - name: dismiss remote copy link
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: dismiss_link
      target_name: target_array_name
      source_port: 0:3:1
      target_port_wwn_or_ip: 10.10.10.10

  - name: dismiss remote copy link
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: dismiss_link
      target_name: target_array_name
      source_port: "1:3:1"
      target_port_wwn_or_ip: 10.10.10.10

  - name: Admit remote copy link
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: admit_link
      target_name: target_array_name
      source_port: 0:3:1
      target_port_wwn_or_ip: 10.10.10.10

  - name: Admit remote copy link
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: admit_link
      target_name: target_array_name
      source_port: "1:3:1"
      target_port_wwn_or_ip: 10.10.10.10

  - name: start remote copy service
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: start_rcopy

  - name: Add volume to remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      remote_copy_group_name: "ansible_CreateRCG-004"
      state: add_volume
      volume_name: "Ansible_volume_01"
      admit_volume_targets:
      - target_name: "target_array_name"
        sec_volume_name: "Target_volume"
      snapshot_name:
      volume_auto_creation: true
      skip_initial_sync: true
      different_secondary_wwn: true

  - name: Add volume to remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      remote_copy_group_name: "ansible_CreateRCG-002"
      state: add_volume
      volume_name: "Ansible_volume_rcg_01"
      admit_volume_targets:
      - target_name: "target_array_name"
        sec_volume_name: "Target_volume"
      snapshot_name: "Ansible_volume_SS_snap_01"
      volume_auto_creation: "false"
      skip_initial_sync: "false"
      different_secondary_wwn:

  - name: Add volume to remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      remote_copy_group_name: "ansible_CreateRCG-002"
      state: add_volume
      volume_name: "Ansible_volume_rcg_01"
      admit_volume_targets:
      - target_name: "target_array_name"
        sec_volume_name: "Target_volume"
      snapshot_name:
      volume_auto_creation: "true"
      skip_initial_sync: "false"
      different_secondary_wwn:

  - name: Add volume to remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      remote_copy_group_name: "ansible_CreateRCG-002"
      state: add_volume
      volume_name: "Ansible_volume_rcg_01"
      admit_volume_targets:
      - target_name: "target_array_name"
        sec_volume_name: "Target_volume"
      snapshot_name: "Ansible_volume_SS_snap_01"
      volume_auto_creation: "false"
      skip_initial_sync: "false"
      different_secondary_wwn:

  - name: Add volume to remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      remote_copy_group_name: "ansible_CreateRCG-002"
      state: add_volume
      volume_name: "Ansible_volume_rcg_01"
      admit_volume_targets:
      - target_name: "target_array_name"
        sec_volume_name: "Target_volume"
      snapshot_name:
      volume_auto_creation: "true"
      skip_initial_sync: true
      different_secondary_wwn:

  - name: Synchronize remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      remote_copy_group_name: "ansible_CreateRCG-002"
      state: synchronize
      no_resync_snapshot: "false"
      target_name: "target_array_name"
      full_sync: "false"

  - name: Synchronize remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      remote_copy_group_name: "ansible_CreateRCG-003"
      state: synchronize
      no_resync_snapshot: "true"
      target_name: "target_array_name"
      full_sync: "true"

  - name: Remove remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: absent
      remote_copy_group_name: "ansible_CreateRCG-004"
      keepSnap: "false"
      remove_secondary_volume:

  - name: Remove volume from remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      state: remove_volume
      volume_name: "Ansible_volume_rcg_01"
      keep_snap: "true"
      remove_secondary_volume: "false"

  - name: Stop remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      remote_copy_group_name: "ansible_CreateRCG-003"
      state: stop
      no_snapshot: "true"
      target_name: "target_array_name"

  - name: Remove volume from remote copy group
    hpe3par_remote_copy:
      storage_system_ip: 10.10.10.1
      storage_system_password: password
      storage_system_username: username
      remote_copy_group_name: "ansible_CreateRCG-002"
      state: remove_volume
      volume_name: "Ansible_volume_rcg_01"
      keep_snap: "false"
      remove_secondary_volume: "true"
'''

RETURN = r'''
'''

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
            remote_copy_targets,
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
    targets_transformed = []
    target_names_list = []
    for target_dict in remote_copy_targets:
        target={}
        for key in target_dict.keys():
            if key == 'target_name':
                if target_dict[key] is None:
                    return (False, False, "Remote Copy Group create failed. Target name is null", {})
                else:
                    target['targetName'] = target_dict.get(key)
                    target_names_list.append(target_dict.get(key))
            elif key == 'target_mode':
                if target_dict.get(key) == 'sync':
                    target['mode'] = 1
                elif target_dict.get(key) == 'periodic':
                    target['mode'] = 3
                elif target_dict.get(key) == 'async':
                    target['mode'] = 4
                else:
                    return (False, False, "Remote Copy Group create failed. Target mode is invalid", {}) 
            elif key == 'user_cpg':
                target['userCPG'] = target_dict.get(key)
            elif key == 'snap_cpg':
                target['snapCPG'] = target_dict.get(key)
            else:
                return (False, False, "Remote Copy Group create failed. Wrong parameter name %s is given." % key, {}) 
        targets_transformed.append(target)
    remote_copy_targets = targets_transformed
    try:
        client_obj.login(storage_system_username, storage_system_password)
        target_name = client_obj.getStorageSystemInfo()['name']
        if target_name in target_names_list:
            return (False, False, "Source and target cannot be same. Source and target both are %s" % target_name, {})
        if not client_obj.remoteCopyGroupExists(remote_copy_group_name):
            optional = {
                'domain': domain,
                'localUserCPG': local_user_cpg,
                'localSnapCPG': local_snap_cpg
            }
            client_obj.createRemoteCopyGroup(remote_copy_group_name, remote_copy_targets, optional)
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
            modify_targets,
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
    targets_transformed = []
    target_names_list = []
    for target_dict in modify_targets:
        target = {}
        for key in target_dict.keys():
            if key == 'target_name':
                target['targetName'] = target_dict.get(key)
                target_names_list.append(target_dict.get(key))
            elif key == 'remote_user_cpg':
                target['remoteUserCPG'] = target_dict.get(key)
            elif key == 'remote_snap_cpg':
                target['remoteSnapCPG'] = target_dict.get(key)
            elif key == 'sync_period':
                if target_dict[key] and target_dict[key] not in range(300, 31622401):
                    return (False, False, "Remote Copy Group modification failed. Valid range of %s is 300-31622400." % key, {})
                target['syncPeriod'] = target_dict.get(key)
            elif key == 'rm_sync_period':
                target['rmSyncPeriod'] = target_dict.get(key)
            elif key == 'target_mode':
                target['mode'] = target_dict.get(key)
            elif key == 'snap_frequency':
                if target_dict[key] and target_dict[key] not in range(300, 31622401):
                    return (False, False, "Remote Copy Group modification failed. Valid range of %s is 300-31622400." % key, {})
                target['snapFrequency'] = target_dict.get(key)
            elif key == 'rm_snap_frequency':
                target['rmSnapFrequency'] = target_dict.get(key)
            elif key == 'policies':
                target['policies'] = target_dict.get(key)
            else:
                return (False, False, "Remote Copy Group modification failed. Wrong parameter name %s is given." % key, {})
        targets_transformed.append(target)
    modify_targets = targets_transformed
    try:
        client_obj.login(storage_system_username, storage_system_password)
        target_name = client_obj.getStorageSystemInfo()['name']
        if target_name in target_names_list:
            return (False, False, "Source and target cannot be same. Source and target both are %s" % target_name, {})
        if client_obj.remoteCopyGroupExists(remote_copy_group_name):
            optional = {
                'localUserCPG': local_user_cpg,
                'localSnapCPG': local_snap_cpg,
                'targets': modify_targets,
                'unsetUserCPG': unset_user_cpg,
                'unsetSnapCPG': unset_snap_cpg
            }
            client_obj.modifyRemoteCopyGroup(remote_copy_group_name, optional)
        else:
            return (False, False, "Remote Copy Group not present", {})
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
            admit_volume_targets,
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
    if not volume_auto_creation and different_secondary_wwn:
        return (False, False, "Add volume to Remote Copy Group failed. differentSecondaryWWN cannot be true if volumeAutoCreation is false", {})
    targets_transformed = []
    target_names_list = []
    for target_dict in admit_volume_targets:
        target = {}
        for key in target_dict.keys():
            if key == 'target_name':
                if target_dict[key] is None:
                    return (False, False, "Remote Copy Group create failed. Target name is null", {})
                else:
                    target['targetName'] = target_dict.get(key)
                    target_names_list.append(target_dict.get(key))
            elif key == 'sec_volume_name':
                if target_dict[key] is None:
                    return (False, False, "Remote Copy Group create failed. Secondary volume is null", {})
                if len(target_dict[key]) < 1 or len(target_dict[key]) > 31:
                    return (False, False, "Add volume to Remote Copy Group failed. Secondary volume name must be atleast 1 character and not more than 31 characters", {})
                target['secVolumeName'] = target_dict.get(key)
            else:
                return (False, False, "Remote Copy Group create failed. Wrong parameter name %s is given." % key, {}) 
        targets_transformed.append(target)
    admit_volume_targets = targets_transformed
    try:
        client_obj.login(storage_system_username, storage_system_password)
        target_name = client_obj.getStorageSystemInfo()['name']
        if target_name in target_names_list:
            return (False, False, "Source and target cannot be same. Source and target both are %s" % target_name, {})
        if client_obj.remoteCopyGroupExists(remote_copy_group_name):
            if not client_obj.remoteCopyGroupVolumeExists(remote_copy_group_name, volume_name):
                optional = {
                    'snapshotName': snapshot_name,
                    'volumeAutoCreation': volume_auto_creation,
                    'skipInitialSync': skip_initial_sync,
                    'differentSecondaryWWN': different_secondary_wwn
                }
                client_obj.addVolumeToRemoteCopyGroup(remote_copy_group_name, volume_name, admit_volume_targets, optional)
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
            starting_snapshots
            ):
    if remote_copy_group_name is None:
        return (False, False, "Start Remote Copy Group failed. Remote Copy Group name is null", {})
    if len(remote_copy_group_name) < 1 or len(remote_copy_group_name) > 31:
        return (False, False, "Start Remote Copy Group failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if client_obj.remoteCopyGroupExists(remote_copy_group_name):
            if not client_obj.remoteCopyGroupStatusStartedCheck(remote_copy_group_name):
                optional = {
                    'skipInitialSync': skip_initial_sync,
                    'targetName': target_name,
                    'startingSnapshots': starting_snapshots
                }
                client_obj.startRemoteCopy(remote_copy_group_name, optional)
            else:
                return (True, False, "Remote Copy Group is already started", {})
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
            if not client_obj.remoteCopyGroupStatusStoppedCheck(remote_copy_group_name):
                optional = {
                    'noSnapshot': no_snapshot,
                    'targetName': target_name
                }
                client_obj.stopRemoteCopy(remote_copy_group_name, optional)
            else:
                return (True, False, "Remote Copy Group is already stopped", {})
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
            full_sync
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
        else:
            return (False, False, "Remote Copy Group not present", {})
    except Exception as e:
        return (False, False, "Synchronize Remote Copy Group failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Remote copy group %s resynchronize started successfully." % remote_copy_group_name, {})

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
            return (True, False, "Remote Copy Group is not present", {})
    except Exception as e:
        return (False, False, "Remote Copy Group delete failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Deleted Remote Copy Group %s successfully." % remote_copy_group_name, {})
'''
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
            local_groups_direction
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
            client_obj.recoverRemoteCopyGroupFromDisaster(remote_copy_group_name, recovery_action_enum, optional)
        else:
            return (True, False, "Remote Copy Group is not present", {})
    except Exception as e:
        return (False, False, "Remote Copy Group recovery failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Recovered Remote Copy Group %s successfully." % remote_copy_group_name, {})
'''
def admit_remote_copy_links(
            client_obj,
            storage_system_username,
            storage_system_password,
            storage_system_ip,
            target_name,
            source_port,
            target_port_wwn_or_ip
            ):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Admit remote copy link failed. Storage system username or password is null",
            {})
    if target_name is None:
        return (False, False, "Admit remote copy link failed. Target name is null", {})
    if source_port is None:
        return (False, False, "Admit remote copy link failed. Source port address is null", {})
    if target_port_wwn_or_ip is None:
        return (False, False, "Admit remote copy link failed. Target port WWN/IP is null", {})
    if storage_system_ip is None:
        return (False, False, "Admit remote copy link failed. Storage system IP address is null", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if target_name == client_obj.getStorageSystemInfo()['name']:
            return (False, False, "Source and target cannot be same. Source and target both are %s" % target_name, {})
        client_obj.setSSHOptions(storage_system_ip, storage_system_username, storage_system_password)
        if client_obj.rcopyLinkExists(target_name, source_port, target_port_wwn_or_ip):
            return (True, False, "Admit remote copy link %s:%s already exists." % (source_port, target_port_wwn_or_ip), {})
        else:
            response = client_obj.admitRemoteCopyLinks(target_name, source_port, target_port_wwn_or_ip)
    except Exception as e:
        return (False, False, "Admit remote copy link failed | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Admit remote copy link %s:%s successful." % (source_port, target_port_wwn_or_ip), {})

def dismiss_remote_copy_links(
            client_obj,
            storage_system_username,
            storage_system_password,
            storage_system_ip,
            target_name,
            source_port,
            target_port_wwn_or_ip
            ):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Dismiss remote copy link failed. Storage system username or password is null",
            {})
    if target_name is None:
        return (False, False, "Dismiss remote copy link failed. Target name is null", {})
    if source_port is None:
        return (False, False, "Dismiss remote copy link failed. Source port address is null", {})
    if target_port_wwn_or_ip is None:
        return (False, False, "Dismiss remote copy link failed. Target port WWN/IP is null", {})
    if storage_system_ip is None:
        return (False, False, "Dismiss remote copy link failed. Storage system IP address is null", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if target_name == client_obj.getStorageSystemInfo()['name']:
            return (False, False, "Source and target cannot be same. Source and target both are %s" % target_name, {})
        client_obj.setSSHOptions(storage_system_ip, storage_system_username, storage_system_password)
        if not client_obj.rcopyLinkExists(target_name, source_port, target_port_wwn_or_ip):
            return (True, False, "Remote copy link %s:%s already not present." % (source_port, target_port_wwn_or_ip), {})
        else:
            response = client_obj.dismissRemoteCopyLinks(target_name, source_port, target_port_wwn_or_ip)
    except Exception as e:
        return (False, False, "Dismiss remote copy link failed| %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Dismiss remote copy link %s:%s successful." % (source_port,target_port_wwn_or_ip), {})

def start_remote_copy_service(
            client_obj,
            storage_system_username,
            storage_system_password,
            storage_system_ip,
            ):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Start remote copy service failed. Storage system username or password is null",
            {})
    if storage_system_ip is None:
        return (False, False, "Start remote copy service failed. Storage system IP address is null", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        client_obj.setSSHOptions(storage_system_ip, storage_system_username, storage_system_password)
        if client_obj.rcopyServiceExists():
            return (True, False, "Remote copy service already started", {})
        else:
            response = client_obj.startrCopy()
    except Exception as e:
        return (False, False, "Start remote copy service failed| %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Start remote copy service successful.", {})

def admit_remote_copy_target(
            client_obj,
            storage_system_username,
            storage_system_password,
            storage_system_ip,
            target_name,
            target_mode,
            remote_copy_group_name,
            local_remote_volume_pair_list
            ):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Admit remote copy target failed. Storage system username or password is null",
            {})
    if target_name is None:
        return (False, False, "Admit remote copy target failed. Target name is null", {})
    if storage_system_ip is None:
        return (False, False, "Admit remote copy target failed. Storage system IP address is null", {})
    if target_mode is None:
        return (False, False, "Admit remote copy target failed. Mode is null", {})
    if remote_copy_group_name is None:
        return (False, False, "Admit remote copy target failed. Remote copy group name is null", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if target_name == client_obj.getStorageSystemInfo()['name']:
            return (False, False, "Source and target cannot be same. Source and target both are %s" % target_name, {})
        client_obj.setSSHOptions(storage_system_ip, storage_system_username, storage_system_password)
        #checking existance of remote_copy_group_name
        if not client_obj.remoteCopyGroupExists(remote_copy_group_name):
            return (False, False, "Remote Copy Group is not present", {})

        #Checking whether target name already present in remote copy
        #If it is already present then target add to remote copy group fails
        if client_obj.targetInRemoteCopyGroupExists(target_name, remote_copy_group_name):
            return (True, False, "Admit remote copy target failed.Target is already present", {})
        optional = { 'volumePairs': local_remote_volume_pair_list }
        results=client_obj.admitRemoteCopyTarget(target_name, target_mode, remote_copy_group_name, optional)
    except Exception as e:
        return (False, False, "Admit remote copy target failed| %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Admit remote copy target %s successful in remote copy group %s." % (target_name, remote_copy_group_name), {})

def dismiss_remote_copy_target(
            client_obj,
            storage_system_username,
            storage_system_password,
            storage_system_ip,
            target_name,
            remote_copy_group_name
            ):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Dismiss remote copy target failed. Storage system username or password is null",
            {})

    if target_name is None:
        return (False, False, "Dismiss remote copy target failed. Target name is null", {})
    if storage_system_ip is None:
        return (False, False, "Dismiss remote copy target failed. Storage system IP address is null", {})
    if remote_copy_group_name is None:
        return (False, False, "Dismiss remote copy target failed. Remote copy group name is null", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if target_name == client_obj.getStorageSystemInfo()['name']:
            return (False, False, "Source and target cannot be same. Source and target both are %s" % target_name, {})
        client_obj.setSSHOptions(storage_system_ip, storage_system_username, storage_system_password)

        #checking existance of remote_copy_group_name
        if not client_obj.remoteCopyGroupExists(remote_copy_group_name):
            return (False, False, "Remote Copy Group %s is not present" % remote_copy_group_name, {})

        #Checking whether target name already present in remote copy
        #If it is already present then target add to remote copy group fails
        if not client_obj.targetInRemoteCopyGroupExists(target_name, remote_copy_group_name):
            return (True, False, "Dismiss remote copy target failed. Target %s is already not present in remote copy group %s"\
                    % (target_name, remote_copy_group_name), {})

        results=client_obj.dismissRemoteCopyTarget(target_name, remote_copy_group_name)
    except Exception as e:
        return (False, False, "Dismiss remote copy target failed| %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, True, "Dismiss remote copy target %s successful." % target_name, {})

def remote_copy_group_status(
            client_obj,
            storage_system_username,
            storage_system_password,
            storage_system_ip,
            remote_copy_group_name
            ):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Remote copy group status failed. Storage system username or password is null",
            {})
    if storage_system_ip is None:
        return (False, False, "Remote copy group status failed. Storage system IP address is null", {})
    if remote_copy_group_name is None:
        return (False, False, "Remote copy group status failed. Remote copy group name is null", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        client_obj.setSSHOptions(storage_system_ip, storage_system_username, storage_system_password)

        #checking existance of remote_copy_group_name
        if not client_obj.remoteCopyGroupExists(remote_copy_group_name):
            return (True, False, "Remote Copy Group %s is not present" % remote_copy_group_name, {})


        remotecopy_status = client_obj.remoteCopyGroupStatusCheck(remote_copy_group_name)
        if not remotecopy_status:
            return (True, False, "Remote copy group %s status is not in complete" % (remote_copy_group_name), {"remote_copy_sync_status":remotecopy_status})
    except Exception as e:
        return (False, False, "Could not get remote copy group status | %s" % (e), {})
    finally:
        client_obj.logout()
    return (True, False, "Remote copy group %s status is complete" % (remote_copy_group_name), {"remote_copy_sync_status":remotecopy_status})

def main():
    fields = {
        "state": {
            "required": True,
            "choices": ['present', 'absent', 'modify', 'add_volume', 'remove_volume', 'start', 'stop', 'synchronize', 'recover', 'admit_link', 
            'dismiss_link','admit_target','dismiss_target', 'start_rcopy', 'remote_copy_status'],
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
            "type": "str"
        },
        "domain": {
            "type": "str"
        },
        "remote_copy_targets": {
            "type": "list"
        },
        "modify_targets": {
            "type": "list"
        },
        "admit_volume_targets": {
            "type": "list"
        },
        "local_user_cpg": {
            "type": "str"
        },
        "local_snap_cpg": {
            "type": "str"
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
            "type": "str"
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
        "source_port": {
            "type": "str"
        },
        "target_port_wwn_or_ip": {
            "type": "str"
        },
        "target_mode": {
            "choices": ['sync', 'periodic', 'async'],
            "type": 'str'
        },
        "local_remote_volume_pair_list": {
            "type": "list",
            "default": []
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
    remote_copy_targets = module.params["remote_copy_targets"]
    modify_targets = module.params["modify_targets"]
    admit_volume_targets = module.params["admit_volume_targets"]
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
    source_port = module.params["source_port"]
    target_port_wwn_or_ip = module.params["target_port_wwn_or_ip"]
    starting_snapshots = module.params["starting_snapshots"]
    no_snapshot = module.params["no_snapshot"]
    no_resync_snapshot = module.params["no_resync_snapshot"]
    full_sync = module.params["full_sync"]
    recovery_action = module.params["recovery_action"]
    volume_name = module.params["volume_name"]
    skip_start = module.params["skip_start"]
    skip_sync = module.params["skip_sync"]
    discard_new_data = module.params["discard_new_data"]
    skip_promote = module.params["skip_promote"]
    stop_groups = module.params["stop_groups"]
    local_groups_direction = module.params["local_groups_direction"]
    local_remote_volume_pair_list = module.params["local_remote_volume_pair_list"]
    target_mode = module.params["target_mode"]

    port_number = client.HPE3ParClient.getPortNumber(
        storage_system_ip, storage_system_username, storage_system_password)
    wsapi_url = 'https://%s:%s/api/v1' % (storage_system_ip, port_number)
    client_obj = client.HPE3ParClient(wsapi_url)

    # States
    if module.params["state"] == "present":
        return_status, changed, msg, issue_attr_dict = create_remote_copy_group(
            client_obj,
            storage_system_username,
            storage_system_password,
            remote_copy_group_name,
            domain,
            remote_copy_targets,
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
            modify_targets,
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
            admit_volume_targets,
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
            starting_snapshots
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
            full_sync
        )
#    elif module.params["state"] == "recover":
#        return_status, changed, msg, issue_attr_dict = recover_remote_copy_group(
#            client_obj,
#            storage_system_username,
#            storage_system_password,
#            remote_copy_group_name,
#            recovery_action,
#            target_name,
#            skip_start,
#            skip_sync,
#            discard_new_data,
#            skip_promote,
#            no_snapshot,
#            stop_groups,
#            local_groups_direction
#        )
    elif module.params["state"] == "admit_link":
        return_status, changed, msg, issue_attr_dict = admit_remote_copy_links(
            client_obj,
            storage_system_username,
            storage_system_password,
            storage_system_ip,
            target_name,
            source_port,
            target_port_wwn_or_ip
        )
    elif module.params["state"] == "dismiss_link":
        return_status, changed, msg, issue_attr_dict = dismiss_remote_copy_links(
            client_obj,
            storage_system_username,
            storage_system_password,
            storage_system_ip,
            target_name,
            source_port,
            target_port_wwn_or_ip
        )
    elif module.params["state"] == "start_rcopy":
        return_status, changed, msg, issue_attr_dict = start_remote_copy_service(
            client_obj,
            storage_system_username,
            storage_system_password,
            storage_system_ip,
        )
    elif module.params["state"] == "admit_target":
        return_status, changed, msg, issue_attr_dict = admit_remote_copy_target(
            client_obj,
            storage_system_username,
            storage_system_password,
            storage_system_ip,
            target_name,
            target_mode,
            remote_copy_group_name,
            local_remote_volume_pair_list
        )
    elif module.params["state"] == "dismiss_target":
        return_status, changed, msg, issue_attr_dict = dismiss_remote_copy_target(
            client_obj,
            storage_system_username,
            storage_system_password,
            storage_system_ip,
            target_name,
            remote_copy_group_name
        )
    elif module.params["state"] == "remote_copy_status":
        return_status, changed, msg, issue_attr_dict = remote_copy_group_status(
            client_obj,
            storage_system_username,
            storage_system_password,
            storage_system_ip,
            remote_copy_group_name
        )
    if return_status:
        if issue_attr_dict:
            module.exit_json(changed=changed, msg=msg, output=issue_attr_dict)
        else:
            module.exit_json(changed=changed, msg=msg)
    else:
        module.fail_json(msg=msg)


if __name__ == '__main__':
    main()
