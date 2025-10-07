# spotify_functions.py

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# --- Functions for API Analysis (First Analysis) ---

def connect_to_spotify(client_id, client_secret):
    """
    Connects to the Spotify API using client credentials.
    Returns the spotipy object.
    """
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                                   client_secret=client_secret))
        print("Successfully connected to the Spotify API!")
        return sp
    except Exception as e:
        print(f"Error connecting to Spotify: {e}")
        return None

def search_playlist(sp, query, limit=5):
    """
    Searches for a playlist on Spotify.
    Returns the playlist ID and name of the first valid result.
    """
    results = sp.search(q=query, type="playlist", limit=limit)
    
    # Loop through the results to find the first valid (non-None) playlist
    if results and results['playlists']['items']:
        for playlist in results['playlists']['items']:
            # This check is crucial to handle empty items from the API
            if playlist:
                playlist_id = playlist['id']
                playlist_name = playlist['name']
                print(f"Success! Found playlist: '{playlist_name}' with ID: {playlist_id}")
                return playlist_id, playlist_name
    
    # If no valid playlist was found after checking all items
    print(f"Could not find any valid playlists for the query: '{query}'")
    return None, None

def get_playlist_tracks(sp, playlist_id):
    """
    Gets all tracks from a given playlist ID.
    Returns a list of dictionaries with song data.
    """
    results = sp.playlist_tracks(playlist_id)
    song_data = []
    
    for item in results['items']:
        track = item['track']
        if track:
            song_info = {
                'name': track['name'],
                'id': track['id'],
                'popularity': track['popularity'],
                'artists': [artist['name'] for artist in track['artists']]
            }
            song_data.append(song_info)
            
    print(f"Collected data for {len(song_data)} songs!")
    return song_data

def create_dataframe(song_data):
    """
    Converts a list of song data into a pandas DataFrame.
    """
    return pd.DataFrame(song_data)


# --- Functions for Dataset Analysis (Second Analysis) ---


def load_spotify_dataset(file_path):
    """Loads the Spotify dataset from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset '{file_path}' loaded successfully with {df.shape[0]} rows.")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

def clean_data(df):
    """Cleans the DataFrame by dropping NAs, an index column, and duplicates."""
    print(f"Original shape: {df.shape}")
    
    # Drop rows with any missing values
    df_cleaned = df.dropna()
    print(f"Shape after dropping NAs: {df_cleaned.shape}")
    
    # Drop the unnecessary 'index' column if it exists
    if 'index' in df_cleaned.columns:
        df_cleaned = df_cleaned.drop(columns=['index'])
        print("Dropped the 'index' column.")
    
    # Check for and drop duplicate tracks based on 'track_id'
    num_duplicates = df_cleaned.duplicated(subset=['track_id']).sum()
    if num_duplicates > 0:
        print(f"Found {num_duplicates} duplicate tracks. Removing them.")
        df_cleaned = df_cleaned.drop_duplicates(subset=['track_id'], keep='first')
    
    print(f"Final shape after cleaning: {df_cleaned.shape}")
    return df_cleaned

def define_hit_songs(df, threshold=87):
    """Creates the 'is_hit' target variable based on a popularity threshold."""
    df['is_hit'] = (df['popularity'] > threshold).astype(int)
    print(f"Created 'is_hit' column with a popularity threshold of > {threshold}.")
    print("\nDistribution of Hits (1) vs. Non-Hits (0):")
    print(df['is_hit'].value_counts())
    return df