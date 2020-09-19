from enum import Enum
from typing import List, Tuple


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls) -> Tuple[Tuple[int, str]]:
        return tuple((item.value, item.name) for item in cls)

    @classmethod
    def values(cls) -> List[int]:
        return [item.value for item in cls]

    @classmethod
    def names(cls) -> List[str]:
        return [item.name for item in cls]
