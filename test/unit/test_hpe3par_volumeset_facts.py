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
from Modules import hpe3par_volumeset_facts as volumeset_facts
import unittest


class TestHpe3parVolumeSetFacts(unittest.TestCase):

    PARAMS = {'storage_system_username': 'USER', 'storage_system_ip': '192.168.0.1', 
              'storage_system_password': 'PASS', 'volumeset_name': 'demovolumeset'}

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
        }
    }

    @mock.patch('Modules.hpe3par_volumeset_facts.client')
    @mock.patch('Modules.hpe3par_volumeset_facts.AnsibleModule')
    def test_module_args(self, mock_module, mock_client):
        """
        hpe3par volumeset facts - test module arguments
        """

        mock_module.params = self.PARAMS
        mock_module.return_value = mock_module
        volumeset_facts.main()
        mock_module.assert_called_with(
            argument_spec=self.fields)

    @mock.patch('Modules.hpe3par_volumeset_facts.client')
    def test_exception_in_login(self, mock_client):
        """
        hpe3par volumeset facts - login error exit fail check
        """
        mock_client.HPE3ParClient.login.side_effect = Exception(
            "Failed to login!")
        result = volumeset_facts.get_volumesets(
            mock_client.HPE3ParClient, "user", "password", None)

        self.assertEqual(
            result, (False, "execution error | Failed to login!", {}))

    @mock.patch('Modules.hpe3par_volumeset_facts.client')
    def test_get_volumeset_username_empty(self, mock_client):
        """
        hpe3par volumeset facts - get volumesets
        """
        result = volumeset_facts.get_volumesets(mock_client, None, "PASS", None)

        self.assertEqual(result, (
            False,
            "Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_volumeset_facts.client')
    def test_get_volumeset_password_empty(self, mock_client):
        """
        hpe3par volumeset facts - get volumesets
        """
        result = volumeset_facts.get_volumesets(mock_client, "USER", None, None)

        self.assertEqual(result, (
            False,
            "Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_volumeset_facts.client')
    def test_main_exit_functionality_fail_volumeset_doesnt_exists(self, mock_client):
        """
        hpe3par volumeset facts - volumeset does not exists exit fail check
        """
        mock_client.HPE3ParClient.volumeSetExists.return_value = False
        result = volumeset_facts.get_volumesets(
            mock_client.HPE3ParClient, "user", "password", "volumesetname")
        self.assertEqual(result, (False, "volume set does not exists", {}))

    @mock.patch('Modules.hpe3par_volumeset_facts.client')
    @mock.patch('Modules.hpe3par_volumeset_facts.AnsibleModule')
    @mock.patch('Modules.hpe3par_volumeset_facts.get_volumesets')
    def test_main_exit_functionality_success_with_volumeset_name(self, mock_volumeset_facts, mock_module, mock_client):
        """
        hpe3par volumeset facts - volumeset by name success check
        """

        RESULT = [
            {
                "comment": "null",
                "domain": "null",
                "flash_cache_policy": "null",
                "id": 1,
                "name": "VVSet_Ansible",
                "qos_enabled": "false",
                "setmembers": [
                    "VV_LUN_01",
                    "VV_LUN_02"
                ],
                "uuid": "null"
            }
        ]

        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_volumeset_facts.return_value = (
            True, "", RESULT)

        volumeset_facts.main()

        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=False, ansible_facts=RESULT)
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)

    @mock.patch('Modules.hpe3par_volumeset_facts.client')
    @mock.patch('Modules.hpe3par_volumeset_facts.AnsibleModule')
    @mock.patch('Modules.hpe3par_volumeset_facts.get_volumesets')
    def test_main_exit_functionality_success_without_volumeset_name(self, mock_volumeset_facts, mock_module, mock_client):
        """
        hpe3par volumeset facts - all volumesets success check
        """

        RESULTS = [
            {
                "comment": "null",
                "domain": "null",
                "flash_cache_policy": "null",
                "id": 1,
                "name": "VVSet_Ansible",
                "qos_enabled": "false",
                "setmembers": [
                    "VV_LUN_01",
                    "VV_LUN_02"
                ],
                "uuid": "null"
            },
            {
                "comment": "null",
                "domain": "null",
                "flash_cache_policy": "null",
                "id": 2,
                "name": "VVSet_Ansible_2",
                "qos_enabled": "false",
                "setmembers": [
                    "VV_LUN_03",
                    "VV_LUN_04"
                ],
                "uuid": "null"
            }
        ]

        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_volumeset_facts.return_value = (
            True, "", RESULTS)

        volumeset_facts.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=False, ansible_facts=RESULTS)
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)


if __name__ == '__main__':
    unittest.main(exit=False)
