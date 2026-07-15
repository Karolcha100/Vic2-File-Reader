from abc import ABC, abstractmethod
from typing import ClassVar, Final





class BasicType[T](ABC):
    """
    Abstract base class for any typed literal value in Vic2 script syntax.

    Stores the raw script token and parses it into the concrete type ``T``
    once, at construction time (fail-fast — an invalid token raises immediately
    rather than failing later when the value is read).
    
    :param raw_value: The raw, unparsed string token as it appears in script.
    :type raw_value: str
    """
    
    _type_name: ClassVar[str]

    def __init__(self, raw_value: str) -> None:
        self._raw_value: str = raw_value
        self._parsed_value: T = self._parse(raw_value)

    @abstractmethod
    def _parse(self, raw_value: str) -> T:
        """
        Parse the raw string token into the concrete stored type.

        :param raw_value: The raw string token.
        :type raw_value: str

        :return: The parsed value.
        :rtype: T
        """
        pass

    def set_raw_value(self, raw_value: str) -> None:
        """
        Set raw value inside Type.

        Also Changes the parsed value to corresponding.

        :param raw_value: Raw string value
        :type raw_value: str
        """
        self._raw_value: str = raw_value
        self._parsed_value: T = self._parse(raw_value)

    def get_raw_value(self) -> str:
        """
        Get raw (unparsed) stored value.

        :return: The unparsed, stored value.
        :rtype: str
        """
        return self._raw_value
    
    def get_parsed_value(self) -> T:
        """
        Get parsed stored value.

        :return: The parsed, stored value.
        :rtype: T
        """
        return self._parsed_value
    
    def explain_my_type_name(self) -> str:
        """
        Explaining Type Name if needed.

        :return: Type Name
        :rtype: str
        """
        return self._type_name




class NumericType[T: int|float](BasicType[T]):
    """
    Basic Numeric Type Implementation.

    :param raw_value: unparsed Value stored inside.
    :type raw_value: str
    """
    _type_class: Final[str] = "[Number]"

    def __init__(self, raw_value: str) -> None:
        super().__init__(raw_value)

    @abstractmethod
    def _parse(self, raw_value: str) -> T:
        """
        Parse the raw string token into the concrete stored type.

        :param raw_value: The raw string token.
        :type raw_value: str

        :return: The parsed value.
        :rtype: T
        """
        pass

    def explain_my_type_class(self) -> str:
        """
        Explaining Type Class if needed.

        :return: Type Class
        :rtype: str
        """
        return self._type_class

class StringType(BasicType[str]):
    """
    Basic String Type Implementation.

    :param raw_value: unparsed Value stored inside.
    :type raw_value: str
    """
    _type_class: Final[str] = "[String]"

    def __init__(self, raw_value: str) -> None:
        super().__init__(raw_value)

    def _parse(self, raw_value: str) -> str:
        """
        Parse the raw string token into the concrete stored type.

        :param raw_value: The raw string token.
        :type raw_value: str

        :return: The parsed value.
        :rtype: str
        """
        return raw_value

    def explain_my_type_class(self) -> str:
        """
        Explaining Type Class if needed.

        :return: Type Class
        :rtype: str
        """
        return self._type_class

