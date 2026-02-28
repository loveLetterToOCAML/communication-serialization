from __future__ import annotations

from implementation.base_constraints import Opaque, Type, Attribute, Uuid, Ulid, Yaml, Toml, SemVer, Certificate, SecretRef, \
    CronString, Color, Json, Url

from pydantic import BaseModel

from decimal import Decimal
from typing import Dict, Any
import datetime


class SparseObject(BaseModel):
    objectType: DefaultBaseType.TYPE
    attributes: Dict[DefaultBaseType.ATTRIBUTE, Any]  # Any is in fact RootSerial but it would cause circular dep


# left is serialization repr, right is related python default type for it
class DefaultBaseType:
    NONE = None
    BOOL = bool
    INT = int
    FLOAT = float
    DECIMAL = Decimal
    STRING = str
    BYTES = bytes


    OPAQUE = Opaque
    TYPE = Type
    ATTRIBUTE = Attribute
    SPARSE_OBJECT = SparseObject

    DATETIME = datetime.datetime
    DATE = datetime.date
    TIME = datetime.time
    TIMEDELTA = datetime.timedelta

    UUID = Uuid
    ULID = Ulid

    JSON_STRING = Json
    YAML_STRING = Yaml
    TOML_STRING = Toml

    SEMANTIC_VERSION = SemVer

    X509_CERTIFICATE = Certificate
    URL = Url

    SECRET_REFERENCE = SecretRef
    CRON_STRING = CronString
    COLOR = Color


class DefaultExternalNetworkBaseType:
    MAC_ADDRESS = MacAddress
    IPV4_ADDRESS = Ipv4Address
    IPV4_RANGE = Ipv4Range
    IPV6_ADDRESS = Ipv6Address
    IPV6_RANGE = Ipv6Range
    NETWORK_SERVICE = NetworkService
    DOMAIN = Domain
    FQDN = Fqdn


class DefaultExternalSocialBaseType:
    EMAIL = Email
    PHONE_NUMBER = PhoneNumber
    SOCIAL_IDENTITY = SocialIdentity
    SOCIAL_NUMBER = SocialNumber
    COUNTRY_NAME = CountryName
    COUNTRY_ALPHA = CountryShort
    ADDRESS = Address
    COMPANY = str
