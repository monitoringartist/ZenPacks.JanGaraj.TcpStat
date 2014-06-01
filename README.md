=========================
ZenPacks.JanGaraj.TcpStat
=========================

About
=====

This SSH-based ZenPack provides TCP state overview for IPv4 and IPv6.

Requirements
============

Zenoss
------

You must first have, or install, Zenoss 4. This ZenPack was tested
against Zenoss 4.2. You can download the free Core
version of Zenoss from http://community.zenoss.org/community/download.


Monitored Systems
-----------------

On monitored system, ss comand must be installed and SSH daemon 
properly configured.


Installation
============

Normal Installation (packaged egg)
----------------------------------

Download the `TCP Stat <http://community.zenoss.org/docs/DOC-XXXX>`_.
Copy this file to your Zenoss server and run the following commands as the zenoss
user.

        zenpack --install ZenPacks.JanGaraj.TcpStat-0.0.2.egg
        zenoss restart

Developer Installation (link mode)
----------------------------------

If you wish to further develop and possibly contribute back to the TcpStat
ZenPack you should clone the git `repository <https://github.com/jangaraj/ZenPacks.JanGaraj.TcpStat>`,
then install the ZenPack in developer mode using the following commands.

        git clone git://github.com/jangaraj/ZenPacks.JanGaraj.TcpStat.git
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

