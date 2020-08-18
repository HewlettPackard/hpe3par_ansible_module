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
description: "On HPE 3PAR and PRIMERA - Create Host - Delete Host
 - Add Initiator Chap - Remove Initiator Chap - Add Target Chap
 - Remove Target Chap - Add FC Path to Host - Remove FC Path from Host
 - Add ISCSI Path to Host - Remove ISCSI Path from Host"
module: hpe3par_host
options:
  chap_name:
    description:
      - "The chap name.\nRequired with actions add_initiator_chap,
       add_target_chap\n"
    required: false
  chap_secret:
    description:
      - "The chap secret for the host or the target\nRequired with actions
       add_initiator_chap, add_target_chap\n"
    required: false
  chap_secret_hex:
    description:
      - "If true, then chapSecret is treated as Hex."
    required: false
    type: bool
  force_path_removal:
    description:
      - "If true, remove WWN(s) or iSCSI(s) even if there are VLUNs that are
       exported to the host.\n"
    required: false
    type: bool
  host_domain:
    description:
      - "Create the host in the specified domain, or in the default domain,
       if unspecified\n"
    required: false
  host_fc_wwns:
    description:
      - "Set one or more WWNs for the host.\nRequired with action
       add_fc_path_to_host, remove_fc_path_from_host\n"
    required: false
  host_iscsi_names:
    description:
      - "Set one or more iSCSI names for the host.\nRequired with action
       add_iscsi_path_to_host, remove_iscsi_path_from_host\n"
    required: false
  host_name:
    description:
      - "Name of the Host."
    required: true
  host_new_name:
    description:
      - "New name of the Host."
    required: true
  host_persona:
    choices:
      - GENERIC
      - GENERIC_ALUA
      - GENERIC_LEGACY
      - HPUX_LEGACY
      - AIX_LEGACY
      - EGENERA
      - ONTAP_LEGACY
      - VMWARE
      - OPENVMS
      - HPUX
      - WINDOWS_SERVER
    description:
      - "ID of the persona to assign to the host. Uses the default persona
       unless you specify the host persona.\n"
    required: false
  state:
    choices:
      - present
      - absent
      - modify
      - add_initiator_chap
      - remove_initiator_chap
      - add_target_chap
      - remove_target_chap
      - add_fc_path_to_host
      - remove_fc_path_from_host
      - add_iscsi_path_to_host
      - remove_iscsi_path_from_host
    description:
      - "Whether the specified Host should exist or not. State also provides
       actions to add and remove initiator and target chap, add fc/iscsi path
       to host.\n"
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
short_description: "Manage HPE 3PAR and PRIMERA Host"
version_added: "2.4"
'''

EXAMPLES = r'''
    - name: Create Host "{{ host_name }}"
      hpe3par_host:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"
        state=present
        host_name="{{ host_name }}"

    - name: Modify Host "{{ host_name }}"
      hpe3par_host:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"
        state=modify
        host_name="{{ host_name }}"
        host_new_name="{{ host_new_name }}"

    - name: Delete Host "{{ new_name }}"
      hpe3par_host:
        storage_system_ip="{{ storage_system_ip }}"
        storage_system_username="{{ storage_system_username }}"
        storage_system_password="{{ storage_system_password }}"
        state=absent
        host_name="{{ host_new_name }}"
'''

RETURN = r'''
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


def create_host(
        client_obj,
        storage_system_username,
        storage_system_password,
        host_name,
        host_iscsi_names,
        host_fc_wwns,
        host_domain,
        host_persona):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Host creation failed. Storage system username or password is \
