# tests/test_mysql_repo.py

import pytest
from db.mysql_repository import MySQLRepository
from model.lexical_entry import Lexeme

@pytest.fixture
def repository():
    return MySQLRepository(host='localhost', user='my_user', password='my_password', database='my_database')

def test_save_and_load_entry(repository):
    entry = Lexeme(
        base_form="test",
        pos="noun",
        definition="a procedure intended to establish the quality, performance, or reliability of something.",
        synonyms={"exam", "trial"},
        antonyms={"non-test"},
        lang="en"
    )
    repository.save_entry(entry)
    entries = repository.load_entries()
    assert entry in entries

def test_find_entry_by_id(repository):
    entry_id = 1
    entry = repository.find_entry_by_id(entry_id)
    assert entry is not None
    assert entry.base_form == "example"
