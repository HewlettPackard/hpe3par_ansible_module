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
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
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
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
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
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
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
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
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
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
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
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
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
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
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
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
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
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
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
    @mock.patch('Modules.hpe3par_remote_copy.admit_remote_copy_links')
    def test_main_exit_admit_remote_copy_links(self, mock_admit_remote_copy_links, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'admit_link',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_admit_remote_copy_links.return_value = (
            True, True, "Admit remote copy link %s:%s successful." % ('0:3:1', '192.168.1.2'), {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Admit remote copy link %s:%s successful." % ('0:3:1', '192.168.1.2'))
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)

    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.dismiss_remote_copy_links')
    def test_main_exit_dismiss_remote_copy_links(self, mock_dismiss_remote_copy_links, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'dismiss_link',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_dismiss_remote_copy_links.return_value = (
            True, True, "Dismiss remote copy link %s:%s successful." % (PARAMS_FOR_PRESENT['source_port'], PARAMS_FOR_PRESENT['target_port_wwn_or_ip']), {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Dismiss remote copy link %s:%s successful." % (PARAMS_FOR_PRESENT['source_port'], PARAMS_FOR_PRESENT['target_port_wwn_or_ip']))
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)

    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.start_remote_copy_service')
    def test_main_exit_start_remote_copy_service(self, mock_start_remote_copy_service, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'start_rcopy',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_start_remote_copy_service.return_value = (
            True, True, "Start remote copy service successful.", {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Start remote copy service successful.")
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)

    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.admit_remote_copy_target')
    def test_main_exit_admit_remote_copy_target(self, mock_admit_remote_copy_target, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'admit_target',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_admit_remote_copy_target.return_value = (
            True, True, "Admit remote copy target %s successful in remote copy group %s."
            % (PARAMS_FOR_PRESENT['target_name'], PARAMS_FOR_PRESENT['remote_copy_group_name']), {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Admit remote copy target %s successful in remote copy group %s."
            % (PARAMS_FOR_PRESENT['target_name'], PARAMS_FOR_PRESENT['remote_copy_group_name']))
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)

    @mock.patch('Modules.hpe3par_remote_copy.client')
    @mock.patch('Modules.hpe3par_remote_copy.AnsibleModule')
    @mock.patch('Modules.hpe3par_remote_copy.dismiss_remote_copy_target')
    def test_main_exit_dismiss_remote_copy_target(self, mock_dismiss_remote_copy_target, mock_module, mock_client):
        """
        hpe3par flash cache - success check
        """
        PARAMS_FOR_PRESENT = {
            'state': 'dismiss_target',
            'storage_system_ip': '192.168.0.1',
            'storage_system_username': 'USER',
            'storage_system_password': 'PASS',
            'remote_copy_group_name': 'rcg_name_1',
            'domain': 'test_domain',
            'remote_copy_targets': [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
            'admit_volume_targets': [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'demo_volume_1'}],
            'modify_targets': [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg': 'FC_r6'}],
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
            'target_name': 'target_name1',
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
            'source_port': '0:3:1',
            'target_port_wwn_or_ip': '192.168.1.2',
            'local_remote_volume_pair_list': [('local_v1','remote_v1'),('local_v2','remote_v2')],
            'target_mode': 'sync'
        }
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_dismiss_remote_copy_target.return_value = (
            True, True, "Dismiss remote copy target %s successful." % (PARAMS_FOR_PRESENT['target_name']), {})
        hpe3par_remote_copy.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Dismiss remote copy target %s successful." % (PARAMS_FOR_PRESENT['target_name']))
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
                                                [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
                                                'localusrcpg1',
                                                'snap_cpg1'
                                                ), (True, True, "Created Remote Copy Group %s successfully." % 'rcg_1', {}))
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        self.assertEqual(hpe3par_remote_copy.create_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'test_domain',
                                                [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
                                                'localusrcpg1',
                                                'snap_cpg1'
                                                ), (True, False, "Remote Copy Group already present", {}))
        self.assertEqual(hpe3par_remote_copy.create_remote_copy_group(mock_client.HPE3ParClient,
                                                None,
                                                'PASS',
                                                'rcg_1',
                                                'test_domain',
                                                [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
                                                'localusrcpg1',
                                                'snap_cpg1'
                                                ), (False, False, "Remote Copy Group create failed. Storage system username or password is null", {}))
        self.assertEqual(hpe3par_remote_copy.create_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                'test_domain',
                                                [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
                                                'localusrcpg1',
                                                'snap_cpg1'
                                                ), (False, False, "Remote Copy Group create failed. Remote Copy Group name is null", {}))
        self.assertEqual(hpe3par_remote_copy.create_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                'test_domain',
                                                [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
                                                'localusrcpg1',
                                                'snap_cpg1'
                                                ), (False, False, "Remote Copy Group create failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {}))

        self.assertEqual(hpe3par_remote_copy.create_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'test_domain',
                                                [{'target_name': 'CSSOS-SSA04','target_mode': 'sync'}],
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
                                                ), (True, False, "Remote Copy Group is not present", {}))
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
        mock_client.HPE3ParClient.remoteCopyGroupStatusStartedCheck.return_value = False
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
        mock_client.HPE3ParClient.remoteCopyGroupStatusStartedCheck.return_value = True
        self.assertEqual(hpe3par_remote_copy.start_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                False,
                                                'CSSOS-SSA04',
                                                ['volName1','snapShot1']
                                                ), (True, False, "Remote Copy Group is already started", {}))

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
        mock_client.HPE3ParClient.remoteCopyGroupStatusStoppedCheck.return_value = False
        mock_client.HPE3ParClient.logout.return_value = True
        

        self.assertEqual(hpe3par_remote_copy.stop_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                True,
                                                'CSSOS-SSA04'
                                                ), (True, True, "Remote copy group %s stopped successfully." % 'rcg_1', {}))
        mock_client.HPE3ParClient.remoteCopyGroupStatusStoppedCheck.return_value = True
        self.assertEqual(hpe3par_remote_copy.stop_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                True,
                                                'CSSOS-SSA04'
                                                ), (True, False, "Remote Copy Group is already stopped", {}))
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
                                                [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'volume_1'}],
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
                                                [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'volume_1'}],
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
                                                [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'volume_1'}],
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
                                                [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'volume_1'}],
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
                                                [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'volume_1'}],
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
                                                [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'volume_1'}],
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
                                                [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'volume_1'}],
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
                                                [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'volume_1'}],
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
                                                [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'volume_1'}],
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
                                                [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'volume_1'}],
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
                                                [{'target_name': 'CSSOS-SSA04','sec_volume_name': 'volume_1'}],
                                                None,
                                                False,
                                                False,
                                                True
                                                ), (False, False, "Add volume to Remote Copy Group failed. differentSecondaryWWN cannot be true if volumeAutoCreation is false", {}))

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
                                                ), (False, False, "Remove volume from Remote Copy Group failed. Remote Copy Group name is null", {}))
        self.assertEqual(hpe3par_remote_copy.remove_volume_from_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                'volume_1',
                                                False,
                                                False
                                                ), (False, False, "Remove volume from Remote Copy Group failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {}))                                        
        self.assertEqual(hpe3par_remote_copy.remove_volume_from_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                None,
                                                False,
                                                False
                                                ), (False, False, "Remove volume from Remote Copy Group failed. Volume name is null", {}))
        self.assertEqual(hpe3par_remote_copy.remove_volume_from_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                False,
                                                False
                                                ), (False, False, "Remove volume from Remote Copy Group failed. Volume name must be atleast 1 character and not more than 31 characters", {}))                                        
        self.assertEqual(hpe3par_remote_copy.remove_volume_from_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'volume_1',
                                                True,
                                                True
                                                ), (False, False, "Remove volume from Remote Copy Group failed. keepSnap and removeSecondaryVolume cannot both be true", {}))

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
                                                False
                                                ), (True, True, "Remote copy group %s resynchronize started successfully." % 'rcg_1', {}))
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.synchronize_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                False,
                                                'CSSOS-SSA04',
                                                False
                                                ), (False, False, "Remote Copy Group not present", {}))
        self.assertEqual(hpe3par_remote_copy.synchronize_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                False,
                                                'CSSOS-SSA04',
                                                False
                                                ), (False, False, "Synchronize Remote Copy Group failed. Remote Copy Group name is null", {}))
        self.assertEqual(hpe3par_remote_copy.synchronize_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                False,
                                                'CSSOS-SSA04',
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
                                                [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg':'FC_r6'}],
                                                False,
                                                False
                                                ), (True, True, "Modify Remote Copy Group %s successfully." % 'rcg_1', {}))

        self.assertEqual(hpe3par_remote_copy.modify_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'localusrcpg1',
                                                'snap_cpg1',
                                                [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg':'FC_r6','snap_frequency':30}],
                                                False,
                                                False
                                                ), (False, False, "Remote Copy Group modification failed. Valid range of snap_frequency is 300-31622400.", {}))

        self.assertEqual(hpe3par_remote_copy.modify_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'localusrcpg1',
                                                'snap_cpg1',
                                                [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg':'FC_r6','sync_period':30}],
                                                False,
                                                False
                                                ), (False, False, "Remote Copy Group modification failed. Valid range of sync_period is 300-31622400.", {}))
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.modify_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'rcg_1',
                                                'localusrcpg1',
                                                'snap_cpg1',
                                                [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg':'FC_r6'}],
                                                False,
                                                False
                                                ), (False, False, "Remote Copy Group not present", {}))
        self.assertEqual(hpe3par_remote_copy.modify_remote_copy_group(mock_client.HPE3ParClient,
                                                None,
                                                'PASS',
                                                'rcg_1',
                                                'localusrcpg1',
                                                'snap_cpg1',
                                                [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg':'FC_r6'}],
                                                False,
                                                False
                                                ), (False, False, "Remote Copy Group modify failed. Storage system username or password is null", {}))
        self.assertEqual(hpe3par_remote_copy.modify_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                'localusrcpg1',
                                                'snap_cpg1',
                                                [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg':'FC_r6'}],
                                                False,
                                                False
                                                ), (False, False, "Remote Copy Group modify failed. Remote Copy Group name is null", {}))
        self.assertEqual(hpe3par_remote_copy.modify_remote_copy_group(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                'remotesdfssfsdssdfsdfdfsfsdfsdfsdfsfsdfsfsdfsdfsdf',
                                                'localusrcpg1',
                                                'snap_cpg1',
                                                [{'target_name': 'CSSOS-SSA04','remote_user_cpg': 'FC_r1','remote_snap_cpg':'FC_r6'}],
                                                False,
                                                False
                                                ), (False, False, "Remote Copy Group modify failed. Remote Copy Group name must be atleast 1 character and not more than 31 characters", {}))

    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_admit_remote_copy_links(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.setSSHOptions.return_value = True
        mock_client.HPE3ParClient.rcopyLinkExists.return_value = False
        mock_client.HPE3ParClient.admitRemoteCopyLinks.return_value = True
        mock_client.HPE3ParClient.logout.return_value = True
        
        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_links(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                '0:3:1',
                                                '192.168.1.2'
                                                ), (True, True, "Admit remote copy link %s:%s successful." % ('0:3:1', '192.168.1.2'), {}))
        mock_client.HPE3ParClient.rcopyLinkExists.return_value = True

        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_links(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                '0:3:1',
                                                '192.168.1.2'
                                                ), (True, False, "Admit remote copy link %s:%s already exists." % ('0:3:1', '192.168.1.2'), {}))
        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_links(mock_client.HPE3ParClient,
                                                None,
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                '0:3:1',
                                                '192.168.1.2'
                                                ), (False, False, "Admit remote copy link failed. Storage system username or password is null", {}))
        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_links(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                'target_name1',
                                                '0:3:1',
                                                '192.168.1.2'
                                                ), (False, False, "Admit remote copy link failed. Storage system IP address is null", {}))
        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_links(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                None,
                                                '0:3:1',
                                                '192.168.1.2'
                                                ), (False, False, "Admit remote copy link failed. Target name is null", {}))
        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_links(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                None,
                                                '192.168.1.2'
                                                ), (False, False, "Admit remote copy link failed. Source port address is null", {}))
        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_links(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                '0:3:1',
                                                None
                                                ), (False, False, "Admit remote copy link failed. Target port WWN/IP is null", {}))

    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_dismiss_remote_copy_links(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.setSSHOptions.return_value = True
        mock_client.HPE3ParClient.rcopyLinkExists.return_value = True
        mock_client.HPE3ParClient.admitRemoteCopyLinks.return_value = True
        mock_client.HPE3ParClient.logout.return_value = True
        
        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_links(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                '0:3:1',
                                                '192.168.1.2'
                                                ), (True, True, "Dismiss remote copy link %s:%s successful." % ('0:3:1', '192.168.1.2'), {}))
        mock_client.HPE3ParClient.rcopyLinkExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_links(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                '0:3:1',
                                                '192.168.1.2'
                                                ), (True, False, "Remote copy link %s:%s already not present." % ('0:3:1', '192.168.1.2'), {}))
        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_links(mock_client.HPE3ParClient,
                                                None,
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                '0:3:1',
                                                '192.168.1.2'
                                                ), (False, False, "Dismiss remote copy link failed. Storage system username or password is null", {}))
        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_links(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                'target_name1',
                                                '0:3:1',
                                                '192.168.1.2'
                                                ), (False, False, "Dismiss remote copy link failed. Storage system IP address is null", {}))
        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_links(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                None,
                                                '0:3:1',
                                                '192.168.1.2'
                                                ), (False, False, "Dismiss remote copy link failed. Target name is null", {}))
        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_links(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                None,
                                                '192.168.1.2'
                                                ), (False, False, "Dismiss remote copy link failed. Source port address is null", {}))
        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_links(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                '0:3:1',
                                                None
                                                ), (False, False, "Dismiss remote copy link failed. Target port WWN/IP is null", {}))

    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_start_remote_copy_service(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.setSSHOptions.return_value = True
        mock_client.HPE3ParClient.rcopyServiceExists.return_value = False
        mock_client.HPE3ParClient.startrCopy.return_value = True
        mock_client.HPE3ParClient.logout.return_value = True

        self.assertEqual(hpe3par_remote_copy.start_remote_copy_service(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                ), (True, True, "Start remote copy service successful.", {}))
        mock_client.HPE3ParClient.rcopyServiceExists.return_value = True

        self.assertEqual(hpe3par_remote_copy.start_remote_copy_service(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                ), (True, False, "Remote copy service already started", {}))
        self.assertEqual(hpe3par_remote_copy.start_remote_copy_service(mock_client.HPE3ParClient,
                                                None,
                                                'PASS',
                                                '192.168.0.1',
                                                ), (False, False, "Start remote copy service failed. Storage system username or password is null", {}))
        self.assertEqual(hpe3par_remote_copy.start_remote_copy_service(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                ), (False, False, "Start remote copy service failed. Storage system IP address is null", {}))

    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_admit_remote_copy_target(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.setSSHOptions.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.admitRemoteCopyTarget.return_value = True
        mock_client.HPE3ParClient.targetInRemoteCopyGroupExists.return_value = False
        mock_client.HPE3ParClient.logout.return_value = True

        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                'sync',
                                                'rcg_1',
                                                [('local_v1','remote_v1'),('local_v2','remote_v2')]
                                                ), (True, True, "Admit remote copy target %s successful in remote copy group %s." % ('target_name1', 'rcg_1'), {}))

        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                'sync',
                                                'rcg_1',
                                                [('local_v1','remote_v1'),('local_v2','remote_v2')]
                                                ), (False, False, "Remote Copy Group is not present", {}))

        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_target(mock_client.HPE3ParClient,
                                                None,
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                'sync',
                                                'rcg_1',
                                                [('local_v1','remote_v1'),('local_v2','remote_v2')]
                                                ), (False, False, "Admit remote copy target failed. Storage system username or password is null", {}))
        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                None,
                                                'sync',
                                                'rcg_1',
                                                [('local_v1','remote_v1'),('local_v2','remote_v2')]
                                                ), (False, False, "Admit remote copy target failed. Target name is null", {}))
        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                'target_name1',
                                                'sync',
                                                'rcg_1',
                                                [('local_v1','remote_v1'),('local_v2','remote_v2')]
                                                ), (False, False, "Admit remote copy target failed. Storage system IP address is null", {}))
        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                None,
                                                'rcg_1',
                                                [('local_v1','remote_v1'),('local_v2','remote_v2')]
                                                ), (False, False, "Admit remote copy target failed. Mode is null", {}))
        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                'sync',
                                                None,
                                                [('local_v1','remote_v1'),('local_v2','remote_v2')]
                                                ), (False, False, "Admit remote copy target failed. Remote copy group name is null", {}))

        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.targetInRemoteCopyGroupExists.return_value = True
        self.assertEqual(hpe3par_remote_copy.admit_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                'sync',
                                                'rcg_1',
                                                [('local_v1','remote_v1'),('local_v2','remote_v2')]
                                                ), (True, False, "Admit remote copy target failed.Target is already present", {}))

    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_dismiss_remote_copy_target(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.setSSHOptions.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.dismissRemoteCopyTarget.return_value = True
        mock_client.HPE3ParClient.targetInRemoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.logout.return_value = True

        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                'rcg_1',
                                                ), (True, True, "Dismiss remote copy target %s successful." % 'target_name1', {}))

        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = False

        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                'rcg_1'
                                                ), (False, False, "Remote Copy Group %s is not present" % 'rcg_1', {}))

        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_target(mock_client.HPE3ParClient,
                                                None,
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                'rcg_1',
                                                ), (False, False, "Dismiss remote copy target failed. Storage system username or password is null", {}))
        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                None,
                                                'rcg_1'
                                                ), (False, False, "Dismiss remote copy target failed. Target name is null", {}))
        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                'target_name1',
                                                'rcg_1'
                                                ), (False, False, "Dismiss remote copy target failed. Storage system IP address is null", {}))
        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                None,
                                                ), (False, False, "Dismiss remote copy target failed. Remote copy group name is null", {}))

        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.targetInRemoteCopyGroupExists.return_value = False
        self.assertEqual(hpe3par_remote_copy.dismiss_remote_copy_target(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'target_name1',
                                                'rcg_1'
                                                ), (True, False, "Dismiss remote copy target failed. Target %s is already not present in remote copy group %s" %('target_name1','rcg_1' ), {}))

    @mock.patch('Modules.hpe3par_remote_copy.client')
    def test_remote_copy_group_status(self, mock_client):
        mock_client.HPE3ParClient.login.return_value = True
        mock_client.HPE3ParClient.setSSHOptions.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupExists.return_value = True
        mock_client.HPE3ParClient.remoteCopyGroupStatusCheck.return_value = True

        mock_client.HPE3ParClient.logout.return_value = True

        self.assertEqual(hpe3par_remote_copy.remote_copy_group_status(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'rcg_1',
                                                ), (True, False, "Remote copy group %s status is complete" % 'rcg_1', {"remote_copy_sync_status":True}))

        mock_client.HPE3ParClient.remoteCopyGroupStatusCheck.return_value = False
        self.assertEqual(hpe3par_remote_copy.remote_copy_group_status(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                'rcg_1',
                                                ), (True, False, "Remote copy group %s status is not in complete" % 'rcg_1', {"remote_copy_sync_status":False}))

        self.assertEqual(hpe3par_remote_copy.remote_copy_group_status(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                '192.168.0.1',
                                                None,
                                                ), (False, False, "Remote copy group status failed. Remote copy group name is null", {}))

        self.assertEqual(hpe3par_remote_copy.remote_copy_group_status(mock_client.HPE3ParClient,
                                                'USER',
                                                'PASS',
                                                None,
                                                'rcg_1',
                                                ), (False, False, "Remote copy group status failed. Storage system IP address is null", {}))

        self.assertEqual(hpe3par_remote_copy.remote_copy_group_status(mock_client.HPE3ParClient,
                                                'USER',
                                                None,
                                                '192.168.0.1',
                                                'rcg_1',
                                                ), (False, False, "Remote copy group status failed. Storage system username or password is null", {}))