null",
            {})
    if host_name is None:
        return (False, False, "Host creation failed. Host name is null", {})
    if len(host_name) < 1 or len(host_name) > 31:
        return (False, False, "Host create failed. Host name must be atleast 1 character and not more than 31 characters", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if not client_obj.hostExists(host_name):
            optional = dict()
            if host_domain is not None:
                optional['domain'] = host_domain

            if host_persona is not None:
                optional['persona'] = getattr(
                    client.HPE3ParClient, host_persona)

            client_obj.createHost(
                host_name,
                host_iscsi_names,
                host_fc_wwns,
                optional)
        else:
            return (True, False, "Host already present", {})
    except Exception as e:
        return (False, False, "Host creation failed | %s" % e, {})
    finally:
        client_obj.logout()
    return (True, True, "Created host %s successfully." % host_name, {})


def modify_host(
        client_obj,
        storage_system_username,
        storage_system_password,
        host_name,
        host_new_name,
        host_persona):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Host modification failed. Storage system username or password is \
null",
            {})
    if host_name is None:
        return (
            False,
            False,
            "Host modification failed. Host name is null",
            {})
    if len(host_name) < 1 or len(host_name) > 31:
        return (False, False, "Host create failed. Host name must be atleast 1 character and not more than 31 characters", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if host_persona is not None:
            host_persona = getattr(
                client.HPE3ParClient, host_persona)

        client_obj.modifyHost(
            host_name, {
                "newName": host_new_name, "persona": host_persona})
    except Exception as e:
        return (False, False, "Host modification failed | %s" % e, {})
    finally:
        client_obj.logout()
    return (True, True, "Modified host %s successfully." % host_name, {})


def delete_host(
        client_obj,
        storage_system_username,
        storage_system_password,
        host_name):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Host deletion failed. Storage system username or password is \
null",
            {})
    if host_name is None:
        return (False, False, "Host deletion failed. Host name is null", {})
    if len(host_name) < 1 or len(host_name) > 31:
        return (False, False, "Host create failed. Host name must be atleast 1 character and not more than 31 characters", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        if client_obj.hostExists(host_name):
            client_obj.deleteHost(host_name)
        else:
            return (True, False, "Host does not exist", {})
    except Exception as e:
        return (False, False, "Host deletion failed | %s" % e, {})
    finally:
        client_obj.logout()
    return (True, True, "Deleted host %s successfully." % host_name, {})


def add_initiator_chap(
        client_obj,
        storage_system_username,
        storage_system_password,
        host_name,
        chap_name,
        chap_secret,
        chap_secret_hex):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Host modification failed. Storage system username or password is \
null",
            {})
    if host_name is None:
        return (
            False,
            False,
            "Host modification failed. Host name is null",
            {})
    if len(host_name) < 1 or len(host_name) > 31:
        return (False, False, "Host create failed. Host name must be atleast 1 character and not more than 31 characters", {})
    if chap_name is None:
        return (
            False,
            False,
            "Host modification failed. Chap name is null",
            {})
    if chap_secret is None:
        return (
            False,
            False,
            "Host modification failed. chap_secret is null",
            {})
    try:
        if chap_secret_hex and len(chap_secret) != 32:
            return (
                False,
                False,
                "Add initiator chap failed. Chap secret hex is false and chap \
secret less than 32 characters",
                {})
        if not chap_secret_hex and (
                len(chap_secret) < 12 or len(chap_secret) > 16):
            return (
                False,
                False,
                "Add initiator chap failed. Chap secret hex is false and chap \
secret less than 12 characters or more than 16 characters",
                {})
        client_obj.login(storage_system_username, storage_system_password)
        client_obj.modifyHost(host_name,
                              {'chapOperationMode':
                               HPE3ParClient.CHAP_INITIATOR,
                               'chapOperation':
                               HPE3ParClient.HOST_EDIT_ADD,
                               'chapName': chap_name,
                               'chapSecret': chap_secret,
                               'chapSecretHex': chap_secret_hex})
    except Exception as e:
        return (False, False, "Add initiator chap failed | %s" % e, {})
    finally:
        client_obj.logout()
    return (True, True, "Added initiator chap.", {})


def remove_initiator_chap(
        client_obj,
        storage_system_username,
        storage_system_password,
        host_name):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Host modification failed. Storage system username or password is \
