from model.lexical_entry import Lexeme


class Word:
    """
    A class to represent a word.

    Attributes:
        lex_entry (Lexeme): The lexical entry.
        surface_form (str): The surface form of the word.
    """

    def __init__(self, lex_entry: Lexeme, surface_form: str) -> None:
        """
        Constructs all the necessary attributes for the word object.

        Args:
            lex_entry (Lexeme): The lexical entry.
            surface_form (str): The surface form of the word.
        """
        self.lex_entry = lex_entry
        self.surface_form = surface_form