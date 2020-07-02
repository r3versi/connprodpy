# Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | The timestamp (in form of Unix Timestamp in milliseconds - see &#x60;https://currentmillis.com/&#x60; for clarifications) of the Event | 
**campaign_id** | **str** | The campaign id the event refers to | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**event_name** | **str** | The event name | 
**event_attributes** | [**list[EventAttribute]**](EventAttribute.md) | Array of name+value tuples containing additional informations about the event | [optional] 
**interactions** | [**list[Interaction]**](Interaction.md) | Array of type+value tuples containing the interactions with the object that led to the action | [optional] 
**sensors** | [**list[Sensor]**](Sensor.md) | Array of name+value tuples containing the sensors values measured by the product (e.g. the temperature reached 100°C) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

