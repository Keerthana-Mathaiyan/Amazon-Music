import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.decomposition import PCA
import numpy as np

# -------------------------------
# 1️⃣ PAGE CONFIG
st.set_page_config(page_title="Amazon Music Cluster Visualizer", layout="wide")

# -------------------------------
# 2️⃣ LOAD DATA
@st.cache_data
def load_data():
    df = pd.read_csv("C:/Users/keert/OneDrive/Desktop/Guvi-project/Amazon music clustering/amazon_music_clusters_all_methods.csv")
    return df

df = load_data()

# -------------------------------
# 3️⃣ SIDEBAR: Toggle between views
sidebar_option = st.sidebar.radio("Select option", ["Clustering Visualizer", "Song Recommender"])

if sidebar_option == "Clustering Visualizer":
    # Select clustering method inside this mode
    method = st.selectbox("Select Clustering Method", ["K-Means", "DBSCAN", "Hierarchical"])

    cluster_col = {
        "K-Means": "cluster",
        "DBSCAN": "cluster_dbscan",
        "Hierarchical": "cluster_hc"
    }[method]

    df_vis = df.dropna(subset=[cluster_col]).copy()
    df_vis[cluster_col] = df_vis[cluster_col].astype(int)

    st.title("🎧 Amazon Music Clustering Dashboard")
    st.markdown("""
    Explore how songs are grouped based on their audio and artist features using   
    **K-Means**, **DBSCAN**, and **Hierarchical Clustering**.
    ---
    """)

    st.subheader("📊 Dataset Overview")
    st.dataframe(df_vis.head(10))

    col1, col2, col3 = st.columns(3)
    col1.metric("Number of Songs", len(df_vis))
    col2.metric("Number of Clusters", df_vis[cluster_col].nunique())
    col3.metric("Genres", df_vis['genres'].nunique())

    st.subheader(f"🎨 {method} Cluster Distribution")
    cluster_counts = df_vis[cluster_col].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(8,4))
    sns.barplot(x=cluster_counts.index, y=cluster_counts.values, ax=ax, palette="viridis")
    ax.set_xlabel("Cluster ID")
    ax.set_ylabel("Number of Songs")
    ax.set_title(f"{method} – Cluster Size Distribution")
    st.pyplot(fig)

    st.subheader("🎼 Average Feature Values per Cluster")
    features = ['danceability', 'energy', 'valence', 'tempo']
    cluster_profile = df_vis.groupby(cluster_col)[features].mean()
    fig, ax = plt.subplots(figsize=(10,5))
    sns.heatmap(cluster_profile, annot=True, cmap='YlGnBu', fmt=".2f", ax=ax)
    ax.set_title(f"{method} – Feature Profile Heatmap")
    st.pyplot(fig)

    st.subheader("🌀 PCA Visualization (2D Projection)")
    numeric_cols = ['danceability', 'energy', 'valence', 'tempo']
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(df_vis[numeric_cols])
    df_vis['pca1'], df_vis['pca2'] = pca_result[:,0], pca_result[:,1]
    fig_pca = px.scatter(
        df_vis, x='pca1', y='pca2',
        color=df_vis[cluster_col].astype(str),
        hover_data=['genres'],
        title=f"{method} – PCA Cluster Visualization",
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    st.plotly_chart(fig_pca, use_container_width=True)
#----
    # Aggregate: count songs per Cluster_Label
    line_data = df_vis.groupby('Cluster_Label').size().reset_index(name='song_count')

    # Plot line graph with Cluster_Label on x-axis and song counts on y-axis
    fig_line = px.line(
        line_data,
        x='Cluster_Label',
        y='song_count',
        title=f"{method} - Number of Songs by Cluster Label",
        markers=True,
        labels={'Cluster_Label': 'Cluster Label', 'song_count': 'Number of Songs'}
    )

    st.subheader(f"📈 {method} - Number of Songs by Cluster Label")
    st.plotly_chart(fig_line, use_container_width=True)

#--------------
 
    st.subheader("🎶 Top Genres by Cluster")
    top_genres = (
        df_vis.groupby(['genres', cluster_col])
        .size()
        .reset_index(name='count')
        .sort_values('count', ascending=False)
        .head(15)
    )
    fig_genres = px.bar(
        top_genres, 
        x='genres', y='count', color=cluster_col,
        title=f"Top Genres across {method} Clusters",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    st.plotly_chart(fig_genres, use_container_width=True)

    st.subheader("⬇️ Download Filtered Cluster Data")
    csv = df_vis.to_csv(index=False).encode('utf-8')
    st.download_button(
        "Download CSV",
        csv,
        f"music_clusters_{method.lower()}.csv",
        "text/csv",
        key='download-csv'
    )

else:
 if sidebar_option == "Song Recommender":
    st.title("🎶 Song Recommender System")
    st.write("Find songs filtered by genre and audio features!")

    method = "K-Means"  # or make selectable if needed
    cluster_col = {
        "K-Means": "cluster",
        "DBSCAN": "cluster_dbscan",
        "Hierarchical": "cluster_hc"
    }[method]

    features = ['danceability', 'energy', 'valence', 'tempo']

    # Filter out NaNs in important columns
    df_nonan = df.dropna(subset=[cluster_col] + features + ['genres']).copy()
    df_nonan[cluster_col] = df_nonan[cluster_col].astype(int)

    mode = st.radio("Select Recommendation Mode:", ["Predefined", "Customized"])

    if mode == "Predefined":
        option = st.selectbox("Choose a predefined filter:",
                              ["Rock (High tempo & energy)",
                               "Classical (Low tempo)",
                               "High Danceability (>0.7)",
                               "Happy (High valence ≈0.9)"])

        if option == "Rock (High tempo & energy)":
            filtered = df_nonan[
                (df_nonan['genres'].str.contains("rock", case=False)) &
                (df_nonan['tempo'] >= 120) &         # Assuming tempo >=120 as high
                (df_nonan['energy'] >= 0.8)
            ]
        elif option == "Classical (Low tempo)":
            filtered = df_nonan[
                df_nonan['genres'].str.contains("classical", case=False) &
                (df_nonan['tempo'] <= 80)            # Assuming low tempo <=80
            ]
        elif option == "High Danceability (>0.7)":
            filtered = df_nonan[
                df_nonan['danceability'] > 0.7
            ]
        elif option == "Happy (High valence ≈0.9)":
            filtered = df_nonan[
                df_nonan['valence'] >= 0.9
            ]

        st.subheader(f"Songs matching '{option}'")
        st.write(f"{len(filtered)} songs found.")
        st.dataframe(filtered[['Cluster_Label', 'genres', 'danceability', 'energy', 'valence', 'tempo']].head(20), hide_index=True)

       #button      
        if not filtered.empty:
            csv = filtered.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Download Filtered Songs as CSV",
                data=csv,
                file_name="recommended_songs.csv",
                mime="text/csv",
                key="download_recommended_csv"
            )
        else:
            st.info("No songs match your filter criteria.")

    else:  # Customized mode
        genres = df_nonan['genres'].unique().tolist()
        selected_genres = st.multiselect("Select Genres", options=genres, default=genres[:5])

        danceability_range = st.slider("Danceability Range", 0.0, 1.0, (0.0, 1.0))
        energy_range = st.slider("Energy Range", 0.0, 1.0, (0.0, 1.0))
        valence_range = st.slider("Valence Range", 0.0, 1.0, (0.0, 1.0))
        tempo_min, tempo_max = float(df_nonan['tempo'].min()), float(df_nonan['tempo'].max())
        tempo_range = st.slider("Tempo Range", tempo_min, tempo_max, (tempo_min, tempo_max))

        filtered = df_nonan[
            (df_nonan['genres'].isin(selected_genres)) &
            (df_nonan['danceability'] >= danceability_range[0]) & (df_nonan['danceability'] <= danceability_range[1]) &
            (df_nonan['energy'] >= energy_range[0]) & (df_nonan['energy'] <= energy_range[1]) &
            (df_nonan['valence'] >= valence_range[0]) & (df_nonan['valence'] <= valence_range[1]) &
            (df_nonan['tempo'] >= tempo_range[0]) & (df_nonan['tempo'] <= tempo_range[1])
        ]

        st.subheader("Songs matching your custom filters")
        st.write(f"{len(filtered)} songs found.")
        st.dataframe(filtered[['Cluster_Label', 'genres', 'danceability', 'energy', 'valence', 'tempo']].head(20), hide_index=True)

        # Add download button if any songs were found
        if not filtered.empty:
            csv = filtered.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Download Filtered Songs as CSV",
                data=csv,
                file_name="recommended_songs.csv",
                mime="text/csv",
                key="download_recommended_csv"
            )
        else:
            st.info("No songs match your filter criteria.")
