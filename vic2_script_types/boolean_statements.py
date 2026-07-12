from __future__ import annotations
from abc import ABC, abstractmethod

from name_statements import NameStatement
from conditions_statements import Condition
from scope_statements import Scope
from vic2_script_types.special_statements import LimitStatement






class BooleanStatement(NameStatement):
    def __init__(self, name: str, content: list[Condition | BooleanStatement | Scope]) -> None:
        super().__init__(name)
        self._content = content




class BoolAND(BooleanStatement):
    def __init__(self, content: list[Condition | BooleanStatement | Scope]) -> None:
        super().__init__("AND", content)
    

class BoolOR(BooleanStatement):
    def __init__(self, content: list[Condition | BooleanStatement | Scope]) -> None:
        super().__init__("OR", content)
    

class BoolNOT(BooleanStatement):
    def __init__(self, content: list[Condition | BooleanStatement | Scope]) -> None:
        super().__init__("NOT", content)