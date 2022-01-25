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
from Modules import hpe3par_cpg_facts as cpg_facts
import unittest


class TestHpe3parCPGFacts(unittest.TestCase):

    PARAMS = {'storage_system_username': 'USER', 'storage_system_ip': '192.168.0.1', 
              'storage_system_password': 'PASS', 'cpg_name': 'ansible_cpg'}

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
        "cpg_name": {
            "type": "str"
        }
    }

    @mock.patch('Modules.hpe3par_cpg_facts.client')
    @mock.patch('Modules.hpe3par_cpg_facts.AnsibleModule')
    def test_module_args(self, mock_module, mock_client):
        """
        hpe3par CPG facts - test module arguments
        """
        mock_module.params = self.PARAMS
        mock_module.return_value = mock_module
        cpg_facts.main()
        mock_module.assert_called_with(
            argument_spec=self.fields)

    @mock.patch('Modules.hpe3par_cpg_facts.client')
    def test_exception_in_login(self, mock_client):
        """
        hpe3par CPG facts - login error exit fail check
        """
        mock_client.HPE3ParClient.login.side_effect = Exception(
            "Failed to login!")
        result = cpg_facts.get_cpgs(
            mock_client.HPE3ParClient, "user", "password", None)

        self.assertEqual(
            result, (False, "execution error | Failed to login!", {}))

    @mock.patch('Modules.hpe3par_cpg_facts.client')
    def test_get_cpg_username_empty(self, mock_client):
        """
        hpe3par CPG facts - get CPGs
        """
        result = cpg_facts.get_cpgs(mock_client, None, "PASS", None)

        self.assertEqual(result, (
            False,
            "Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_cpg_facts.client')
    def test_get_cpg_password_empty(self, mock_client):
        """
        hpe3par CPG facts - get CPGs
        """
        result = cpg_facts.get_cpgs(mock_client, "USER", None, None)

        self.assertEqual(result, (
            False,
            "Storage system username or password is null",
            {}))

    @mock.patch('Modules.hpe3par_cpg_facts.client')
    def test_main_exit_functionality_fail_cpg_doesnt_exists(self, mock_client):
        """
        hpe3par CPG facts - CPG does not exists exit fail check
        """
        mock_client.HPE3ParClient.cpgExists.return_value = False
        result = cpg_facts.get_cpgs(
            mock_client.HPE3ParClient, "user", "password", "hostname")
        self.assertEqual(result, (False, "cpg does not exists", {}))

    @mock.patch('Modules.hpe3par_cpg_facts.client')
    @mock.patch('Modules.hpe3par_cpg_facts.AnsibleModule')
    @mock.patch('Modules.hpe3par_cpg_facts.get_cpgs')
    def test_main_exit_functionality_success_with_cpg_name(self, mock_cpg_facts, mock_module, mock_client):
        """
        hpe3par CPG facts - CPG by name success check
        """
        RESULT = [
            {
                "id": "id",
                "uuid": "uuid",
                "name": "dummy",
                "state": "state",
                "domain": "domain",
                "warningPct": "warningPct",
                "numTPVVs": "numTPVVs",
                "numFPVVs": "numFPVVs",
                "numTDVVs": "numTDVVs",
                "UsrUsage": "UsrUsage",
                "SAUsage": "SAUsage",
                "SDUsage": "SDUsage",
                "failedStates": "failedStates",
                "degradedStates": "degradedStates",
                "additionalStates": "additionalStates",
                "dedupCapable": "dedupCapable",
                "sharedSpaceMiB": "sharedSpaceMiB",
                "freeSpaceMiB": "freeSpaceMiB",
                "totalSpaceMiB": "totalSpaceMiB",
                "rawSharedSpaceMiB": "rawSharedSpaceMiB",
                "rawFreeSpaceMiB": "rawFreeSpaceMiB",
                "rawTotalSpaceMiB": "rawTotalSpaceMiB",
                "tdvvVersion": "tdvvVersion",
                "ddsRsvdMiB": "ddsRsvdMiB"
            }
        ]

        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_cpg_facts.return_value = (
            True, "", RESULT)

        cpg_facts.main()

        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=False, ansible_facts=RESULT)
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)

    @mock.patch('Modules.hpe3par_cpg_facts.client')
    @mock.patch('Modules.hpe3par_cpg_facts.AnsibleModule')
    @mock.patch('Modules.hpe3par_cpg_facts.get_cpgs')
    def test_main_exit_functionality_success_without_cpg_name(self, mock_cpg_facts, mock_module, mock_client):
        """
        hpe3par CPG facts - all CPGs success check
        """

        RESULTS = [
            {
                "id": "id",
                "uuid": "uuid",
                "name": "dummy",
                "state": "state",
                "domain": "domain",
                "warningPct": "warningPct",
                "numTPVVs": "numTPVVs",
                "numFPVVs": "numFPVVs",
                "numTDVVs": "numTDVVs",
                "UsrUsage": "UsrUsage",
                "SAUsage": "SAUsage",
                "SDUsage": "SDUsage",
                "failedStates": "failedStates",
                "degradedStates": "degradedStates",
                "additionalStates": "additionalStates",
                "dedupCapable": "dedupCapable",
                "sharedSpaceMiB": "sharedSpaceMiB",
                "freeSpaceMiB": "freeSpaceMiB",
                "totalSpaceMiB": "totalSpaceMiB",
                "rawSharedSpaceMiB": "rawSharedSpaceMiB",
                "rawFreeSpaceMiB": "rawFreeSpaceMiB",
                "rawTotalSpaceMiB": "rawTotalSpaceMiB",
                "tdvvVersion": "tdvvVersion",
                "ddsRsvdMiB": "ddsRsvdMiB"
            },
            {
                "id": "id2",
                "uuid": "uuid2",
                "name": "dummy2",
                "state": "state",
                "domain": "domain",
                "warningPct": "warningPct",
                "numTPVVs": "numTPVVs",
                "numFPVVs": "numFPVVs",
                "numTDVVs": "numTDVVs",
                "UsrUsage": "UsrUsage",
                "SAUsage": "SAUsage",
                "SDUsage": "SDUsage",
                "failedStates": "failedStates",
                "degradedStates": "degradedStates",
                "additionalStates": "additionalStates",
                "dedupCapable": "dedupCapable",
                "sharedSpaceMiB": "sharedSpaceMiB",
                "freeSpaceMiB": "freeSpaceMiB",
                "totalSpaceMiB": "totalSpaceMiB",
                "rawSharedSpaceMiB": "rawSharedSpaceMiB",
                "rawFreeSpaceMiB": "rawFreeSpaceMiB",
                "rawTotalSpaceMiB": "rawTotalSpaceMiB",
                "tdvvVersion": "tdvvVersion",
                "ddsRsvdMiB": "ddsRsvdMiB"
            }
        ]

        # This creates a instance of the AnsibleModule mock.
        mock_module.params = self.PARAMS
        mock_module.return_value = mock_module
        instance = mock_module.return_value
        mock_cpg_facts.return_value = (
            True, "", RESULTS)

        cpg_facts.main()
        # AnsibleModule.exit_json should be called
        instance.exit_json.assert_called_with(
            changed=False, ansible_facts=RESULTS)
        # AnsibleModule.fail_json should not be called
        self.assertEqual(instance.fail_json.call_count, 0)


if __name__ == '__main__':
    unittest.main(exit=False)
