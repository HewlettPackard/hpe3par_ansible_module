# HPE 3PAR modules for Ansible

The HPE 3PAR modules for Ansible enable automation of storage provisioning for the HPE 3PAR StoreServ array. The modules use the Python 3PAR SDK to communicate with the storage array over the WSAPI REST interface.

## Requirements
* Ansible ver. 2.5
* [hpe3par_sdk](https://pypi.org/project/hpe3par_sdk/)
* 3PAR OS - 3.2.2 MU6, 3.3.1 MU1
* WSAPI service should be enabled on the 3PAR storage array.

## Configuration
* Install Ansible and [hpe3par_sdk](https://pypi.org/project/hpe3par_sdk/)
* Modify ansible.cfg file to point the library to the Modules folder
```
library=/home/user/workspace/hpe3par_ansible/Modules
```

## Modules
This is developed as a set of modules and example playbooks to provision the following:
* [CPG](Modules/readme.md#hpe3par_cpg---manage-hpe-3par-cpg)
* [Host](Modules/readme.md#hpe3par_host---manage-hpe-3par-host)
* [Volume](Modules/readme.md#hpe3par_volume---manage-hpe-3par-volume)
* [VLUN](Modules/readme.md#hpe3par_vlun---manage-hpe-3par-vlun)
* [Host Set](Modules/readme.md#hpe3par_hostset---manage-hpe-3par-host-set)
* [Volume Set](Modules/readme.md#hpe3par_volumeset---manage-hpe-3par-volume-set)
* [Volume Offline Clone](Modules/readme.md#hpe3par_offline_clone---manage-hpe-3par-offline-clone)
* [Volume Online Clone](Modules/readme.md#hpe3par_online_clone---manage-hpe-3par-online-clone)
* [Volume Snapshot](Modules/readme.md#hpe3par_snapshot---manage-hpe-3par-snapshots)
* [QOS](Modules/readme.md#hpe3par_qos---manage-hpe-3par-qos-rules)
* [Flash Cache](Modules/readme.md#hpe3par_flash_cache---manage-hpe-3par-flash-cache)
* [Remote Copy](Modules/readme.md#hpe3par_remote_copy---manage-hpe-3par-remote-copy)


## Examples
``` {.sourceCode .yaml}
- name: Create CPG "{{ cpg_name }}"
  hpe3par_cpg:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=present
    cpg_name="{{ cpg_name }}"
    domain="{{ domain }}"
    growth_increment="{{ growth_increment }}"
    growth_increment_unit="{{ growth_increment_unit }}"
    growth_limit="{{ growth_limit }}"
    growth_limit_unit="{{ growth_limit_unit }}"
    growth_warning="{{ growth_warning }}"
    growth_warning_unit="{{ growth_warning_unit }}"
    raid_type="{{ raid_type }}"
    set_size="{{ set_size }}"
    high_availability="{{ high_availability }}"
    disk_type="{{ disk_type }}"

- name: Delete CPG "{{ cpg_name }}"
  hpe3par_cpg:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=absent
```
    
## Non Idempotent Actions

Actions are **_Idempotent_** when they can be run multiple times on the same system and the results will always be identical, without producing unintended side effects.

The following actions are **_non-idempotent_**:

- **Clone:** resync, create_offline
- **Snapshot:** restore online, restore offline
- **Virtual Volume:** grow (grow_to_size is idempotent)
- **VLUN:** All actions become non-idempotent when <em>autolun</em> is set to <em>true</em>

