from abc import ABC, abstractmethod
from vic2_script_manegement.typing.registries import Registry






class Domain[T](ABC):
    """
    Describes the set of raw values considered valid for a specific script field.
    """

    @abstractmethod
    def is_valid(self, value: T) -> bool:
        """
        Checks if value is valid.

        :param value: value to check
        :type value: T

        :return: If value is in Domain
        :rtype: bool
        """
        pass


class RangeDomain[T: float|int](Domain[T]):
    """
    Numeric range domain, specific to a single field (e.g. literacy: 0.0-1.0).

    :param lower: Lower Bound
    :type lower: float

    :param upper: Upper Bound
    :type upper: float
    """
    def __init__(self, lower: T, upper: T) -> None:
        self._lower: T = lower
        self._upper: T = upper

    def is_valid(self, value: T) -> bool:
        """
        Checks if value in bounds.

        :param value: raw (unparsed) value
        :type value: T

        :return: If value is in Domain
        :rtype: bool
        """
        return self._lower <= value <= self._upper


class RegistryDomain(Domain[str]):
    """
    Domain resolved dynamically against a runtime-loaded game/mod data registry.

    Used for fields whose valid values (e.g. TAGs, pop types) depend on the
    currently loaded mod rather than being fixed in code.

    :param category: Registry category to check membership against (e.g. ``"tag"``).
    :type category: str

    :param registry: Shared registry populated from loaded game/mod files.
    :type registry: Registry
    """

    def __init__(self, category: str, registry: Registry) -> None:
        self._category: str = category
        self._registry: Registry = registry

    def is_valid(self, value: str) -> bool:
        """
        Checks if value is valid.

        :param value: value to check
        :type value: str

        :return: If value is in Domain
        :rtype: bool
        """
        return self._registry.contains(self._category, value)