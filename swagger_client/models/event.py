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


class Event(object):
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
        'timestamp': 'int',
        'campaign_id': 'str',
        'location': 'Location',
        'event_name': 'str',
        'event_attributes': 'list[EventAttribute]',
        'interactions': 'list[Interaction]',
        'sensors': 'list[Sensor]'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'campaign_id': 'campaignId',
        'location': 'location',
        'event_name': 'eventName',
        'event_attributes': 'eventAttributes',
        'interactions': 'interactions',
        'sensors': 'sensors'
    }

    def __init__(self, timestamp=None, campaign_id=None, location=None, event_name=None, event_attributes=None, interactions=None, sensors=None):  # noqa: E501
        """Event - a model defined in Swagger"""  # noqa: E501
        self._timestamp = None
        self._campaign_id = None
        self._location = None
        self._event_name = None
        self._event_attributes = None
        self._interactions = None
        self._sensors = None
        self.discriminator = None
        self.timestamp = timestamp
        if campaign_id is not None:
            self.campaign_id = campaign_id
        if location is not None:
            self.location = location
        self.event_name = event_name
        if event_attributes is not None:
            self.event_attributes = event_attributes
        if interactions is not None:
            self.interactions = interactions
        if sensors is not None:
            self.sensors = sensors

    @property
    def timestamp(self):
        """Gets the timestamp of this Event.  # noqa: E501

        The timestamp (in form of Unix Timestamp in milliseconds - see `https://currentmillis.com/` for clarifications) of the Event  # noqa: E501

        :return: The timestamp of this Event.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Event.

        The timestamp (in form of Unix Timestamp in milliseconds - see `https://currentmillis.com/` for clarifications) of the Event  # noqa: E501

        :param timestamp: The timestamp of this Event.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def campaign_id(self):
        """Gets the campaign_id of this Event.  # noqa: E501

        The campaign id the event refers to  # noqa: E501

        :return: The campaign_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this Event.

        The campaign id the event refers to  # noqa: E501

        :param campaign_id: The campaign_id of this Event.  # noqa: E501
        :type: str
        """

        self._campaign_id = campaign_id

    @property
    def location(self):
        """Gets the location of this Event.  # noqa: E501


        :return: The location of this Event.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Event.


        :param location: The location of this Event.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def event_name(self):
        """Gets the event_name of this Event.  # noqa: E501

        The event name  # noqa: E501

        :return: The event_name of this Event.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this Event.

        The event name  # noqa: E501

        :param event_name: The event_name of this Event.  # noqa: E501
        :type: str
        """
        if event_name is None:
            raise ValueError("Invalid value for `event_name`, must not be `None`")  # noqa: E501

        self._event_name = event_name

    @property
    def event_attributes(self):
        """Gets the event_attributes of this Event.  # noqa: E501

        Array of name+value tuples containing additional informations about the event  # noqa: E501

        :return: The event_attributes of this Event.  # noqa: E501
        :rtype: list[EventAttribute]
        """
        return self._event_attributes

    @event_attributes.setter
    def event_attributes(self, event_attributes):
        """Sets the event_attributes of this Event.

        Array of name+value tuples containing additional informations about the event  # noqa: E501

        :param event_attributes: The event_attributes of this Event.  # noqa: E501
        :type: list[EventAttribute]
        """

        self._event_attributes = event_attributes

    @property
    def interactions(self):
        """Gets the interactions of this Event.  # noqa: E501

        Array of type+value tuples containing the interactions with the object that led to the action  # noqa: E501

        :return: The interactions of this Event.  # noqa: E501
        :rtype: list[Interaction]
        """
        return self._interactions

    @interactions.setter
    def interactions(self, interactions):
        """Sets the interactions of this Event.

        Array of type+value tuples containing the interactions with the object that led to the action  # noqa: E501

        :param interactions: The interactions of this Event.  # noqa: E501
        :type: list[Interaction]
        """

        self._interactions = interactions

    @property
    def sensors(self):
        """Gets the sensors of this Event.  # noqa: E501

        Array of name+value tuples containing the sensors values measured by the product (e.g. the temperature reached 100°C)  # noqa: E501

        :return: The sensors of this Event.  # noqa: E501
        :rtype: list[Sensor]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this Event.

        Array of name+value tuples containing the sensors values measured by the product (e.g. the temperature reached 100°C)  # noqa: E501

        :param sensors: The sensors of this Event.  # noqa: E501
        :type: list[Sensor]
        """

        self._sensors = sensors

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
        if issubclass(Event, dict):
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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
