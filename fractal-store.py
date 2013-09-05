#!/opt/pypy/bin/pypy
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

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from Queue import Queue
import random

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("192.168.0.1", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register an instance; all the methods of the instance are
# published as XML-RPC methods.
class MyStore(object):
    def __init__(self):
        """initializes a Store"""
        self.store = Queue(maxsize=30)
        self.size = (24, 80)
        self.typesOfFractals = ['julia', 'mandelbrot', 'test']
    def put(self,item):
        """puts an item into the queue"""
        try:
            self.store.put_nowait(item)
        except:
            pass
        return True
    def get(self):
        """gets an item out of the store"""
        try:
            return self.store.get_nowait()
        except:
            return False
    def set_size(self, height, width):
        """sets a size for the console"""
        self.size = (int(height), int(width))
        return True
    def get_size(self):
        """Gets the console size"""
        return self.size
    def pick_type(self):
        """pick the type of fractal to generate"""
        return random.choice(self.typesOfFractals)

server.register_instance(MyStore())

# Run the server's main loop
server.serve_forever()
