"""Database access for the webshop scripts.

Two ways to get a connection to the SQLite database:

* ``connect()``: a context manager. It commits when the ``with`` block ends
  normally, rolls back if an exception occurs, and always closes the
  connection.
* ``get_connection()``: returns a plain connection. The caller must commit
  and close it.

Both enable foreign key enforcement. The database location defaults to
``DBFiles/webshop.db`` next to this script's folder. Set the environment
variable ``WEBSHOP_DB`` to use another file.

Examples:
    from db import connect, get_connection

    with connect() as conn:
        conn.execute("UPDATE products SET stock = ? WHERE product_id = ?", (50, 5))

    conn = get_connection()
    try:
        ...
    finally:
        conn.close()
"""

import os
import sqlite3
from pathlib import Path
from contextlib import contextmanager

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB = PROJECT_ROOT / "DBFiles" / "webshop.db"

DB_PATH = Path(os.environ.get("WEBSHOP_DB", DEFAULT_DB))


def get_connection():
    """Open the webshop database and return the connection.

    Foreign keys are enabled. The caller is responsible for calling
    ``commit()`` after changes and ``close()`` when done.

    Raises:
        FileNotFoundError: if the database file does not exist.
    """
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not found: {DB_PATH}\n"
            "Create it first or set the WEBSHOP_DB environment variable."
        )
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


@contextmanager
def connect():
    """Open the webshop database as a context manager and yield the connection.

    If the block finishes normally, changes are committed; if it raises an
    exception, they are rolled back and the exception is re-raised. The
    connection is always closed at the end.

    Raises:
        FileNotFoundError: if the database file does not exist.
    """
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
