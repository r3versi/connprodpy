# coding: utf-8

"""
    Connected Product API

    This API bundle allows to collect usage data from different \"connected products\". A connected product is an IoT consumer product connected to the IoT platform through a digital interface. Possible connected products are: <ul> <li>natively connected products (e.g. smart kitchen appliances, smart coffee machines, smart fridge, etc.);</li> <li>regular products connected through a gateway and equipped with additional sensors (e.g. bags or luggages with NFC or Bluetooth tags, etc.)</li> </ul> <p>To register for the first time a new product, the <code>init</code> method must be invoked.</p> <p>After registration, every product usage event (e.g. state change, sensors value change, user interaction with the product, etc.) is sent to the platform using the <code>event</code> method. </p>  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from connprod.api_client import ApiClient


class UserProductApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_user_products(self, **kwargs):  # noqa: E501
        """Returns all the user products  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_products(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserProductsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_products_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_products_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_products_with_http_info(self, **kwargs):  # noqa: E501
        """Returns all the user products  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_products_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserProductsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_products" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/cab/products', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserProductsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_user_product(self, object_id, **kwargs):  # noqa: E501
        """Removes a product from a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_user_product(object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str object_id: identifier for the product (e.g. MAC address of the device, serial number, etc.) - format: <code>prefix:value</code> where prefix is: <code>mac</code>, <code>serial</code>, etc.. and value is without ':' special character. Example: <code>mac:AABBCCDDEEFF</code> (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_user_product_with_http_info(object_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_user_product_with_http_info(object_id, **kwargs)  # noqa: E501
            return data

    def remove_user_product_with_http_info(self, object_id, **kwargs):  # noqa: E501
        """Removes a product from a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_user_product_with_http_info(object_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str object_id: identifier for the product (e.g. MAC address of the device, serial number, etc.) - format: <code>prefix:value</code> where prefix is: <code>mac</code>, <code>serial</code>, etc.. and value is without ':' special character. Example: <code>mac:AABBCCDDEEFF</code> (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['object_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_user_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'object_id' is set
        if ('object_id' not in params or
                params['object_id'] is None):
            raise ValueError("Missing the required parameter `object_id` when calling `remove_user_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_id' in params:
            path_params['objectId'] = params['object_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/cab/products/{objectId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
