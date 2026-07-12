from __future__ import annotations
from abc import ABC, abstractmethod







class NameStatement(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name

    def get_my_name(self) -> str:
        return self.name



class Equation(NameStatement):
    def __init__(self, name: str, value: str) -> None:
        super().__init__(name)
        self.value: str = value

    def get_my_name(self) -> str:
        return super().get_my_name()

class Condition(NameStatement):
    """
    Note that it should store `'eq' -> [value]` when `condition = value`.
    
    Else it stores `arg_name -> [value]`.
    """
    def __init__(self, name: str, value: str|None = None, arguments: list[Equation]|None = None) -> None:
        if value is None and arguments is None:
            raise ValueError(f"[Condition <{name}>]: value = arguments = None")
        
        if value is not None and arguments is not None:
            raise ValueError(f"[Condition <{name}>]: value and arguments Are Both not None")

        super().__init__(name)

        self.value: str|None = value

        if arguments is not None:
            self.arguments: list[Equation] = arguments

    def get_my_name(self) -> str:
        return super().get_my_name()

class Effect(NameStatement):
    """
    Note that it should store `'eq' -> [value]` when `effect = value`.
    
    Else it stores `arg_name -> [value]`.
    """
    def __init__(self, name: str, value: str|None = None, arguments: list[Equation]|None = None) -> None:
        super().__init__(name)


        if value is None and arguments is None:
            raise ValueError(f"[Condition <{name}>]: value = arguments = None")
        
        if value is not None and arguments is not None:
            raise ValueError(f"[Condition <{name}>]: value and arguments Are Both not None")

        self.value: str|None = value
        if arguments is not None:
            self.arguments: list[Equation] = arguments

    def get_my_name(self) -> str:
        return super().get_my_name()

class Scope(NameStatement):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        self.content: list[Condition|Effect|LimitStatement]

    def get_my_name(self) -> str:
        return super().get_my_name()
    
    def add_substatement(self, substatement: Condition|Effect|LimitStatement) -> None:
        self.content.append(substatement)

class ModifierEffect(NameStatement):
    def __init__(self, name: str, content: list[Equation]) -> None:
        super().__init__(name)
        self.content: list[Equation]

    def get_my_name(self) -> str:
        return super().get_my_name()

class TreeRoot(NameStatement):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.content: list[ListDType|BlockDType|Equation]

    def get_my_name(self) -> str:
        return super().get_my_name()
    
    def add_substatement(self, substatement: ListDType|BlockDType|Equation) -> None:
        self.content.append(substatement)

class ListDType(NameStatement):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.content: list[str]

    def get_my_name(self) -> str:
        return super().get_my_name()
    
    def add_element(self, element: str) -> None:
        self.content.append(element)

class BlockDType(NameStatement):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.content: list[BlockDType|ListDType|GroupPopModifier|PopModifier|Equation]

    def get_my_name(self) -> str:
        return super().get_my_name()
    
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