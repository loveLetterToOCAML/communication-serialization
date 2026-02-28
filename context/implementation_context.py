from implementation.base_types import DefaultBaseType

import contextvars


BaseTypesModel = contextvars.ContextVar('base_types', default=DefaultBaseType)
