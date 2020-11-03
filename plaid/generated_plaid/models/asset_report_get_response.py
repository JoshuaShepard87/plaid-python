# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class AssetReportGetResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'report': 'AssetReport',
        'warnings': 'list[Warning]',
        'request_id': 'str'
    }

    attribute_map = {
        'report': 'report',
        'warnings': 'warnings',
        'request_id': 'request_id'
    }

    def __init__(self, report=None, warnings=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """AssetReportGetResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._report = None
        self._warnings = None
        self._request_id = None
        self.discriminator = None

        if report is not None:
            self.report = report
        if warnings is not None:
            self.warnings = warnings
        if request_id is not None:
            self.request_id = request_id

    @property
    def report(self):
        """Gets the report of this AssetReportGetResponse.  # noqa: E501


        :return: The report of this AssetReportGetResponse.  # noqa: E501
        :rtype: AssetReport
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this AssetReportGetResponse.


        :param report: The report of this AssetReportGetResponse.  # noqa: E501
        :type report: AssetReport
        """

        self._report = report

    @property
    def warnings(self):
        """Gets the warnings of this AssetReportGetResponse.  # noqa: E501

        If the Asset Report generation was successful but identity information cannot be returned, this array will contain information about the errors causing identity information to be missing  # noqa: E501

        :return: The warnings of this AssetReportGetResponse.  # noqa: E501
        :rtype: list[Warning]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this AssetReportGetResponse.

        If the Asset Report generation was successful but identity information cannot be returned, this array will contain information about the errors causing identity information to be missing  # noqa: E501

        :param warnings: The warnings of this AssetReportGetResponse.  # noqa: E501
        :type warnings: list[Warning]
        """

        self._warnings = warnings

    @property
    def request_id(self):
        """Gets the request_id of this AssetReportGetResponse.  # noqa: E501

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :return: The request_id of this AssetReportGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AssetReportGetResponse.

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :param request_id: The request_id of this AssetReportGetResponse.  # noqa: E501
        :type request_id: str
        """

        self._request_id = request_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssetReportGetResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetReportGetResponse):
            return True

        return self.to_dict() != other.to_dict()