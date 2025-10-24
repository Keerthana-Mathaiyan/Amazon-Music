🚀 Amazon Music Cluster Visualizer & Song Recommender 🎵

Overview:

This interactive web app built with Streamlit allows users to explore music clustering and get song recommendations based on audio and artist features.

Features:
🎨 Clustering Visualizer

     Choose clustering method: K-Means, DBSCAN, Hierarchical

     View cluster size, average feature heatmaps, PCA projection

     Explore top genres per cluster

    ⬇️ Download cluster data CSV

🎧 Song Recommender

Predefined filters: Rock, Classical, High Danceability, Happy

Customized filters on genre and audio features

Browse filtered songs and attributes

⬇️ Download filtered songs CSV

Technologies Used
🐍 Python 3.x

🌐 Streamlit for the web UI

📊 Pandas, Seaborn, Matplotlib, Plotly for data visualization

🔍 Scikit-learn PCA for dimensionality reduction

Installation & Usage
bash
git clone https://github.com/yourusername/amazon-music-visualizer.git
cd amazon-music-visualizer
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
Select your analysis mode in the sidebar

Explore clusters or try song recommendation filters

Download data anytime using the provided buttons
