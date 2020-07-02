# coding: utf-8

"""
    Connected Product API

    This API bundle allows to collect usage data from different \"connected products\". A connected product is an IoT consumer product connected to the IoT platform through a digital interface. Possible connected products are: <ul> <li>natively connected products (e.g. smart kitchen appliances, smart coffee machines, smart fridge, etc.);</li> <li>regular products connected through a gateway and equipped with additional sensors (e.g. bags or luggages with NFC or Bluetooth tags, etc.)</li> </ul> <p>To register for the first time a new product, the <code>init</code> method must be invoked.</p> <p>After registration, every product usage event (e.g. state change, sensors value change, user interaction with the product, etc.) is sent to the platform using the <code>event</code> method. </p>  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from models.location import Location  # noqa: E501
from swagger_client.rest import ApiException


class TestLocation(unittest.TestCase):
    """Location unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLocation(self):
        """Test Location"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.location.Location()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
