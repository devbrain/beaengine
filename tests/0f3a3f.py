#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Pblic License as pblished by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Pblic License for more details.
#
#    You should have received a copy of the GNU General Pblic License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *


class TestSuite:

    def test(self):


        # EVEX.128.66.0F3A.W0 3f /r ib
        # VPCMPb k1 {k2}, xmm2, xmm3/m128/m32bcst, imm8

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3f2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqb ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqb k4, xmm0, xmmword ptr [rax], 10h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3f2011'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpltb ')
        assert_equal(myDisasm.instr.repr, 'vpcmpltb k4, xmm0, xmmword ptr [rax], 11h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3f2012'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpleb ')
        assert_equal(myDisasm.instr.repr, 'vpcmpleb k4, xmm0, xmmword ptr [rax], 12h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3f2013'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpfalseb ')
        assert_equal(myDisasm.instr.repr, 'vpcmpfalseb k4, xmm0, xmmword ptr [rax], 13h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3f2014'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpneqb ')
        assert_equal(myDisasm.instr.repr, 'vpcmpneqb k4, xmm0, xmmword ptr [rax], 14h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3f2015'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpnltb ')
        assert_equal(myDisasm.instr.repr, 'vpcmpnltb k4, xmm0, xmmword ptr [rax], 15h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3f2016'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpnleb ')
        assert_equal(myDisasm.instr.repr, 'vpcmpnleb k4, xmm0, xmmword ptr [rax], 16h')

        myEVEX = EVEX('EVEX.128.66.0F3A.W0')
        Buffer = '{}3f2017'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmptrueb ')
        assert_equal(myDisasm.instr.repr, 'vpcmptrueb k4, xmm0, xmmword ptr [rax], 17h')

        # EVEX.256.66.0F3A.W0 3f /r ib
        # VPCMPb k1 {k2}, ymm2, ymm3/m256/m32bcst, imm8

        myEVEX = EVEX('EVEX.256.66.0F3A.W0')
        Buffer = '{}3f2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqb ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqb k4, ymm0, ymmword ptr [rax], 10h')

        # EVEX.512.66.0F3A.W0 3f /r ib
        # VPCMPb k1 {k2}, zmm2, zmm3/m512/m32bcst, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W0')
        Buffer = '{}3f2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqb ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqb k4, zmm0, zmmword ptr [rax], 10h')



        # EVEX.128.66.0F3A.W1 3f /r ib
        # VPCMPw k1 {k2}, xmm2, xmm3/m128/m64bcst, imm8

        myEVEX = EVEX('EVEX.128.66.0F3A.W1')
        Buffer = '{}3f2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqw ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqw k4, xmm0, xmmword ptr [rax], 10h')

        # EVEX.256.66.0F3A.W1 3f /r ib
        # VPCMPw k1 {k2}, ymm2, ymm3/m256/m64bcst, imm8

        myEVEX = EVEX('EVEX.256.66.0F3A.W1')
        Buffer = '{}3f2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqw ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqw k4, ymm0, ymmword ptr [rax], 10h')

        # EVEX.512.66.0F3A.W1 3f /r ib
        # VPCMPw k1 {k2}, zmm2, zmm3/m512/m64bcst, imm8

        myEVEX = EVEX('EVEX.512.66.0F3A.W1')
        Buffer = '{}3f2010'.format(myEVEX.prefix()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(myDisasm.instr.Instruction.Opcode, 0x3f)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'vpcmpeqw ')
        assert_equal(myDisasm.instr.repr, 'vpcmpeqw k4, zmm0, zmmword ptr [rax], 10h')
