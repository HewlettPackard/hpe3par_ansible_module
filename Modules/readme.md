source

:   hpe3par\_cpg.py

hpe3par\_cpg - Manage HPE 3PAR and PRIMERA CPG
==============================================

Synopsis
--------

-   Create and delete CPG on HPE 3PAR and PRIMERA.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
            <tr>
        <th class="head"><div class="cell-border">Parameter</div></th>
        <th class="head"><div class="cell-border">Choices/<font color="blue">Defaults</font></div></th>
                    <th class="head" width="100%"><div class="cell-border">Comments</div></th>
    </tr>
                <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>cpg_name</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Name of the CPG.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>disk_type</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>FC</li>
                                                                                                                                                                                                                    <li>NL</li>
                                                                                                                                                                                                                    <li>SSD</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies that physical disks must have the specified device type.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>domain</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the name of the domain in which the object will reside.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>growth_increment</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">-1.0</div>
                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the growth increment the amount of logical disk storage created on each auto-grow operation.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>growth_increment_unit</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>MiB</li>
                                                                                                                                                                                                                    <li><div style="color: blue"><b>GiB</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                                    <li>TiB</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Unit of growth increment.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>growth_limit</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">-1.0</div>
                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies that the autogrow operation is limited to the specified storage amount that sets the growth limit.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>growth_limit_unit</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>MiB</li>
                                                                                                                                                                                                                    <li><div style="color: blue"><b>GiB</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                                    <li>TiB</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Unit of growth limit.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>growth_warning</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">-1.0</div>
                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies that the threshold of used logical disk space when exceeded results in a warning alert.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>growth_warning_unit</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>MiB</li>
                                                                                                                                                                                                                    <li><div style="color: blue"><b>GiB</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                                    <li>TiB</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Unit of growth warning.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>high_availability</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>PORT</li>
                                                                                                                                                                                                                    <li>CAGE</li>
                                                                                                                                                                                                                    <li>MAG</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies that the layout must support the failure of one port pair, one cage, or one magazine.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>raid_type</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>R0</li>
                                                                                                                                                                                                                    <li>R1</li>
                                                                                                                                                                                                                    <li>R5</li>
                                                                                                                                                                                                                    <li>R6</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the RAID type for the logical disk.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>set_size</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">-1</div>
                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the set size in the number of chunklets.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>state</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>present</li>
                                                                                                                                                                                                                    <li>absent</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Whether the specified CPG should exist or not.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_ip</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system IP address.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_password</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system password.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_username</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system user name.</div>
                                                                                            </div>
            </td>
        </tr>
                    </table>
<br/>
Examples
--------

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
    cpg_name="{{ cpg_name }}"
```


### Author

-   Farhan Nomani (@farhan7500)
-   Gautham P Hegde (@gautamphegde)

source

:   hpe3par\_flash\_cache.py


hpe3par\_flash\_cache - Manage HPE 3PAR and PRIMERA Flash Cache
===============================================================

Synopsis
--------

-   On HPE 3PAR and PRIMERA - Create Flash Cache - Delete Flash Cache

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
            <tr>
        <th class="head"><div class="cell-border">Parameter</div></th>
        <th class="head"><div class="cell-border">Choices/<font color="blue">Defaults</font></div></th>
                    <th class="head" width="100%"><div class="cell-border">Comments</div></th>
    </tr>
                <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>mode</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Simulator 1 Real 2 (default)</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>size_in_gib</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the node pair size of the Flash Cache on the system.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>state</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>present</li>
                                                                                                                                                                                                                    <li>absent</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Whether the specified Flash Cache should exist or not.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_ip</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system IP address.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_password</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system password.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_username</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system user name.</div>
                                                                                            </div>
            </td>
        </tr>
                    </table>
<br/>
Examples
--------

``` {.sourceCode .yaml}
- name: Create Flash Cache
  hpe3par_flash_cache:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=present
    size_in_gib="{{ size_in_gib }}"

- name: Delete Flash Cache
  hpe3par_flash_cache:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=absent
