CREATE TABLE IF NOT EXISTS Location_Metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    wiki_data TEXT,
    landmarks TEXT
);