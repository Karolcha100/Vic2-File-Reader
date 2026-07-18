from __future__ import annotations
from abc import ABC, abstractmethod
from typing.types_basic import BasicType
from script_node import ScriptNode







class NameStatement(ScriptNode):
    """
    Any Statement in Vic2 Scrpit Language which have a name.

    :param name: Name of This Statement
    :type name: str
    """
    def __init__(self, name: str) -> None:
        self._name: str = name

    def get_name(self) -> str:
        """
        Returns Name of This Statement.

        :return: name
        :rtype: str
        """
        return self._name
    
    @abstractmethod
    def to_script(self, depth: int) -> str:
        ...