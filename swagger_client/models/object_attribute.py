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


class ObjectAttribute(object):
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
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None):  # noqa: E501
        """ObjectAttribute - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._value = None
        self.discriminator = None
        self.name = name
        self.value = value

    @property
    def name(self):
        """Gets the name of this ObjectAttribute.  # noqa: E501

        The property name  # noqa: E501

        :return: The name of this ObjectAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectAttribute.

        The property name  # noqa: E501

        :param name: The name of this ObjectAttribute.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this ObjectAttribute.  # noqa: E501

        The property value  # noqa: E501

        :return: The value of this ObjectAttribute.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ObjectAttribute.

        The property value  # noqa: E501

        :param value: The value of this ObjectAttribute.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(ObjectAttribute, dict):
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
        if not isinstance(other, ObjectAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
