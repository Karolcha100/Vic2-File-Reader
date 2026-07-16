from abc import ABC, abstractmethod

from statements_name import NameStatement
from typing.types_basic import BasicType, NumericType, StringType
from script_node import ScriptNode






class Effect[T: list[Effect[BasicType]] | BasicType](NameStatement, ScriptNode):
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

    # @abstractmethod
    # def execute(self, checked: T) -> bool:
    #     """
        
    #     """
    #     ...

    def get_inside(self) -> T:
        """
        
        """
        return self._value
    
    @abstractmethod
    def to_script(self) -> str:
        ...
    



class EffectWithArguments(Effect[list[Effect[BasicType]]]):
    """
    
    """

    def __init__(self, name: str, value: list[Effect[BasicType]]) -> None:
        super().__init__(name, value)

    # def execute(self, checked: list[Effect[BasicType]]) -> bool:
    #     return sum(
    #         [
    #             cond_value.execute(cond_incoming.get_inside())
    #             for cond_value, cond_incoming in zip(self._value, checked)
    #         ]
    #     ) == len(checked)
    
    def to_script(self) -> str:
        return_str = self._name + " = {\n"

        for cond in self._value:
            return_str += "\t" + cond.to_script() + "\n"

        return return_str + "}"


class EffectEquation(Effect[BasicType]):
    """
    
    """

    def __init__(self, name: str, value: BasicType) -> None:
        super().__init__(name, value)

    # def execute(self, checked: BasicType) -> bool:

    #     if isinstance(checked, NumericType):
    #         return self._value.get_parsed_value() <= checked.get_parsed_value()
        
    #     if isinstance(checked, StringType):
    #         return self._value.get_parsed_value() == checked.get_parsed_value()
        
    #     raise ValueError(f"unrecognized type")
            
    def to_script(self) -> str:
        return f"{self._name} = {self._value.get_raw_value()}"