from abc import ABC, abstractmethod

from statements_name import Equation, ListOfEquations
from typing.types_basic import BasicType






class Condition(ABC):
    """
    Abstract Condition Statement.
    """
    
    @abstractmethod
    def get_inside(self) -> dict[str, BasicType]:
        """
        Get value or arguments with corresponding values from Condition.

        If no arguments for Condition, it returns:
        >>> {"self": value}

        :return: Mapping arguments to values
        :rtype: dict[str, BasicType]
        """
        ...

    @abstractmethod
    def set_inside(self, name: str, value: BasicType) -> None:
        """
        Set inside value in Condition.

        If no arguments in Condition, name should be:
        >>> name: str = "self"

        :param name: Name of argument if any in Condition, else `"self"`
        :type name: str

        :param value: Value to set
        :type value: BasicType
        """
        ...

    @abstractmethod
    def evaluate(self) -> bool:
        """
        Checks if Condition is Met.

        :return: If condition is met.
        :rtype: bool
        """
        ...




class ConditionEquation(Equation, Condition):
    """
    Condition in form of Equation.

    In Short: 
    ```
    name = value
    ```

    :param name: Name of Condition
    :type name: str

    :param value: Value assigned to Condition
    :type value: BasicType
    """
    def __init__(self, name: str, value: BasicType) -> None:
        super().__init__(name, value)

    def get_inside(self) -> dict[str, BasicType]:
        """
        Get value from Condition.

        It returns:
        >>> {"self": value}

        :return: condition itself mapped to value 
        :rtype: dict[str, BasicType]
        """
        return {"self": self.get_value()}
    
    def set_inside(self, name: str, value: BasicType) -> None:
        """
        Set inside value in Condition.

        Name should be:
        >>> name: str = "self"

        :param name: should be always`"self"`
        :type name: str

        :param value: Value to set
        :type value: BasicType
        """
        if name != "self":
            raise ValueError(f"Other name than {"self"} provided in [set_inside]: {name}")
        
        self.set_value(value)




class ConditionWithArguments(ListOfEquations, Condition):
    """
    Condition in form of List of Equations.

    In Short:
    ```
    name = {
        Equation
        Equation
        ...
    }
    ```
    
    :param name: Name of Condition
    :type name: str

    :param arguments: Equations assigned to Condition
    :type arguments: list[Equation]

    :raises Not Enough Equations: When number of provided Arguments is below 1
    """
    def __init__(self, name: str, arguments: list[Equation]) -> None:
        super().__init__(name, arguments)

    def get_inside(self) -> dict[str, BasicType]:
        """
        Get arguments with corresponding values from Condition.

        :return: Mapping arguments to values
        :rtype: dict[str, BasicType]
        """
        return {equation.get_name(): equation.get_value() for equation in self.get_values()}
    
    def set_inside(self, name: str, value: BasicType) -> None:
        """
        Set inside value in Condition.


        :param name: Name of argument if any in Condition
        :type name: str

        :param value: Value to set
        :type value: BasicType
        """
        self.set_value(name, value)