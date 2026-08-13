from enum import Enum


class OptimizedDataTypes(Enum):
    ALIAS = 1  # alias named types to create shortcuts within the type trees for frequently used types

    UINT8 = 2
    UINT16 = 3
    UINT32 = 4
    UINT64 = 5
