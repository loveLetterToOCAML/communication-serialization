from implementation.basetypes import DefaultBaseType

import contextvars


BaseTypesModel = contextvars.ContextVar('base_types', default=DefaultBaseType)
