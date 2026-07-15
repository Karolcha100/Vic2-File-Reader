from __future__ import annotations

from statements_name import NameStatement
from statements_boolean import BoolAND, BooleanStatement
from statements_condition import Condition
from statements_scope import Scope






class LimitStatement(NameStatement):
    def __init__(self, content: list[Condition | BooleanStatement | Scope]) -> None:
        super().__init__("limit")
        self._content: BoolAND = BoolAND(content)