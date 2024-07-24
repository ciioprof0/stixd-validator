from typing import Any, Dict, List, Optional, Set
import mysql.connector
from db.repository import *


class MySQLRepository(AbstractRepository):

    def __init__(self, connection_params):
        self.connection_params = connection_params

    def _connect(self):
        return mysql.connector.connect(**self.connection_params)

    def load_entries(self) -> List:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM entries")
        rows = cursor.fetchall()
        conn.close()
        return [self._map_row_to_entry(row) for row in rows]

    def save_entry(self, entry) -> None:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO entries (field1, field2) VALUES (%s, %s)",
            (entry.field1, entry.field2)
        )
        conn.commit()
        conn.close()

    def find_entry_by_id(self, entry_id: int):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM entries WHERE id = %s", (entry_id,))
        row = cursor.fetchone()
        conn.close()
        return self._map_row_to_entry(row)

    def _map_row_to_entry(self, row):
        # Map a database row to an entry object
        pass