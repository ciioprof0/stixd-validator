from enum import Enum

# Common Enumerations
class Language(Enum):
    """Enumeration for Languages."""
    EN = "en"
    # More languages can be added here

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

# Noun Enumerations
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

# Verb Enumerations
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