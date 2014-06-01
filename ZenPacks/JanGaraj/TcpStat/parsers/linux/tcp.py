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

class tcp(CommandParser):

    def processResults(self, cmd, result):
        """
        Process the results of "/bin/cat /proc/net/tcp<6>".
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

        # mapping from linux source code tcp.h - used ss terminology for TCP states (not netstat)
        mapping = {
            'ESTAB'     : '01',
            'SYN-SENT'  : '02',
            'SYN-RECV'  : '03',
            'FIN-WAIT-1': '04',
            'FIN-WAIT-2': '05',
            'TIME-WAIT' : '06',
            'UNCONN'    : '07',
            'CLOSE-WAIT': '08',
            'LAST-ACK'  : '09',
            'LISTEN'    : '0A',
            'CLOSING'   : '0B',
            'UNKNOWN'   : '0C'
        } 
        connections = [l.split()[3] for l in cmd.result.output.split('\n') if not l.startswith('  sl') and l.strip()]
        for dp in cmd.points:
            result.values.append((dp, connections.count(mapping[dp.id])))
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
