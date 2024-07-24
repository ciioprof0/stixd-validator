from model.enums import *


class LexicalEntry:
    """
    A class to represent a lexical entry.

    Attributes:
        base_form (str): The base form of the lexical entry.
        pos (PartOfSpeech): The part of speech.
        definition (str): The definition of the lexical entry.
        synonyms (Set[LexicalEntry]): A set of synonyms.
        antonyms (Set[LexicalEntry]): A set of antonyms.
    """

    def __init__(self, base_form: str, pos: PartOfSpeech, definition: str, synonyms: Set['LexicalEntry'], antonyms: Set['LexicalEntry']) -> None:
        """
        Constructs all the necessary attributes for the lexical entry object.

        Args:
            base_form (str): The base form of the lexical entry.
            pos (PartOfSpeech): The part of speech.
            definition (str): The definition of the lexical entry.
            synonyms (Set[LexicalEntry]): A set of synonyms.
            antonyms (Set[LexicalEntry]): A set of antonyms.
        """
        self.base_form = base_form
        self.pos = pos
        self.definition = definition
        self.synonyms = synonyms
        self.antonyms = antonyms