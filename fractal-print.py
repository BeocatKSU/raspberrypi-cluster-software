#!/usr/bin/env python
# Copyright (c) 2013, Adam Tygart
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of Kansas State University nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL ADAM TYGART BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import os, time
from base64 import b64decode
import argparse

parser = argparse.ArgumentParser(description="Generates Fractals")
parser.add_argument('-d', '--destination', type=str, default='192.168.0.1', help='IP to send the fractals to')

args = parser.parse_args()

if sys.version_info[0] < 3:
    import xmlrpclib
    s = xmlrpclib.ServerProxy('http://' + args.destination + ':8000')
else:
    import xmlrpc.client
    s = xmlrpc.client.ServerProxy('http://' + args.destination + ':8000')

(height, width) = os.popen('stty size', 'r').read().split()
height = int(height)
width = int(width)
s.set_size(height,width)
while True:
    try:
        fractal = b64decode(s.get())
        fractal = fractal.rstrip('\n')
        print(fractal)
    except:
        pass
        #print("Didn't get a fractal")
    time.sleep(1.0)
