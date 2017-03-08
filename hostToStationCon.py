
#Wired host talking to wireless access points 

import sys 
import os
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.link import TCLink 
from mininet.cli import CLI
from mininet.log import setLogLevel 

class wifitopo(Topo):

	def __init__(self, **opts):
	

		super(wifitopo, self). __init__(**opts)
		#build network 
	
		net = Mininet(controller=Controller, link=TCLink, switch=OVSKernelSwitch)

		#create network nodes

		h1 = net.addHost('h1', mac='00:00:00:00:00:01', ip='10.0.0.1/8')
		h2 = net.addHost('h2', mac='00:00:00:00:00:02', ip='10.0.0.2/8')
		s1 = net.addSwitch('s1', mac='00:00:00:00:00:03', ip='10.0.0.3/8')
		s2 = net.addSwitch('s2', mac='00:00:00:00:00:04', ip='10.0.0.4/8')
		ap1 = net.addAccessPoint('ap1',ssid= 'new-ssid1', mode = '9', channel='1',position='30,30,0')
		sta1 = net.addStation('sta1', wlans=2, mac='00:00:00:00:00:05', ip='10.0.0.5/8')
		sta2 = net.addStation('sta2', mac='00:00:00:00:00:04', ip='10.0.0.6/8')
		c1 = net.addController('c1', controller=Controller )
		

		#add links 

		net.addLink(h1,s1)
		net.addLink(h2,s2)
		net.addLink(s1,s2)
		net.addLink(s2,ap1)
		net.addLink(c1,s1)
		net.addLink(c1,s2)
		net.addLink(ap1,sta1)
		net.addLink(ap1,sta2)
		
topos = {'wifitopo': (lambda: wifitopo())}
	
def start_network():
	
	#start network
 
	topo = wifitopo()
	net.topo = topo
	net.build()
	c1.start()
	ap1.start([c1])
	net.speed(10)
	CLI(net)
	net.stop()
	os.system('sudo mn -c')


if __name__ == '__main__':
	setLogLevel('info')
	start_network()