```

### Author

-   Farhan Nomani (<nomani@hpe.com>)

source

:   hpe3par\_host.py


hpe3par\_host - Manage HPE 3PAR and PRIMERA Host
================================================

Synopsis
--------

-   On HPE 3PAR and PRIMERA - Create Host - Delete Host - Add Initiator
    Chap - Remove Initiator Chap - Add Target Chap - Remove Target
    Chap - Add FC Path to Host - Remove FC Path from Host - Add ISCSI
    Path to Host - Remove ISCSI Path from Host

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
            <tr>
        <th class="head"><div class="cell-border">Parameter</div></th>
        <th class="head"><div class="cell-border">Choices/<font color="blue">Defaults</font></div></th>
                    <th class="head" width="100%"><div class="cell-border">Comments</div></th>
    </tr>
                <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>chap_name</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The chap name.
Required with actions add_initiator_chap, add_target_chap</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>chap_secret</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The chap secret for the host or the target
Required with actions add_initiator_chap, add_target_chap</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>chap_secret_hex</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>If true, then chapSecret is treated as Hex.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>force_path_removal</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>If true, remove WWN(s) or iSCS<em>s</em> even if there are VLUNs that are exported to the host.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>host_domain</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Create the host in the specified domain, or in the default domain, if unspecified</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>host_fc_wwns</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Set one or more WWNs for the host.
Required with action add_fc_path_to_host, remove_fc_path_from_host</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>host_iscsi_names</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Set one or more iSCSI names for the host.
Required with action add_iscsi_path_to_host, remove_iscsi_path_from_host</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>host_name</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Name of the Host.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>host_new_name</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>New name of the Host.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>host_persona</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>GENERIC</li>
                                                                                                                                                                                                                    <li>GENERIC_ALUA</li>
                                                                                                                                                                                                                    <li>GENERIC_LEGACY</li>
                                                                                                                                                                                                                    <li>HPUX_LEGACY</li>
                                                                                                                                                                                                                    <li>AIX_LEGACY</li>
                                                                                                                                                                                                                    <li>EGENERA</li>
                                                                                                                                                                                                                    <li>ONTAP_LEGACY</li>
                                                                                                                                                                                                                    <li>VMWARE</li>
                                                                                                                                                                                                                    <li>OPENVMS</li>
                                                                                                                                                                                                                    <li>HPUX</li>
                                                                                                                                                                                                                    <li>WINDOWS_SERVER</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>ID of the persona to assign to the host. Uses the default persona unless you specify the host persona.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>state</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>present</li>
                                                                                                                                                                                                                    <li>absent</li>
                                                                                                                                                                                                                    <li>modify</li>
                                                                                                                                                                                                                    <li>add_initiator_chap</li>
                                                                                                                                                                                                                    <li>remove_initiator_chap</li>
                                                                                                                                                                                                                    <li>add_target_chap</li>
                                                                                                                                                                                                                    <li>remove_target_chap</li>
                                                                                                                                                                                                                    <li>add_fc_path_to_host</li>
                                                                                                                                                                                                                    <li>remove_fc_path_from_host</li>
                                                                                                                                                                                                                    <li>add_iscsi_path_to_host</li>
                                                                                                                                                                                                                    <li>remove_iscsi_path_from_host</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Whether the specified Host should exist or not. State also provides actions to add and remove initiator and target chap, add fc/iscsi path to host.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_ip</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system IP address.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_password</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system password.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_username</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system user name.</div>
                                                                                            </div>
            </td>
        </tr>
                    </table>
<br/>
Examples
--------

``` {.sourceCode .yaml}
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
```

### Author

-   Farhan Nomani (<nomani@hpe.com>)

source

:   hpe3par\_hostset.py


hpe3par\_hostset - Manage HPE 3PAR and PRIMERA Host Set
=======================================================

Synopsis
--------

-   On HPE 3PAR and PRIMERA - Create Host Set - Add Hosts to Host Set -
    Remove Hosts from Host Set

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
            <tr>
        <th class="head"><div class="cell-border">Parameter</div></th>
        <th class="head"><div class="cell-border">Choices/<font color="blue">Defaults</font></div></th>
                    <th class="head" width="100%"><div class="cell-border">Comments</div></th>
    </tr>
                <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>domain</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The domain in which the VV set or host set will be created.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>hostset_name</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Name of the host set to be created.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>setmembers</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The host to be added to the set.
Required with action add_hosts, remove_hosts</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>state</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>present</li>
                                                                                                                                                                                                                    <li>absent</li>
                                                                                                                                                                                                                    <li>add_hosts</li>
                                                                                                                                                                                                                    <li>remove_hosts</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Whether the specified Host Set should exist or not. State also provides actions to add or remove hosts from host set</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_ip</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system IP address.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_password</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system password.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_username</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system user name.</div>
                                                                                            </div>
            </td>
        </tr>
                    </table>
<br/>
Examples
--------

``` {.sourceCode .yaml}
- name: Create hostset "{{ hostsetset_name }}"
  hpe3par_hostset:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=present
    hostset_name="{{ hostset_name }}"
    setmembers="{{ add_host_setmembers }}"

- name: Add hosts to Hostset "{{ hostsetset_name }}"
  hpe3par_hostset:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=add_hosts
    hostset_name="{{ hostset_name }}"
    setmembers="{{ add_host_setmembers2 }}"

- name: Remove hosts from Hostset "{{ hostsetset_name }}"
  hpe3par_hostset:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=remove_hosts
    hostset_name="{{ hostset_name }}"
    setmembers="{{ remove_host_setmembers }}"

- name: Delete Hostset "{{ hostset_name }}"
  hpe3par_hostset:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=absent
    hostset_name="{{ hostset_name }}"
```

### Author

-   Farhan Nomani (<nomani@hpe.com>)

source

:   hpe3par\_offline\_clone.py
  

hpe3par\_offline\_clone - Manage HPE 3PAR and PRIMERA Offline Clone
===================================================================

Synopsis
--------

-   On HPE 3PAR and PRIMERA - Create Offline Clone - Delete Clone -
    Resync Clone - Stop Cloning

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
            <tr>
        <th class="head"><div class="cell-border">Parameter</div></th>
        <th class="head"><div class="cell-border">Choices/<font color="blue">Defaults</font></div></th>
                    <th class="head" width="100%"><div class="cell-border">Comments</div></th>
    </tr>
                <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>base_volume_name</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the source volume.
Required with action present, absent, stop</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>clone_name</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the destination volume.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>dest_cpg</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the destination CPG for an online copy.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>priority</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>HIGH</li>
                                                                                                                                                                                                                    <li><div style="color: blue"><b>MEDIUM</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                                    <li>LOW</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Priority of action.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>save_snapshot</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Enables (true) or disables (false) saving the the snapshot of the source volume after completing the copy of the volume.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>skip_zero</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Enables (true) or disables (false) copying only allocated portions of the source VV from a thin provisioned source.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>state</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>present</li>
                                                                                                                                                                                                                    <li>absent</li>
                                                                                                                                                                                                                    <li>resync</li>
                                                                                                                                                                                                                    <li>stop</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Whether the specified Clone should exist or not. State also provides actions to resync and stop clone</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_ip</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system IP address.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_password</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system password.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_username</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system user name.</div>
                                                                                            </div>
            </td>
        </tr>
                    </table>
<br/>
Examples
--------

``` {.sourceCode .yaml}
- name: Create Clone {{ clone_name }}
  hpe3par_offline_clone:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=present
    clone_name={{ clone_name }}
    base_volume_name="{{ volume_name }}"
    dest_cpg="{{ cpg }}"
    priority="MEDIUM"

