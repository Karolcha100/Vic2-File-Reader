from __future__ import annotations
from abc import ABC, abstractmethod

from vic2_script_types.statements_name import Equation, ListOfEquations






class Scope(NameStatement):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.content: list[Condition|Effect|LimitStatement]

    def get_name(self) -> str:
        return super().get_name()
    
    def add_substatement(self, substatement: Condition|Effect|LimitStatement) -> None:
        self.content.append(substatement)




class ModifierEffect(NameStatement):
    def __init__(self, name: str, content: list[Equation]) -> None:
        super().__init__(name)
        self.content: list[Equation]

    def get_name(self) -> str:
        return super().get_name()

class TreeRoot(NameStatement):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.content: list[ListDType|BlockDType|Equation]

    def get_name(self) -> str:
        return super().get_name()
    
    def add_substatement(self, substatement: ListDType|BlockDType|Equation) -> None:
        self.content.append(substatement)

class ListDType(NameStatement):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.content: list[str]

    def get_name(self) -> str:
        return super().get_name()
    
    def add_element(self, element: str) -> None:
        self.content.append(element)

class BlockDType(NameStatement):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.content: list[BlockDType|ListDType|GroupPopModifier|PopModifier|Equation]

    def get_name(self) -> str:
        return super().get_name()
    
    def add_substatement(self, substatement: BlockDType|ListDType|GroupPopModifier|PopModifier|Equation) -> None:
        self.content.append(substatement)






class GroupPopModifier:
    def __init__(self) -> None:
        self.content: list[PopModifier] = []

class PopModifier:
    def __init__(self) -> None:
        self.factor: float
        self.content: BoolAND