#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 Igor Volodin.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
import serial
from gnuradio import gr

class srig_py(gr.basic_block):
    """
    docstring for block srig_py
    """
    def __init__(self, serialPort, pin0, pin1, pin2, pin3):
        gr.basic_block.__init__(self,
            name="srig_py",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
	self.states = {True:'1', False:'0'}
	self.port = serial.Serial(serialPort, baudrate=9600, timeout=3.0)
	if (self.port.isOpen()):
	    print "SRIG: Re-open serial port %s" % serialPort
	    self.port.close()
	    self.port.open()
	else:
	    print "SRIG: Open serial port %s" % serialPort
	    self.port.open()
	self.p0_cstate = pin0
	self.p1_cstate = pin1
	self.p2_cstate = pin2
	self.p3_cstate = pin3

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items
    def set_pin0(self, pin0):
	if self.p0_cstate != pin0:
	    self.p0_cstate = pin0
	    cmd = """S0P%s\n""" % self.states[pin0]
	    self.port.write(cmd)
	    print "SRIG: Pin 0 %s" % pin0
    def set_pin1(self, pin1):
	if self.p1_cstate != pin1:
	    self.p1_cstate = pin1
	    cmd = """S1P%s\n""" % self.states[pin1]
	    self.port.write(cmd)
	    print "SRIG: Pin 1 %s" % pin1
    def set_pin2(self, pin2):
	if self.p2_cstate != pin2:
	    self.p2_cstate = pin2
	    cmd = """S2P%s\n""" % self.states[pin2]
	    self.port.write(cmd)
	    print "SRIG: Pin 2 %s" % pin2
    def set_pin3(self, pin3):
	if self.p3_cstate != pin3:
	    self.p3_cstate = pin3
	    cmd = """S3P%s\n""" % self.states[pin3]
	    self.port.write(cmd)
	    print "SRIG: Pin 3 %s" % pin3

    def general_work(self, input_items, output_items):
        output_items[0][:] = input_items[0]
        consume(0, len(input_items[0]))
        #self.consume_each(len(input_items[0]))
        return len(output_items[0])
