from abc import ABC, abstractmethod





class ScriptNode(ABC):
    """
    Common interface for all AST nodes participating in round-trip
    script serialization.
    """

    @abstractmethod
    def to_script(self, depth: int) -> str:
        """
        Serialize this node back into its Victoria 2 script representation.

        :return: The script-formatted string for this node.
        :rtype: str
        """
        ...