# coding: utf-8

"""
    Connected Product API

    This API bundle allows to collect usage data from different \"connected products\". A connected product is an IoT consumer product connected to the IoT platform through a digital interface. Possible connected products are: <ul> <li>natively connected products (e.g. smart kitchen appliances, smart coffee machines, smart fridge, etc.);</li> <li>regular products connected through a gateway and equipped with additional sensors (e.g. bags or luggages with NFC or Bluetooth tags, etc.)</li> </ul> <p>To register for the first time a new product, the <code>init</code> method must be invoked.</p> <p>After registration, every product usage event (e.g. state change, sensors value change, user interaction with the product, etc.) is sent to the platform using the <code>event</code> method. </p>  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Location(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'geo': 'Geo',
        'plus_code': 'str'
    }

    attribute_map = {
        'geo': 'geo',
        'plus_code': 'plusCode'
    }

    def __init__(self, geo=None, plus_code=None):  # noqa: E501
        """Location - a model defined in Swagger"""  # noqa: E501
        self._geo = None
        self._plus_code = None
        self.discriminator = None
        if geo is not None:
            self.geo = geo
        if plus_code is not None:
            self.plus_code = plus_code

    @property
    def geo(self):
        """Gets the geo of this Location.  # noqa: E501


        :return: The geo of this Location.  # noqa: E501
        :rtype: Geo
        """
        return self._geo

    @geo.setter
    def geo(self, geo):
        """Sets the geo of this Location.


        :param geo: The geo of this Location.  # noqa: E501
        :type: Geo
        """

        self._geo = geo

    @property
    def plus_code(self):
        """Gets the plus_code of this Location.  # noqa: E501

        The location according to the Plus Code definition `https://plus.codes/`  # noqa: E501

        :return: The plus_code of this Location.  # noqa: E501
        :rtype: str
        """
        return self._plus_code

    @plus_code.setter
    def plus_code(self, plus_code):
        """Sets the plus_code of this Location.

        The location according to the Plus Code definition `https://plus.codes/`  # noqa: E501

        :param plus_code: The plus_code of this Location.  # noqa: E501
        :type: str
        """

        self._plus_code = plus_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Location, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
