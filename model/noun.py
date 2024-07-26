from model.enums import *
from model.lexical_entry import Lexeme
from model.word import Word


class Noun(Word):
    """
    A class to represent a noun.

    Attributes:
        lex_entry (Lexeme): The lexical entry.
        surface_form (str): The surface form of the word.
        case (Case): The grammatical case.
        number (Number): The grammatical number.
        gender (Gender): The grammatical gender.
    """

    def __init__(
        self,
        lex_entry: Lexeme,
        surface_form: str,
        case: Case,
        number: Number,
        gender: Gender
    ) -> None:
        """
        Constructs all the necessary attributes for the noun object.

        Args:
            lex_entry (Lexeme): The lexical entry.
            surface_form (str): The surface form of the word.
            case (Case): The grammatical case.
            number (Number): The grammatical number.
            gender (Gender): The grammatical gender.
        """
        super().__init__(lex_entry, surface_form)
        self.case = case
        self.number = number
        self.gender = gender