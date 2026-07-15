





class Registry:
    """Mutable, shared store of known identifier values per category (tag, pop_type, culture...).

    A single instance should be shared by reference across the parser, validators,
    and GUI, so that runtime additions or removals are immediately visible everywhere.
    """

    def __init__(self) -> None:
        """Initialize an empty registry with no registered categories or values."""
        self._categories: dict[str, set[str]] = {}

    def register(self, category: str, value: str) -> None:
        """Add a new valid value to the given category.

        :param category: The registry category (e.g. ``"tag"``, ``"pop_type"``).
        :type category: str
        :param value: The value to register as valid within that category.
        :type value: str
        :return: None
        :rtype: None
        """
        self._categories.setdefault(category, set()).add(value)

    def unregister(self, category: str, value: str) -> None:
        """Remove a previously registered value from the given category.

        :param category: The registry category to remove the value from.
        :type category: str
        :param value: The value to remove.
        :type value: str
        :return: None
        :rtype: None
        :raises KeyError: If the category does not exist, or the value is not
            currently registered within it.
        """
        if category not in self._categories or value not in self._categories[category]:
            raise KeyError(f"Value {value!s} is not registered under category {category!s}")
        self._categories[category].remove(value)

    def contains(self, category: str, value: str) -> bool:
        """Check whether ``value`` is currently a valid member of ``category``.

        :param category: The registry category to check.
        :type category: str
        :param value: The value to look up.
        :type value: str
        :return: ``True`` if the value is registered under the category, ``False`` otherwise.
        :rtype: bool
        """
        return value in self._categories.get(category, set())

    def list_values(self, category: str) -> frozenset[str]:
        """Return all currently known values in the given category.

        :param category: The registry category to list.
        :type category: str
        :return: An immutable snapshot of the currently registered values.
        :rtype: frozenset[str]
        """
        return frozenset(self._categories.get(category, set()))