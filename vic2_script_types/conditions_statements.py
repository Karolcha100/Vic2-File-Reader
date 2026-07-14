from abc import ABC, abstractmethod

from name_statements import Equation, ListOfEquations






class Condition(ABC):
    def __init__(self) -> None:
        pass





class ConditionEquation(Equation):
    """
    Condition in form of Equation.

    In Short: 
    ```
    name = value
    ```

    :param name: Name of Condition
    :type name: str

    :param value: Value assigned to Condition
    :type value: str
    """
    def __init__(self, name: str, value: str) -> None:
        super().__init__(name, value)
    

class ConditionWithArguments(ListOfEquations):
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