from __future__ import annotations

from statements_name import NameStatement
from statements_condition import Condition
from statements_scope import Scope





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