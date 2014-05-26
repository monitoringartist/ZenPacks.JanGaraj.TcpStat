################################################################################
# 
# This program is part of the TcpStat Zenpack for Zenoss.
# Copyright (C) 2014 Jan Garaj - www.jangaraj.com
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.gnu.org/licenses/
#
################################################################################


from Products.ZenRRD.CommandParser import CommandParser

class ss(CommandParser):

    def processResults(self, cmd, result):
        """
        Process the results of "ss --tcp --all --numeric" or "ss -tan".
        """
        exitCode = getattr(cmd.result, 'exitCode', 0)
        if exitCode != 0:
            evt = dict(
                       device = cmd.deviceConfig.device,
                       summary = 'Problem with command on device',
                       message = 'Command: %s, output: %s' % (cmd.command, cmd.result.stderr),
                       severity = cmd.severity,
                       eventKey = cmd.eventKey,
                       eventClass = cmd.eventClass,
                       component = cmd.component)
            result.events.append(evt)
            return result

        connectionsIpv4 = [l.split()[0] for l in cmd.result.output.split('\n') if not l.startswith('State') and ':' in l and l.count(':')<3]
        connectionsIpv6 = [l.split()[0] for l in cmd.result.output.split('\n') if not l.startswith('State') and ':' in l and l.count(':')>2]
        for dp in cmd.points:
            if '_ipv4' in dp.id:
                result.values.append((dp, connectionsIpv4.count(dp.id.replace('_ipv4', ''))))
            else:
                result.values.append((dp, connectionsIpv6.count(dp.id.replace('_ipv6', ''))))
        evt = dict(
                   device = cmd.deviceConfig.device,
                   summary = 'Problem with command on device',
                   message = 'Clearing problem',
                   severity = 0,
                   eventKey = cmd.eventKey,
                   eventClass = cmd.eventClass,
                   component = cmd.component)
        result.events.append(evt)

        return result
