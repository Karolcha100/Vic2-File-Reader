from typing import ClassVar

from types_basic import NumericType






class IntType(NumericType[int]):
    """
    Integer Type Implementation.

    :param raw_value: unparsed Value stored inside.
    :type raw_value: str
    """
    _type_name: ClassVar[str] = "[int]"

    def __init__(self, raw_value: str) -> None:
        super().__init__(raw_value)

    def _parse(self, raw_value: str) -> int:
        """
        Parse the raw string token into the concrete stored type.

        String should be Integer.

        :param raw_value: The raw string token.
        :type raw_value: str

        :return: The parsed value.
        :rtype: int
        """
        return int(raw_value)


class FloatType(NumericType[float]):
    """
    Float Type Implementation.

    Note that game implements float precision to 3 decimals.

    :param raw_value: unparsed Value stored inside.
    :type raw_value: str
    """
    _type_name: ClassVar[str] = "[float]"

    def __init__(self, raw_value: str) -> None:
        super().__init__(raw_value)

    def _parse(self, raw_value: str) -> float:
        """
        Parse the raw string token into the concrete stored type.

        String Should be float

        :param raw_value: The raw string token.
        :type raw_value: str

        :return: The parsed value.
        :rtype: float
        """
        return float(raw_value)


class Percent(NumericType):
    """
    Percent Type Implementation.

    String Should be integer (from 0 to 100)

    :param raw_value: unparsed Value stored inside.
    :type raw_value: str
    """
    _type_name: ClassVar[str] = "[percent]"

    def __init__(self, raw_value: str) -> None:
        super().__init__(raw_value)

    def _parse(self, raw_value: str) -> int:
        """
        Parse the raw string token into the concrete stored type.

        :param raw_value: The raw string token.
        :type raw_value: str

        :return: The parsed value.
        :rtype: int
        """
        return int(raw_value)