🚀 Amazon Music Cluster Visualizer & Song Recommender 🎵

🔍Overview:

This interactive web app built with Streamlit allows users to explore music clustering and get song recommendations based on audio and artist features.


File Name:  
 📄single_genre_artists -  dataset
 📽️Amazon Music Clustering-ppt - have a explanation of streamlit app 
 📊amazon_music_clusters_all_methods - output from colab notebook which is used in streamlit app
 📝Amazon_Music_Culstering_ - colab notebook
🌐app.py - streamlit code
 📝 Project guide lines - have the E2E information about the process involved in this project
Streamlit OUTPUT file:
   📊music_clusters_dbscan-output
   📊music_clusters_hierarchical-output
   📊music_clusters_k-means-output
   📊recommended_songs-output

Features Include: 

♦️danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, etc.


Data Set Explanation:

♦️This dataset provides audio characteristics of Amazon Music songs that define how a song "sounds." These include rhythm, mood, intensity, and instrumentation.



| Column Name         | What It Is                                                   | Why It Matters                                                                            |
| ------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| `id_songs`          | Unique identifier for each song                              | Used to uniquely identify and track songs in the database                                 |
| `name_song`         | Name of the song                                             | Useful for display, search, and user interaction                                          |
| `popularity_songs`  | Popularity score of the song (usually 0–100 scale)           | Indicates how well the song is performing; important for recommendation and ranking       |
| `duration_ms`       | Length of the song in milliseconds                           | Important for playback, playlist creation, and analysis of song length trends             |
| `explicit`          | Whether the song has explicit lyrics (true/false)            | Needed for content filtering, especially for underage users                               |
| `id_artists`        | Unique ID(s) of the artist(s) who made the song              | Helps in linking songs to artist profiles                                                 |
| `release_date`      | Date the song was released                                   | Useful for understanding trends over time or artist evolution                             |
| `danceability`      | Score (0-1) describing how suitable the song is for dancing  | Helps in mood-based recommendations (e.g., party playlists)                               |
| `energy`            | Score (0-1) representing intensity and activity of the track | Used in mood analysis and dynamic playlist creation                                       |
| `key`               | Musical key (e.g., C = 0, C#/Db = 1, ..., B = 11)            | Used in music theory analysis, DJing, or harmonically mixing songs                        |
| `loudness`          | Average loudness in decibels (dB)                            | Reflects how “loud” a song sounds; helps in normalization                                 |
| `mode`              | 1 = major, 0 = minor                                         | Major is happy/uplifting, minor is sad/dark — helps in emotional analysis                 |
| `speechiness`       | Amount of spoken words (higher = more talk-like)             | Helps distinguish between songs and spoken-word content like podcasts                     |
| `acousticness`      | Confidence score (0-1) of whether the track is acoustic      | Indicates if the song uses acoustic instruments; useful for genre and mood categorization |
| `instrumentalness`  | Prediction of whether a track contains no vocals             | Instrumentals vs. vocal tracks; good for background music recommendations                 |
| `liveness`          | Presence of an audience in the recording (0–1)               | Higher = more likely it's a live performance                                              |
| `valence`           | Musical positivity (0 = sad, 1 = happy)                      | Crucial for emotion-based playlists (e.g., feel-good music)                               |
| `tempo`             | Tempo in BPM (beats per minute)                              | Important for DJing, workouts, and mood pacing                                            |
| `time_signature`    | Beats per bar (e.g., 4 = common time)                        | Useful in rhythmic analysis and mixing                                                    |
| `followers`         | Number of followers the artist has on the platform           | A measure of artist popularity and influence                                              |
| `genres`            | Genre(s) associated with the artist                          | Key for categorizing music and recommendations                                            |
| `name_artists`      | Name(s) of the artist(s)                                     | For readability and display                                                               |
| `popularity_artist` | Popularity score of the artist (0–100 scale)                 | Shows how well-known the artist is overall; may influence song popularity                 |



🔗 HOW THESE FEATURES ARE RELATED

1. Songs & Artists

♦️id_songs and id_artists link songs to their creators.

♦️Each song has a corresponding artist (name_artists, id_artists), and artists can have multiple songs.

♦️popularity_songs often correlates with popularity_artist, but not always — a less popular artist might have a hit song.

2. Popularity & Audio Features

♦️Songs with higher danceability, energy, or valence might be more popular because they are more engaging or feel-good.

♦️On the other hand, acoustic or instrumental tracks may have niche popularity.

3. Artist Metrics

♦️followers, genres, and popularity_artist describe the artist's overall reach and appeal.

♦️These can help explain why a song might gain traction quickly (famous artist = more likely to go viral).

4. Mood and Emotion

♦️valence, mode, tempo, energy, danceability work together to define the mood of a song.

♦️You can cluster songs into "happy", "sad", "chill", or "hype" playlists using these values.

5. Temporal Patterns

♦️release_date can be used to study trends over time:

♦️Are songs getting shorter?

♦️Is there a rise in danceable music?

♦️Do certain genres trend at different times?


📊 How You Could Use This Dataset

♦️Recommendation systems: Suggest songs based on user preferences in mood, tempo, or popularity.

♦️Trend analysis: Analyze how music styles evolve over time.

♦️Genre classification: Use audio features to predict or cluster music genres.

♦️Artist analysis: Study how an artist's style, popularity, or follower base changes over time.

♦️Hit prediction: Build a machine learning model to predict whether a song will be popular.


Features:

🎨Clustering Visualizer

 ♦️Choose clustering method: K-Means, DBSCAN, Hierarchical

 ♦️View cluster size, average feature heatmaps, PCA projection

 ♦️Explore top genres per cluster

 ♦️⬇️ Download cluster data CSV

🎧 Song Recommender

 ♦️Predefined filters: Rock, Classical, High Danceability, Happy

 ♦️Customized filters on genre and audio features

 ♦️Browse filtered songs and attributes

 ♦️⬇️ Download filtered songs CSV

📂 File Structure

Technologies Used
 🐍 Python 3.x

 🌐 Streamlit for the web UI

 📊 Pandas, Seaborn, Matplotlib, Plotly for data visualization

 🔍 Scikit-learn PCA for dimensionality reduction

Installation & Usage

     git clone https://github.com/yourusername/amazon-music-visualizer.git
     cd amazon-music-visualizer
     python -m venv venv
     source venv/bin/activate  # Windows: venv\Scripts\activate
     pip install -r requirements.txt
     streamlit run app.py
 ♦️Select your analysis mode in the sidebar

 ♦️Explore clusters or try song recommendation filters

 ♦️Download data anytime using the provided buttons
