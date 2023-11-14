import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_events (
    artist          VARCHAR,
    auth            VARCHAR,
    firstName       VARCHAR,
    gender          VARCHAR,
    itemInSession   INTEGER,
    lastName        VARCHAR,
    length          FLOAT,
    level           VARCHAR,
    location        VARCHAR,
    method          VARCHAR,
    page            VARCHAR,
    registration    FLOAT,
    sessionId       INTEGER,
    song            VARCHAR,
    status          INTEGER,
    ts              TIMESTAMP,
    userAgent       VARCHAR,
    userId          INTEGER
)
""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs (
    num_songs        INTEGER,
    artist_id        VARCHAR,
    artist_latitude  DECIMAL(9,6),
    artist_longitude DECIMAL(9,6),
    artist_location  VARCHAR(MAX),
    artist_name      VARCHAR(MAX),
    song_id          VARCHAR,
    title            VARCHAR(MAX),
    duration         FLOAT,
    year             INTEGER
)
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id     INTEGER IDENTITY(0,1) PRIMARY KEY,
    start_time      TIMESTAMP,
    user_id         INTEGER,
    level           VARCHAR,
    song_id         VARCHAR,
    artist_id       VARCHAR,
    session_id      INTEGER,
    location        VARCHAR(MAX),
    user_agent      VARCHAR(MAX)
)
DISTSTYLE EVEN;
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id     INTEGER PRIMARY KEY,
    first_name  VARCHAR,
    last_name   VARCHAR,
    gender      VARCHAR,
    level       VARCHAR
)
DISTSTYLE ALL;
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id     VARCHAR PRIMARY KEY,
    title       VARCHAR,
    artist_id   VARCHAR,
    year        INTEGER,
    duration    FLOAT
)
DISTSTYLE ALL;
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id   VARCHAR PRIMARY KEY,
    name        VARCHAR,
    location    VARCHAR,
    latitude    DECIMAL(9,6),
    longitude   DECIMAL(9,6)
)
DISTSTYLE ALL;
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time  TIMESTAMP PRIMARY KEY,
    hour        INTEGER,
    day         INTEGER,
    week        INTEGER,
    month       INTEGER,
    year        INTEGER,
    weekday     VARCHAR
)
DISTSTYLE ALL;
""")

# STAGING TABLES

staging_events_copy = ("""
COPY staging_events FROM {}
CREDENTIALS 'aws_iam_role={}'
JSON {}
REGION 'us-west-2'
TIMEFORMAT as 'epochmillisecs';
""").format(config.get("S3", "LOG_DATA"), config.get("IAM_ROLE", "ARN"), config.get("S3", "LOG_JSONPATH"))

staging_songs_copy = ("""
COPY staging_songs FROM {}
CREDENTIALS 'aws_iam_role={}'
JSON 'auto'
REGION 'us-west-2';
""").format(config.get("S3", "SONG_DATA"), config.get("IAM_ROLE", "ARN"))

# FINAL TABLES

songplay_table_insert = ("""
INSERT INTO songplays (
                        start_time,
                        user_id,
                        level,
                        song_id,
                        artist_id,
                        session_id,
                        location,
                        user_agent
                       )
SELECT DISTINCT(e.ts)    AS start_time,
       e.userId          AS user_id,
       e.level           AS level,
       s.song_id         AS song_id,
       s.artist_id       AS artist_id,
       e.sessionId       AS session_id,
       e.location        AS location,
       e.userAgent       AS user_agent
FROM staging_events as e
JOIN staging_songs as s ON (e.artist = s.artist_name AND e.song = s.title)
WHERE e.page = 'NextSong';
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
SELECT
    DISTINCT(userId) AS user_id, 
    firstName        AS first_name, 
    lastName         AS last_name, 
    gender, 
    level
FROM staging_events
WHERE user_id IS NOT NULL;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
SELECT
    DISTINCT(song_id), 
    title, 
    artist_id, 
    year, 
    duration
FROM staging_songs
WHERE song_id IS NOT NULL;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
SELECT  
    DISTINCT(artist_id), 
    artist_name            AS name, 
    artist_location        AS location, 
    artist_latitude        AS latitude, 
    artist_longitude       AS longitude
FROM staging_songs
WHERE artist_id IS NOT NULL;
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
SELECT 
    DISTINCT(ts)               AS start_time, 
    EXTRACT(hour FROM ts)      AS hour, 
    EXTRACT(day FROM ts)       AS day,
    EXTRACT(week FROM ts)      AS week, 
    EXTRACT(month FROM ts)     AS month,
    EXTRACT(year FROM ts)      AS year, 
    EXTRACT(weekday FROM ts)   AS weekday
FROM staging_events;
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
