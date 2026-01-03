CREATE TABLE IF NOT EXISTS Location_Alias (
    location_id INTEGER NOT NULL,
    alias TEXT NOT NULL,
    FOREIGN KEY (location_id) REFERENCES Location_Metadata(id)
);