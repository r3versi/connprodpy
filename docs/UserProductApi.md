# connprod.UserProductApi

All URIs are relative to *https://hackathon.tim.it/connprod*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_products**](UserProductApi.md#get_user_products) | **GET** /cab/products | Returns all the user products
[**remove_user_product**](UserProductApi.md#remove_user_product) | **DELETE** /cab/products/{objectId} | Removes a product from a user

# **get_user_products**
> UserProductsResponse get_user_products()

Returns all the user products

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
api_instance = connprod.UserProductApi(connprod.ApiClient(configuration))

try:
    # Returns all the user products
    api_response = api_instance.get_user_products()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserProductApi->get_user_products: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProductsResponse**](UserProductsResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_product**
> remove_user_product(object_id)

Removes a product from a user

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
api_instance = connprod.UserProductApi(connprod.ApiClient(configuration))
object_id = 'object_id_example' # str | identifier for the product (e.g. MAC address of the device, serial number, etc.) - format: <code>prefix:value</code> where prefix is: <code>mac</code>, <code>serial</code>, etc.. and value is without ':' special character. Example: <code>mac:AABBCCDDEEFF</code>

try:
    # Removes a product from a user
    api_instance.remove_user_product(object_id)
except ApiException as e:
    print("Exception when calling UserProductApi->remove_user_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| identifier for the product (e.g. MAC address of the device, serial number, etc.) - format: &lt;code&gt;prefix:value&lt;/code&gt; where prefix is: &lt;code&gt;mac&lt;/code&gt;, &lt;code&gt;serial&lt;/code&gt;, etc.. and value is without &#x27;:&#x27; special character. Example: &lt;code&gt;mac:AABBCCDDEEFF&lt;/code&gt; | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

