from typing import TypeVar, Generic, Tuple, Dict, Any, Type, Union


T = TypeVar('T')


class TMutable(Generic[T]):
    def __init__(self, value: Any):
        self.__mutable_value = T(value)

    def __add__(self, other):
        return self.__mutable_value + other

    def __str__(self):
        return f'{self.__mutable_value}'


class MutableMeta(type, Generic[T]):
    __IMMUTABLE_TYPES = (
        bool,
        int,
        float,
        str,
        tuple,
    )

    @classmethod
    def __is_immutable(mcs, type_value: Type):
        return type_value in mcs.__IMMUTABLE_TYPES

    def __new__(mcs, name: str, base: T, namespace: Dict[str, Any]):
        if not mcs.__is_immutable(base):
            return base
        result_cls = super(MutableMeta, mcs).__new__(mcs, name, tuple(), namespace)




class MBoolean(bool, metaclass=MutableMeta):
    pass


class MInteger(int, metaclass=MutableMeta):
    pass


class MFloat(float, metaclass=MutableMeta):
    pass


class MString(str, metaclass=MutableMeta):
    pass


class MTuple(tuple, metaclass=MutableMeta):
    pass
