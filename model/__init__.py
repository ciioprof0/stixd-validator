# model/__init__.py

from .corpus import Corpus
from .enums import Language, Number, Person, PartOfSpeech
from .enums import Case, Gender, Tense, Mood, Transitivity, Voice
from .lexical_entry import LexicalEntry
from .noun import Noun
from .verb import FiniteVerb
from .word import Word

__all__ = [
    "Corpus",
    "Language",
    "Number",
    "Person",
    "PartOfSpeech",
    "Case",
    "Gender",
    "Tense",
    "Mood",
    "Transitivity",
    "Voice",
    "LexicalEntry",
    "Noun",
    "FiniteVerb",
    "Word"
]