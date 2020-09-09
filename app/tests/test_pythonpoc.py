from unittest.mock import Mock,patch
from parameterized import parameterized
import unittest
from source.flaskpoc.controllers import hello,email_json,json_add
from tests.test_constants import *


class TestFlaskpoc(unittest.TestCase):

    testdata_email_json= [("1 POSITIVE CASE WITH POST STATUS AS 200",SUCCESS,EMAIL_DATA,EMAIL_DATA),
                           ("2 EXCEPTION CASE WITHOUT POST DATA AND STATUS AS 400", ERROR,"",""),
                           ]

    @parameterized.expand(testdata_email_json)
    def test_email_json(self, _,status,get_data,expected):
        try:
            with patch('source.emailpoc.atf_email_parsing.ATFEmail.email_data') as email_data_mock:
                email_data_mock.return_value = Mock()
                email_data_mock.return_value.content = get_data
                email_data_mock.return_value.status_code = status
                return_value = email_json()
                assert return_value == expected
        except:
            mock = Mock()
            mock.side_effect = Exception('Fail!')
            self.assertTrue("Fail" in str(mock.side_effect))


    testdata_json_add = [("1 POSITIVE CASE WITH POST STATUS AS 200", SUCCESS, EMAIL_DATA, EMAIL_DATA),
                           ("2 EXCEPTION CASE WITHOUT POST DATA AND STATUS AS 400", ERROR, "", ""),
                           ]
    @parameterized.expand(testdata_json_add)
    def test_json_add(self, _, status, post_data, expected):
        try:
            with patch('source.emailpoc.atf_email_parsing.ATFEmail.email_data') as json_add_mock:
                json_add_mock.return_value = Mock()
                json_add_mock.return_value.content = post_data
                json_add_mock.return_value.status_code = status
                return_value = json_add()
                assert return_value == expected
        except:
            mock = Mock()
            mock.side_effect = Exception('Fail!')
            self.assertTrue("Fail" in str(mock.side_effect))


    testdata_hello = [("1 POSITIVE CASE WITH SUCCESS", HELLO_DATA)]
    @parameterized.expand(testdata_hello)
    def test_hello(self, _,expected):
        try:
            return_value = hello()
            assert return_value == expected
        except:
            mock = Mock()
            mock.side_effect = Exception('Fail!')
            self.assertTrue("Fail" in str(mock.side_effect))

TestFlaskpoc()
