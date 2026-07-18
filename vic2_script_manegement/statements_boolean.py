from __future__ import annotations

from statements_name import NameStatement
from statements_condition import Condition
from statements_scope import TriggerScope





class BooleanStatement(NameStatement):
    def __init__(self, name: str, content: list[Condition | BooleanStatement | TriggerScope]) -> None:
        super().__init__(name)
        self._content: list[Condition | BooleanStatement | TriggerScope] = content

    def to_script(self, depth: int) -> str:    
        text = f"{"\t"*depth}{self._name} = " + "{\n"

        for cont in self._content:
            text += cont.to_script(depth+1)

        return text + f"{"\t"*depth}" + "}"
    



class BoolAND(BooleanStatement):
    def __init__(self, content: list[Condition | BooleanStatement | TriggerScope]) -> None:
        super().__init__("AND", content)
    

class BoolOR(BooleanStatement):
    def __init__(self, content: list[Condition | BooleanStatement | TriggerScope]) -> None:
        super().__init__("OR", content)
    

class BoolNOT(BooleanStatement):
    def __init__(self, content: list[Condition | BooleanStatement | TriggerScope]) -> None:
        super().__init__("NOT", content)