ZenPacks.JanGaraj.TcpStat
=========================

This SSH-based ZenPack provides TCP state statistic for IPv4 and IPv6.

Please donate to author, so he can continue to publish other awesome projects 
for free:

[![Paypal donate button](http://jangaraj.com/img/github-donate-button02.png)]
(https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=8LB6J222WRUZ4)

![TCP States IPv4](https://raw.github.com/monitoringartist/ZenPacks.JanGaraj.TcpStat/master/TCP_States_IPv4.png)
![TCP States IPv6](https://raw.github.com/monitoringartist/ZenPacks.JanGaraj.TcpStat/master/TCP_States_IPv6.png)

Requirements
============

Zenoss
------

You must first have, or install, Zenoss 4. This ZenPack was tested
against Zenoss 4.2.5. You can download the free Core
version of Zenoss from http://community.zenoss.org/community/download.

Monitored Systems
-----------------

On monitored system, /bin/cat command must be installed and SSH daemon 
properly configured. ZenPack fetchs statistic from /proc/net/tcp and /proc/net/tcp6, so /proc filesystem must be mounted.
Notes:
- netstat command is slow (especially if you have box with 40k connections)
- ss command is quick, but its location depends on Linux distribution
- the best approach is using directly /proc/net/tcp(6) in this case

Installation
============

Normal Installation (packaged egg)
----------------------------------

Download the egg file http://wiki.zenoss.org/download/zenpacks/ZenPacks.JanGaraj.TcpStat/1.0.0/ZenPacks.JanGaraj.TcpStat-1.0.0.egg .
Copy this file to your Zenoss server and run the following commands as the zenoss
user.

        zenpack --install ZenPacks.JanGaraj.TcpStat-1.0.0.egg
        zenoss restart

Developer Installation (link mode)
----------------------------------

If you wish to further develop and possibly contribute back to the TcpStat
ZenPack you should clone the git repository https://github.com/monitoringartist/ZenPacks.JanGaraj.TcpStat,
then install the ZenPack in developer mode using the following commands.

        git clone git://github.com/monitoringartist/ZenPacks.JanGaraj.TcpStat.git
        zenpack --link --install ZenPacks.JanGaraj.TcpStat
        zenoss restart

zProperties
===========

Please configure device SSH settings properly (zCommandUsername, zCommandPassword/zKeyPath)

Usage
=====

Go to the specific device (yes, it needs to already be added) and bind TcpStat/TcpStat6 templates.

Installing the ZenPack will add the following items to your Zenoss system:

Monitoring Templates
--------------------

- /Devices/Server/rrdTemplates/TcpStat
- /Devices/Server/rrdTemplates/TcpStat6

Event Classes
--------------------

- /Events/Status/TcpStat

Author
======

[Devops Monitoring zExpert](http://www.jangaraj.com), who loves monitoring 
systems, which start with letter Z. Those are Zabbix and Zenoss.

Professional monitoring services:

[![Monitoring Artist](http://monitoringartist.com/img/github-monitoring-artist-logo.jpg)]
(http://www.monitoringartist.com)
