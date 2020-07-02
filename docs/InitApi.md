# connprod.InitApi

All URIs are relative to *https://hackathon.tim.it/connprod*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_init**](InitApi.md#add_init) | **POST** /cab/products/{objectId}/init | Register a new connected product

# **add_init**
> Init add_init(body, object_id)

Register a new connected product

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
api_instance = connprod.InitApi(connprod.ApiClient(configuration))
body = connprod.Init() # Init | Init object to register
object_id = 'object_id_example' # str | identifier for the product (e.g. MAC address of the device, serial number, etc.) - format: <code>prefix:value</code> where prefix is: <code>mac</code>, <code>serial</code>, etc.. and value is without ':' special character. Example: <code>mac:AABBCCDDEEFF</code>

try:
    # Register a new connected product
    api_response = api_instance.add_init(body, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InitApi->add_init: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Init**](Init.md)| Init object to register | 
 **object_id** | **str**| identifier for the product (e.g. MAC address of the device, serial number, etc.) - format: &lt;code&gt;prefix:value&lt;/code&gt; where prefix is: &lt;code&gt;mac&lt;/code&gt;, &lt;code&gt;serial&lt;/code&gt;, etc.. and value is without &#x27;:&#x27; special character. Example: &lt;code&gt;mac:AABBCCDDEEFF&lt;/code&gt; | 

### Return type

[**Init**](Init.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

