from abc import ABC, abstractmethod





class BasicType[T](ABC):
    def __init__(self, my_type: str, value: T) -> None:
        self._my_type: str = my_type
        self._value: T = value
    
    def get_my_type(self) -> str:
        return self._my_type    # `i.e. [TAG]` or `[yes/no]`
    
    def get_stored_value(self) -> T:
        return self._value



class BooleanType(BasicType):
    def __init__(self, stored_value: str) -> None:
        super().__init__("Bool", stored_value)
        