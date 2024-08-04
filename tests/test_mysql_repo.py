import pytest
from unittest.mock import patch, MagicMock
from db.mysql_repository import MySQLRepository
from model.lexical_entry import Lexeme

@pytest.fixture
def repository():
    connection_params = {
        'host': 'localhost',
        'user': 'my_user',
        'password': 'my_password',
        'database': 'my_database'
    }
    with patch('mysql.connector.connect'):
        return MySQLRepository(connection_params)

def test_save_and_load_entry(repository):
    mock_conn = patch('mysql.connector.connect').start()
    mock_cursor = MagicMock()
    mock_conn.return_value.cursor.return_value = mock_cursor

    entry = Lexeme(
        base_form="test",
        pos="noun",
        definition="a procedure intended to establish the quality, performance, or reliability of something.",
        synonyms={"exam", "trial"},
        antonyms={"non-test"}
    )

    # Mock the save_entry method
    repository.save_entry(entry)
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO entries (base_form, pos, definition, synonyms, antonyms) VALUES (%s, %s, %s, %s, %s)",
        (entry.base_form, entry.pos, entry.definition, ",".join(entry.synonyms), ",".join(entry.antonyms))
    )
    mock_conn.return_value.commit.assert_called_once()

    # Mock the load_entries method
    mock_cursor.fetchall.return_value = [
        (1, "test", "noun", "a procedure intended to establish the quality, performance, or reliability of something.", "exam,trial", "non-test")
    ]
    entries = repository.load_entries()
    assert len(entries) == 1
    assert entries[0].base_form == "test"

    patch.stopall()

def test_find_entry_by_id(repository):
    mock_conn = patch('mysql.connector.connect').start()
    mock_cursor = MagicMock()
    mock_conn.return_value.cursor.return_value = mock_cursor

    # Mock the find_entry_by_id method
    entry_id = 1
    mock_cursor.fetchone.return_value = (1, "example", "noun", "a sample of something to be imitated or avoided", "sample", "counterexample")
    entry = repository.find_entry_by_id(entry_id)
    assert entry is not None
    assert entry.base_form == "example"

    patch.stopall()
