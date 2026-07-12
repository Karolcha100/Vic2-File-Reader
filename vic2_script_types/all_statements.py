from __future__ import annotations
from abc import ABC, abstractmethod

from name_statements import Equation, ListOfEquations






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




class NoNameStatements(ABC):
    def __init__(self) -> None:
        pass



class GroupPopModifier:
    def __init__(self) -> None:
        self.content: list[PopModifier] = []

class PopModifier:
    def __init__(self) -> None:
        self.factor: float
        self.content: BoolAND

class LimitStatement:
    def __init__(self) -> None:
        self.content: BoolAND




class BooleanStatements(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_my_type(self) -> str:
        pass



class BoolAND(BooleanStatements):
    def __init__(self) -> None:
        self.content: list[BooleanStatements|Scope|Condition] = []

    def get_my_type(self) -> str:
        return "AND"
    
class BoolOR(BooleanStatements):
    def __init__(self) -> None:
        self.content: list[BooleanStatements|Scope|Condition] = []

    def get_my_type(self) -> str:
        return "OR"
    
class BoolNOT(BooleanStatements):
    def __init__(self) -> None:
        self.content: list[BooleanStatements|Scope|Condition] = []

    def get_my_type(self) -> str:
        return "NOT"