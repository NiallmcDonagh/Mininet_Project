import sys
import os
from mininet.topo import Topo
from mininet.net import Mininet
#from mininet.util import irange, dumpNodeConnections, dumpPorts, dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSKernelSwitch, RemoteController

class nialltopo(Topo):

	def __init__(self, **opts):
	
		super(nialltopo, self). __init__(**opts)
		
	host0 = self.addHost('h0')
        host1 = self.addHost('h1')
		
	switch0 = self.addSwitch('s0')
        switch1 = self.addSwitch('s1')
		
	self.addLink(host0, switch0) # s0.port_1: host0
        self.addLink(host1, switch1) # s1.port_2: host1
	self.addLink(switch0, switch1) # s0.port_2: s1.port_2:
		
topos = {'nialltopo': (lambda: nialltopo()) }

def start_network():
	topo = nialltopo()
	net = mininet(autoSetMacs=True)
	net.topo = topo
	net.start()
	CLI(net)
	net.stop()
	os.system('sudo mn -c')

if __name__ == '__main__':
    setLogLevel('info')
    #if len(sys.argv) > 1:
     #   controller_ip = str(sys.argv[1])
    #else:
     #   controller_ip = None
    start_network() 
	