null",
            {})
    if host_name is None:
        return (
            False,
            False,
            "Host modification failed. Host name is null",
            {})
    if len(host_name) < 1 or len(host_name) > 31:
        return (False, False, "Host create failed. Host name must be atleast 1 character and not more than 31 characters", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        client_obj.modifyHost(
            host_name, {
                'chapOperation': HPE3ParClient.HOST_EDIT_REMOVE})
    except Exception as e:
        return (False, False, "Remove initiator chap failed | %s" % e, {})
    finally:
        client_obj.logout()
    return (True, True, "Removed initiator chap.", {})


def initiator_chap_exists(
        client_obj,
        storage_system_username,
        storage_system_password,
        host_name):
    try:
        client_obj.login(storage_system_username, storage_system_password)
        return client_obj.getHost(host_name).initiator_chap_enabled
    finally:
        client_obj.logout()


def add_target_chap(
        client_obj,
        storage_system_username,
        storage_system_password,
        host_name,
        chap_name,
        chap_secret,
        chap_secret_hex):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Host modification failed. Storage system username or password is \
null",
            {})
    if host_name is None:
        return (
            False,
            False,
            "Host modification failed. Host name is null",
            {})
    if len(host_name) < 1 or len(host_name) > 31:
        return (False, False, "Host create failed. Host name must be atleast 1 character and not more than 31 characters", {})
    if chap_name is None:
        return (
            False,
            False,
            "Host modification failed. Chap name is null",
            {})
    if chap_secret is None:
        return (
            False,
            False,
            "Host modification failed. chap_secret is null",
            {})
    if chap_secret_hex and len(chap_secret) != 32:
        return (
            False,
            False,
            'Attribute chap_secret must be 32 hexadecimal characters if \
chap_secret_hex is true',
            {})
    if not chap_secret_hex and (
            len(chap_secret) < 12 or len(chap_secret) > 16):
        return (
            False,
            False,
            'Attribute chap_secret must be 12 to 16 character if \
chap_secret_hex is false',
            {})
    try:
        if initiator_chap_exists(
                client_obj,
                storage_system_username,
                storage_system_password,
                host_name):
            client_obj.login(storage_system_username, storage_system_password)
            mod_request = {
                'chapOperationMode': HPE3ParClient.CHAP_TARGET,
                'chapOperation': HPE3ParClient.HOST_EDIT_ADD,
                'chapName': chap_name,
                'chapSecret': chap_secret,
                'chapSecretHex': chap_secret_hex}
            client_obj.modifyHost(host_name, mod_request)
        else:
            return (True, False, "Initiator chap does not exist", {})
    except Exception as e:
        return (False, False, "Add target chap failed | %s" % e, {})
    finally:
        client_obj.logout()
    return (True, True, "Added target chap.", {})


def remove_target_chap(
        client_obj,
        storage_system_username,
        storage_system_password,
        host_name):
    print (storage_system_username)
    print (storage_system_password)
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Host modification failed. Storage system username or password is \
null",
            {})
    if host_name is None:
        return (
            False,
            False,
            "Host modification failed. Host name is null",
            {})
    if len(host_name) < 1 or len(host_name) > 31:
        return (False, False, "Host create failed. Host name must be atleast 1 character and not more than 31 characters", {})
    try:
        client_obj.login(storage_system_username, storage_system_password)
        mod_request = {
            'chapOperation': HPE3ParClient.HOST_EDIT_REMOVE,
            'chapRemoveTargetOnly': True}
        client_obj.modifyHost(host_name, mod_request)
    except Exception as e:
        return (False, False, "Remove target chap failed | %s" % e, {})
    finally:
        client_obj.logout()
    return (True, True, "Removed target chap.", {}) 


def add_fc_path_to_host(
        client_obj,
        storage_system_username,
        storage_system_password,
        host_name,
        host_fc_wwns):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Host modification failed. Storage system username or password is \
