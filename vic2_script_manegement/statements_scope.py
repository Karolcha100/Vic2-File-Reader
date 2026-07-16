from statements_name import NameStatement





class TriggerScope(NameStatement):
    def __init__(self, name: str, content: list[Condition|Effect|LimitStatement]) -> None:
        super().__init__(name)

        self._content: list[Condition|Effect|LimitStatement] = content