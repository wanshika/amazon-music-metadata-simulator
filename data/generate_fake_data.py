import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import os

# Create directories if they don't exist
os.makedirs("data", exist_ok=True)

fake = Faker()

# Configuration
NUM_TRACKS = 1000
NUM_ARTISTS = 200
NUM_RIGHTS = 1000
GENRES = ['Pop', 'Rock', 'Jazz', 'Hip Hop', 'Classical', 'EDM', 'Country']

# Generate Artists
artists = []
for i in range(1, NUM_ARTISTS + 1):
    artists.append({
        'artist_id': f"A{i:04d}",
        'name': fake.name(),
        'country': fake.country_code()
    })
df_artists = pd.DataFrame(artists)

# Generate Tracks
tracks = []
for i in range(1, NUM_TRACKS + 1):
    artist = random.choice(artists)
    tracks.append({
        'track_id': f"T{i:05d}",
        'title': fake.sentence(nb_words=3).replace(".", ""),
        'duration_sec': random.randint(120, 420),
        'genre': random.choice(GENRES),
        'artist_id': artist['artist_id']
    })
df_tracks = pd.DataFrame(tracks)

# Generate Rights
rights = []
for i in range(1, NUM_RIGHTS + 1):
    track = random.choice(tracks)
    start_date = fake.date_between(start_date='-3y', end_date='-1y')
    end_date = start_date + timedelta(days=random.randint(30, 1000))
    rights.append({
        'rights_id': f"R{i:05d}",
        'track_id': track['track_id'],
        'owner_name': fake.company(),
        'valid_from': start_date.strftime("%Y-%m-%d"),
        'valid_to': end_date.strftime("%Y-%m-%d")
    })
df_rights = pd.DataFrame(rights)

# Save to CSV (in data/ directory)
df_artists.to_csv("data/artists.csv", index=False)
df_tracks.to_csv("data/tracks.csv", index=False)
df_rights.to_csv("data/rights.csv", index=False)

# Optional Preview
print("✅ Data generated and saved:")
print(df_artists.head())
print(df_tracks.head())
print(df_rights.head())
