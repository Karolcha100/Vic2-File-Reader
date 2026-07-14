from abc import ABC, abstractmethod

from name_statements import Equation, ListOfEquations
from typing.types_basic import BasicType






class Condition(ABC):
    """
    Abstract Condition Statement.
    """
    
    @abstractmethod
    def get_values(self) -> list[]





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