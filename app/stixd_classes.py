from enum import Enum
from typing import Set, Optional, List, Dict, Any

# Enumerations Classes
class PartOfSpeech(Enum):
    """Enumeration for coarse Universal POS Tag Set."""
    ADJ = "ADJ"
    ADP = "ADP"
    ADV = "ADV"
    CONJ = "CONJ"
    DET = "DET"
    INTJ = "INTJ"
    NOUN = "NOUN"
    NUM = "NUM"
    VERB = "VERB"
    PRON = "PRON"
    PRT = "PRT"
    PUNCT = "PUNCT"
    X = "Other"

class Case(Enum):
    """Enumeration for Noun Cases."""
    ACCUSATIVE = "accusative"
    ABLATIVE = "ablative"
    NOMINATIVE = "nominative"
    DATIVE = "dative"
    LOCATIVE = "locative"
    INSTRUMENTAL = "instrumental"

class Gender(Enum):
    """Enumeration for Noun Genders."""
    FEMININE = "feminine"
    MASCULINE = "masculine"
    NEUTER = "neuter"

class Number(Enum):
    """Enumeration for Numbers."""
    SINGULAR = "singular"
    PLURAL = "plural"
    DUAL = "dual"

class Person(Enum):
    """Enumeration for Persons."""
    FIRST_PERSON = "first_person"
    SECOND_PERSON = "second_person"
    THIRD_PERSON = "third_person"

class Tense(Enum):
    """Enumeration for Verb Tenses."""
    PRESENT = "present"
    PAST = "past"
    FUTURE = "future"

class Mood(Enum):
    """Enumeration for Verb Moods."""
    INDICATIVE = "indicative"
    IMPERATIVE = "imperative"
    SUBJUNCTIVE = "subjunctive"
    CONDITIONAL = "conditional"

class Voice(Enum):
    """Enumeration for Verb Voices."""
    ACTIVE = "active"
    PASSIVE = "passive"
    MIDDLE = "middle"
    CAUSATIVE = "causative"
    REFLEXIVE = "reflexive"

class Transitivity(Enum):
    """Enumeration for Verb Transitivity."""
    INTRANSITIVE = "intransitive"
    TRANSITIVE1 = "transitive1"
    TRANSITIVE2 = "transitive2"
    DITRANSITIVE1 = "ditransitive1"
    DITRANSITIVE2 = "ditransitive2"
    DITRANSITIVE3 = "ditransitive3"
    DITRANSITIVE4 = "ditransitive4"

class Language(Enum):
    """Enumeration for Languages."""
    EN = "en"
    # More languages can be added here

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

class Word:
    """
    A class to represent a word.

    Attributes:
        lex_entry (LexicalEntry): The lexical entry.
        surface_form (str): The surface form of the word.
    """

    def __init__(self, lex_entry: LexicalEntry, surface_form: str) -> None:
        """
        Constructs all the necessary attributes for the word object.

        Args:
            lex_entry (LexicalEntry): The lexical entry.
            surface_form (str): The surface form of the word.
        """
        self.lex_entry = lex_entry
        self.surface_form = surface_form

class FiniteVerb(Word):
    """
    A class to represent a finite verb.

    Attributes:
        lex_entry (LexicalEntry): The lexical entry.
        surface_form (str): The surface form of the word.
        person (Person): The grammatical person.
        number (Number): The grammatical number.
        tense (Tense): The tense.
        voice (Voice): The voice.
        mood (Mood): The mood.
    """

    def __init__(
        self,
        lex_entry: LexicalEntry,
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
            lex_entry (LexicalEntry): The lexical entry.
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

class Noun(Word):
    """
    A class to represent a noun.

    Attributes:
        lex_entry (LexicalEntry): The lexical entry.
        surface_form (str): The surface form of the word.
        case (Case): The grammatical case.
        number (Number): The grammatical number.
        gender (Gender): The grammatical gender.
    """

    def __init__(
        self,
        lex_entry: LexicalEntry,
        surface_form: str,
        case: Case,
        number: Number,
        gender: Gender
    ) -> None:
        """
        Constructs all the necessary attributes for the noun object.

        Args:
            lex_entry (LexicalEntry): The lexical entry.
            surface_form (str): The surface form of the word.
            case (Case): The grammatical case.
            number (Number): The grammatical number.
            gender (Gender): The grammatical gender.
        """
        super().__init__(lex_entry, surface_form)
        self.case = case
        self.number = number
        self.gender = gender

class Corpus:
    """
    A class to represent a corpus entry.

    Attributes:
        url (str): The URL from which the data was scraped.
        page_hash (str): The hash of the page content.
        text (str): The raw scraped text.
        metadata (Optional[Dict[str, Any]]): Additional metadata.
        date_scraped (str): The date when the data was scraped.
        tokens (Optional[List[str]]): Tokenized text.
        pos_tags (Optional[Dict[str, str]]): POS tags for the tokens.
        named_entities (Optional[Dict[str, str]]): Named entities.
        processed_text (Optional[str]): Cleaned and preprocessed text.
        lemmas (Optional[List[str]]): Lemmatized text.
        vocabulary (Optional[Set[str]]): Unique set of words.
        sentiment (Optional[Dict[str, Any]]): Sentiment analysis results.
        keywords (Optional[List[str]]): Extracted keywords or key phrases.
    """

    def __init__(
        self,
        url: str,
        page_hash: str,
        text: str,
        metadata: Optional[Dict[str, Any]] = None,
        date_scraped: Optional[str] = None,
        tokens: Optional[List[str]] = None,
        pos_tags: Optional[Dict[str, str]] = None,
        named_entities: Optional[Dict[str, str]] = None,
        processed_text: Optional[str] = None,
        lemmas: Optional[List[str]] = None,
        vocabulary: Optional[Set[str]] = None,
        sentiment: Optional[Dict[str, Any]] = None,
        keywords: Optional[List[str]] = None
    ) -> None:
        """
        Constructs all the necessary attributes for the corpus object.

        Args:
            url (str): The URL from which the data was scraped.
            page_hash (str): The hash of the page content.
            text (str): The raw scraped text.
            metadata (Optional[Dict[str, Any]]): Additional metadata.
            date_scraped (Optional[str]): The date when the data was scraped.
            tokens (Optional[List[str]]): Tokenized text.
            pos_tags (Optional[Dict[str, str]]): POS tags for the tokens.
            named_entities (Optional[Dict[str, str]]): Named entities.
            processed_text (Optional[str]): Cleaned and preprocessed text.
            lemmas (Optional[List[str]]): Lemmatized text.
            vocabulary (Optional[Set[str]]): Unique set of words.
            sentiment (Optional[Dict[str, Any]]): Sentiment analysis results.
            keywords (Optional[List[str]]): Extracted keywords or key phrases.
        """
        self.url = url
        self.page_hash = page_hash
        self.text = text
        self.metadata = metadata
        self.date_scraped = date_scraped
        self.tokens = tokens
        self.pos_tags = pos_tags
        self.named_entities = named_entities
        self.processed_text = processed_text
        self.lemmas = lemmas
        self.vocabulary = vocabulary
        self.sentiment = sentiment
        self.keywords = keywords
