from __future__ import annotations
from curses import qiflush
from sqlalchemy import text
from database import engine

def run_sql(query: str):
    with engine.begin() as conn:
        result = conn.execute(text(query))
        return result.fetchall() if result.returns_rows else result.rowcount

# query = """INSERT INTO appointments (patient_name, reason, preferred_time, canceled, created_at) VALUES ('John Doe', 'checkup', '2026-01-24 14:30:00', 0, datetime('now'))"""
query = """SELECT * FROM appointments"""
print(run_sql(query))