null",
            {})
    if host_name is None:
        return (
            False,
            False,
            "Host modification failed. Host name is null",
            {})
    if len(host_name) < 1 or len(host_name) > 31:
        return (False, False, "Host create failed. Host name must be atleast 1 character and not more than 31 characters", {})
    if host_fc_wwns is None:
        return (
            False,
            False,
            "Host modification failed. host_fc_wwns is null",
            {})
    try:
        client_obj.login(storage_system_username, storage_system_password)

        # check if wwn is already assigned
        wwn_new = []
        wwn_same_host = []
        wwn_other_host = []

        for wwn in host_fc_wwns:
            wwn_list = [wwn]
            host_list = client_obj.queryHost(wwns=wwn_list)
            for host_obj in host_list:
                host_name_3par = host_obj.name
                if host_name == host_name_3par:
                    wwn_same_host.append(wwn)
                else:
                    wwn_other_host.append(wwn)

            if host_list == []:
                wwn_new.append(wwn)

        if wwn_other_host:
            str_wwn = ", ".join(wwn_other_host)
            client_obj.logout()
            return(False, False, "FC path(s) %s already assigned to other host" % str_wwn, {})
        elif wwn_new:
            mod_request = {
                'pathOperation': HPE3ParClient.HOST_EDIT_ADD,
                'FCWWNs': wwn_new}
            client_obj.modifyHost(host_name, mod_request)
            client_obj.logout()
            str_wwn = ", ".join(wwn_new)
            return (True, True, "Added FC path(s) %s to host successfully." % str_wwn, {})
        elif wwn_same_host:
            str_wwn = ", ".join(wwn_same_host)
            client_obj.logout()
            return(True, False, "FC path(s) %s already assigned to this host" % str_wwn, {})

    except Exception as e:
        return (False, False, "Add FC path to host failed | %s" % e, {})
    finally:
        client_obj.logout()


def remove_fc_path_from_host(
        client_obj,
        storage_system_username,
        storage_system_password,
        host_name,
        host_fc_wwns,
        force_path_removal):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Host modification failed. Storage system username or password is \
null",
            {})
    if host_name is None:
        return (
            False,
            False,
            "Host modification failed. Host name is null",
            {})
    if len(host_name) < 1 or len(host_name) > 31:
        return (False, False, "Host create failed. Host name must be atleast 1 character and not more than 31 characters", {})
    if host_fc_wwns is None:
        return (
            False,
            False,
            "Host modification failed. host_fc_wwns is null",
            {})
    try:
        client_obj.login(storage_system_username, storage_system_password)

        # check various possibilities
        wwn_new = []
        wwn_same_host = []
        wwn_other_host = []

        for wwn in host_fc_wwns:
            wwn_list = [wwn]
            host_list = client_obj.queryHost(wwns=wwn_list)
            for host_obj in host_list:
                host_name_3par = host_obj.name
                if host_name == host_name_3par:
                    wwn_same_host.append(wwn)
                else:
                    wwn_other_host.append(wwn)

            if host_list == []:
                wwn_new.append(wwn)

        if wwn_other_host:
            str_wwn = ", ".join(wwn_other_host)
            client_obj.logout()
            return(False, False, "FC path(s) %s assigned to other host" % str_wwn, {})
        elif wwn_same_host:
            mod_request = {
                'pathOperation': HPE3ParClient.HOST_EDIT_REMOVE,
                'FCWWNs': wwn_same_host,
                'forcePathRemoval': force_path_removal}
            client_obj.modifyHost(host_name, mod_request)
            client_obj.logout()
            str_wwn = ", ".join(wwn_same_host)
            return (True, True, "Removed FC path(s) %s from host successfully." % str_wwn, {})
        elif wwn_new:
            str_wwn = ", ".join(wwn_new)
            client_obj.logout()
            return(True, False, "FC path(s) %s seem to be already removed" % str_wwn, {})

    except Exception as e:
        return (False, False, "Remove FC path from host failed | %s" % e, {})
    finally:
        client_obj.logout()


def add_iscsi_path_to_host(
        client_obj,
        storage_system_username,
        storage_system_password,
        host_name,
        host_iscsi_names):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Host modification failed. Storage system username or password is \
