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


class Geo(object):
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
        'lat': 'int',
        'lng': 'int'
    }

    attribute_map = {
        'lat': 'lat',
        'lng': 'lng'
    }

    def __init__(self, lat=None, lng=None):  # noqa: E501
        """Geo - a model defined in Swagger"""  # noqa: E501
        self._lat = None
        self._lng = None
        self.discriminator = None
        self.lat = lat
        self.lng = lng

    @property
    def lat(self):
        """Gets the lat of this Geo.  # noqa: E501

        The latitude value, floating-point with range [-90, 90]  # noqa: E501

        :return: The lat of this Geo.  # noqa: E501
        :rtype: int
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Geo.

        The latitude value, floating-point with range [-90, 90]  # noqa: E501

        :param lat: The lat of this Geo.  # noqa: E501
        :type: int
        """
        if lat is None:
            raise ValueError("Invalid value for `lat`, must not be `None`")  # noqa: E501

        self._lat = lat

    @property
    def lng(self):
        """Gets the lng of this Geo.  # noqa: E501

        The longitude value, floating-point with range [-180, 180]  # noqa: E501

        :return: The lng of this Geo.  # noqa: E501
        :rtype: int
        """
        return self._lng

    @lng.setter
    def lng(self, lng):
        """Sets the lng of this Geo.

        The longitude value, floating-point with range [-180, 180]  # noqa: E501

        :param lng: The lng of this Geo.  # noqa: E501
        :type: int
        """
        if lng is None:
            raise ValueError("Invalid value for `lng`, must not be `None`")  # noqa: E501

        self._lng = lng

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
        if issubclass(Geo, dict):
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
        if not isinstance(other, Geo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other