from context.implementation_context import BaseTypesModel

from a_root import SerialType, Root

from enum import Enum


class BaseDataTypes(Enum):
    NONE = 1
    BOOL = 2
    INT = 3
    FLOAT = 4
    DECIMAL = 5
    STRING = 6
    BYTES = 7

    # from there and below all subtypes are kind of string with constraints on formatting or semantics
    OPAQUE = 100     # like bytes but may contain additional information about source / destination the opaque is dedicated to
    TYPE = 101       # this is simple uint8_t array to locate valid types in the full tree
    ATTRIBUTE = 102  # this is simple uint8_t array to locate the attribute type, with additional uint8_t / uint16_t ? for matching the attribute location
    SPARSE_OBJECT = 103  # this is type + attributes number + attributes for a given object

    DATETIME = 110
    DATE = 111
    TIME = 112
    TIMEDELTA = 113

    UUID = 120
    ULID = 121

    # purpose of current serialization process is to not serialize opaque as json, yaml or toml;
    # but specific externally related components with require them anyway so let's keep them in basic
    JSON_STRING = 130
    YAML_STRING = 131
    TOML_STRING = 132

    SEMANTIC_VERSION = 140

    X509_CERTIFICATE = 150
    URL = 151

    SECRET_REFERENCE = 160
    CRON_STRING = 161
    COLOR = 162


    OTHER_EXTERNAL_NETWORK = 240
    OTHER_EXTERNAL_SOCIAL = 241


class ExternalNetworkBaseTypes(Enum):
    MAC_ADDRESS = 1
    IPV4_ADDRESS = 2
    IPV4_RANGE = 3
    IPV6_ADDRESS = 4
    IPV6_RANGE = 5
    NETWORK_SERVICE = 6
    DOMAIN = 7
    FQDN = 8


class ExternalSocialBaseTypes(Enum):
    EMAIL = 1
    PHONE_NUMBER = 2
    SOCIAL_IDENTITY = 3
    SOCIAL_NUMBER = 4
    COUNTRY_NAME = 5
    COUNTRY_ALPHA = 6
    ADDRESS = 7
    COMPANY = 8


Base = Root.register_serialization_child(SerialType.BaseTypes, BaseDataTypes)
ExternalNetworkBase = Base.register_serialization_child(BaseDataTypes.OTHER_EXTERNAL_NETWORK, ExternalNetworkBaseTypes)
ExternalSocialBase = Base.register_serialization_child(BaseDataTypes.OTHER_EXTERNAL_NETWORK, ExternalSocialBaseTypes)


# don't know if this is best way to proceed to inject dependency of type implementation (do we really need this
# dependency injection at runtime? Guess this will be fixed and should not change a lot)
BaseTypes = BaseTypesModel.get()
