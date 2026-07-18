from abc import ABC, abstractmethod

from statements_name import NameStatement
from typing.types_basic import BasicType, NumericType, StringType






class Condition[T: list[Condition[BasicType]] | BasicType](NameStatement):
    """
    Abstract Condition Statement.
    """

    def __init__(self, name: str, value: T) -> None:
        super().__init__(name)
        self._value: T = value

    def set_inside(self, value: T) -> None:
        """
        
        """
        self._value = value

    @abstractmethod
    def evaluate(self, checked: T) -> bool:
        """
        
        """
        ...

    def get_inside(self) -> T:
        """
        
        """
        return self._value
    
    @abstractmethod
    def to_script(self, depth: int) -> str:
        ...
    



class ConditionWithArguments(Condition[list[Condition[BasicType]]]):
    """
    
    """

    def __init__(self, name: str, value: list[Condition[BasicType]]) -> None:
        super().__init__(name, value)

    def evaluate(self, checked: list[Condition[BasicType]]) -> bool:
        return sum(
            [
                cond_value.evaluate(cond_incoming.get_inside())
                for cond_value, cond_incoming in zip(self._value, checked)
            ]
        ) == len(checked)
    
    def to_script(self, depth: int) -> str:
        return_str = f"{"\t"*depth}{self._name}" + " = {\n"

        for cond in self._value:
            return_str += cond.to_script(depth+1)

        return return_str + f"{"\t"*depth}" + "}"


class ConditionEquation(Condition[BasicType]):
    """
    
    """

    def __init__(self, name: str, value: BasicType) -> None:
        super().__init__(name, value)

    def evaluate(self, checked: BasicType) -> bool:

        if isinstance(checked, NumericType):
            return self._value.get_parsed_value() <= checked.get_parsed_value()
        
        if isinstance(checked, StringType):
            return self._value.get_parsed_value() == checked.get_parsed_value()
        
        raise ValueError(f"unrecognized type")
            
    def to_script(self, depth: int) -> str:
        return f"{"\t"*depth}{self._name} = {self._value.get_raw_value()}\n"