- name: Stop Clone {{ clone_name }}
  hpe3par_offline_clone:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=stop
    clone_name={{ clone_name }}
    base_volume_name="{{ volume_name }}"

- name: Delete clone {{ clone_name }}
  hpe3par_offline_clone:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=absent
    clone_name={{ clone_name }}
    base_volume_name="{{ volume_name }}"
```

### Author

-   Farhan Nomani (<nomani@hpe.com>)

source

:   hpe3par\_online\_clone.py

hpe3par\_online\_clone - Manage HPE 3PAR and PRIMERA Online Clone
=================================================================

Synopsis
--------

-   On HPE 3PAR and PRIMERA - Create Online Clone - Delete Clone -
    Resync Clone

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
            <tr>
        <th class="head"><div class="cell-border">Parameter</div></th>
        <th class="head"><div class="cell-border">Choices/<font color="blue">Defaults</font></div></th>
                    <th class="head" width="100%"><div class="cell-border">Comments</div></th>
    </tr>
                <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>base_volume_name</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the source volume.
Required with action present, absent, stop</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>clone_name</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the destination volume.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>compression</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Enables (true) or disables (false) compression of the created volume. Only tpvv or tdvv are compressed.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>dest_cpg</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the destination CPG for an online copy.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>snap_cpg</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the snapshot CPG for an online copy.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>state</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>present</li>
                                                                                                                                                                                                                    <li>absent</li>
                                                                                                                                                                                                                    <li>resync</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Whether the specified Clone should exist or not. State also provides actions to resync clone</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_ip</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system IP address.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_password</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system password.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_username</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system user name.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>tdvv</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Enables (true) or disables (false) whether the online copy is a TDVV.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>tpvv</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Enables (true) or disables (false) whether the online copy is a TPVV.</div>
                                                                                            </div>
            </td>
        </tr>
                    </table>
<br/>
Examples
--------

``` {.sourceCode .yaml}
- name: Create Clone clone_volume_ansible
  hpe3par_online_clone:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=present
    clone_name="clone_volume_ansible"
    base_volume_name="{{ volume_name }}"
    dest_cpg="{{ cpg }}"
    tpvv=False
    tdvv=False
    compression=False
    snap_cpg="{{ cpg }}"

- name: sleep for 100 seconds and continue with play
  wait_for:
    timeout=100

- name: Delete clone "clone_volume_ansible"
  hpe3par_online_clone:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=absent
    clone_name="clone_volume_ansible"
    base_volume_name="{{ volume_name }}"
```

### Author

-   Farhan Nomani (<nomani@hpe.com>)

source

:   hpe3par\_qos.py
 

hpe3par\_qos - Manage HPE 3PAR and PRIMERA QoS Rules
====================================================

Synopsis
--------

-   On HPE 3PAR and PRIMERA - Create QoS Rule - Delete QoS Rule - Modify
    QoS Rule

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
            <tr>
        <th class="head"><div class="cell-border">Parameter</div></th>
        <th class="head"><div class="cell-border">Choices/<font color="blue">Defaults</font></div></th>
                    <th class="head" width="100%"><div class="cell-border">Comments</div></th>
    </tr>
                <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>bwmax_limit_kb</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">-1</div>
                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Bandwidth rate maximum limit in kilobytes per second.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>bwmax_limit_op</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>ZERO</li>
                                                                                                                                                                                                                    <li>NOLIMIT</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>When set to 1, the bandwidth maximum limit is 0. When set to 2, the bandwidth maximum limit is none (NoLimit).</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>bwmin_goal_kb</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">-1</div>
                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Bandwidth rate minimum goal in kilobytes per second.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>bwmin_goal_op</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>ZERO</li>
                                                                                                                                                                                                                    <li>NOLIMIT</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>When set to 1, the bandwidth minimum goal is 0. When set to 2, the bandwidth minimum goal is none (NoLimit).</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>default_latency</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>If true, set latencyGoal to the default value. If false and the latencyGoal value is positive, then set the value. Default is false.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>enable</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>If true, enable the QoS rule for the target object. If false, disable the QoS rule for the target object.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>iomax_limit</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">-1</div>
                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>I/O-per-second maximum limit.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>iomax_limit_op</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>ZERO</li>
                                                                                                                                                                                                                    <li>NOLIMIT</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>When set to 1, the I/O maximum limit is 0. When set to 2, the I/O maximum limit is none (NoLimit).</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>iomin_goal</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">-1</div>
                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>I/O-per-second minimum goal.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>iomin_goal_op</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>ZERO</li>
                                                                                                                                                                                                                    <li>NOLIMIT</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>When set to 1, the I/O minimum goal is 0. When set to 2, the I/O minimum goal is none (NoLimit).</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>latency_goal</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Latency goal in milliseconds. Do not use with latencyGoaluSecs.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>latency_goal_usecs</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Latency goal in microseconds. Do not use with latencyGoal.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>priority</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li><div style="color: blue"><b>LOW</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                                    <li>NORMAL</li>
                                                                                                                                                                                                                    <li>HIGH</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>QoS priority.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>qos_target_name</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The name of the target object on which the new QoS rules will be created.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>state</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>present</li>
                                                                                                                                                                                                                    <li>absent</li>
                                                                                                                                                                                                                    <li>modify</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Whether the specified QoS Rule should exist or not. State also provides actions to modify QoS Rule</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_ip</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system IP address.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_password</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system password.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_username</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system user name.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>type</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>vvset</li>
                                                                                                                                                                                                                    <li>sys</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Type of QoS target.</div>
                                                                                            </div>
            </td>
        </tr>
                    </table>
<br/>
Examples
--------

``` {.sourceCode .yaml}
- name: Create QoS
  hpe3par_qos:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=present
    qos_target_name="{{ qos_target_name }}"
    priority='NORMAL'
    bwmin_goal_kb="{{ bwmin_goal_kb }}"
    bwmax_limit_kb="{{ bwmax_limit_kb }}"
    iomin_goal_op="{{ iomin_goal_op }}"
    default_latency="{{ default_latency }}"
    enable="{{ enable }}"
    bwmin_goal_op="{{ bwmin_goal_op }}"
    bwmax_limit_op="{{ bwmax_limit_op }}"
    latency_goal_usecs="{{ latency_goal_usecs }}"
    type="{{ type }}"
    iomax_limit_op="{{ iomax_limit_op }}"

