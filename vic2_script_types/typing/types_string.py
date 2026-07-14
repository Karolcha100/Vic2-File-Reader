from typing import ClassVar

from types_basic import StringType





class BoolType(StringType):
    """
    Boolean Type Implementation.

    :param raw_value: unparsed Value stored inside.
    :type raw_value: str
    """

    _type_name: ClassVar[str] = "[yes/no]"
    
    def __init__(self, raw_value: str) -> None:
        super().__init__(raw_value)


class TagType(StringType):
    """
    Tag Type Implementation.

    :param raw_value: unparsed Value stored inside.
    :type raw_value: str
    """

    _type_name: ClassVar[str] = "[TAG]"

    def __init__(self, raw_value: str) -> None:
        super().__init__(raw_value)


class PopType(StringType):
    """
    Pop Type Implementation.

    :param raw_value: unparsed Value stored inside.
    :type raw_value: str
    """

    _type_name: ClassVar[str] = "[poptype]"

    def __init__(self, raw_value: str) -> None:
        super().__init__(raw_value)