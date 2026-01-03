CREATE TABLE IF NOT EXISTS Graphics (
    location_id INTEGER NOT NULL,
    season TEXT NOT NULL,
    condition TEXT NOT NULL,
    image BLOB,
    FOREIGN KEY (location_id) REFERENCES Location_Metadata(id)
)