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


def convert_to_binary_multiple(size, size_unit):
    size_mib = 0
    if size_unit == 'GiB':
        size_mib = size * 1024
    elif size_unit == 'TiB':
        size_mib = size * 1048576
    elif size_unit == 'MiB':
        size_mib = size
    return int(size_mib)

def get_volume_type(volume_type):
    enum_type = ''
    if volume_type == 'thin':
        enum_type = ['TPVV', 1]
    elif volume_type == 'thin_dedupe':
        enum_type = ['TDVV', 3]
    elif volume_type == 'full':
        enum_type = ['FPVV', 2]
    return enum_type

def convert_to_hours(time, unit):
    hours = 0
    if unit == 'Days':
        hours = time * 24
    elif unit == 'Hours':
        hours = time
    return hours