- name: Modify QoS
  hpe3par_qos:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=modify
    qos_target_name="{{ qos_target_name }}"
    priority="{{ priority }}"
    bwmin_goal_kb="{{ bwmin_goal_kb }}"
    bwmax_limit_kb="{{ bwmax_limit_kb }}"
    iomin_goal_op="{{ iomin_goal_op }}"
    default_latency="{{ default_latency }}"
    enable="{{ enable }}"
    bwmin_goal_op="{{ bwmin_goal_op }}"
    bwmax_limit_op="{{ bwmax_limit_op }}"
    latency_goal_usecs="{{ latency_goal_usecs }}"
    type="{{ type }}"
    iomax_limit_op="{{ iomax_limit_op }}"

- name: Delete QoS
  hpe3par_qos:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=absent
    qos_target_name="{{ qos_target_name }}"
    type="{{ type }}"
```

### Author

-   Farhan Nomani (<nomani@hpe.com>)

source

:   hpe3par\_snapshot.py

hpe3par\_snapshot - Manage HPE 3PAR and PRIMERA Snapshots
=========================================================

Synopsis
--------

-   On HPE 3PAR and PRIMERA - Create Snapshot - Delete Snapshot - Modify
    Snapshot - Create Schedule - Modify Schedule - Suspend Schedule -
    Resume Schedule - Delete Schedule

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
            <tr>
        <th class="head"><div class="cell-border">Parameter</div></th>
        <th class="head"><div class="cell-border">Choices/<font color="blue">Defaults</font></div></th>
                    <th class="head" width="100%"><div class="cell-border">Comments</div></th>
    </tr>
                <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>allow_remote_copy_parent</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Allows the promote operation to proceed even if the RW parent volume is currently in a Remote Copy volume group, if that group has not been started. If the Remote Copy group has been started, this command fails.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>base_volume_name</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the source volume.
Required with action present</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>expiration_hours</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the relative time from the current time that the volume expires. Value is a positive integer and in the range of 1 to 43,800 hours, or 1825 days.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>expiration_time</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the relative time from the current time that the volume expires. Value is a positive integer and in the range of 1 to 43,800 hours, or 1825 days.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>expiration_unit</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li><div style="color: blue"><b>Hours</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                                    <li>Days</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Unit of Expiration Time.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>new_name</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>New name of the volume.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>new_schedule_name</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>New Name of the schedule.</div>
                                                                                            </div>
            </td>
        </tr>            
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>priority</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>HIGH</li>
                                                                                                                                                                                                                    <li>MEDIUM</li>
                                                                                                                                                                                                                    <li>LOW</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Does not apply to online promote operation or to stop promote operation.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>read_only</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies that the copied volume is read-only. false(default) The volume is read/write.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>retention_hours</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the relative time from the current time that the volume expires. Value is a positive integer and in the range of 1 to 43,800 hours, or 1825 days.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>retention_time</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies the relative time from the current time that the volume will expire. Value is a positive integer and in the range of 1 to 43,800 hours, or 1825 days.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>retention_unit</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li><div style="color: blue"><b>Hours</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                                    <li>Days</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Unit of Retention Time.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>rm_exp_time</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Enables (false) or disables (true) resetting the expiration time. If false, and expiration time value is a positive number, then set.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>snapshot_name</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies a snapshot volume name.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>schedule_name</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Specifies name of the schedule.</div>
                                                                                            </div>
            </td>
        </tr>  
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>task_freq</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Frequency as special string for the schedule to be created.</div>
                                                                                            </div>
            </td>
        </tr>                
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>state</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>present</li>
                                                                                                                                                                                                                    <li>absent</li>
                                                                                                                                                                                                                    <li>modify</li>
                                                                                                                                                                                                                    <li>restore_offline</li>
                                                                                                                                                                                                                    <li>restore_online</li>
                                                                                                                                                                                                                    <li>create_schedule</li>
                                                                                                                                                                                                                    <li>modify_schedule</li>
                                                                                                                                                                                                                    <li>suspend_schedule</li>
                                                                                                                                                                                                                    <li>resume_schedule</li>
                                                                                                                                                                                                                    <li>delete_schedule</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Whether the specified Snapshot should exist or not. State also provides actions to modify and restore snapshots.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_ip</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system IP address.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_password</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system password.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_username</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system user name.</div>
                                                                                            </div>
            </td>
        </tr>
                    </table>
<br/>
Examples
--------

``` {.sourceCode .yaml}
- name: Create Volume snasphot my_ansible_snapshot
  hpe3par_snapshot:
    storage_system_ip: 10.10.10.1
    storage_system_username: username
    storage_system_password: password
    state: present
    snapshot_name: snap-volume
    base_volume_name: test_volume
    read_only: False
    
