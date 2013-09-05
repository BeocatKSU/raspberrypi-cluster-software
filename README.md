raspberrypi-cluster-software
============================

This holds the software we have written for the raspberry pi cluster.

fractal-*
  For the fractal display, start the fractal-store.py, then fractal-generate.py and then fractal-print.py on the display.
  you may need to modify the ip address it connects to.

Checkout this repo into /boot/beocat
Install pypy into /opt/pypy
Set ip address in /boot/ipaddress.txt
Set eth0 to manual config
Add '''/boot/beocat/startup.py &''' before the exit 0 in /etc/rc.local
On the headnode after the boot login and run '''/boot/beocat/fractal-print.py'''
