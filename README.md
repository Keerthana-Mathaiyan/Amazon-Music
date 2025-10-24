Amazon Music Cluster Visualizer & Song Recommender
Overview
This interactive web app built with Streamlit allows users to explore and visualize music clustering and get song recommendations based on audio and artist features. It demonstrates the use of multiple clustering algorithms and provides intuitive visualizations along with a powerful song filtering and recommendation system.

Features
Clustering Visualizer

Choose from K-Means, DBSCAN, or Hierarchical clustering methods

View cluster distribution, feature profiles, and PCA 2D projections

Explore top genres within each cluster

Download clustered data as CSV

Song Recommender

Select predefined filters like Rock, Classical, High Danceability, or Happy songs

Customize filtering by genres and audio features (danceability, energy, valence, tempo)

View filtered songs with key attributes

Download filtered song lists as CSV

Technologies Used
Python 3.x

Streamlit for web app interface

Pandas for data manipulation

Matplotlib & Seaborn for static plots

Plotly Express for interactive visualizations

scikit-learn PCA for dimensionality reduction

Installation
Clone the repository:
git clone https://github.com/yourusername/amazon-music-visualizer.git

Create and activate a virtual environment (optional but recommended):

bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install requirements:

bash
pip install -r requirements.txt
Run the Streamlit app:

bash
streamlit run app.py
Usage
Select between Clustering Visualizer and Song Recommender in the sidebar.

For Clustering Visualizer, pick a clustering method and explore various plots.

For Song Recommender, select a recommendation mode and apply filters.

Use the download buttons to export filtered data as CSV files.

File Structure
app.py — Main Streamlit app

amazon_music_clusters_all_methods.csv — Dataset with song features and cluster labels

requirements.txt — Python dependencies

License
This project is licensed under the MIT License.

For questions, feedback, or contributions, please open an issue or a pull request. Enjoy exploring music clusters and finding your next favorite song! 🎶