- name: Restore offline Volume snasphot my_ansible_snapshot
  hpe3par_snapshot:
    storage_system_ip: 10.10.10.1
    storage_system_username: username
    storage_system_password: password
    state: restore_offline
    snapshot_name: snap-volume
    priority: MEDIUM
    
- name: Restore offline Volume snasphot my_ansible_snapshot
  hpe3par_snapshot:
    storage_system_ip: 10.10.10.1
    storage_system_username: username
    storage_system_password: password
    state: restore_online
    snapshot_name: snap-volume
    
- name: Modify/rename snasphot my_ansible_snapshot to my_ansible_snapshot_renamed
  hpe3par_snapshot:
    storage_system_ip: 10.10.10.1
    storage_system_username: username
    storage_system_password: password
    state: modify
    snapshot_name: snap-volume
    new_name: snapshot-volume
    
- name: Delete snasphot my_ansible_snapshot_renamed
  hpe3par_snapshot:
    storage_system_ip: 10.10.10.1
    storage_system_username: username
    storage_system_password: password
    state: absent
    snapshot_name: snap-volume
    
- name: Create schedule my_ansible_sc
  hpe3par_snapshot:
    storage_system_ip: 10.10.10.1
    storage_system_username: username
    storage_system_password: password
    state: create_schedule
    schedule_name: my_ansible_sc
    base_volume_name: test_volume
    
- name: Modify schedule my_ansible_sc
  hpe3par_snapshot:
    storage_system_ip: 10.10.10.1
    storage_system_username: username
    storage_system_password: password
    state: create_schedule
    schedule_name: my_ansible_sc
    new_schedule_name: test_ansible_sc
- name: Delete schedule my_ansible_sc

  hpe3par_snapshot:
    storage_system_ip: 10.10.10.1
    storage_system_username: username
    storage_system_password: password
    state: delete_schedule
    schedule_name: my_ansible_sc   
```

### Author

-   Farhan Nomani (<nomani@hpe.com>)

source

:   hpe3par\_vlun.py


hpe3par\_vlun - Manage HPE 3PAR and PRIMERA VLUN
================================================

Synopsis
--------

-   On HPE 3PAR and PRIMERA - Export volume to host - Export volumeset
    to host - Export volume to hostset - Export volumeset to hostset -
    Unexport volume from host - Unexport volumeset from host - Unexport
    volume from hostset - Unexport volumeset from hostset

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
            <tr>
        <th class="head"><div class="cell-border">Parameter</div></th>
        <th class="head"><div class="cell-border">Choices/<font color="blue">Defaults</font></div></th>
                    <th class="head" width="100%"><div class="cell-border">Comments</div></th>
    </tr>
                <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>autolun</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                                    <li>yes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>States whether the lun number should be autosigned.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>card_port</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Port number on the FC card.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>host_name</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Name of the host to which the volume or VV set is to be exported.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>host_set_name</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Name of the host set to which the volume or VV set is to be exported. 
Required with action export_volume_to_hostset, unexport_volume_from_hostset, export_volumeset_to_hostset, unexport_volumeset_from_hostset</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>lunid</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>LUN ID.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>node_val</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>System node.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>slot</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>PCI bus slot in the node.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>state</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>export_volume_to_host</li>
                                                                                                                                                                                                                    <li>unexport_volume_from_host</li>
                                                                                                                                                                                                                    <li>export_volumeset_to_host</li>
                                                                                                                                                                                                                    <li>unexport_volumeset_from_host</li>
                                                                                                                                                                                                                    <li>export_volume_to_hostset</li>
                                                                                                                                                                                                                    <li>unexport_volume_from_hostset</li>
                                                                                                                                                                                                                    <li>export_volumeset_to_hostset</li>
                                                                                                                                                                                                                    <li>unexport_volumeset_from_hostset</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Whether the specified export should exist or not.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_ip</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system IP address.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_password</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system password.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_username</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system user name.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>volume_name</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Name of the volume to export.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>volume_set_name</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Name of the VV set to export.
Required with action export_volumeset_to_host, unexport_volumeset_from_host, export_volumeset_to_hostset, unexport_volumeset_from_hostset</div>
                                                                                            </div>
            </td>
        </tr>
                    </table>
<br/>
Examples
--------

``` {.sourceCode .yaml}
- name: Create VLUN
  hpe3par_vlun:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=export_volume_to_host
    volume_name="{{ volume_name }}"
    host_name="{{ host_name }}"
    lunid="{{ lunid }}"
    autolun="{{ autolun }}"

- name: Create VLUN
  hpe3par_vlun:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=export_volume_to_hostset
    volume_name="{{ vlun_volume_name }}"
    host_set_name="{{ hostset_name }}"
    lunid="{{ lunid }}"
    autolun="{{ autolun }}"

- name: Create VLUN
  hpe3par_vlun:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=export_volumeset_to_host
    volume_set_name="{{ volumeset_name }}"
    host_name="{{ vlun_host_name }}"
    lunid="{{ lunid }}"
    autolun="{{ autolun }}"

- name: Create VLUN
  hpe3par_vlun:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=export_volumeset_to_hostset
    volume_set_name="{{ volumeset_name }}"
    host_set_name="{{ hostset_name }}"
    lunid="{{ lunid }}"
    autolun="{{ autolun }}"

- name: Delete VLUN
  hpe3par_vlun:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=unexport_volume_from_host
    volume_name="{{ volume_name }}"
    host_name="{{ host_name }}"
    lunid="{{ lunid }}"
