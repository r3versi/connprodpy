# connprod.EventApi

All URIs are relative to *https://hackathon.tim.it/connprod*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_event**](EventApi.md#add_event) | **POST** /cab/products/{objectId}/event | Add a new event for a connected product
[**add_events**](EventApi.md#add_events) | **POST** /cab/products/{objectId}/events | Add an array of new events for a connected product
[**get_events**](EventApi.md#get_events) | **GET** /cab/products/{objectId}/events | Get events for the specified connected product

# **add_event**
> Event add_event(body, object_id)

Add a new event for a connected product

### Example
```python
from __future__ import print_function
import time
import connprod
from connprod.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = connprod.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = connprod.EventApi(connprod.ApiClient(configuration))
body = connprod.Event() # Event | Event object to be added
object_id = 'object_id_example' # str | identifier for the product (e.g. MAC address of the device, serial number, etc.) - format: <code>prefix:value</code> where prefix is: <code>mac</code>, <code>serial</code>, etc.. and value is without ':' special character. Example: <code>mac:AABBCCDDEEFF</code>

try:
    # Add a new event for a connected product
    api_response = api_instance.add_event(body, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->add_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Event**](Event.md)| Event object to be added | 
 **object_id** | **str**| identifier for the product (e.g. MAC address of the device, serial number, etc.) - format: &lt;code&gt;prefix:value&lt;/code&gt; where prefix is: &lt;code&gt;mac&lt;/code&gt;, &lt;code&gt;serial&lt;/code&gt;, etc.. and value is without &#x27;:&#x27; special character. Example: &lt;code&gt;mac:AABBCCDDEEFF&lt;/code&gt; | 

### Return type

[**Event**](Event.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_events**
> Events add_events(body, object_id)

Add an array of new events for a connected product

### Example
```python
from __future__ import print_function
import time
import connprod
from connprod.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = connprod.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = connprod.EventApi(connprod.ApiClient(configuration))
body = [connprod.Event()] # list[Event] | Events array object that needs to be added for the connected product
object_id = 'object_id_example' # str | identifier for the product (e.g. MAC address of the device, serial number, etc.) - format: <code>prefix:value</code> where prefix is: <code>mac</code>, <code>serial</code>, etc.. and value is without ':' special character. Example: <code>mac:AABBCCDDEEFF</code>

try:
    # Add an array of new events for a connected product
    api_response = api_instance.add_events(body, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->add_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Event]**](Event.md)| Events array object that needs to be added for the connected product | 
 **object_id** | **str**| identifier for the product (e.g. MAC address of the device, serial number, etc.) - format: &lt;code&gt;prefix:value&lt;/code&gt; where prefix is: &lt;code&gt;mac&lt;/code&gt;, &lt;code&gt;serial&lt;/code&gt;, etc.. and value is without &#x27;:&#x27; special character. Example: &lt;code&gt;mac:AABBCCDDEEFF&lt;/code&gt; | 

### Return type

[**Events**](Events.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> Events get_events(object_id, time_min=time_min, time_max=time_max)

Get events for the specified connected product

### Example
```python
from __future__ import print_function
import time
import connprod
from connprod.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = connprod.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = connprod.EventApi(connprod.ApiClient(configuration))
object_id = 'object_id_example' # str | identifier for the product (e.g. MAC address of the device, serial number, etc.) - format: <code>prefix:value</code> where prefix is: <code>mac</code>, <code>serial</code>, etc.. and value is without ':' special character. Example: <code>mac:AABBCCDDEEFF</code>
time_min = 'time_min_example' # str | The min date to filter the data (ISO format YYYY/MM/DD)  In case of null value, It will be set to one week ago or, in case timeMax has a value,  It will be set to timeMax minus one week (optional)
time_max = 'time_max_example' # str | The max date to filter the data (ISO format YYYY/MM/DD)  In case of null value, It will be now or timeMin plus one week (optional)

try:
    # Get events for the specified connected product
    api_response = api_instance.get_events(object_id, time_min=time_min, time_max=time_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| identifier for the product (e.g. MAC address of the device, serial number, etc.) - format: &lt;code&gt;prefix:value&lt;/code&gt; where prefix is: &lt;code&gt;mac&lt;/code&gt;, &lt;code&gt;serial&lt;/code&gt;, etc.. and value is without &#x27;:&#x27; special character. Example: &lt;code&gt;mac:AABBCCDDEEFF&lt;/code&gt; | 
 **time_min** | **str**| The min date to filter the data (ISO format YYYY/MM/DD)  In case of null value, It will be set to one week ago or, in case timeMax has a value,  It will be set to timeMax minus one week | [optional] 
 **time_max** | **str**| The max date to filter the data (ISO format YYYY/MM/DD)  In case of null value, It will be now or timeMin plus one week | [optional] 

### Return type

[**Events**](Events.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

