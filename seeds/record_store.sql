DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
); 

CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name_artist text,
    genre text
);


INSERT INTO albums (title, release_year, artist_id) VALUES ('Lateralus', 2001, 1);


INSERT INTO artists (name_artist, genre) VALUES ('Tool', 'Rock');
INSERT INTO artists (name_artist, genre) VALUES ('Mastodon', 'Rock');