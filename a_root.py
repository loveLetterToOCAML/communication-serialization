from enum import Enum

from pydantic import BaseModel

from ab_basetypes import BaseDataTypes


class SerialType(Enum):
    Optimized = 1       # specific convention between communication systems to optimize size of produced serialization
    BaseTypes = 2       # all common types including per-domain shared conventions (str with constraints as instance)
    GenericsData = 3    # ability to serialize generics with chosen serialization types

    Authority = 4       # includes authentication, identification / session, access controls, in a global domain
    Interaction = 5     # includes interaction related, result, error, exception, ...
    Communication = 6   # includes network related (routing), secure related, interaction (results, errors)
    SelfExecution = 7   # includes sup and inf execution context, self perception of current execution

    Data = 10           # includes knowledge, filer, vault, cache, database, backup, structured logs intents
    Action = 11
    Persist = 12
    Config = 13
    Context = 14
    Infra = 15
    Visualization = 16

    Craft = 20
    Test = 21
    Replicate = 22
    Understand = 23
    Exploration = 24

    ModelExternal = 30
    Instrument = 31
    Measure = 32


class RootSerial(BaseModel):
    Type: BaseDataTypes.TYPE

# better explicit than implicit / dynamic: explicitly declare the attributes as params, do it for every subclass
# 0 -> 0x10: precedence happens at child level
# 0x10 -> 0xff: precedence happens at parent level (so below 0xff Type is defined here for all subtypes)
class SerialParams(Enum):
    Type = 0


Root = register_serialization_context()
RootParams = register_serialization_params_context(Root, SerialParams)
