import unittest
from app.stixd_classes import (
    PartOfSpeech, Case, Gender, Number, Person, Tense, Mood, Voice, Transitivity, Language,
    LexicalEntry, Word, FiniteVerb, Noun, Corpus
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
        self.base_form = "run"
        self.pos = PartOfSpeech.VERB
        self.definition = "to move swiftly on foot"
        self.synonyms = set()
        self.antonyms = set()
        self.lex_entry = LexicalEntry(self.base_form, self.pos, self.definition, self.synonyms, self.antonyms)

    def test_lexical_entry_attributes(self):
        self.assertEqual(self.lex_entry.base_form, self.base_form)
        self.assertEqual(self.lex_entry.pos, self.pos)
        self.assertEqual(self.lex_entry.definition, self.definition)
        self.assertEqual(self.lex_entry.synonyms, self.synonyms)
        self.assertEqual(self.lex_entry.antonyms, self.antonyms)

class TestWord(unittest.TestCase):
    def setUp(self):
        self.base_form = "run"
        self.pos = PartOfSpeech.VERB
        self.definition = "to move swiftly on foot"
        self.lex_entry = LexicalEntry(self.base_form, self.pos, self.definition, set(), set())
        self.surface_form = "running"
        self.word = Word(self.lex_entry, self.surface_form)

    def test_word_attributes(self):
        self.assertEqual(self.word.lex_entry, self.lex_entry)
        self.assertEqual(self.word.surface_form, self.surface_form)

class TestFiniteVerb(unittest.TestCase):
    def setUp(self):
        self.base_form = "run"
        self.pos = PartOfSpeech.VERB
        self.definition = "to move swiftly on foot"
        self.lex_entry = LexicalEntry(self.base_form, self.pos, self.definition, set(), set())
        self.surface_form = "runs"
        self.person = Person.THIRD_PERSON
        self.number = Number.SINGULAR
        self.tense = Tense.PRESENT
        self.voice = Voice.ACTIVE
        self.mood = Mood.INDICATIVE
        self.finite_verb = FiniteVerb(self.lex_entry, self.surface_form, self.person, self.number, self.tense, self.voice, self.mood)

    def test_finite_verb_attributes(self):
        self.assertEqual(self.finite_verb.lex_entry, self.lex_entry)
        self.assertEqual(self.finite_verb.surface_form, self.surface_form)
        self.assertEqual(self.finite_verb.person, self.person)
        self.assertEqual(self.finite_verb.number, self.number)
        self.assertEqual(self.finite_verb.tense, self.tense)
        self.assertEqual(self.finite_verb.voice, self.voice)
        self.assertEqual(self.finite_verb.mood, self.mood)

class TestNoun(unittest.TestCase):
    def setUp(self):
        self.base_form = "dog"
        self.pos = PartOfSpeech.NOUN
        self.definition = "a domesticated carnivorous mammal"
        self.lex_entry = LexicalEntry(self.base_form, self.pos, self.definition, set(), set())
        self.surface_form = "dogs"
        self.case = Case.NOMINATIVE
        self.number = Number.PLURAL
        self.gender = Gender.MASCULINE
        self.noun = Noun(self.lex_entry, self.surface_form, self.case, self.number, self.gender)

    def test_noun_attributes(self):
        self.assertEqual(self.noun.lex_entry, self.lex_entry)
        self.assertEqual(self.noun.surface_form, self.surface_form)
        self.assertEqual(self.noun.case, self.case)
        self.assertEqual(self.noun.number, self.number)
        self.assertEqual(self.noun.gender, self.gender)

class TestCorpus(unittest.TestCase):
    def setUp(self):
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
        self.assertEqual(self.corpus_entry.url, self.url)
        self.assertEqual(self.corpus_entry.page_hash, self.page_hash)
        self.assertEqual(self.corpus_entry.text, self.text)
        self.assertEqual(self.corpus_entry.metadata, self.metadata)
        self.assertEqual(self.corpus_entry.date_scraped, self.date_scraped)
        self.assertEqual(self.corpus_entry.tokens, self.tokens)
        self.assertEqual(self.corpus_entry.pos_tags, self.pos_tags)
        self.assertEqual(self.corpus_entry.named_entities, self.named_entities)
        self.assertEqual(self.corpus_entry.processed_text, self.processed_text)
        self.assertEqual(self.corpus_entry.lemmas, self.lemmas)
        self.assertEqual(self.corpus_entry.vocabulary, self.vocabulary)
        self.assertEqual(self.corpus_entry.sentiment, self.sentiment)
        self.assertEqual(self.corpus_entry.keywords, self.keywords)

if __name__ == "__main__":
    unittest.main()

