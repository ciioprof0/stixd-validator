import unittest
from app.stixd_classes import (
    PartOfSpeech, Case, Gender, Number, Person, Tense, Mood, Voice, Transitivity, Language,
    LexicalEntry, Word, FiniteVerb, Noun
)

class TestEnumerations(unittest.TestCase):
    def test_part_of_speech_enum(self):
        self.assertEqual(PartOfSpeech.ADJ.value, "ADJ")
        self.assertEqual(PartOfSpeech.NOUN.name, "NOUN")

    def test_case_enum(self):
        self.assertEqual(Case.ACCUSATIVE.value, "accusative")
        self.assertEqual(Case.DATIVE.name, "DATIVE")

    def test_gender_enum(self):
        self.assertEqual(Gender.FEMININE.value, "feminine")
        self.assertEqual(Gender.NEUTER.name, "NEUTER")

    def test_number_enum(self):
        self.assertEqual(Number.SINGULAR.value, "singular")
        self.assertEqual(Number.PLURAL.name, "PLURAL")

    def test_person_enum(self):
        self.assertEqual(Person.FIRST_PERSON.value, "first_person")
        self.assertEqual(Person.THIRD_PERSON.name, "THIRD_PERSON")

    def test_tense_enum(self):
        self.assertEqual(Tense.PRESENT.value, "present")
        self.assertEqual(Tense.FUTURE.name, "FUTURE")

    def test_mood_enum(self):
        self.assertEqual(Mood.INDICATIVE.value, "indicative")
        self.assertEqual(Mood.SUBJUNCTIVE.name, "SUBJUNCTIVE")

    def test_voice_enum(self):
        self.assertEqual(Voice.ACTIVE.value, "active")
        self.assertEqual(Voice.REFLEXIVE.name, "REFLEXIVE")

    def test_transitivity_enum(self):
        self.assertEqual(Transitivity.INTRANSITIVE.value, "intransitive")
        self.assertEqual(Transitivity.DITRANSITIVE3.name, "DITRANSITIVE3")

    def test_language_enum(self):
        self.assertEqual(Language.EN.value, "en")
        self.assertEqual(Language.EN.name, "EN")

class TestLexicalEntry(unittest.TestCase):
    def setUp(self):
        self.synonyms = set()
        self.antonyms = set()
        self.lex_entry = LexicalEntry("run", PartOfSpeech.VERB, "to move swiftly on foot", self.synonyms, self.antonyms)

    def test_lexical_entry_attributes(self):
        self.assertEqual(self.lex_entry.base_form, "run")
        self.assertEqual(self.lex_entry.pos, PartOfSpeech.VERB)
        self.assertEqual(self.lex_entry.definition, "to move swiftly on foot")
        self.assertEqual(self.lex_entry.synonyms, self.synonyms)
        self.assertEqual(self.lex_entry.antonyms, self.antonyms)

class TestWord(unittest.TestCase):
    def setUp(self):
        self.lex_entry = LexicalEntry("run", PartOfSpeech.VERB, "to move swiftly on foot", set(), set())
        self.word = Word(self.lex_entry, "running")

    def test_word_attributes(self):
        self.assertEqual(self.word.lex_entry, self.lex_entry)
        self.assertEqual(self.word.surface_form, "running")

class TestFiniteVerb(unittest.TestCase):
    def setUp(self):
        self.lex_entry = LexicalEntry("run", PartOfSpeech.VERB, "to move swiftly on foot", set(), set())
        self.finite_verb = FiniteVerb(self.lex_entry, "runs", Person.THIRD_PERSON, Number.SINGULAR, Tense.PRESENT, Voice.ACTIVE, Mood.INDICATIVE)

    def test_finite_verb_attributes(self):
        self.assertEqual(self.finite_verb.lex_entry, self.lex_entry)
        self.assertEqual(self.finite_verb.surface_form, "runs")
        self.assertEqual(self.finite_verb.person, Person.THIRD_PERSON)
        self.assertEqual(self.finite_verb.number, Number.SINGULAR)
        self.assertEqual(self.finite_verb.tense, Tense.PRESENT)
        self.assertEqual(self.finite_verb.voice, Voice.ACTIVE)
        self.assertEqual(self.finite_verb.mood, Mood.INDICATIVE)

class TestNoun(unittest.TestCase):
    def setUp(self):
        self.lex_entry = LexicalEntry("dog", PartOfSpeech.NOUN, "a domesticated carnivorous mammal", set(), set())
        self.noun = Noun(self.lex_entry, "dogs", Case.NOMINATIVE, Number.PLURAL, Gender.MASCULINE)

    def test_noun_attributes(self):
        self.assertEqual(self.noun.lex_entry, self.lex_entry)
        self.assertEqual(self.noun.surface_form, "dogs")
        self.assertEqual(self.noun.case, Case.NOMINATIVE)
        self.assertEqual(self.noun.number, Number.PLURAL)
        self.assertEqual(self.noun.gender, Gender.MASCULINE)

if __name__ == "__main__":
    unittest.main()
