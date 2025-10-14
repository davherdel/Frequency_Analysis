Project Description: Music Hits - From Data Patterns to Brain Science
Overall Goal
This project explores the characteristics of popular "hit" songs through two distinct analytical approaches. The first analysis uses the Spotify API to perform a direct comparison between a mainstream hits playlist and a niche genre playlist. The second analysis uses a large, pre-existing Spotify dataset to test several hypotheses about the audio features that correlate with high popularity scores and the third analysis focus on the Brain Science of the music and brain frequencies and how they correlate with each other.
________________


Part 1: Comparative Analysis of Playlists (API-Driven)
Objective
The goal of this analysis was to directly compare the fundamental characteristics (specifically, the popularity score) of songs on a "Top 100" playlist versus songs on a "Absolutely Horrible Songs" playlist. This serves as a practical, API-driven method to establish a baseline difference between contemporary hits and classic, niche tracks.
Methodology
1. Data Collection (Spotify API):
   * A connection to the Spotify API was established using personal developer credentials.
   * The API's search endpoint was used to find a "Top 100" playlist, and its track data (name, artist, ID, popularity) was extracted.
   * The same process was repeated to find a "Absolutely Horrible Songs" playlist and extract its track data.
2. Data Structuring & Feature Engineering:
   * The collected data for each playlist was loaded into two separate pandas DataFrames.
   * A target variable, is_hit, was engineered: songs from the "Top 100" playlist were labeled with 1, and songs from the "Absolutely Horrible Songs" playlist were labeled with 0.
   * The two DataFrames were concatenated into a single master DataFrame for comparative analysis.
3. Analysis & Visualization:
   * The .groupby('is_hit') function was used to calculate and compare descriptive statistics for the popularity score of the two groups.
   * Visualizations, including box plots, KDE plots, and bar charts, were created to visually inspect the differences in popularity distribution between the two playlists.
________________


Part 2: Predicting Viral Hits from Audio Features (Dataset-Driven)
Objective & Hypothesis
This analysis aimed to identify which audio features are common among viral hits, using a large dataset of over 100,000 songs.
* Hypothesis: "Songs that become viral hits often share a common set of audio features, such as high danceability and a simple, repetitive structure."
Methodology
1. Data Loading & Cleaning:
   * A dataset (spotify_dataset.csv) was loaded into a pandas DataFrame.
   * The data was cleaned by handling null values, dropping unnecessary columns (index), and removing duplicate tracks based on their unique track_id.
2. Defining a "Hit" (Target Variable):
   * A data-driven rule was established to classify songs. A song is defined as a "hit" if its popularity score is greater than 87.
   * This rule created a binary target variable, is_hit (1 for hits, 0 for non-hits), allowing for direct comparison between the two groups.
3. Exploratory Data Analysis (EDA) & Hypothesis Testing:
   * The core of the analysis involved comparing the audio features of "hits" versus "non-hits" to test several hypotheses.
   * The following features were analyzed using .groupby() and visualizations (box plots, KDE plots, violin plots, etc.):
      * Energy & Danceability: Are hit songs more energetic and danceable?
      * Valence (Mood): Do hit songs have a happier or sadder mood?
      * Tempo & Duration: Is there a specific tempo or song length that is more common in hits?
      * Loudness: Are hit songs commercially louder?
      * Mode: Are hits more likely to be in a Major key versus a Minor key?
      * Genre: Are certain genres more likely to produce hits?
      * Explicit Content: Is there a correlation between explicit lyrics and popularity?
________________


Part 3: The Science of Sound - A Deep-Dive
Objective & Hypothesis
This final analysis goes beyond Spotify's pre-calculated metadata to answer the "why" behind our findings. While the dataset analysis showed what features are common in hits, this part explores the fundamental sonic characteristics that might explain the brain's positive response to these songs.

* Hypothesis: The high danceability and energy scores of hit songs correspond to specific, measurable patterns in their frequency spectrum and rhythmic structure that are engaging to the human brain.
Methodology
This deep-dive analysis was conducted thanks to libraries like **librosa, scipy.io, scipy.signal,** on a sample of hit and non-hit songs from our dataset.

**1. Data Loading:**
   * Audio files for a representative sample of songs were loaded into the analysis environment.
   * Each library was imported with an specific objective, listed as follows:
   *   NumPy - Perform the actual FFT computation
   *   SciPy - Add advance signal-processing tools
   *   Librosa - Simplify loading and analyzing audio signals for music and **ML**
   *   Matplotlib - Create charts and visualizations
     
**2. Fast Fourier Transform: The Origin**
   * The **FFT**, or Fast Fourier Transform, is a mathematical process that converts audio signals from the time domain to the frequency domain.
   * **FFT** was first proposed in the early 1800's by **Jean-Baptiste Joseph Fourier**, who at the time proposed that all signals like **heat vibrations, vibrations, or sound** can be decomposed into **basic frequency components**
   * Back in 1965, James Cooley and John Turkey presented the efficient, computational version we use today through the **Cooley-Turkey FFT algorithm.**

**3. Feature Extraction & Visualization**
   * FFT digitally separates music into its individual frequencies, allowing us to **analyze its structure, identify dominant tones, and visualize spectral composition.**
   * The libraries were used to extract raw soundwave data and analyze its core components:
      * **Waveforms & Spectrograms:** Visualized to see the energy and frequency distribution across the duration of each song.
      * **Frequency Spectrum Analysis:** Analyzed to identify the dominant sonic ranges (e.g., strong bass, clear midrange) that are part of each track.
      * **Beat & Tempo Analysis:** Extracted rhythmic patterns and tempo directly from the audio signal to understand the song's underlying groove.
      * **Harmonic-Percussive Separation:** Isolated the melodic/tonal elements from the rhythmic elements to analyze their complexity and interaction.


Technical Implementation
To ensure the code was organized, reusable, and clean, a modular approach was taken. All data loading, API interaction, and data cleaning logic was refactored from the notebooks into a single spotify_functions.py file. The main analysis notebooks now import this custom module to prepare the data, separating the data preparation steps from the exploratory analysis and visualization.

Links: 
Google Slides - https://docs.google.com/presentation/d/16YASe1phYjWynylYeruJQQJCUnU0U9M8yrNNw0bl6vw/edit?slide=id.g38ab2b38ad2_0_51#slide=id.g38ab2b38ad2_0_51
Spotify API - https://developer.spotify.com/documentation/web-api
Spotify Dataset - https://www.kaggle.com/datasets/melissamonfared/spotify-tracks-attributes-and-popularity
Kanban board - https://app.asana.com/1/1211526368051919/project/1211526545558584/list/1211526448867750
https://librosa.org/doc/latest/
https://docs.scipy.org/doc/scipy/reference/fft.html