null",
            {})
    if host_name is None:
        return (
            False,
            False,
            "Host modification failed. Host name is null",
            {})
    if len(host_name) < 1 or len(host_name) > 31:
        return (False, False, "Host create failed. Host name must be atleast 1 character and not more than 31 characters", {})
    if host_iscsi_names is None:
        return (
            False,
            False,
            "Host modification failed. host_iscsi_names is null",
            {})

    try:
        client_obj.login(storage_system_username, storage_system_password)

        # check if iscsi name is already assigned
        iqn_new = []
        iqn_same_host = []
        iqn_other_host = []

        for iqn in host_iscsi_names:
            iscsi_name = [iqn]
            host_list = client_obj.queryHost(iqns=iscsi_name)
            for host_obj in host_list:
                host_name_3par = host_obj.name
                if host_name == host_name_3par:
                    iqn_same_host.append(iqn)
                else:
                    iqn_other_host.append(iqn)

            if host_list == []:
                iqn_new.append(iqn)

        if iqn_other_host:
            str_iqn = ", ".join(iqn_other_host)
            client_obj.logout()
            return(False, False, "iSCSI name(s) %s already assigned to other host" % str_iqn, {})
        elif iqn_new:
            mod_request = {
                'pathOperation': HPE3ParClient.HOST_EDIT_ADD,
                'iSCSINames': iqn_new}
            client_obj.modifyHost(host_name, mod_request)
            client_obj.logout()
            str_iqn = ", ".join(iqn_new)
            return (True, True, "Added iSCSI path(s) %s to host successfully." % str_iqn, {})
        elif iqn_same_host:
            str_iqn = ", ".join(iqn_same_host)
            client_obj.logout()
            return(True, False, "iSCSI name(s) %s already assigned to this host" % str_iqn, {})

    except Exception as e:
        return (False, False, "Add ISCSI path to host failed | %s" % e, {})
    finally:
        client_obj.logout()


def remove_iscsi_path_from_host(
        client_obj,
        storage_system_username,
        storage_system_password,
        host_name,
        host_iscsi_names,
        force_path_removal):
    if storage_system_username is None or storage_system_password is None:
        return (
            False,
            False,
            "Host modification failed. Storage system username or password is \
null",
            {})
    if host_name is None:
        return (
            False,
            False,
            "Host modification failed. Host name is null",
            {})
    if len(host_name) < 1 or len(host_name) > 31:
        return (False, False, "Host create failed. Host name must be atleast 1 character and not more than 31 characters", {})
    if host_iscsi_names is None:
        return (
            False,
            False,
            "Host modification failed. host_iscsi_names is null",
            {})

    try:
        client_obj.login(storage_system_username, storage_system_password)

        # check various possibilities
        iqn_new = []
        iqn_same_host = []
        iqn_other_host = []

        for iqn in host_iscsi_names:
            iscsi_name = [iqn]
            host_list = client_obj.queryHost(iqns=iscsi_name)
            for host_obj in host_list:
                host_name_3par = host_obj.name
                if host_name == host_name_3par:
                    iqn_same_host.append(iqn)
                else:
                    iqn_other_host.append(iqn)

            if host_list == []:
                iqn_new.append(iqn)

        if iqn_other_host:
            str_iqn = ", ".join(iqn_other_host)
            client_obj.logout()
            return(False, False, "iSCSI name(s) %s assigned to other host" % str_iqn, {})
        elif iqn_same_host:
            mod_request = {
                'pathOperation': HPE3ParClient.HOST_EDIT_REMOVE,
                'iSCSINames': iqn_same_host,
                'forcePathRemoval': force_path_removal}
            client_obj.modifyHost(host_name, mod_request)
            client_obj.logout()
            str_iqn = ", ".join(iqn_same_host)
            return(True, True, "Removed iSCSI path(s) %s from host successfully." % str_iqn, {})
        elif iqn_new:
            str_iqn = ", ".join(iqn_new)
            client_obj.logout()
            return(True, False, "iSCSI name(s) %s seem to be already removed" % str_iqn, {})

    except Exception as e:
        return (
            False,
            False,
            "Remove ISCSI path from host failed | %s" %
            e,
            {})
    finally:
        client_obj.logout()


