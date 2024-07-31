# tests/test_classes.py

import pytest
from model.enums import *
from model.lexical_entry import Lexeme
from model.noun import Noun
from model.verb import FiniteVerb
from model.word import Word
from model.corpus import Corpus

class TestEnumerations:
    def test_part_of_speech_enum(self):
        assert PartOfSpeech.ADJ.value == "ADJ"
        assert PartOfSpeech.NOUN.name == "NOUN"

    def test_case_enum(self):
        assert Case.ACCUSATIVE.value == "accusative"
        assert Case.DATIVE.name == "DATIVE"

    def test_gender_enum(self):
        assert Gender.FEMININE.value == "feminine"
        assert Gender.NEUTER.name == "NEUTER"

    def test_number_enum(self):
        assert Number.SINGULAR.value == "singular"
        assert Number.PLURAL.name == "PLURAL"

    def test_person_enum(self):
        assert Person.FIRST_PERSON.value == "first_person"
        assert Person.THIRD_PERSON.name == "THIRD_PERSON"

    def test_tense_enum(self):
        assert Tense.PRESENT.value == "present"
        assert Tense.FUTURE.name == "FUTURE"

    def test_mood_enum(self):
        assert Mood.INDICATIVE.value == "indicative"
        assert Mood.SUBJUNCTIVE.name == "SUBJUNCTIVE"

    def test_voice_enum(self):
        assert Voice.ACTIVE.value == "active"
        assert Voice.REFLEXIVE.name == "REFLEXIVE"

    def test_transitivity_enum(self):
        assert Transitivity.INTRANSITIVE.value == "intransitive"
        assert Transitivity.DITRANSITIVE3.name == "DITRANSITIVE3"

    def test_language_enum(self):
        assert Language.EN.value == "en"
        assert Language.EN.name == "EN"

class TestLexeme:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.base_form = "run"
        self.pos = PartOfSpeech.VERB
        self.definition = "to move swiftly on foot"
        self.synonyms = set()
        self.antonyms = set()
        self.lex_entry = Lexeme(self.base_form, self.pos, self.definition, self.synonyms, self.antonyms)

    def test_lexical_entry_attributes(self):
        assert self.lex_entry.base_form == self.base_form
        assert self.lex_entry.pos == self.pos
        assert self.lex_entry.definition == self.definition
        assert self.lex_entry.synonyms == self.synonyms
        assert self.lex_entry.antonyms == self.antonyms

class TestWord:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.base_form = "run"
        self.pos = PartOfSpeech.VERB
        self.definition = "to move swiftly on foot"
        self.lex_entry = Lexeme(self.base_form, self.pos, self.definition, set(), set())
        self.surface_form = "running"
        self.word = Word(self.lex_entry, self.surface_form)

    def test_word_attributes(self):
        assert self.word.lex_entry == self.lex_entry
        assert self.word.surface_form == self.surface_form

class TestFiniteVerb:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.base_form = "run"
        self.pos = PartOfSpeech.VERB
        self.definition = "to move swiftly on foot"
        self.lex_entry = Lexeme(self.base_form, self.pos, self.definition, set(), set())
        self.surface_form = "runs"
        self.person = Person.THIRD_PERSON
        self.number = Number.SINGULAR
        self.tense = Tense.PRESENT
        self.voice = Voice.ACTIVE
        self.mood = Mood.INDICATIVE
        self.finite_verb = FiniteVerb(self.lex_entry, self.surface_form, self.person, self.number, self.tense, self.voice, self.mood)

    def test_finite_verb_attributes(self):
        assert self.finite_verb.lex_entry == self.lex_entry
        assert self.finite_verb.surface_form == self.surface_form
        assert self.finite_verb.person == self.person
        assert self.finite_verb.number == self.number
        assert self.finite_verb.tense == self.tense
        assert self.finite_verb.voice == self.voice
        assert self.finite_verb.mood == self.mood

class TestNoun:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.base_form = "dog"
        self.pos = PartOfSpeech.NOUN
        self.definition = "a domesticated carnivorous mammal"
        self.lex_entry = Lexeme(self.base_form, self.pos, self.definition, set(), set())
        self.surface_form = "dogs"
        self.case = Case.NOMINATIVE
        self.number = Number.PLURAL
        self.gender = Gender.MASCULINE
        self.noun = Noun(self.lex_entry, self.surface_form, self.case, self.number, self.gender)

    def test_noun_attributes(self):
        assert self.noun.lex_entry == self.lex_entry
        assert self.noun.surface_form == self.surface_form
        assert self.noun.case == self.case
        assert self.noun.number == self.number
        assert self.noun.gender == self.gender

class TestCorpus:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = "http://example.com"
        self.page_hash = "abc123"
        self.text = "This is a test text."
        self.metadata = {"author": "John Doe"}
        self.date_scraped = "2024-01-01 12:00:00"
        self.tokens = ["This", "is", "a", "test", "text"]
        self.pos_tags = {"This": "DET", "is": "VERB", "a": "DET", "test": "NOUN", "text": "NOUN"}
        self.named_entities = {"John Doe": "PERSON"}
        self.processed_text = "this is a test text"
        self.lemmas = ["this", "be", "a", "test", "text"]
        self.vocabulary = {"this", "be", "a", "test", "text"}
        self.sentiment = {"polarity": 0.0, "subjectivity": 0.0}
        self.keywords = ["test", "text"]

        self.corpus_entry = Corpus(
            url=self.url,
            page_hash=self.page_hash,
            text=self.text,
            metadata=self.metadata,
            date_scraped=self.date_scraped,
            tokens=self.tokens,
            pos_tags=self.pos_tags,
            named_entities=self.named_entities,
            processed_text=self.processed_text,
            lemmas=self.lemmas,
            vocabulary=self.vocabulary,
            sentiment=self.sentiment,
            keywords=self.keywords
        )

    def test_corpus_attributes(self):
        assert self.corpus_entry.url == self.url
        assert self.corpus_entry.page_hash == self.page_hash
        assert self.corpus_entry.text == self.text
        assert self.corpus_entry.metadata == self.metadata
        assert self.corpus_entry.date_scraped == self.date_scraped
        assert self.corpus_entry.tokens == self.tokens
        assert self.corpus_entry.pos_tags == self.pos_tags
  
