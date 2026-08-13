from pydantic import BaseModel

from enum import Enum


class StringConstraint(Enum):
    UUID = 1
    ULID = 2

    JSON_STRING = 3
    YAML_STRING = 4
    TOML_STRING = 5

    SEMANTIC_VERSION = 6

    SECRET_REFERENCE = 7
    CRON_STRING = 8
    COLOR = 9

    URL = 10
    MAC_ADDRESS = 11
    IPV4_ADDRESS = 12
    IPV4_RANGE = 13
    IPV6_ADDRESS = 14
    IPV6_RANGE = 15
    NETWORK_SERVICE = 16
    DOMAIN = 17
    FQDN = 18

    EMAIL = 19
    PHONE_NUMBER = 20
    SOCIAL_IDENTITY = 21
    SOCIAL_NUMBER = 22
    COUNTRY_NAME = 23
    COUNTRY_SHORT = 24
    ADDRESS = 25


class BytesConstraint(Enum):
    OPAQUE = 1
    TYPE = 2
    CHILD_TYPE = 3

    X509_CERTIFICATE = 5


class IntConstraint(Enum):
    ATTRIBUTE = 1


class StringWithConstraint(BaseModel):
    constraint: StringConstraint
    data: str

class BytesWithConstraints(BaseModel):
    constraint: BytesConstraint
    data: bytes

class IntWithConstraints(BaseModel):
    constraint: IntConstraint
    data: int


# TODO: add validation of input data for each type
# Warning: some types are contextual, like the TYPE one which requires knowing all valid nodes of the type tree

class Uuid(StringConstraint):
    constraint: StringConstraint = StringConstraint.UUID

class Ulid(StringConstraint):
    constraint: StringConstraint = StringConstraint.ULID

class Json(StringConstraint):
    constraint: StringConstraint = StringConstraint.JSON_STRING

class Yaml(StringConstraint):
    constraint: StringConstraint = StringConstraint.YAML_STRING

class Toml(StringConstraint):
    constraint: StringConstraint = StringConstraint.TOML_STRING

class SemVer(StringConstraint):
    constraint: StringConstraint = StringConstraint.SEMANTIC_VERSION

class SecretRef(StringConstraint):
    constraint: StringConstraint = StringConstraint.SECRET_REFERENCE

class CronString(StringConstraint):
    constraint: StringConstraint = StringConstraint.CRON_STRING

class Color(StringConstraint):
    constraint: StringConstraint = StringConstraint.COLOR

class Url(StringConstraint):
    constraint: StringConstraint = StringConstraint.URL

class MacAddress(StringConstraint):
    constraint: StringConstraint = StringConstraint.MAC_ADDRESS

class Ipv4Address(StringConstraint):
    constraint: StringConstraint = StringConstraint.IPV4_ADDRESS

class Ipv4Range(StringConstraint):
    constraint: StringConstraint = StringConstraint.IPV4_RANGE

class Ipv6Address(StringConstraint):
    constraint: StringConstraint = StringConstraint.IPV6_ADDRESS

class Ipv6Range(StringConstraint):
    constraint: StringConstraint = StringConstraint.IPV6_RANGE

class NetworkService(StringConstraint):
    constraint: StringConstraint = StringConstraint.NETWORK_SERVICE

class Domain(StringConstraint):
    constraint: StringConstraint = StringConstraint.DOMAIN

class Fqdn(StringConstraint):
    constraint: StringConstraint = StringConstraint.FQDN

class Email(StringConstraint):
    constraint: StringConstraint = StringConstraint.EMAIL

class PhoneNumber(StringConstraint):
    constraint: StringConstraint = StringConstraint.PHONE_NUMBER

class SocialIdentity(StringConstraint):
    constraint: StringConstraint = StringConstraint.SOCIAL_IDENTITY

class SocialNumber(StringConstraint):
    constraint: StringConstraint = StringConstraint.SOCIAL_NUMBER

class CountryName(StringConstraint):
    constraint: StringConstraint = StringConstraint.COUNTRY_NAME

class CountryShort(StringConstraint):
    constraint: StringConstraint = StringConstraint.COUNTRY_SHORT

class Address(StringConstraint):
    constraint: StringConstraint = StringConstraint.ADDRESS


class Opaque(BytesConstraint):
    constraint: BytesConstraint = BytesConstraint.OPAQUE

class Type(BytesConstraint):
    constraint: BytesConstraint = BytesConstraint.TYPE

class ChildType(BytesConstraint):
    constraint: BytesConstraint = BytesConstraint.CHILD_TYPE

class Certificate(BytesConstraint):
    constraint: BytesConstraint = BytesConstraint.X509_CERTIFICATE


class Attribute(IntConstraint):
    constraint: IntConstraint = IntConstraint.ATTRIBUTE