def main():

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

    module = AnsibleModule(argument_spec=fields)

    if client is None:
        module.fail_json(msg='the python hpe3par_sdk module is required')
    if HPE3ParClient is None:
        module.fail_json(msg='the python python-3parclient module is required')

    storage_system_ip = module.params["storage_system_ip"]
    storage_system_username = module.params["storage_system_username"]
    storage_system_password = module.params["storage_system_password"]

    host_name = module.params["host_name"]
    host_new_name = module.params["host_new_name"]
    host_domain = module.params["host_domain"]
    host_fc_wwns = module.params["host_fc_wwns"]
    host_iscsi_names = module.params["host_iscsi_names"]
    host_persona = module.params["host_persona"]
    chap_name = module.params["chap_name"]
    chap_secret = module.params["chap_secret"]
    chap_secret_hex = module.params["chap_secret_hex"]
    force_path_removal = module.params["force_path_removal"]

    port_number = client.HPE3ParClient.getPortNumber(
        storage_system_ip, storage_system_username, storage_system_password)
    wsapi_url = 'https://%s:%s/api/v1' % (storage_system_ip, port_number)
    client_obj = client.HPE3ParClient(wsapi_url)

    # States
    if module.params["state"] == "present":
        return_status, changed, msg, issue_attr_dict = create_host(
            client_obj, storage_system_username, storage_system_password,
            host_name, host_iscsi_names, host_fc_wwns, host_domain,
            host_persona)
    elif module.params["state"] == "modify":
        return_status, changed, msg, issue_attr_dict = modify_host(
            client_obj, storage_system_username, storage_system_password,
            host_name, host_new_name, host_persona)
    elif module.params["state"] == "absent":
        return_status, changed, msg, issue_attr_dict = delete_host(
            client_obj, storage_system_username, storage_system_password,
            host_name)
    elif module.params["state"] == "add_initiator_chap":
        return_status, changed, msg, issue_attr_dict = add_initiator_chap(
            client_obj, storage_system_username, storage_system_password,
            host_name, chap_name, chap_secret, chap_secret_hex)
    elif module.params["state"] == "remove_initiator_chap":
        return_status, changed, msg, issue_attr_dict = (
            remove_initiator_chap(client_obj, storage_system_username,
                                  storage_system_password,
                                  host_name))
    elif module.params["state"] == "add_target_chap":
        return_status, changed, msg, issue_attr_dict = add_target_chap(
            client_obj, storage_system_username, storage_system_password,
            host_name, chap_name, chap_secret, chap_secret_hex)
    elif module.params["state"] == "remove_target_chap":
        return_status, changed, msg, issue_attr_dict = remove_target_chap(
            client_obj, storage_system_username, storage_system_password,
            host_name)
    elif module.params["state"] == "add_fc_path_to_host":
        return_status, changed, msg, issue_attr_dict = add_fc_path_to_host(
            client_obj, storage_system_username, storage_system_password,
            host_name, host_fc_wwns)
    elif module.params["state"] == "remove_fc_path_from_host":
        return_status, changed, msg, issue_attr_dict = (
            remove_fc_path_from_host(client_obj, storage_system_username,
                                     storage_system_password, host_name,
                                     host_fc_wwns, force_path_removal))
    elif module.params["state"] == "add_iscsi_path_to_host":
        return_status, changed, msg, issue_attr_dict = add_iscsi_path_to_host(
            client_obj, storage_system_username, storage_system_password,
            host_name, host_iscsi_names)
    elif module.params["state"] == "remove_iscsi_path_from_host":
        return_status, changed, msg, issue_attr_dict = (
            remove_iscsi_path_from_host(client_obj, storage_system_username,
                                        storage_system_password, host_name,
                                        host_iscsi_names, force_path_removal))

    if return_status:
        if issue_attr_dict:
            module.exit_json(changed=changed, msg=msg, issue=issue_attr_dict)
        else:
            module.exit_json(changed=changed, msg=msg)
    else:
        module.fail_json(msg=msg)


if __name__ == '__main__':
    main()
