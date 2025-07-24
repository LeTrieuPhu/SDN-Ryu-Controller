#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import OVSSwitch
from mininet.topo import Topo


class MyTopo(Topo):
    "Simple topology example."

    def emptyNet():
        net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)


        c1 = net.addController('c1', controller=RemoteController, ip="127.0.0.1", port=6633)

        h2 = net.addHost( 'h2', ip='10.0.10.2/24', mac='00:00:00:00:00:02' )
        h3 = net.addHost( 'h3', ip='10.0.10.3/24', mac='00:00:00:00:00:03' )
        h4 = net.addHost( 'h4', ip='10.0.20.4/24', mac='00:00:00:00:00:04' )
        h5 = net.addHost( 'h5', ip='10.0.20.5/24', mac='00:00:00:00:00:05' )





        s1 = net.addSwitch('s1',dpid='0000000000000001',cls=OVSSwitch, protocols='OpenFlow13')
        s2 = net.addSwitch('s2',dpid='0000000000000002',cls=OVSSwitch, protocols='OpenFlow13')
        r1 = net.addSwitch('r1',dpid='0000000000000021',cls=OVSSwitch, protocols='OpenFlow13')



        net.addLink(s1, h2)
        net.addLink(s1, h3)
        net.addLink(s2, h4)
        net.addLink(s2, h5)

        net.addLink(r1, s1)
        net.addLink(r1, s2)

        net.build()
        c1.start()
        s1.start([c1])
        s2.start([c1])
        r1.start([c1])


        h2.cmd("ip route add default via 10.0.10.1")
        h3.cmd("ip route add default via 10.0.10.1")
        h4.cmd("ip route add default via 10.0.20.1")
        h5.cmd("ip route add default via 10.0.20.1")

        net.start()
        CLI(net)
        net.stop()

    if __name__ == '__main__':
        setLogLevel('info')
    emptyNet()


topos = {'mytopo': (lambda: MyTopo())}
