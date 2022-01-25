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
from Modules import hpe3par_volume_facts as volume_facts
import unittest


class TestHpe3parVolumeFacts(unittest.TestCase):

    PARAMS = {'storage_system_username': 'USER', 'storage_system_ip': '192.168.0.1', 
              'storage_system_password': 'PASS', 'volume_name': 'volume'}

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
        "volume_name": {
            "type": "str"
        }
    }

    @mock.patch('Modules.hpe3par_volume_facts.client')
    @mock.patch('Modules.hpe3par_volume_facts.AnsibleModule')
    def test_module_args(self, mock_module, mock_client):
        """
        hpe3par volume facts - test module arguments
        """

        mock_module.params = self.PARAMS
        mock_module.return_value = mock_module
        volume_facts.main()
        mock_module.assert_called_with(
            argument_spec=self.fields)

    @mock.patch('Modules.hpe3par_volume_facts.client')
    def test_exception_in_login(self, mock_client):
        """
        hpe3par volume facts - login error exit fail check
        """
        mock_client.HPE3ParClient.login.side_effect = Exception(
            "Failed to login!")
        result = volume_facts.get_volumes(
            mock_client.HPE3ParClient, "user", "password", None)

        self.assertEqual(
            result, (False, "execution error | Failed to login!", {}))

    @mock.patch('Modules.hpe3par_volume_facts.client')
    def test_get_volume_username_empty(self, mock_client):
        """
        hpe3par volume facts - get volumes
        """
        result = volume_facts.get_volumes(mock_client, None, "PASS", None)

        self.assertEqual(result, (
            False,
            "Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_volume_facts.client')
    def test_get_volume_password_empty(self, mock_client):
        """
        hpe3par volume facts - get volumes
        """
        result = volume_facts.get_volumes(mock_client, "USER", None, None)

        self.assertEqual(result, (
            False,
            "Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_volume_facts.client')
    def test_main_exit_functionality_fail_volume_doesnt_exists(self, mock_client):
        """
        hpe3par volume facts - volume does not exists exit fail check
        """
        mock_client.HPE3ParClient.volumeExists.return_value = False
        result = volume_facts.get_volumes(
            mock_client.HPE3ParClient, "user", "password", "hostname")
        self.assertEqual(result, (False, "volume does not exists", {}))

    @mock.patch('Modules.hpe3par_volume_facts.client')
    @mock.patch('Modules.hpe3par_volume_facts.AnsibleModule')
    @mock.patch('Modules.hpe3par_volume_facts.get_volumes')
    def test_main_exit_functionality_success_with_volume_name(self, mock_volume_facts, mock_module, mock_client):
        """
        hpe3par volume facts - volume by name success check
        """

        RESULT = [
            {
                "additional_states": [],
                "admin_space": {
                    "free_MiB": 454,
                    "raw_reserved_MiB": 1536,
                    "reserved_MiB": 512,
                    "used_MiB": 58
                },
                "base_id": 228,
                "capacity_efficiency": {
                    "compaction": 49.3,
                    "compression": "null",
                    "data_reduction": "null",
                    "deduplication": "null",
                    "over_provisioning": "null"
                },
                "comment": "null",
                "compression_state": "null",
                "copy_of": "null",
                "copy_type": 1,
                "creation_time8601": "2020-02-18T17:30:12+01:00",
                "creation_time_sec": 1582043412,
                "deduplication_state": "null",
                "domain": "doamin",
                "expiration_time8601": "null",
                "expiration_time_sec": "null",
                "failed_states": [],
                "host_write_mib": "null",
                "id": 228,
                "links": [],
                "name": "ansible",
                "parent_id": "null",
                "phys_parent_id": "null",
                "policies": {
                    "caching": "true",
                    "fsvc": "false",
                    "host_dif": "null",
                    "one_host": "false",
                    "stale_ss": "true",
                    "system": "false",
                    "zero_detect": "true"
                },
                "provisioning_type": 2,
                "read_only": "false",
                "retention_time8601": "null",
                "retention_time_sec": "null",
                "ro_child_id": "null",
                "rw_child_id": "null",
                "shared_parent_id": "null",
                "size_mib": 819200,
                "snap_cpg": "null",
                "snapshot_space": {
                    "free_MiB": 0,
                    "raw_reserved_MiB": 0,
                    "reserved_MiB": 0,
                    "used_MiB": 0
                },
                "ss_spc_alloc_limit_pct": 0,
                "ss_spc_alloc_warning_pct": 0,
                "state": 1,
                "total_reserved_mib": "null",
                "total_used_mib": "null",
                "udid": "null",
                "user_cpg": "r1",
                "user_space": {
                    "free_MiB": 16348,
                    "raw_reserved_MiB": 37595,
                    "reserved_MiB": 32896,
                    "used_MiB": 16548
                },
                "usr_spc_alloc_limit_pct": 0,
                "usr_spc_alloc_warning_pct": 0,
                "uuid": "b7af74ab-740e-4157-85ae-40d3f42d1828",
                "wwn": "60002AC000000000000000010000518A"
            }
        ]

        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_volume_facts.return_value = (
            True, "", RESULT)

        volume_facts.main()

        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=False, ansible_facts=RESULT)
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)

    @mock.patch('Modules.hpe3par_volume_facts.client')
    @mock.patch('Modules.hpe3par_volume_facts.AnsibleModule')
    @mock.patch('Modules.hpe3par_volume_facts.get_volumes')
    def test_main_exit_functionality_success_without_volume_name(self, mock_volume_facts, mock_module, mock_client):
        """
        hpe3par volume facts - all volumes success check
        """

        RESULTS = [
            {
                "additional_states": [],
                "admin_space": {
                    "free_MiB": 454,
                    "raw_reserved_MiB": 1536,
                    "reserved_MiB": 512,
                    "used_MiB": 58
                },
                "base_id": 228,
                "capacity_efficiency": {
                    "compaction": 49.3,
                    "compression": "null",
                    "data_reduction": "null",
                    "deduplication": "null",
                    "over_provisioning": "null"
                },
                "comment": "null",
                "compression_state": "null",
                "copy_of": "null",
                "copy_type": 1,
                "creation_time8601": "2020-02-18T17:30:12+01:00",
                "creation_time_sec": 1582043412,
                "deduplication_state": "null",
                "domain": "doamin",
                "expiration_time8601": "null",
                "expiration_time_sec": "null",
                "failed_states": [],
                "host_write_mib": "null",
                "id": 228,
                "links": [],
                "name": "ansible",
                "parent_id": "null",
                "phys_parent_id": "null",
                "policies": {
                    "caching": "true",
                    "fsvc": "false",
                    "host_dif": "null",
                    "one_host": "false",
                    "stale_ss": "true",
                    "system": "false",
                    "zero_detect": "true"
                },
                "provisioning_type": 2,
                "read_only": "false",
                "retention_time8601": "null",
                "retention_time_sec": "null",
                "ro_child_id": "null",
                "rw_child_id": "null",
                "shared_parent_id": "null",
                "size_mib": 819200,
                "snap_cpg": "null",
                "snapshot_space": {
                    "free_MiB": 0,
                    "raw_reserved_MiB": 0,
                    "reserved_MiB": 0,
                    "used_MiB": 0
                },
                "ss_spc_alloc_limit_pct": 0,
                "ss_spc_alloc_warning_pct": 0,
                "state": 1,
                "total_reserved_mib": "null",
                "total_used_mib": "null",
                "udid": "null",
                "user_cpg": "r1",
                "user_space": {
                    "free_MiB": 16348,
                    "raw_reserved_MiB": 37595,
                    "reserved_MiB": 32896,
                    "used_MiB": 16548
                },
                "usr_spc_alloc_limit_pct": 0,
                "usr_spc_alloc_warning_pct": 0,
                "uuid": "b7af74ab-740e-4157-85ae-40d3f42d1828",
                "wwn": "60002AC000000000000000010000518A"
            },
            {
                "additional_states": [],
                "admin_space": {
                    "free_MiB": 454,
                    "raw_reserved_MiB": 1536,
                    "reserved_MiB": 512,
                    "used_MiB": 58
                },
                "base_id": 228,
                "capacity_efficiency": {
                    "compaction": 49.3,
                    "compression": "null",
                    "data_reduction": "null",
                    "deduplication": "null",
                    "over_provisioning": "null"
                },
                "comment": "null",
                "compression_state": "null",
                "copy_of": "null",
                "copy_type": 1,
                "creation_time8601": "2020-03-18T17:30:12+01:00",
                "creation_time_sec": 1582043412,
                "deduplication_state": "null",
                "domain": "doamin",
                "expiration_time8601": "null",
                "expiration_time_sec": "null",
                "failed_states": [],
                "host_write_mib": "null",
                "id": 228,
                "links": [],
                "name": "ansible2",
                "parent_id": "null",
                "phys_parent_id": "null",
                "policies": {
                    "caching": "true",
                    "fsvc": "false",
                    "host_dif": "null",
                    "one_host": "false",
                    "stale_ss": "true",
                    "system": "false",
                    "zero_detect": "true"
                },
                "provisioning_type": 2,
                "read_only": "false",
                "retention_time8601": "null",
                "retention_time_sec": "null",
                "ro_child_id": "null",
                "rw_child_id": "null",
                "shared_parent_id": "null",
                "size_mib": 819200,
                "snap_cpg": "null",
                "snapshot_space": {
                    "free_MiB": 0,
                    "raw_reserved_MiB": 0,
                    "reserved_MiB": 0,
                    "used_MiB": 0
                },
                "ss_spc_alloc_limit_pct": 0,
                "ss_spc_alloc_warning_pct": 0,
                "state": 1,
                "total_reserved_mib": "null",
                "total_used_mib": "null",
                "udid": "null",
                "user_cpg": "r1",
                "user_space": {
                    "free_MiB": 16348,
                    "raw_reserved_MiB": 37595,
                    "reserved_MiB": 32896,
                    "used_MiB": 16548
                },
                "usr_spc_alloc_limit_pct": 0,
                "usr_spc_alloc_warning_pct": 0,
                "uuid": "b7af74ab-740e-4157-85ae-40d3f42d1829",
                "wwn": "60002AC000000000000000020000518A"
            }
        ]

        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_volume_facts.return_value = (
            True, "", RESULTS)

        volume_facts.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=False, ansible_facts=RESULTS)
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)


if __name__ == '__main__':
    unittest.main(exit=False)
