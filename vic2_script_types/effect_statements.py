from name_statements import Equation, ListOfEquations






class EffectEquation(Equation):
    """
    Effect in form of Equation.

    In Short: 
    ```
    name = value
    ```

    :param name: Name of Effect
    :type name: str

    :param value: Value assigned to Effect
    :type value: str
    """
    def __init__(self, name: str, value: str) -> None:
        super().__init__(name, value)

    

class EffectWithArguments(ListOfEquations):
    """
    Effect in form of List of Equations.

    In Short:
    ```
    name = {
        Equation
        Equation
        ...
    }
    ```
    
    :param name: Name of Effect
    :type name: str

    :param arguments: Equations assigned to Effect
    :type arguments: list[Equation]

    :raises Not Enough Equations: When number of provided Arguments is below 1
    """
    def __init__(self, name: str, arguments: list[Equation]) -> None:
        super().__init__(name, arguments)