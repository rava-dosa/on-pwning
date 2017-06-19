#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import struct
import sys

import z3


def LODWORD(n):
    return n & 0xffffffff


solver = z3.Solver()

table = [
    0x926d, 0x5475, 0x0752, 0xb4c1, 0xc5c9, 0xa89e, 0x7372, 0x4004, 0xe15d, 0x3922, 0x5262, 0x99ae, 0xd5e5, 0xc6f8,
    0x12c9, 0x1783, 0x9832, 0x39ca, 0x5847, 0x0345, 0x8f77, 0xc5a0, 0x2e35, 0x4e4e, 0x2428, 0xcfec, 0x974a, 0xcecf,
    0x41f2, 0x691b, 0xad9e, 0x48a9, 0xfec5, 0xb9b7, 0x4526, 0x8476, 0xa69e, 0x14fb, 0x2ccd, 0xe193, 0x5d51, 0x65a0,
    0x6252, 0xd42d, 0x7e51, 0x2999, 0x87f5, 0x23d3, 0x5947, 0x21ad, 0x027a, 0x2e58, 0x36b5, 0x3fc3, 0xabbc, 0x876e,
    0xd669, 0x17fd, 0x8a63, 0xf219, 0x6de6, 0xa8b2, 0xe91c, 0x3cda, 0xc3a2, 0x9f38, 0x55fe, 0x3528, 0x1352, 0x687e,
    0x7bdc, 0x9ab3, 0x3522, 0xe6af, 0x7fe2, 0x729d, 0x2841, 0x3d22, 0xb98b, 0xe200, 0x34a5, 0x27eb, 0x13a8, 0x522f,
    0x73a7, 0xd7c9, 0x17b1, 0x3eaf, 0x11ca, 0x08d6, 0x49d7, 0xff8b, 0x4317, 0x24c2, 0x57f2, 0xcc99, 0x2413, 0xd03d,
    0xbb25, 0xe6e7, 0xa149, 0x5f66, 0xa0da, 0x5b97, 0x070d, 0x1027, 0x4204, 0x8265, 0xb6af, 0xe4b7, 0x8546, 0xaf78,
    0x2e9d, 0x5032, 0x3d53, 0x8ef5, 0x4737, 0xa7bd, 0xee80, 0xb071, 0xa144, 0x06ba, 0x6737, 0xb7cc, 0xa57b, 0x3ab9,
    0x4a1f, 0x2a24, 0x8227, 0xf8c0, 0x90dd, 0xc986, 0x4586, 0x278f, 0xcca4, 0x31ca, 0x312b, 0xe5a2, 0x204d, 0x5855,
    0x7821, 0x5175, 0x7dd8, 0x8f2a, 0xb9ce, 0x8202, 0xe72c, 0xfeac, 0x240c, 0xe8cf, 0xf5a8, 0xbe4f, 0xb8f4, 0x92d8,
    0xe10c, 0x9e3e, 0xca17, 0x8c27, 0xf992, 0x1006, 0xe877, 0x538a, 0x5121, 0x6795, 0x6df9, 0x62a4, 0xab0d, 0x6421,
    0x1c92
]

