from __future__ import annotations
from abc import ABC, abstractmethod
from typing.types_basic import BasicType






class NameStatement(ABC):
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
    



class Equation(NameStatement):
    """
    Any Equation, mapping `name` of Statement `to` corresponding `value`.

    In Short: 
    ```
    name = value
    ```

    :param name: Name of Statement
    :type name: str

    :param value: Value assigned to Statement
    :type value: BasicType
    """
    def __init__(self, name: str, value: BasicType) -> None:
        super().__init__(name)
        self._value: BasicType = value
    
    def get_value(self) -> BasicType:
        """
        Returns Value, stored in Equation.

        :return: value
        :rtype: str
        """
        return self._value
    
    def set_value(self, value: BasicType) -> None:
        """
        Sets Value stored in Equation.

        :param value: Value to set
        :type value: BasicType
        """
        self._value = value


class ListOfEquations(NameStatement):
    """
    Any List of Equations, mapping `name` to list of multiple `Equation`.

    In Short: 
    ```
    name = {
        Equation
        Equation
        ...
    }
    ```

    There Should be **atlest 1** equation.

    :param name: Name of Statement
    :type name: str

    :param equations: Equations assigned to Statement
    :type equations: list[Equation]

    :raises Not Enough Equations: When number of provided Equations is below 1
    """
    def __init__(self, name: str, equations: list[Equation]) -> None:
        if len(equations) == 0:
            raise ValueError(f"Not Enough Equations")

        super().__init__(name)
        self._equations: list[Equation] = equations
    
    def get_values(self) -> list[Equation]:
        """
        Returns Names mapped to Values, in stored Equations.

        :return: List of Equations
        :rtype: list[Equation]
        """
        return self._equations
    
    def set_value(self, name: str, value: BasicType) -> None:
        """
        Sets Value stored in Equation.

        :param value: Value to set
        :type value: BasicType
        """
        for i, equation in enumerate(self._equations):
            if equation.get_name() == name:
                self._equations[i].set_value(value)
                break

        raise ValueError(f"name = {name}, not in Equations")