```

### Author

-   Farhan Nomani (<nomani@hpe.com>)

source

:   hpe3par\_volume.py


hpe3par\_volume - Manage HPE 3PAR and PRIMERA Volume
====================================================

Synopsis
--------

-   On HPE 3PAR and PRIMERA - Create Volume - Delete Volume - Modify
    Volume - Grow Volume - Grow Volume to certain size - Change Snap
    CPG - Change User CPG - Convert Provisioning TypeError - Set Snap
    CPG

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <b>compression</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Specifes whether the compression is on or off.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>cpg</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the name of the CPG from which the volume user space will be allocated.
Required with action present, change_user_cpg</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>expiration_hours</b>
                                                                        </td>
                            <td>
                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">0</div>
                                </td>
                                                            <td>
                                                                    <div>Remaining time, in hours, before the volume expires.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>keep_vv</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Name of the new volume where the original logical disks are saved.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>new_name</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the new name for the volume.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>retention_hours</b>
                                                                        </td>
                            <td>
                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">0</div>
                                </td>
                                                            <td>
                                                                    <div>Sets the number of hours to retain the volume.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>rm_exp_time</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Enables false or disables true resetting the expiration time. If false, and expiration time value is a positive. number, then set.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>rm_ss_spc_alloc_limit</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Enables false or disables true removing the snapshot space allocation limit. If false, and limit value is 0, setting  ignored.If false, and limit value is a positive number, then set.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>rm_ss_spc_alloc_warning</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Enables false or disables true removing the snapshot space allocation warning. If false, and warning value is a positive number, then set.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>rm_usr_spc_alloc_limit</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Enables false or disables true the allocation limit. If false, and limit value is a positive number, then set.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>rm_usr_spc_alloc_warning</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Enables false or disables true removing the user space allocation warning. If false, and warning value is a positive number, then set.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>size</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the size of the volume.
Required with action present, grow, grow_to_size</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>size_unit</b>
                                                                        </td>
                            <td>
                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>MiB</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>GiB</li>
                                                                                                                                                                                            <li>TiB</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the unit of the volume size.
Required with action present, grow, grow_to_size</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>snap_cpg</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the name of the CPG from which the snapshot space will be allocated.
Required with action change_snap_cpg</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>ss_spc_alloc_limit_pct</b>
                                                                        </td>
                            <td>
                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">0</div>
                                </td>
                                                            <td>
                                                                    <div>Prevents the snapshot space of  the virtual volume from growing beyond the indicated percentage of the virtual volume size.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>ss_spc_alloc_warning_pct</b>
                                                                        </td>
                            <td>
                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">0</div>
                                </td>
                                                            <td>
                                                                    <div>Generates a warning alert when the reserved snapshot space of the virtual volume exceeds the indicated percentage of the virtual volume size.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>state</b>
                                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                            <td>
                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                            <li>present</li>
                                                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>modify</li>
                                                                                                                                                                                            <li>grow</li>
                                                                                                                                                                                            <li>grow_to_size</li>
                                                                                                                                                                                            <li>change_snap_cpg</li>
                                                                                                                                                                                            <li>change_user_cpg</li>
                                                                                                                                                                                            <li>convert_type</li>
                                                                                                                                                                                            <li>set_snap_cpg</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Whether the specified Volume should exist or not. State also provides actions to modify volume properties.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>storage_system_ip</b>
                                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>The storage system IP address.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>storage_system_password</b>
                                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>The storage system password.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>storage_system_username</b>
                                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>The storage system user name.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>type</b>
                                                                        </td>
                            <td>
                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>thin</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>thin_dedupe</li>
                                                                                                                                                                                            <li>full</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the type of the volume.
Required with action convert_type. Full provisioning is not supported on Primera array</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>usr_spc_alloc_limit_pct</b>
                                                                        </td>
                            <td>
                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">0</div>
                                </td>
                                                            <td>
                                                                    <div>Prevents the user space of the TPVV from growing beyond the indicated percentage of the virtual volume size. After reaching this limit, any new writes to the virtual volume will fail.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>usr_spc_alloc_warning_pct</b>
                                                                        </td>
                            <td>
                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">0</div>
                                </td>
                                                            <td>
                                                                    <div>Generates a warning alert when the user data space of the TPVV exceeds the specified percentage of the virtual volume size.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>volume_name</b>
                                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Name of the Virtual Volume.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>wait_for_task_to_end</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Setting to true makes the resource to wait until a task asynchronous operation, for ex convert type ends.</div>
                                                                            </td>
        </tr>
                    </table>
<br/>
Examples
--------

``` {.sourceCode .yaml}
- name: Create Volume "{{ volume_name }}"
  hpe3par_volume:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=present
    volume_name="{{ volume_name }}"
    cpg="{{ cpg }}"
    size="{{ size }}"
    snap_cpg="{{ snap_cpg }}"

- name: Change provisioning type of Volume "{{ volume_name }}" to "{{ type }}"
  hpe3par_volume:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=convert_type
    volume_name="{{ volume_name }}"
    type="{{ type }}"
    cpg="{{ cpg }}"
    wait_for_task_to_end="{{ wait_for_task_to_end }}"

- name: Set Snap CPG of Volume "{{ volume_name }}" to "{{ snap_cpg }}"
  hpe3par_volume:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=set_snap_cpg
    volume_name="{{ volume_name }}"
    snap_cpg="{{ snap_cpg }}"

- name: Change snap CPG of Volume "{{ volume_name }}" to "{{ snap_cpg }}"
  hpe3par_volume:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=change_snap_cpg
    volume_name="{{ volume_name }}"
    snap_cpg="{{ snap_cpg }}"
    wait_for_task_to_end="{{ wait_for_task_to_end }}"

