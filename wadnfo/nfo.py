#!/usr/bin/python
# -*- coding: utf8 -*-

from DoomWAD import DoomWad

wad = DoomWad.from_file("exploit.wad")
print "TYPE \t ENTRIES \t OFFSET"
print wad.magic, " \t ", wad.num_index_entries, " \t " , hex(wad.index_offset)
