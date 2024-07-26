from model.enums import *
from model.word import Word
from model.lexical_entry import Lexeme


class FiniteVerb(Word):
    """
    A class to represent a finite verb.

    Attributes:
        lex_entry (Lexeme): The lexical entry.
        surface_form (str): The surface form of the word.
        person (Person): The grammatical person.
        number (Number): The grammatical number.
        tense (Tense): The tense.
        voice (Voice): The voice.
        mood (Mood): The mood.
    """

    def __init__(
        self,
        lex_entry: Lexeme,
        surface_form: str,
        person: Person,
        number: Number,
        tense: Tense,
        voice: Voice,
        mood: Mood
    ) -> None:
        """
        Constructs all the necessary attributes for the finite verb object.

        Args:
            lex_entry (Lexeme): The lexical entry.
            surface_form (str): The surface form of the word.
            person (Person): The grammatical person.
            number (Number): The grammatical number.
            tense (Tense): The tense.
            voice (Voice): The voice.
            mood (Mood): The mood.
        """
        super().__init__(lex_entry, surface_form)
        self.person = person
        self.number = number
        self.tense = tense
        self.voice = voice
        self.mood = mood