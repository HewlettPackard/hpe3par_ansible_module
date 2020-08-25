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
from Modules import hpe3par_host as host
from ansible.module_utils.basic import AnsibleModule as ansible
import unittest
from hpe3par_sdk.models import Host

class TestHpe3parHost(unittest.TestCase):

    maxDiff = None

    PARAMS_FOR_PRESENT = {'state': 'present', 'storage_system_ip': '192.168.0.1', 'storage_system_username': 'USER',
                          'storage_system_password': 'PASS', 'host_name': 'host', 'host_domain': 'domain', 'host_new_name': 'new',
                          'host_fc_wwns': ['PASS'], 'host_iscsi_names': ['host'], 'host_persona': 'GENERIC', 'force_path_removal': 'true',
                          'chap_name': 'chap', 'chap_secret': 'secret', 'chap_secret_hex': 'true'}

    fields = {
        "state": {
            "required": True,
            "choices": [
                'present',
                'absent',
                'modify',
                'add_initiator_chap',
                'remove_initiator_chap',
                'add_target_chap',
                'remove_target_chap',
                'add_fc_path_to_host',
                'remove_fc_path_from_host',
                'add_iscsi_path_to_host',
                'remove_iscsi_path_from_host'],
            "type": 'str'},
        "storage_system_ip": {
            "required": True,
            "type": "str"},
        "storage_system_username": {
            "required": True,
            "type": "str",
            "no_log": True},
        "storage_system_password": {
            "required": True,
            "type": "str",
            "no_log": True},
        "host_name": {
            "type": "str"},
        "host_domain": {
            "type": "str"},
        "host_new_name": {
            "type": "str"},
        "host_fc_wwns": {
            "type": "list"},
        "host_iscsi_names": {
            "type": "list"},
        "host_persona": {
            "required": False,
            "type": "str",
            "choices": [
                "GENERIC",
                "GENERIC_ALUA",
                "GENERIC_LEGACY",
                "HPUX_LEGACY",
                "AIX_LEGACY",
                "EGENERA",
                "ONTAP_LEGACY",
                "VMWARE",
                "OPENVMS",
                "HPUX",
                "WINDOWS_SERVER"]},
        "force_path_removal": {
            "type": "bool"},
        "chap_name": {
            "type": "str"},
        "chap_secret": {
            "type": "str"},
        "chap_secret_hex": {
            "type": "bool"}}

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    def test_module_args(self, mock_module, mock_client):
        """
        hpe3par flash cache - test module arguments
        """

        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        host.main()
        mock_module.assert_called_with(
            argument_spec=self.fields)

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.create_host')
    def test_main_exit_functionality_success_without_issue_attr_dict(self, mock_host, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_host.return_value = (
            True, True, "Created host host successfully.", {})
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Created host host successfully.")

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.create_host')
    def test_main_exit_functionality_success_with_issue_attr_dict(self, mock_host, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_host.return_value = (
            True, True, "Created host host successfully.", {"dummy": "dummy"})
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Created host host successfully.", issue={"dummy": "dummy"})

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.create_host')
    def test_main_exit_functionality_fail(self, mock_host, mock_module, mock_client):
        """
        hpe3par host - exit fail check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_host.return_value = (
            False, False, "Host creation failed.", {"dummy": "dummy"})
        host.main()

        # AnsibleModule.exit_json should not be activated
        self.assertEqual(instance.exit_json.call_count, 0)
        # AnsibleModule.fail_json should be called
        instance.fail_json.assert_called_with(msg='Host creation failed.')

    @mock.patch('Modules.hpe3par_host.client')
    def test_create_host_username_empty(self, mock_client):
        """
        hpe3par host - create a host
        """
        result = host.create_host(
            mock_client, None, None, None, None, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host creation failed. Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_create_host_hostname_empty(self, mock_client):
        """
        hpe3par host - create a host
        """
        result = host.create_host(
            mock_client, "user", "pass", None, None, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host creation failed. Host name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_create_host_create_already_present(self, mock_client):
        """
        hpe3par host - create a host
        """
        result = host.create_host(
            mock_client, "user", "pass", "host", None, None, None, None)
        self.assertEqual(result, (True, False, "Host already present", {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_create_host_create_exception_in_login(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - create a host
        """
        mock_HPE3ParClient.HOST_EDIT_REMOVE = 1
        mock_client.HPE3ParClient.login.side_effect = Exception(
            "Failed to login!")
        result = host.create_host(
            mock_client.HPE3ParClient, "user", "password", 'host_name', None, None, None, None)
        self.assertEqual(
            result, (False, False, "Host creation failed | Failed to login!", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_create_host_create_sucess_login(self, mock_client):
        """
        hpe3par flash cache - create a flash cache
        """
        mock_client.HPE3ParClient.hostExists.return_value = False
        result = host.create_host(mock_client.HPE3ParClient, "user",
                                  "password", "hostname", None, None, "domain", "GENERIC")
        self.assertEqual(
            result, (True, True, "Created host hostname successfully.", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_delete_host_username_empty(self, mock_client):
        """
        hpe3par host - create a host
        """
        result = host.delete_host(mock_client, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host deletion failed. Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_delete_host_hostname_empty(self, mock_client):
        """
        hpe3par host - create a host
        """
        result = host.delete_host(mock_client, "user", "pass", None)

        self.assertEqual(result, (
            False,
            False,
            "Host deletion failed. Host name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_delete_host_create_sucess_login(self, mock_client):
        """
        hpe3par host - create a host
        """
        result = host.delete_host(mock_client, "user", "pass", "host")
        self.assertEqual(
            result, (True, True, "Deleted host host successfully.", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_delete_host_create_exception_in_login(self, mock_client):
        """
        hpe3par host - create a host
        """
        mock_client.HPE3ParClient.login.side_effect = Exception(
            "Failed to login!")
        result = host.delete_host(
            mock_client.HPE3ParClient, "user", "password", 'host_name')
        self.assertEqual(
            result, (False, False, "Host deletion failed | Failed to login!", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_delete_host_create_already_present(self, mock_client):
        """
        hpe3par flash cache - create a flash cache
        """
        mock_client.HPE3ParClient.hostExists.return_value = False
        result = host.delete_host(
            mock_client.HPE3ParClient, "user", "password", "hostname")
        self.assertEqual(result, (True, False, "Host does not exist", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_modify_host_username_empty(self, mock_client):
        """
        hpe3par host - Modify a host
        """
        result = host.modify_host(mock_client, None, None, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_modify_host_hostname_empty(self, mock_client):
        """
        hpe3par host - Modify a host
        """
        result = host.modify_host(
            mock_client, "user", "pass", None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Host name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_modify_host_create_exception_in_login(self, mock_client):
        """
        hpe3par host - Modify a host
        """
        mock_client.HPE3ParClient.login.side_effect = Exception(
            "Failed to login!")
        result = host.modify_host(
            mock_client.HPE3ParClient, "user", "password", "host_name", None, None)
        self.assertEqual(
            result, (False, False, "Host modification failed | Failed to login!", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_modify_host_create_success(self, mock_client):
        """
        hpe3par host - Modify a host
        """
        result = host.modify_host(
            mock_client.HPE3ParClient, "user", "password", "host_name", None, None)
        self.assertEqual(
            result, (True, True, "Modified host host_name successfully.", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_initiator_chap_username_empty(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        result = host.add_initiator_chap(
            mock_client, None, None, None, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_initiator_chap_hostname_empty(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        result = host.add_initiator_chap(
            mock_client, "user", "pass", None, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Host name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_initiator_chap_chapname_empty(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        result = host.add_initiator_chap(
            mock_client, "user", "pass", "host", None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Chap name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_initiator_chap_chapsecret_empty(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        result = host.add_initiator_chap(
            mock_client, "user", "pass", "host", "chap", None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. chap_secret is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_initiator_chap_chaphex_true(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        result = host.add_initiator_chap(
            mock_client, "user", "pass", "host", "chap", "secret", True)

        self.assertEqual(result, (
            False,
            False,
            "Add initiator chap failed. Chap secret hex is false and chap secret less than 32 characters",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_initiator_chap_chaphex_false(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        result = host.add_initiator_chap(
            mock_client, "user", "pass", "host", "chap", "secret", False)

        self.assertEqual(result, (
            False,
            False,
            "Add initiator chap failed. Chap secret hex is false and chap secret less than 12 characters or more than 16 characters",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_add_initiator_chap_success(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        mock_HPE3ParClient.CHAP_INITIATOR = 1
        result = host.add_initiator_chap(
            mock_client.HPE3ParClient, "user", "pass", "host", "chap", "secretsecretsecretsecretsecret12", True)

        self.assertEqual(result, (
            True, True, "Added initiator chap.", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_initiator_chap_exception(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        mock_client.login.side_effect = Exception("Failed to login!")
        mock_client.return_value = mock_client
        result = host.add_initiator_chap(
            mock_client, "user", "pass", "host", "chap", "secretsecretsecretsecretsecret12", True)

        self.assertEqual(result, (
            False, False, "Add initiator chap failed | Failed to login!", {}))

# Target chap.

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_target_chap_username_empty(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        result = host.add_target_chap(
            mock_client, None, None, None, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_target_chap_hostname_empty(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        result = host.add_target_chap(
            mock_client, "user", "pass", None, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Host name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_target_chap_chapname_empty(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        result = host.add_target_chap(
            mock_client, "user", "pass", "host", None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Chap name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_target_chap_chapsecret_empty(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        result = host.add_target_chap(
            mock_client, "user", "pass", "host", "chap", None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. chap_secret is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_target_chap_chaphex_true(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        result = host.add_target_chap(
            mock_client, "user", "pass", "host", "chap", "secret", True)

        self.assertEqual(result, (
            False,
            False,
            "Attribute chap_secret must be 32 hexadecimal characters if chap_secret_hex is true",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_target_chap_chaphex_false(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        result = host.add_target_chap(
            mock_client, "user", "pass", "host", "chap", "secret", False)

        self.assertEqual(result, (
            False,
            False,
            "Attribute chap_secret must be 12 to 16 character if chap_secret_hex is false",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.initiator_chap_exists')
    def test_add_target_chap_exists(self, mock_initiator_chap_exists, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        mock_initiator_chap_exists.return_value = False
        result = host.add_target_chap(mock_client.HPE3ParClient, "user",
                                      "pass", "host", "chap", "secretsecretsecretsecretsecret12", True)

        self.assertEqual(result, (
            True, False, "Initiator chap does not exist", {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_add_target_chap_success(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        mock_HPE3ParClient.CHAP_TARGET = 1
        result = host.add_target_chap(
            mock_client, "user", "pass", "host", "chap", "secretsecretsecretsecretsecret12", True)

        self.assertEqual(result, (
            True, True, "Added target chap.", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_target_chap_exception(self, mock_client):
        """
        hpe3par host - add_initiator_chap
        """
        mock_client.login.side_effect = Exception("Failed to login!")
        mock_client.return_value = mock_client
        result = host.add_target_chap(
            mock_client, "user", "pass", "host", "chap", "secretsecretsecretsecretsecret12", True)

        self.assertEqual(result, (
            False, False, "Add target chap failed | Failed to login!", {}))

# initiator_chap_exists

    @mock.patch('Modules.hpe3par_host.client')
    def test_initiator_chap_exists_sucess(self, mock_client):
        """
        hpe3par host - initiator_chap_exists
        """
        result = host.initiator_chap_exists(
            mock_client, "user", "pass", "host")
#        self.assertEqual(result, True)

# Remove

    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_initiator_chap_username_empty(self, mock_client):
        """
        hpe3par host - remove_initiator_chap
        """
        result = host.remove_initiator_chap(mock_client, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_initiator_chap_hostname_empty(self, mock_client):
        """
        hpe3par host - remove_initiator_chap
        """
        result = host.remove_initiator_chap(mock_client, "user", "pass", None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Host name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_remove_initiator_chap_sucess(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - remove_initiator_chap
        """
        mock_HPE3ParClient.HOST_EDIT_REMOVE = 1
        result = host.remove_initiator_chap(
            mock_client, "user", "pass", "host")

        self.assertEqual(result, (
            True, True, "Removed initiator chap.", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_initiator_chap_exception(self, mock_client):
        """
        hpe3par host - remove_initiator_chap
        """
        mock_client.login.side_effect = Exception("Failed to login!")
        mock_client.return_value = mock_client
        result = host.remove_initiator_chap(
            mock_client, "user", "pass", "host")

        self.assertEqual(result, (
            False, False, "Remove initiator chap failed | Failed to login!", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_target_chap_username_empty(self, mock_client):
        """
        hpe3par host - remove_target_chap
        """
        result = host.remove_target_chap(mock_client, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_target_chap_hostname_empty(self, mock_client):
        """
        hpe3par host - remove_target_chap
        """
        result = host.remove_target_chap(mock_client, "user", "pass", None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Host name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_remove_target_chap_success(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - remove_target_chap
        """
        mock_HPE3ParClient.HOST_EDIT_REMOVE = 1
        result = host.remove_target_chap(
            mock_client.HPE3ParClient, "user", "pass", "host")

        self.assertEqual(result, (
            True, True, "Removed target chap.", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_target_chap_exception(self, mock_client):
        """
        hpe3par host - remove_target_chap
        """
        mock_client.login.side_effect = Exception("Failed to login!")
        mock_client.return_value = mock_client
        result = host.remove_target_chap(mock_client, "user", "pass", "host")

        self.assertEqual(result, (
            False, False, "Remove target chap failed | Failed to login!", {}))

    # Add FC
    @mock.patch('Modules.hpe3par_host.client')
    def test_add_FC_username_empty(self, mock_client):
        """
        hpe3par host - add_fc_path_to_host
        """
        result = host.add_fc_path_to_host(mock_client, None, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_FC_hostname_empty(self, mock_client):
        """
        hpe3par host - add_fc_path_to_host
        """
        result = host.add_fc_path_to_host(
            mock_client, "user", "pass", None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Host name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_FC_empty(self, mock_client):
        """
        hpe3par host - add_fc_path_to_host
        """
        result = host.add_fc_path_to_host(
            mock_client, "user", "pass", "host", None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. host_fc_wwns is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_add_FC_success(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - add_fc_path_to_host
        """
        mock_client.HPE3ParClient.queryHost.return_value = []
        mock_HPE3ParClient.HOST_EDIT_ADD = 1
        result = host.add_fc_path_to_host(
            mock_client.HPE3ParClient, "user", "pass", "hostname", ['fc_wwn'])

        self.assertEqual(result, (
            True, True, "Added FC path(s) fc_wwn to host successfully.", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_FC_exception(self, mock_client):
        """
        hpe3par host - add_fc_path_to_host
        """
        mock_client.login.side_effect = Exception("Failed to login!")
        mock_client.return_value = mock_client
        result = host.add_fc_path_to_host(
            mock_client, "user", "pass", "hostname", "fc_wwn")

        self.assertEqual(result, (
            False, False, "Add FC path to host failed | Failed to login!", {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_add_FC_same_host(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - add_fc_path_to_host
        """
        object_hash = {'name': 'hostname'}
        host_obj = Host(object_hash)
        mock_client.HPE3ParClient.queryHost.return_value = [host_obj]
        wwn_list = ['wwn.333', 'wwn.222']
        result = host.add_fc_path_to_host(
            mock_client.HPE3ParClient, "user", "pass", "hostname", wwn_list)

        self.assertEqual(result, (
            True, False, "FC path(s) wwn.333, wwn.222 already assigned to this host", {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_add_FC_assigned_other_host(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - add_fc_path_to_host
        """
        object_hash = {'name': 'other_hostname'}
        host_obj = Host(object_hash)
        mock_client.HPE3ParClient.queryHost.return_value = [host_obj]
        wwn_list = ['wwn.111', 'wwn.000']
        result = host.add_fc_path_to_host(
            mock_client.HPE3ParClient, "user", "pass", "hostname", wwn_list)

        self.assertEqual(result, (
            False, False, "FC path(s) wwn.111, wwn.000 already assigned to other host", {}))

    # Remove FC
    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_fc_username_empty(self, mock_client):
        """
        hpe3par host - remove_fc_path_from_host
        """
        result = host.remove_fc_path_from_host(
            mock_client, None, None, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_fc_hostname_empty(self, mock_client):
        """
        hpe3par host - remove_fc_path_from_host
        """
        result = host.remove_fc_path_from_host(
            mock_client, "user", "pass", None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Host name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_fc_fcwwns_empty(self, mock_client):
        """
        hpe3par host - remove_fc_path_from_host
        """
        result = host.remove_fc_path_from_host(
            mock_client, "user", "pass", "host", None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. host_fc_wwns is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_remove_fc_sucess(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - remove_fc_path_from_host
        """
        object_hash = {'name': 'hostname'}
        host_obj = Host(object_hash)
        mock_client.HPE3ParClient.queryHost.return_value = [host_obj]
        mock_HPE3ParClient.HOST_EDIT_REMOVE = 1
        result = host.remove_fc_path_from_host(
            mock_client.HPE3ParClient, "user", "pass", "hostname", ['fc_wwn'], None)

        self.assertEqual(result, (
            True, True, "Removed FC path(s) fc_wwn from host successfully.", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_fc_exception(self, mock_client):
        """
        hpe3par host - remove_fc_path_from_host
        """
        mock_client.login.side_effect = Exception("Failed to login!")
        mock_client.return_value = mock_client
        result = host.remove_fc_path_from_host(
            mock_client, "user", "pass", "host", "fcwwns", None)

        self.assertEqual(result, (
            False, False, "Remove FC path from host failed | Failed to login!", {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_remove_fc_already_removed(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - remove_fc_path_from_host
        """
        mock_client.HPE3ParClient.queryHost.return_value = []
        wwn_list = ['wwn.333', 'wwn.222']
        result = host.remove_fc_path_from_host(
            mock_client.HPE3ParClient, "user", "pass", "hostname", wwn_list, None)

        self.assertEqual(result, (
            True, False, "FC path(s) wwn.333, wwn.222 seem to be already removed", {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_remove_fc_assigned_other_host(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - remove_fc_path_from_host
        """
        object_hash = {'name': 'other_hostname'}
        host_obj = Host(object_hash)
        mock_client.HPE3ParClient.queryHost.return_value = [host_obj]
        wwn_list = ['wwn.111', 'wwn.000']
        result = host.remove_fc_path_from_host(
            mock_client.HPE3ParClient, "user", "pass", "hostname", wwn_list, None)

        self.assertEqual(result, (
            False, False, "FC path(s) wwn.111, wwn.000 assigned to other host", {}))

    # Add ISCSI
    @mock.patch('Modules.hpe3par_host.client')
    def test_add_iscsi_username_empty(self, mock_client):
        """
        hpe3par host - add_iscsi_path_to_host
        """
        result = host.add_iscsi_path_to_host(
            mock_client, None, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_iscsi_hostname_empty(self, mock_client):
        """
        hpe3par host - add_iscsi_path_to_host
        """
        result = host.add_iscsi_path_to_host(
            mock_client, "user", "pass", None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Host name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_iscsi_empty(self, mock_client):
        """
        hpe3par host - add_iscsi_path_to_host
        """
        result = host.add_iscsi_path_to_host(
            mock_client, "user", "pass", "host", None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. host_iscsi_names is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_add_iscsi_sucess(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - add_iscsi_path_to_host
        """
        mock_client.HPE3ParClient.queryHost.return_value = []
        mock_HPE3ParClient.HOST_EDIT_ADD = 1
        result = host.add_iscsi_path_to_host(
            mock_client.HPE3ParClient, "user", "pass", "hostname", ['iscsi_iqn'])

        self.assertEqual(result, (
            True, True, "Added iSCSI path(s) iscsi_iqn to host successfully.", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_add_iscsi_exception(self, mock_client):
        """
        hpe3par host - add_iscsi_path_to_host
        """
        mock_client.login.side_effect = Exception("Failed to login!")
        mock_client.return_value = mock_client
        result = host.add_iscsi_path_to_host(
            mock_client, "user", "pass", "hostname", "iscsi_iqn")

        self.assertEqual(result, (
            False, False, "Add ISCSI path to host failed | Failed to login!", {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_add_iscsi_assigned_same_host(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - add_iscsi_path_to_host
        """
        object_hash = {'name': 'hostname'}
        host_obj = Host(object_hash)
        mock_client.HPE3ParClient.queryHost.return_value = [host_obj]
        iqn_list = ['iqn.333', 'iqn.222']
        result = host.add_iscsi_path_to_host(
            mock_client.HPE3ParClient, "user", "pass", "hostname", iqn_list)

        self.assertEqual(result, (
            True, False, "iSCSI name(s) iqn.333, iqn.222 already assigned to this host", {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_add_iscsi_assigned_other_host(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - add_iscsi_path_to_host
        """
        object_hash = {'name': 'other_hostname'}
        host_obj = Host(object_hash)
        mock_client.HPE3ParClient.queryHost.return_value = [host_obj]
        iqn_list = ['iqn.111', 'iqn.000']
        result = host.add_iscsi_path_to_host(
            mock_client.HPE3ParClient, "user", "pass", "hostname", iqn_list)

        self.assertEqual(result, (
            False, False, "iSCSI name(s) iqn.111, iqn.000 already assigned to other host", {}))

    # Remove ISCSI
    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_iscsi_username_empty(self, mock_client):
        """
        hpe3par host - remove_iscsi_path_from_host
        """
        result = host.remove_iscsi_path_from_host(
            mock_client, None, None, None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_iscsi_hostname_empty(self, mock_client):
        """
        hpe3par host - remove_iscsi_path_from_host
        """
        result = host.remove_iscsi_path_from_host(
            mock_client, "user", "pass", None, None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. Host name is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_iscsi_empty(self, mock_client):
        """
        hpe3par host - remove_iscsi_path_from_host
        """
        result = host.remove_iscsi_path_from_host(
            mock_client, "user", "pass", "host", None, None)

        self.assertEqual(result, (
            False,
            False,
            "Host modification failed. host_iscsi_names is null",
            {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_remove_iscsi_sucess(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - remove_iscsi_path_from_host
        """
        object_hash = {'name': 'hostname'}
        host_obj = Host(object_hash)
        mock_client.HPE3ParClient.queryHost.return_value = [host_obj]
        mock_HPE3ParClient.HOST_EDIT_REMOVE = 1
        result = host.remove_iscsi_path_from_host(
            mock_client.HPE3ParClient, "user", "pass", "hostname", ['iscsi_iqn'], None)

        self.assertEqual(result, (
            True, True, "Removed iSCSI path(s) iscsi_iqn from host successfully.", {}))

    @mock.patch('Modules.hpe3par_host.client')
    def test_remove_iscsi_exception(self, mock_client):
        """
        hpe3par host - remove_iscsi_path_from_host
        """
        mock_client.login.side_effect = Exception("Failed to login!")
        mock_client.return_value = mock_client
        result = host.remove_iscsi_path_from_host(
            mock_client, "user", "pass", "host", "iscsi", None)

        self.assertEqual(result, (
            False, False, "Remove ISCSI path from host failed | Failed to login!", {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_remove_iscsi_already_removed(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - remove_iscsi_path_from_host
        """
        mock_client.HPE3ParClient.queryHost.return_value = []
        iqn_list = ['iqn.333', 'iqn.222']
        result = host.remove_iscsi_path_from_host(
            mock_client.HPE3ParClient, "user", "pass", "hostname", iqn_list, None)

        self.assertEqual(result, (
            True, False, "iSCSI name(s) iqn.333, iqn.222 seem to be already removed", {}))

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.HPE3ParClient')
    def test_remove_iscsi_assigned_other_host(self, mock_HPE3ParClient, mock_client):
        """
        hpe3par host - remove_iscsi_path_from_host
        """
        object_hash = {'name': 'other_hostname'}
        host_obj = Host(object_hash)
        mock_client.HPE3ParClient.queryHost.return_value = [host_obj]
        iqn_list = ['iqn.111', 'iqn.000']
        result = host.remove_iscsi_path_from_host(
            mock_client.HPE3ParClient, "user", "pass", "hostname", iqn_list, None)

        self.assertEqual(result, (
            False, False, "iSCSI name(s) iqn.111, iqn.000 assigned to other host", {}))

# main tests

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.create_host')
    def test_main_exit_functionality_success_without_issue_attr_dict_present(self, mock_host, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "present"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_host.return_value = (
            True, True, "Created host host successfully.", {})
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Created host host successfully.")

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.create_host')
    def test_main_exit_functionality_success_without_issue_attr_dict_absent(self, mock_host, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "absent"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Deleted host host successfully.")

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.create_host')
    def test_main_exit_functionality_success_without_issue_attr_dict_modify(self, mock_host, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "modify"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Modified host host successfully.")

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.add_initiator_chap')
    def test_main_exit_functionality_success_without_issue_attr_dict_add_initiator_chap(self, mock_add_initiator_chap, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "add_initiator_chap"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_add_initiator_chap.return_value = (
            True, True, "Add_initiator_chap successfully.", {})
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Add_initiator_chap successfully.")

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.add_initiator_chap')
    def test_main_exit_functionality_success_without_issue_attr_dict_add_initiator_chap(self, mock_add_initiator_chap, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "add_initiator_chap"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_add_initiator_chap.return_value = (
            True, True, "Add_initiator_chap successfully.", {})
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Add_initiator_chap successfully.")

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.add_initiator_chap')
    def test_main_exit_functionality_success_without_issue_attr_dict_add_initiator_chap(self, mock_add_initiator_chap, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "add_initiator_chap"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_add_initiator_chap.return_value = (
            True, True, "Add_initiator_chap successfully.", {})
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Add_initiator_chap successfully.")

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.remove_initiator_chap')
    def test_main_exit_functionality_success_without_issue_attr_dict_remove_initiator_chap(self, mock_add_initiator_chap, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "remove_initiator_chap"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_add_initiator_chap.return_value = (
            True, True, "Remove_initiator_chap successfully.", {})
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="Remove_initiator_chap successfully.")

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.add_target_chap')
    def test_main_exit_functionality_success_without_issue_attr_dict_add_target_chap(
            self, mock_add_target_chap, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "add_target_chap"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_add_target_chap.return_value = (
            True, True, "add_target_chap successfully.", {})
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="add_target_chap successfully.")
    """
    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    def test_main_exit_functionality_success_without_issue_attr_dict_remove_target_chap(
            self, mock_module, mock_client):
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "remove_target_chap"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        host.remove_target_chap = mock.Mock(return_value=(
            True, True, "Remove_target_chap successfully.", {}))
        host.main()
        # AnsibleModule.exit_json should be called
        mock_module.exit_json.assert_called_with(
            changed=True, msg="Remove_target_chap successfully.")
    """

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.add_fc_path_to_host')
    def test_main_exit_functionality_success_without_issue_attr_dict_add_fc_path_to_host(self, mock_add_fc_path_to_host, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "add_fc_path_to_host"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_add_fc_path_to_host.return_value = (
            True, True, "add_fc_path_to_host successfully.", {})
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="add_fc_path_to_host successfully.")

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.remove_fc_path_from_host')
    def test_main_exit_functionality_success_without_issue_attr_dict_remove_fc_path_from_host(self, mock_remove_fc_path_from_host, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "remove_fc_path_from_host"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_remove_fc_path_from_host.return_value = (
            True, True, "remove_fc_path_from_host successfully.", {})
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="remove_fc_path_from_host successfully.")

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.add_iscsi_path_to_host')
    def test_main_exit_functionality_success_without_issue_attr_dict_add_iscsi_path_to_host(self, mock_add_iscsi_path_to_host, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "add_iscsi_path_to_host"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_add_iscsi_path_to_host.return_value = (
            True, True, "add_iscsi_path_to_host successfully.", {})
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="add_iscsi_path_to_host successfully.")
        # AnsibleModule.fail_json should not be called
        # self.assertEqual(instance.fail_json.call_count, 0)

    @mock.patch('Modules.hpe3par_host.client')
    @mock.patch('Modules.hpe3par_host.AnsibleModule')
    @mock.patch('Modules.hpe3par_host.remove_iscsi_path_from_host')
    def test_main_exit_functionality_success_without_issue_attr_dict_remove_iscsi_path_from_host(
            self, mock_remove_iscsi_path_from_host, mock_module, mock_client):
        """
        hpe3par host - success check
        """
        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS_FOR_PRESENT
        mock_module.params["state"] = "remove_iscsi_path_from_host"
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_remove_iscsi_path_from_host.return_value = (
            True, True, "remove_iscsi_path_from_host successfully.", {})
        host.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=True, msg="remove_iscsi_path_from_host successfully.")


if __name__ == '__main__':
    unittest.main(exit=False)
