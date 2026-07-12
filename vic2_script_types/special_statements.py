from __future__ import annotations

from name_statements import NameStatement
from boolean_statements import BoolAND, BooleanStatement
from conditions_statements import Condition
from scope_statements import Scope






class LimitStatement(NameStatement):
    def __init__(self, content: list[Condition | BooleanStatement | Scope]) -> None:
        super().__init__("limit")
        self._content: BoolAND = BoolAND(content)