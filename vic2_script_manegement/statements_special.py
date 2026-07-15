from __future__ import annotations

from vic2_script_types.statements_name import NameStatement
from vic2_script_types.statements_boolean import BoolAND, BooleanStatement
from vic2_script_types.statements_conditions import Condition
from vic2_script_types.statements_scope import Scope






class LimitStatement(NameStatement):
    def __init__(self, content: list[Condition | BooleanStatement | Scope]) -> None:
        super().__init__("limit")
        self._content: BoolAND = BoolAND(content)