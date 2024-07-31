from typing import Any, Dict, List, Optional, Set
import mysql.connector
from db.repository import AbstractRepository
from model.lexical_entry import Lexeme

class MySQLRepository(AbstractRepository):

    def __init__(self, connection_params):
        self.connection_params = connection_params

    def _connect(self):
        return mysql.connector.connect(**self.connection_params)

    def load_entries(self) -> List[Lexeme]:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM entries")
        rows = cursor.fetchall()
        conn.close()
        return [self._map_row_to_entry(row) for row in rows]

    def save_entry(self, entry: Lexeme) -> None:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO entries (base_form, pos, definition, synonyms, antonyms) VALUES (%s, %s, %s, %s, %s)",
            (entry.base_form, entry.pos, entry.definition, ",".join(entry.synonyms), ",".join(entry.antonyms))
        )
        conn.commit()
        conn.close()

    def find_entry_by_id(self, entry_id: int) -> Optional[Lexeme]:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM entries WHERE id = %s", (entry_id,))
        row = cursor.fetchone()
        conn.close()
        return self._map_row_to_entry(row) if row else None

    def _map_row_to_entry(self, row) -> Lexeme:
        if not row:
            return None
        id, base_form, pos, definition, synonyms, antonyms = row
        return Lexeme(
            base_form=base_form,
            pos=pos,
            definition=definition,
            synonyms=set(synonyms.split(",")),
            antonyms=set(antonyms.split(","))
        )