- name: Grow Volume "{{ volume_name }} by "{{ size }}" {{ size_unit }}"
  hpe3par_volume:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=grow
    volume_name="{{ volume_name }}"
    size="{{ size }}"
    size_unit="{{ size_unit }}"

- name: Grow Volume "{{ volume_name }} to "{{ size }}" {{ size_unit }}"
  hpe3par_volume:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=grow_to_size
    volume_name="{{ volume_name }}"
    size="{{ size }}"
    size_unit="{{ size_unit }}"

- name: Rename Volume "{{ volume_name }} to {{ new_name }}"
  hpe3par_volume:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=modify
    volume_name="{{ volume_name }}"
    new_name="{{ new_name }}"

- name: Delete Volume "{{ volume_name }}"
  hpe3par_volume:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=absent
    volume_name="{{ new_name }}"
```

### Author

-   Farhan Nomani (<nomani@hpe.com>)

source

:   hpe3par\_volumeset.py
 

hpe3par\_volumeset - Manage HPE 3PAR and PRIMERA Volume Set
===========================================================

Synopsis
--------

-   On HPE 3PAR and PRIMERA - Create Volume Set - Add Volumes to Volume
    Set - Remove Volumes from Volume Set

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
            <tr>
        <th class="head"><div class="cell-border">Parameter</div></th>
        <th class="head"><div class="cell-border">Choices/<font color="blue">Defaults</font></div></th>
                    <th class="head" width="100%"><div class="cell-border">Comments</div></th>
    </tr>
                <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>domain</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The domain in which the VV set or host set will be created.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>setmembers</b>
                                                                            </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The virtual volume to be added to the set.
Required with action add_volumes, remove_volumes</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>state</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                                                <li>present</li>
                                                                                                                                                                                                                    <li>absent</li>
                                                                                                                                                                                                                    <li>add_volumes</li>
                                                                                                                                                                                                                    <li>remove_volumes</li>
                                                                                            </ul>
                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Whether the specified Volume Set should exist or not. State also provides actions to add or remove volumes from volume set</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_ip</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system IP address.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_password</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system password.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>storage_system_username</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>The storage system user name.</div>
                                                                                            </div>
            </td>
        </tr>
                            <tr class="return-value-column">
                            <td>
                <div class="outer-elbow-container">
                                            <div class="elbow-key">
                        <b>volumeset_name</b>
                        <br/><div style="font-size: small; color: red">required</div>                                                    </div>
                </div>
            </td>
                            <td>
                <div class="cell-border">
                                                                                                                                                                                        </div>
            </td>
                                                            <td>
                <div class="cell-border">
                                                                                <div>Name of the volume set to be created.</div>
                                                                                            </div>
            </td>
        </tr>
                    </table>
<br/>
Examples
--------

``` {.sourceCode .yaml}
- name: Create volume set "{{ volumeset_name }}"
  hpe3par_volumeset:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=present
    volumeset_name="{{ volumeset_name }}"
    setmembers="{{ add_vol_setmembers }}"

- name: Add volumes to Volumeset "{{ volumeset_name }}"
  hpe3par_volumeset:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=add_volumes
    volumeset_name="{{ volumeset_name }}"
    setmembers="{{ add_vol_setmembers2 }}"

- name: Remove volumes from Volumeset "{{ volumeset_name }}"
  hpe3par_volumeset:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=remove_volumes
    volumeset_name="{{ volumeset_name }}"
    setmembers="{{ remove_vol_setmembers }}"

- name: Delete Volumeset "{{ volumeset_name }}"
  hpe3par_volumeset:
    storage_system_ip="{{ storage_system_ip }}"
    storage_system_username="{{ storage_system_username }}"
    storage_system_password="{{ storage_system_password }}"
    state=absent
    volumeset_name="{{ volumeset_name }}"
