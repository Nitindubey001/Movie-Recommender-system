# app.py
import json
import streamlit as st
from recommend import df, recommend_movies
from omdb_utils import get_movie_details

# Load config
config = json.load(open("config.json"))
OMDB_API_KEY = config["OMDB_API_KEY"]

# App configuration
st.set_page_config(
    page_title="🎬 Fantastic Movie Recommender",
    page_icon="🍿",
    layout="centered"
)

# Header
st.markdown("<h1 style='text-align: center;'>🍿 Fantastic Movie Recommender</h1>", unsafe_allow_html=True)
st.markdown("### Get personalized movie suggestions based on your favorite movie!")

# Movie selection
movie_list = sorted(df['title'].dropna().unique())
selected_movie = st.selectbox("🎥 Choose a movie you like:", movie_list)

# Recommend button
if st.button("✨ Recommend Me Movies!"):
    with st.spinner("Crunching data and finding awesome picks..."):
        recommendations = recommend_movies(selected_movie)

        if recommendations is None or recommendations.empty:
            st.warning("😞 Sorry, no recommendations found.")
        else:
            st.success("🔥 Top Picks Just for You:")
            for _, row in recommendations.iterrows():
                movie_title = row['title']
                plot, poster, genre, rating = get_movie_details(movie_title, OMDB_API_KEY)

                with st.container():
                    st.markdown("---")
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        if poster and poster != "N/A":
                            st.image(poster, width=120)
                        else:
                            st.image("https://via.placeholder.com/120x180?text=No+Image", width=120)

                    with col2:
                        st.markdown(f"### 🎬 {movie_title}")
                        st.markdown(f"**🎭 Genre:** {genre if genre else '_Not available_'}")
                        st.markdown(f"**⭐ IMDB Rating:** {rating if rating else '_N/A_'}")
                        st.markdown(f"**📝 Plot:** {plot if plot and plot != 'N/A' else '_Plot not available_'}")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
