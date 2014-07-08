from __future__ import print_function

import os
import traceback

from ptp import PTP
from libptp.tools.metasploit.report import MetasploitReport
from libptp.constants import UNKNOWN, INFO, LOW, MEDIUM


__testname__ = 'metasploit'


REPORTS = {
    # Scanner
    'auxiliary/scanner/ftp/anonymous': {
        'report_low.metasploit': LOW,
        'report_medium.metasploit': MEDIUM,
    },
    'auxiliary/scanner/ftp/ftp_version': {
        'report_info.metasploit': INFO,
        'report_info2.metasploit': INFO,
    },
    'auxiliary/scanner/ftp/ftp_login': {
        'report_low.metasploit': LOW,
        'report_medium.metasploit': MEDIUM,
    },
    'auxiliary/scanner/smtp/smtp_enum': {
        'report_low.metasploit': LOW,
        'report_low2.metasploit': LOW,
    },
    'auxiliary/scanner/vnc/vnc_login': {
        'report_medium.metasploit': MEDIUM,
        'report_medium2.metasploit': MEDIUM,
    },
    'auxiliary/scanner/vnc/vnc_none_auth': {
        'report_medium.metasploit': MEDIUM,
    },
    'auxiliary/scanner/x11/open_x11': {
        'report_medium.metasploit': MEDIUM,
        'report_medium2.metasploit': MEDIUM,
    },
    # TODO: Add report examples for EMC AlphaStor.
    'auxiliary/scanner/mssql/mssql_ping': {
        'report_info.metasploit': INFO,
        'report_info2.metasploit': INFO,
        'report_info3.metasploit': INFO,
    },
    'auxiliary/scanner/mssql/mssql_login': {
        'report_medium.metasploit': MEDIUM,
        'report_medium2.metasploit': MEDIUM,
    },
    'auxiliary/scanner/mssql/mssql_hashdump': {
        'report_medium.metasploit': MEDIUM,
    },
    # TODO: Add report examples for MSSQL Schema dump.
    # TODO: Add report examples for DCERPC endpoint mapper.
    # TODO: Add report examples for DCERPC hidden.
    'auxiliary/scanner/smb/smb_version': {
        'report_info.metasploit': INFO,
        'report_info2.metasploit': INFO,
        'report_info3.metasploit': INFO,
    },
    'auxiliary/scanner/smb/pipe_auditor': {
        'report_info.metasploit': INFO,
        'report_info2.metasploit': INFO,
    },
    'auxiliary/scanner/smb/smb_enumusers': {
        'report_info.metasploit': INFO,
        'report_info2.metasploit': INFO,
        'report_info3.metasploit': INFO,
    },
    'auxiliary/scanner/smb/smb_login': {
        'report_medium.metasploit': MEDIUM,
        'report_medium2.metasploit': MEDIUM,
        'report_unknown.metasploit': UNKNOWN,
    },
    'auxiliary/scanner/snmp/snmp_enumusers': {
        'report_info.metasploit': INFO,
    },
    'auxiliary/scanner/snmp/snmp_enumshares': {
        'report_info.metasploit': INFO,
    },
    # TODO: Add report examples for SNMP enums.
    # TODO: Add report examples for SNMP AIX version.
    'auxiliary/scanner/snmp/snmp_login': {
        'report_info.metasploit': INFO,
        'report_medium.metasploit': MEDIUM,
        'report_medium2.metasploit': MEDIUM,
    }
}


def run():
    try:
        reports = REPORTS.iteritems()
    except AttributeError:  # Python3
        reports = REPORTS.items()

    for plugin, outputs in reports:
        print('\t> %s' % plugin)
        for output in outputs:
            ptp = PTP('metasploit')
            print('\t\ttest parse():', end=' ')
            res = 'ok'
            try:
                ptp.parse(
                    pathname=os.path.join(
                        os.getcwd(),
                        'tests/metasploit/',
                        plugin),
                    filename=output,
                    plugin=plugin)
            except Exception:
                print(traceback.format_exc())
                res = 'ko'
            print(res)

            print('\t\ttest get_highest_ranking():', end=' ')
            res = 'ok'
            try:
                assert ptp.get_highest_ranking() == outputs[output]
            except Exception:
                print(traceback.format_exc())
                res = 'ko'
            print(res)