```

### Author

-   Farhan Nomani (<nomani@hpe.com>)

source

:   hpe3par\_remote\_copy.py

hpe3par\_remote\_copy - Manage HPE 3PAR and PRIMERA Remote Copy
===============================================================

Synopsis
--------

-   On HPE 3PAR and PRIMERA - Create Remote Copy Group - Modify Remote
    Copy Group - Add Volumes to Remote Copy Group - Remove Volumes from
    Remote Copy Group -Synchronize Remote Copy Group - Delete Remote
    Copy Group - Admit Remote Copy Link - Dismiss Remote Copy Link -
    Start Remote Copy Group - Stop Remote Copy Group - Admit Remote Copy
    Target - Dismiss Remote Copy Target - Start Remote Copy Service -
    Remote Copy Status

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <b>admit_volume_targets</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specify at least one pair of target_name and sec_volume_name.
 Attributes are target_name, sec_volume_name.
 Used with state[s] - add_volume</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>different_secondary_wwn</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Setting differentSecondaryWWN to true, 
 ensures that the system uses a different WWN on the secondary volume. Defaults to false. Use with volumeAutoCreation only.
 Used with state[s] - add_volume</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>domain</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the domain in which to create the Remote Copy group.
 Used with state[s] - present</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>full_sync</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Enables (true) or disables (false) forcing a full synchronization of the Remote Copy group, even if the volumes are already synchronized. Applies only to volume groups in synchronous mode, and can be used to resynchronize volumes that have become inconsistent.
 Used with state[s] - synchronize</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>keep_snap</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Enables (true) or disables (false) retention 
 of the local volume resynchronization snapshot.
 Used with state[s] - absent, remove_volume</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>local_remote_volume_pair_list</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Is a list of dictionaries, where each dictionary contains source and target volumes pairs i.e. [{&#x27;sourceVolumeName&#x27;:&#x27;secondary_vv1&#x27;, &#x27;targetVolumeName&#x27;:&#x27;secondary_vv2&#x27;}, ..].
 Used with state[s] - admit_target</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>local_snap_cpg</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the local snap CPG used for auto-created volumes.
 Used with state[s] - present, modify</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>local_user_cpg</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the local user CPG used for auto-created volumes.
 Used with state[s] - present, modify</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>modify_targets</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the attributes of the target of the Remote Copy group.
 Attributes are target_name, remote_user_cpg, remote_snap_cpg,
 sync_period, rm_sync_period, target_mode, snap_frequency, rm_snap_frequency, policies.
 Used with state[s] - modify</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>no_resync_snapshot</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Enables (true) or disables (false) saving the resynchronization snapshot. Applicable only to Remote Copy groups in asychronous periodic mode.
 Used with state[s] - synchronize</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>no_snapshot</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>If true, this option turns off creation of snapshots in synchronous and periodic modes, and deletes the current synchronization snapshots.
 Used with state[s] - stop</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>remote_copy_group_name</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the name of the Remote Copy group to create.
 Used with state[s] - present, absent, modify, add_volume,
 remove_volume, start, stop, synchronize, admit_target,
 dismiss_target, remote_copy_status</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>remote_copy_targets</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the attributes of the target of the Remote Copy group.
 Attributes are target_name, target_mode, user_cpg, snap_cpg.
 Used with state[s] - present</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>remove_secondary_volume</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Enables (true) or disables (false) deletion of the remote volume on the secondary array from the system. Defaults to false. Do not use with keepSnap.
 Used with state[s] - remove_volume</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>skip_initial_sync</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>If skipInitialSync is set to true, the volume should skip the initial sync. 
 This is for the admission of volumes that have been presynced with the target volume. 
 This cannot be set to true if the snapshot name is specified.
 Used with state[s] - add_volume, start</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>snapshot_name</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>The optional read-only snapshotName is a starting snapshot when 
 the group is started without performing a full resynchronization. 
 Instead, for synchronized groups, the volume synchronizes deltas 
 between this snapshotName and the base volume. For periodic groups, 
 the volume synchronizes deltas between this snapshotName and a snapshot of the base.
 Used with state[s] - add_volume</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>source_port</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>node:slot:port Specifies the node, slot, and port of the Ethernet port on the local system Ethernet port on the local system.
 Used with state[s] - admit_link, dismiss_link</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>starting_snapshots</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>When used, you must specify all the volumes inthe group. While specifying the pair, the starting snapshot is optional. When not used, the system performs a full resynchronization of the volume.
 Used with state[s] - start</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>state</b>
                                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                            <td>
                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                            <li>present</li>
                                                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>modify</li>
                                                                                                                                                                                            <li>add_volume</li>
                                                                                                                                                                                            <li>remove_volume</li>
                                                                                                                                                                                            <li>start</li>
                                                                                                                                                                                            <li>stop</li>
                                                                                                                                                                                            <li>synchronize</li>
                                                                                                                                                                                            <li>admit_link</li>
                                                                                                                                                                                            <li>dismiss_link</li>
                                                                                                                                                                                            <li>admit_target</li>
                                                                                                                                                                                            <li>dismiss_target</li>
                                                                                                                                                                                            <li>start_rcopy</li>
                                                                                                                                                                                            <li>remote_copy_status</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Whether the specified Remote Copy Group should exist or not. State also provides actions to modify Remote copy Group ,add/remove volumes, start/stop/synchronize remote copy group, Add/remove remote copy link, start remote copy services, admit/dismiss target.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>storage_system_ip</b>
                                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>The storage system IP address.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>storage_system_password</b>
                                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>The storage system password.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>storage_system_username</b>
                                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>The storage system user name.</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>target_mode</b>
                                                                        </td>
                            <td>
                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                            <li>sync</li>
                                                                                                                                                                                            <li>periodic</li>
                                                                                                                                                                                            <li>async</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the mode of the target as either synchronous (sync), asynchronous periodic (periodic), or asynchronous streaming (async).
 Used with state[s] - admit_target</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>target_name</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the target name associated with the Remote Copy group to be created.
 Used with state[s] - start, stop, synchronize, admit_link, dismiss_link, admit_target, dismiss_target</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>target_port_wwn_or_ip</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>IP/WWN address of the peer port on the target system.
 Used with state[s] - admit_link, dismiss_link</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>unset_snap_cpg</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Enables (true) or disables (false) setting the 
 localSnapCPG and remoteSnapCPG of the Remote Copy group.
 Used with state[s] - modify</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>unset_user_cpg</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>Enables (true) or disables (false) setting the localUserCPG and 
 remoteUserCPG of the Remote Copy group.
 Used with state[s] - modify</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>volume_auto_creation</b>
                <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                            <td>
                                                                                                                                                                                                                <ul><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                                                    <div>If volumeAutoCreation is set to true, 
 the secondary volumes should be created automatically 
 on the target using the CPG. associated with the Remote Copy group on that target. This cannot be set to true if the snapshot name is specified.
 Used with state[s] - add_volume</div>
                                                                            </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <b>volume_name</b>
                                                                        </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                                                    <div>Specifies the name of the existing virtual volume to be admitted to an existing Remote Copy group.
 Used with state[s] - add_volume, remove_volume</div>
                                                                            </td>
        </tr>
                    </table>
<br/>
Examples
--------

``` {.sourceCode .yaml+jinja}
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
```

### Author

-   Arshad Ansari(<arshad.alam.ansari@hpe.com>)

