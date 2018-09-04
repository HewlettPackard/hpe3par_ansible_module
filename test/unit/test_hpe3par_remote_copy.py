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


import mock
import unittest
from Modules import hpe3par_remote_copy
from ansible.module_utils.basic import AnsibleModule


class TestHpe3parRemoteCopy(unittest.TestCase):

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

    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    def test_module_args(self, mock_module, mock_client):
        """
        hpe3par remote copy - test module arguments
        """

        PARAMS_FOR_PRESENT = {
            'state': 'present',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'targets': [{'targetName': 'CSSOS-SSA04','mode': 1}],
            'local_user_cpg': 'localusrcpg1',
            'local_snap_cpg': 'snap_cpg1',
            'keep_snap': False,
            'unset_user_cpg': False,
            'unset_snap_cpg': False,
            'snapshot_name': 'snapshot_1',
            'volume_auto_creation': False,
            'skip_initial_sync': False,
            'different_secondary_wwn': False,
            'remove_secondary_volume': False,
            'target_name': 'targetName1',
            'starting_snapshots': ['volName1','snapShot1'],
            'no_snapshot': False,
            'no_resync_snapshot': False,
            'full_sync': False,
            'recovery_action': 'REVERSE_GROUP',
            'skip_start': False,
            'skip_sync': False,
            'discard_new_data': False,
            'skip_promote': False,
            'stop_groups': False,
            'local_groups_direction': False,
            'volume_name': 'volume_1',
            'wait_for_task_to_end': False
        }

        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        hpe3par_remote_copy.main()
        mock_module.assert_called_with(
            argument_spec=self.fields)

    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.create_remote_copy_group')
    def test_main_exit_present(self, mock_create_remote_copy_group, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'present',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'targets': [{'targetName': 'CSSOS-SSA04','mode': 1}],
            'local_user_cpg': 'localusrcpg1',
            'local_snap_cpg': 'snap_cpg1',
            'keep_snap': False,
            'unset_user_cpg': False,
            'unset_snap_cpg': False,
            'snapshot_name': 'snapshot_1',
            'volume_auto_creation': False,
            'skip_initial_sync': False,
            'different_secondary_wwn': False,
            'remove_secondary_volume': False,
            'target_name': 'targetName1',
            'starting_snapshots': ['volName1','snapShot1'],
            'no_snapshot': False,
            'no_resync_snapshot': False,
            'full_sync': False,
            'recovery_action': 'REVERSE_GROUP',
            'skip_start': False,
            'skip_sync': False,
            'discard_new_data': False,
            'skip_promote': False,
            'stop_groups': False,
            'local_groups_direction': False,
            'volume_name': 'volume_1',
            'wait_for_task_to_end': False
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_create_remote_copy_group.return_value = (
            True, True, "Created Remote Copy Group successfully.", {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Created Remote Copy Group successfully.")
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)

    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.delete_remote_copy_group')
    def test_main_exit_absent(self, mock_delete_remote_copy_group, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'absent',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'targets': [{'targetName': 'CSSOS-SSA04','mode': 1}],
            'local_user_cpg': 'localusrcpg1',
            'local_snap_cpg': 'snap_cpg1',
            'keep_snap': False,
            'unset_user_cpg': False,
            'unset_snap_cpg': False,
            'snapshot_name': 'snapshot_1',
            'volume_auto_creation': False,
            'skip_initial_sync': False,
            'different_secondary_wwn': False,
            'remove_secondary_volume': False,
            'target_name': 'targetName1',
            'starting_snapshots': ['volName1','snapShot1'],
            'no_snapshot': False,
            'no_resync_snapshot': False,
            'full_sync': False,
            'recovery_action': 'REVERSE_GROUP',
            'skip_start': False,
            'skip_sync': False,
            'discard_new_data': False,
            'skip_promote': False,
            'stop_groups': False,
            'local_groups_direction': False,
            'volume_name': 'volume_1',
            'wait_for_task_to_end': False
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_delete_remote_copy_group.return_value = (
            True, True, "Deleted Remote Copy Group successfully.", {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Deleted Remote Copy Group successfully.")
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)

    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.modify_remote_copy_group')
    def test_main_exit_modify(self, mock_modify_remote_copy_group, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'modify',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'targets': [{'targetName': 'CSSOS-SSA04','mode': 1}],
            'local_user_cpg': 'localusrcpg1',
            'local_snap_cpg': 'snap_cpg1',
            'keep_snap': False,
            'unset_user_cpg': False,
            'unset_snap_cpg': False,
            'snapshot_name': 'snapshot_1',
            'volume_auto_creation': False,
            'skip_initial_sync': False,
            'different_secondary_wwn': False,
            'remove_secondary_volume': False,
            'target_name': 'targetName1',
            'starting_snapshots': ['volName1','snapShot1'],
            'no_snapshot': False,
            'no_resync_snapshot': False,
            'full_sync': False,
            'recovery_action': 'REVERSE_GROUP',
            'skip_start': False,
            'skip_sync': False,
            'discard_new_data': False,
            'skip_promote': False,
            'stop_groups': False,
            'local_groups_direction': False,
            'volume_name': 'volume_1',
            'wait_for_task_to_end': False
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_modify_remote_copy_group.return_value = (
            True, True, "Modified Remote Copy Group successfully.", {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Modified Remote Copy Group successfully.")
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)

    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.add_volume_to_remote_copy_group')
    def test_main_exit_add_volume(self, mock_add_volume_to_remote_copy_group, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'add_volume',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'targets': [{'targetName': 'CSSOS-SSA04','mode': 1}],
            'local_user_cpg': 'localusrcpg1',
            'local_snap_cpg': 'snap_cpg1',
            'keep_snap': False,
            'unset_user_cpg': False,
            'unset_snap_cpg': False,
            'snapshot_name': 'snapshot_1',
            'volume_auto_creation': False,
            'skip_initial_sync': False,
            'different_secondary_wwn': False,
            'remove_secondary_volume': False,
            'target_name': 'targetName1',
            'starting_snapshots': ['volName1','snapShot1'],
            'no_snapshot': False,
            'no_resync_snapshot': False,
            'full_sync': False,
            'recovery_action': 'REVERSE_GROUP',
            'skip_start': False,
            'skip_sync': False,
            'discard_new_data': False,
            'skip_promote': False,
            'stop_groups': False,
            'local_groups_direction': False,
            'volume_name': 'volume_1',
            'wait_for_task_to_end': False
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_add_volume_to_remote_copy_group.return_value = (
            True, True, "Added volume to Remote Copy Group successfully.", {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Added volume to Remote Copy Group successfully.")
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)

		
    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.remove_volume_from_remote_copy_group')
    def test_main_exit_remove_volume(self, mock_remove_volume_to_remote_copy_group, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'remove_volume',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'targets': [{'targetName': 'CSSOS-SSA04','mode': 1}],
            'local_user_cpg': 'localusrcpg1',
            'local_snap_cpg': 'snap_cpg1',
            'keep_snap': False,
            'unset_user_cpg': False,
            'unset_snap_cpg': False,
            'snapshot_name': 'snapshot_1',
            'volume_auto_creation': False,
            'skip_initial_sync': False,
            'different_secondary_wwn': False,
            'remove_secondary_volume': False,
            'target_name': 'targetName1',
            'starting_snapshots': ['volName1','snapShot1'],
            'no_snapshot': False,
            'no_resync_snapshot': False,
            'full_sync': False,
            'recovery_action': 'REVERSE_GROUP',
            'skip_start': False,
            'skip_sync': False,
            'discard_new_data': False,
            'skip_promote': False,
            'stop_groups': False,
            'local_groups_direction': False,
            'volume_name': 'volume_1',
            'wait_for_task_to_end': False
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_remove_volume_to_remote_copy_group.return_value = (
            True, True, "Removed volume from Remote Copy Group successfully.", {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Removed volume from Remote Copy Group successfully.")
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)	

    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.start_remote_copy_group')
    def test_main_exit_start_remote_copy_group(self, mock_start_remote_copy_group, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'start',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'targets': [{'targetName': 'CSSOS-SSA04','mode': 1}],
            'local_user_cpg': 'localusrcpg1',
            'local_snap_cpg': 'snap_cpg1',
            'keep_snap': False,
            'unset_user_cpg': False,
            'unset_snap_cpg': False,
            'snapshot_name': 'snapshot_1',
            'volume_auto_creation': False,
            'skip_initial_sync': False,
            'different_secondary_wwn': False,
            'remove_secondary_volume': False,
            'target_name': 'targetName1',
            'starting_snapshots': ['volName1','snapShot1'],
            'no_snapshot': False,
            'no_resync_snapshot': False,
            'full_sync': False,
            'recovery_action': 'REVERSE_GROUP',
            'skip_start': False,
            'skip_sync': False,
            'discard_new_data': False,
            'skip_promote': False,
            'stop_groups': False,
            'local_groups_direction': False,
            'volume_name': 'volume_1',
            'wait_for_task_to_end': False
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_start_remote_copy_group.return_value = (
            True, True, "Started Remote Copy Group successfully.", {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Started Remote Copy Group successfully.")
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)	

    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.stop_remote_copy_group')
    def test_main_exit_stop_remote_copy_group(self, mock_stop_remote_copy_group, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'stop',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'targets': [{'targetName': 'CSSOS-SSA04','mode': 1}],
            'local_user_cpg': 'localusrcpg1',
            'local_snap_cpg': 'snap_cpg1',
            'keep_snap': False,
            'unset_user_cpg': False,
            'unset_snap_cpg': False,
            'snapshot_name': 'snapshot_1',
            'volume_auto_creation': False,
            'skip_initial_sync': False,
            'different_secondary_wwn': False,
            'remove_secondary_volume': False,
            'target_name': 'targetName1',
            'starting_snapshots': ['volName1','snapShot1'],
            'no_snapshot': False,
            'no_resync_snapshot': False,
            'full_sync': False,
            'recovery_action': 'REVERSE_GROUP',
            'skip_start': False,
            'skip_sync': False,
            'discard_new_data': False,
            'skip_promote': False,
            'stop_groups': False,
            'local_groups_direction': False,
            'volume_name': 'volume_1',
            'wait_for_task_to_end': False
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_stop_remote_copy_group.return_value = (
            True, True, "Stopped Remote Copy Group successfully.", {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Stopped Remote Copy Group successfully.")
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)	


    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.synchronize_remote_copy_group')
    def test_main_exit_synchronize_remote_copy_group(self, mock_synchronize_remote_copy_group, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'synchronize',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'targets': [{'targetName': 'CSSOS-SSA04','mode': 1}],
            'local_user_cpg': 'localusrcpg1',
            'local_snap_cpg': 'snap_cpg1',
            'keep_snap': False,
            'unset_user_cpg': False,
            'unset_snap_cpg': False,
            'snapshot_name': 'snapshot_1',
            'volume_auto_creation': False,
            'skip_initial_sync': False,
            'different_secondary_wwn': False,
            'remove_secondary_volume': False,
            'target_name': 'targetName1',
            'starting_snapshots': ['volName1','snapShot1'],
            'no_snapshot': False,
            'no_resync_snapshot': False,
            'full_sync': False,
            'recovery_action': 'REVERSE_GROUP',
            'skip_start': False,
            'skip_sync': False,
            'discard_new_data': False,
            'skip_promote': False,
            'stop_groups': False,
            'local_groups_direction': False,
            'volume_name': 'volume_1',
            'wait_for_task_to_end': False
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_synchronize_remote_copy_group.return_value = (
            True, True, "Synchronized Remote Copy Group successfully.", {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Synchronized Remote Copy Group successfully.")
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)	

    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.recover_remote_copy_group')
    def test_main_exit_recover_remote_copy_group(self, mock_recover_remote_copy_group, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'recover',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'targets': [{'targetName': 'CSSOS-SSA04','mode': 1}],
            'local_user_cpg': 'localusrcpg1',
            'local_snap_cpg': 'snap_cpg1',
            'keep_snap': False,
            'unset_user_cpg': False,
            'unset_snap_cpg': False,
            'snapshot_name': 'snapshot_1',
            'volume_auto_creation': False,
            'skip_initial_sync': False,
            'different_secondary_wwn': False,
            'remove_secondary_volume': False,
            'target_name': 'targetName1',
            'starting_snapshots': ['volName1','snapShot1'],
            'no_snapshot': False,
            'no_resync_snapshot': False,
            'full_sync': False,
            'recovery_action': 'REVERSE_GROUP',
            'skip_start': False,
            'skip_sync': False,
            'discard_new_data': False,
            'skip_promote': False,
            'stop_groups': False,
            'local_groups_direction': False,
            'volume_name': 'volume_1',
            'wait_for_task_to_end': False
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_recover_remote_copy_group.return_value = (
            True, True, "Synchronized Remote Copy Group successfully.", {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Synchronized Remote Copy Group successfully.")
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)    


    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_create_remote_copy_group(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = False
        mock_client.HPE3ParClient.createRemoteCopyGroup.return_value = True
        mock_client.HPE3ParClient.logout.return_value = True

        self.assertEqual(hpe3par_remote_copy.create_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'test_domain',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'localusrcpg1',
                                                'snap_cpg1'
                                                ), (True, True, "Created Remote Copy Group %s successfully." % 'rcg_1', {}))
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        self.assertEqual(hpe3par_remote_copy.create_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'test_domain',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'localusrcpg1',
                                                'snap_cpg1'
                                                ), (True, False, "Remote Copy Group already present", {}))
        self.assertEqual(hpe3par_remote_copy.create_remote_copy_group(mock_client.HPE3ParClient,
                                                None,
                                                'PASS',
                                                'rcg_1',
                                                'test_domain',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'localusrcpg1',
                                                'snap_cpg1'
                                                ), (False, False, "Remote Copy Group create failed. Storage system username or password is null", {}))
        self.assertEqual(hpe3par_remote_copy.create_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                'test_domain',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'localusrcpg1',
                                                'snap_cpg1'
                                                ), (False, False, "Remote Copy Group create failed. Remote Copy Group name is null", {}))
        self.assertEqual(hpe3par_remote_copy.create_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                'test_domain',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'localusrcpg1',
                                                'snap_cpg1'
                                                ), (False, False, "Remote Copy Group create failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {}))

        self.assertEqual(hpe3par_remote_copy.create_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'test_domain',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                None,
                                                'snap_cpg1'
                                                ), (False, False, "Either both local_user_cpg and local_snap_cpg must be present, or none of them must be present", {}))

    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_delete_remote_copy_group(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.removeRemoteCopyGroup.return_value = True
        mock_client.HPE3ParClient.logout.return_value = True
        

        self.assertEqual(hpe3par_remote_copy.delete_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                False
                                                ), (True, True, "Deleted Remote Copy Group %s successfully." % 'rcg_1', {}))

        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.delete_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                False
                                                ), (True, False, "Remote Copy Group is already present", {}))
        self.assertEqual(hpe3par_remote_copy.delete_remote_copy_group(mock_client.HPE3ParClient,
                                                None,
                                                'PASS',
                                                'rcg_1',
                                                False
                                                ), (False, False, "Remote Copy Group delete failed. Storage system username or password is null", {}))
        self.assertEqual(hpe3par_remote_copy.delete_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                False
                                                ), (False, False, "Remote Copy Group delete failed. Remote Copy Group name is null", {}))
        self.assertEqual(hpe3par_remote_copy.delete_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                False
                                                ), (False, False, "Remote Copy Group delete failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {}))

    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_start_remote_copy_group(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.startRemoteCopy.return_value = True
        mock_client.HPE3ParClient.logout.return_value = True
        

        self.assertEqual(hpe3par_remote_copy.start_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                False,
                                                'CSSOS-SSA04',
                                                ['volName1','snapShot1']
                                                ), (True, True, "Remote copy group %s started successfully." % 'rcg_1', {}))

        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.start_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                False,
                                                'CSSOS-SSA04',
                                                ['volName1','snapShot1']
                                                ), (False, False, "Remote Copy Group not present", {}))
        self.assertEqual(hpe3par_remote_copy.start_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                False,
                                                'CSSOS-SSA04',
                                                ['volName1','snapShot1']
                                                ), (False, False, "Start Remote Copy Group failed. Remote Copy Group name is null", {}))
        self.assertEqual(hpe3par_remote_copy.start_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                False,
                                                'CSSOS-SSA04',
                                                ['volName1','snapShot1']
                                                ), (False, False, "Start Remote Copy Group failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {}))
 
    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_stop_remote_copy_group(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.stopRemoteCopy.return_value = True
        mock_client.HPE3ParClient.logout.return_value = True
        

        self.assertEqual(hpe3par_remote_copy.stop_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                True,
                                                'CSSOS-SSA04'
                                                ), (True, True, "Remote copy group %s stopped successfully." % 'rcg_1', {}))
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.stop_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                True,
                                                'CSSOS-SSA04'
                                                ), (False, False, "Remote Copy Group not present", {}))
        self.assertEqual(hpe3par_remote_copy.stop_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                True,
                                                'CSSOS-SSA04'
                                                ), (False, False, "Stop Remote Copy Group failed. Remote Copy Group name is null", {}))
        self.assertEqual(hpe3par_remote_copy.stop_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                True,
                                                'CSSOS-SSA04'
                                                ), (False, False, "Stop Remote Copy Group failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {}))                                        

    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_add_volume_to_remote_copy_group(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.addVolumeToRemoteCopyGroup.return_value = True
        mock_client.HPE3ParClient.logout.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupVolumeExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.add_volume_to_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'volume_1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'snapshot_1',
                                                False,
                                                False,
                                                False
                                                ), (True, True, "Volume %s added to Remote Copy Group %s successfully." % ('volume_1', 'rcg_1'), {}))
        mock_client.HPE3ParClient.remoteCopyGroupVolumeExists.return_value = True
        self.assertEqual(hpe3par_remote_copy.add_volume_to_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'volume_1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'snapshot_1',
                                                False,
                                                False,
                                                False
                                                ), (True, False, "Volume %s already present in Remote Copy Group %s" % ('volume_1', 'rcg_1'), {})) 
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.add_volume_to_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'volume_1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'snapshot_1',
                                                False,
                                                False,
                                                False
                                                ), (False, False, "Remote Copy Group not present", {}))
        self.assertEqual(hpe3par_remote_copy.add_volume_to_remote_copy_group(mock_client.HPE3ParClient,
                                                None,
                                                'PASS',
                                                'rcg_1',
                                                'volume_1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'snapshot_1',
                                                False,
                                                False,
                                                False
                                                ), (False, False, "Add volume to Remote Copy Group failed. Storage system username or password is null", {}))
        self.assertEqual(hpe3par_remote_copy.add_volume_to_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                'volume_1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'snapshot_1',
                                                False,
                                                False,
                                                False
                                                ), (False, False, "Add volume to Remote Copy Group failed. Remote Copy Group name is null", {}))
        self.assertEqual(hpe3par_remote_copy.add_volume_to_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                'volume_1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'snapshot_1',
                                                False,
                                                False,
                                                False
                                                ), (False, False, "Add volume to Remote Copy Group failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {}))                                        
        self.assertEqual(hpe3par_remote_copy.add_volume_to_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                None,
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'snapshot_1',
                                                False,
                                                False,
                                                False
                                                ), (False, False, "Add volume to Remote Copy Group failed. Volume name is null", {}))
        self.assertEqual(hpe3par_remote_copy.add_volume_to_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'snapshot_1',
                                                False,
                                                False,
                                                False
                                                ), (False, False, "Add volume to Remote Copy Group failed. Volume name must be atleast 1 character and not more than 31 characters", {}))                                        
        self.assertEqual(hpe3par_remote_copy.add_volume_to_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'volume_1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'snapshot_1',
                                                True,
                                                False,
                                                False
                                                ), (False, False, "Add volume to Remote Copy Group failed. volumeAutoCreation cannot be true if snapshot name is given", {}))
        self.assertEqual(hpe3par_remote_copy.add_volume_to_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'volume_1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                'snapshot_1',
                                                False,
                                                True,
                                                False
                                                ), (False, False, "Add volume to Remote Copy Group failed. skipInitialSync cannot be true if snapshot name is given", {}))
        self.assertEqual(hpe3par_remote_copy.add_volume_to_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'volume_1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                None,
                                                False,
                                                False,
                                                True
                                                ), (False, False, "Add volume to Remote Copy Group failed. skipInitialSync cannot be true if snapshot name is not given", {}))

    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_remove_volume_from_remote_copy_group(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.removeVolumeFromRemoteCopyGroup.return_value = True
        mock_client.HPE3ParClient.logout.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupVolumeExists.return_value = True

        self.assertEqual(hpe3par_remote_copy.remove_volume_from_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'volume_1',
                                                False,
                                                False
                                                ), (True, True, "Volume %s removed from Remote Copy Group %s successfully." % ('volume_1', 'rcg_1'), {}))
        mock_client.HPE3ParClient.remoteCopyGroupVolumeExists.return_value = False
        self.assertEqual(hpe3par_remote_copy.remove_volume_from_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'volume_1',
                                                False,
                                                False
                                                ), (True, False, "Volume %s is not present in Remote Copy Group %s" % ('volume_1', 'rcg_1'), {}))
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.remove_volume_from_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'volume_1',
                                                False,
                                                False
                                                ), (False, False, "Remote Copy Group not present", {}))
        self.assertEqual(hpe3par_remote_copy.remove_volume_from_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                'volume_1',
                                                False,
                                                False
                                                ), (False, False, "Remove volume to Remote Copy Group failed. Remote Copy Group name is null", {}))
        self.assertEqual(hpe3par_remote_copy.remove_volume_from_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                'volume_1',
                                                False,
                                                False
                                                ), (False, False, "Remove volume to Remote Copy Group failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {}))                                        
        self.assertEqual(hpe3par_remote_copy.remove_volume_from_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                None,
                                                False,
                                                False
                                                ), (False, False, "Remove volume to Remote Copy Group failed. Volume name is null", {}))
        self.assertEqual(hpe3par_remote_copy.remove_volume_from_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                False,
                                                False
                                                ), (False, False, "Remove volume to Remote Copy Group failed. Volume name must be atleast 1 character and not more than 31 characters", {}))                                        
        self.assertEqual(hpe3par_remote_copy.remove_volume_from_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'volume_1',
                                                True,
                                                True
                                                ), (False, False, "Remove volume to Remote Copy Group failed. keepSnap and removeSecondaryVolume cannot both be true", {}))

    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_synchronize_remote_copy_group(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.synchronizeRemoteCopyGroup.return_value = True
        mock_client.HPE3ParClient.logout.return_value = True


        self.assertEqual(hpe3par_remote_copy.synchronize_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                False,
                                                'CSSOS-SSA04',
                                                False,
                                                False
                                                ), (True, True, "Remote copy group %s resynchronized successfully." % 'rcg_1', {}))
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.synchronize_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                False,
                                                'CSSOS-SSA04',
                                                False,
                                                False
                                                ), (False, False, "Remote Copy Group not present", {}))
        self.assertEqual(hpe3par_remote_copy.synchronize_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                False,
                                                'CSSOS-SSA04',
                                                False,
                                                False
                                                ), (False, False, "Synchronize Remote Copy Group failed. Remote Copy Group name is null", {}))
        self.assertEqual(hpe3par_remote_copy.synchronize_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                False,
                                                'CSSOS-SSA04',
                                                False,
                                                False
                                                ), (False, False, "Synchronize Remote Copy Group failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {}))                                        

    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_modify_remote_copy_group(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.modifyRemoteCopyGroup.return_value = True
        mock_client.HPE3ParClient.logout.return_value = True
        

        self.assertEqual(hpe3par_remote_copy.modify_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'localusrcpg1',
                                                'snap_cpg1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                False,
                                                False
                                                ), (True, True, "Modify Remote Copy Group %s successfully." % 'rcg_1', {}))
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.modify_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'localusrcpg1',
                                                'snap_cpg1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                False,
                                                False
                                                ), (True, False, "Remote Copy Group not present", {}))
        self.assertEqual(hpe3par_remote_copy.modify_remote_copy_group(mock_client.HPE3ParClient,
                                                None,
                                                'PASS',
                                                'rcg_1',
                                                'localusrcpg1',
                                                'snap_cpg1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                False,
                                                False
                                                ), (False, False, "Remote Copy Group modify failed. Storage system username or password is null", {}))
        self.assertEqual(hpe3par_remote_copy.modify_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                'localusrcpg1',
                                                'snap_cpg1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                False,
                                                False
                                                ), (False, False, "Remote Copy Group modify failed. Remote Copy Group name is null", {}))
        self.assertEqual(hpe3par_remote_copy.modify_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                'localusrcpg1',
                                                'snap_cpg1',
                                                [{'targetName': 'CSSOS-SSA04','mode': 1}],
                                                False,
                                                False
                                                ), (False, False, "Remote Copy Group modify failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {})) 

