from vic2_script_manegement.typing.types_basic import BasicType
from vic2_script_manegement.typing.domains import Domain






class TypingValidator:
    """Associates a specific script keyword with its expected literal type and domain.

    :param keyword: The script keyword, e.g. ``"militancy"`` or ``"primary_culture"``.
    :type keyword: str

    :param value_type: The BasicType subclass expected for this field.
    :type value_type: type[BasicType]

    :param domain: The domain used to validate raw values for this field.
    :type domain: Domain
    """

    def __init__(self, keyword: str, value_type: type[BasicType], domain: Domain) -> None:
        self.keyword: str = keyword
        self.value_type: type[BasicType] = value_type
        self.domain: Domain = domain

    def validate_value(self, value: BasicType) -> bool:
        """
        Check whether a value satisfies its field schema.
        
        :param value: value to check
        :type value: BasicType
        """
        if not isinstance(value, self.value_type):
            return False
        return self.domain.is_valid(value.get_raw_value())

    def __str__(self) -> str:
        return self.keyword