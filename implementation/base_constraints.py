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


class BytesConstraint(Enum):
    OPAQUE = 1
    TYPE = 2

    X509_CERTIFICATE = 3


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


class Opaque(StringConstraint):
    constraint: StringConstraint = BytesConstraint.OPAQUE

class Type(StringConstraint):
    constraint: StringConstraint = BytesConstraint.TYPE

class Certificate(StringConstraint):
    constraint: StringConstraint = BytesConstraint.X509_CERTIFICATE


class Attribute(StringConstraint):
    constraint: StringConstraint = IntConstraint.ATTRIBUTE