func = [
    lambda inp: LODWORD(LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0x280)/4])) + LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(table[(0x2b0-0x2B0)/4]) * LODWORD(inp[0])) - LODWORD(LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0x2AC)/4]))) - LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0x2A8)/4]))) - LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0x2A4)/4]))) + LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0x2A0)/4]))) + LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0x29C)/4]))) + LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0x298)/4]))) + LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0x294)/4]))) + LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0x290)/4]))) + LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0x28C)/4]))) + LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0x288)/4]))) + LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0x284)/4])))),
    lambda inp: LODWORD(LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0x24C)/4])) + LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(table[(0x2b0-0x27C)/4]) * LODWORD(inp[0]) + LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0x278)/4])) - LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0x274)/4]))) + LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0x270)/4]))) + LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0x26C)/4]))) + LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0x268)/4]))) - LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0x264)/4]))) - LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0x260)/4]))) - LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0x25C)/4]))) - LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0x258)/4]))) - LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0x254)/4]))) - LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0x250)/4])))),
    lambda inp: LODWORD(LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0x218)/4])) + LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(-LODWORD(table[(0x2b0-0x248)/4])) * LODWORD(inp[0]) + LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0x244)/4])) - LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0x240)/4]))) + LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0x23C)/4]))) - LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0x238)/4]))) - LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0x234)/4]))) - LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0x230)/4]))) - LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0x22C)/4]))) + LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0x228)/4]))) - LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0x224)/4]))) + LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0x220)/4]))) + LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0x21C)/4])))),
    lambda inp: LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(table[(0x2b0-0x214)/4]) * LODWORD(inp[0])) - LODWORD(LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0x210)/4]))) - LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0x20C)/4]))) - LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0x208)/4]))) + LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0x204)/4]))) - LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0x200)/4]))) + LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0x1FC)/4]))) + LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0x1F8)/4]))) - LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0x1F4)/4]))) - LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0x1F0)/4]))) + LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0x1EC)/4]))) - LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0x1E8)/4]))) - LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0x1E4)/4]))),
    lambda inp: LODWORD(LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0x1B0)/4])) + LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(-LODWORD(table[(0x2b0-0x1E0)/4])) * LODWORD(inp[0]) + LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0x1DC)/4])) + LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0x1D8)/4]))) + LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0x1D4)/4]))) + LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0x1D0)/4]))) - LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0x1CC)/4]))) - LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0x1C8)/4]))) - LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0x1C4)/4]))) + LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0x1C0)/4]))) + LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0x1BC)/4]))) - LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0x1B8)/4]))) + LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0x1B4)/4])))),
    lambda inp: LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(-LODWORD(table[(0x2b0-0x1AC)/4])) * LODWORD(inp[0])) - LODWORD(LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0x1A8)/4]))) + LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0x1A4)/4]))) - LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0x1A0)/4]))) - LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0x19C)/4]))) - LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0x198)/4]))) + LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0x194)/4]))) + LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0x190)/4]))) - LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0x18C)/4]))) - LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0x188)/4]))) + LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0x184)/4]))) + LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0x180)/4]))) - LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0x17C)/4]))),
    lambda inp: LODWORD(LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0x148)/4])) + LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(-LODWORD(table[(0x2b0-0x178)/4])) * LODWORD(inp[0]) + LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0x174)/4])) + LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0x170)/4]))) - LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0x16C)/4]))) - LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0x168)/4]))) - LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0x164)/4]))) - LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0x160)/4]))) + LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0x15C)/4]))) - LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0x158)/4]))) + LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0x154)/4]))) - LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0x150)/4]))) - LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0x14C)/4])))),
    lambda inp: LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(-LODWORD(table[(0x2b0-0x144)/4])) * LODWORD(inp[0]) + LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0x140)/4])) - LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0x13C)/4]))) - LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0x138)/4]))) - LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0x134)/4]))) - LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0x130)/4]))) + LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0x12C)/4]))) + LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0x128)/4]))) - LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0x124)/4]))) - LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0x120)/4]))) - LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0x11C)/4]))) + LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0x118)/4]))) - LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0x114)/4]))),
    lambda inp: LODWORD(LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0xE0)/4])) + LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(table[(0x2b0-0x110)/4]) * LODWORD(inp[0]) + LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0x10C)/4])) - LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0x108)/4]))) + LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0x104)/4]))) + LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0x100)/4]))) + LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0xFC)/4]))) - LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0xF8)/4]))) - LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0xF4)/4]))) - LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0xF0)/4]))) - LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0xEC)/4]))) + LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0xE8)/4]))) - LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0xE4)/4])))),
    lambda inp: LODWORD(LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0xAC)/4])) + LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(-LODWORD(table[(0x2b0-0xDC)/4])) * LODWORD(inp[0]) + LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0xD8)/4])) - LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0xD4)/4]))) + LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0xD0)/4]))) - LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0xCC)/4]))) - LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0xC8)/4]))) + LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0xC4)/4]))) + LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0xC0)/4]))) + LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0xBC)/4]))) + LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0xB8)/4]))) + LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0xB4)/4]))) - LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0xB0)/4])))),
    lambda inp: LODWORD(LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0x78)/4])) + LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(-LODWORD(table[(0x2b0-0xA8)/4])) * LODWORD(inp[0])) - LODWORD(LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0xA4)/4]))) - LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0xA0)/4]))) - LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0x9C)/4]))) - LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0x98)/4]))) + LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0x94)/4]))) + LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0x90)/4]))) + LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0x8C)/4]))) - LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0x88)/4]))) + LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0x84)/4]))) + LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0x80)/4]))) - LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0x7C)/4])))),
    lambda inp: LODWORD(LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0x44)/4])) + LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(table[(0x2b0-0x74)/4]) * LODWORD(inp[0]) + LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0x70)/4])) - LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0x6C)/4]))) - LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0x68)/4]))) + LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0x64)/4]))) + LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0x60)/4]))) - LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0x5C)/4]))) - LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0x58)/4]))) + LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0x54)/4]))) + LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0x50)/4]))) - LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0x4C)/4]))) + LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0x48)/4])))),

    lambda inp: LODWORD(LODWORD(LODWORD((inp[0x30/4])) * LODWORD(table[(0x2b0-0x10)/4])) + LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(LODWORD(table[(0x2b0-0x40)/4]) * LODWORD(inp[0]) + LODWORD((inp[0x4/4])) * LODWORD(table[(0x2b0-0x3C)/4])) - LODWORD(LODWORD((inp[0x8/4])) * LODWORD(table[(0x2b0-0x38)/4]))) + LODWORD(LODWORD((inp[0xc/4])) * LODWORD(table[(0x2b0-0x34)/4]))) + LODWORD(LODWORD((inp[0x10/4])) * LODWORD(table[(0x2b0-0x30)/4]))) - LODWORD(LODWORD((inp[0x14/4])) * LODWORD(table[(0x2b0-0x2C)/4]))) - LODWORD(LODWORD((inp[0x18/4])) * LODWORD(table[(0x2b0-0x28)/4]))) + LODWORD(LODWORD((inp[0x1c/4])) * LODWORD(table[(0x2b0-0x24)/4]))) + LODWORD(LODWORD((inp[0x20/4])) * LODWORD(table[(0x2b0-0x20)/4]))) + LODWORD(LODWORD((inp[0x24/4])) * LODWORD(table[(0x2b0-0x1C)/4]))) - LODWORD(LODWORD((inp[0x28/4])) * LODWORD(table[(0x2b0-0x18)/4]))) + LODWORD(LODWORD((inp[0x2c/4])) * LODWORD(table[(0x2b0-0x14)/4])))),
]
constraints = [
    0x1468753,
    0x162f30,
    0xffb2939c,
    0xffac90e3,
    0x76d288,
    0xff78bf99,
    0xfff496e3,
    0xff525e90,
    0xfffd7704,
    0x897cbb,
    0xffc05f9f,
    0x3e4761,
    0x1b4945,
]

input_array = [z3.BitVec('i%d' % i, 32) for i in range(len(constraints))]
for f, c in zip(func, constraints):
    solver.add(f(input_array) == c)

assert solver.check() == z3.sat
model = solver.model()
print ''.join(chr(model[v].as_long()) for v in input_array)
# Math is hard!