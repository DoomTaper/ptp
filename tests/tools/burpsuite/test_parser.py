# -*- coding: UTF-8 -*-
import mock
import json
import unittest

from lxml import etree
from hamcrest import assert_that, has_entry, equal_to

from ptp.tools.burpsuite.parser import BurpXMLParser


def lxml_etree_parse(string):
    return etree.fromstring(string).getroottree()

class TestBurpXMLParser(unittest.TestCase):

    ###
    # BurpXMLParser.is_mine
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_burp_xml_is_mine(self, mock_lxml_etree_parse):
        from .burp_1_6_30_report import report_true
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_true]):
            BurpXMLParser.__format__ = ''
            self.assertTrue(BurpXMLParser.is_mine('foo', 'bar', first=True))
        

    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_burp_xml_is_not_mine(self, mock_lxml_etree_parse):
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=['foo.bar']):
            BurpXMLParser.__format__ = ''
            self.assertFalse(BurpXMLParser.is_mine('foo', 'bar', first=True))

    ###
    # BurpXMLParser.parse_metadata
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_burp_xml_parse_metadata(self, mock_lxml_etree_parse):
        from .burp_1_6_30_report import report_true
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_true]):
            BurpXMLParser.__format__ = ''
            my_burp = BurpXMLParser('foo', 'bar', first=True)
            assert_that(my_burp.parse_metadata(), has_entry('version', '1.6.30'))

    ###
    # BurpXMLParser.parse_report
    ###
    @mock.patch('lxml.etree.parse', side_effect=lxml_etree_parse)
    def test_parser_burp_xml_parse_report(self, mock_lxml_etree_parse):
        from .burp_1_6_30_report import report_true
        with mock.patch('ptp.libptp.parser.AbstractParser._recursive_find', return_value=[report_true]):
            BurpXMLParser.__format__ = ''
            my_burp = BurpXMLParser()
            report = my_burp.parse_report()
            assert_that(9, equal_to(len(report[-1]['transactions'])))