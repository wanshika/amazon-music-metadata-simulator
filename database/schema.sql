-- Artists Table
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(5)
);

-- Tracks Table
CREATE TABLE IF NOT EXISTS tracks (
    track_id VARCHAR(10) PRIMARY KEY,
    title VARCHAR(100),
    duration_sec INT,
    genre VARCHAR(50),
    artist_id VARCHAR(10),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

-- Rights Table
CREATE TABLE IF NOT EXISTS rights (
    rights_id VARCHAR(10) PRIMARY KEY,
    track_id VARCHAR(10),
    owner_name VARCHAR(100),
    valid_from DATE,
    valid_to DATE,
    FOREIGN KEY (track_id) REFERENCES tracks(track_id)
);
