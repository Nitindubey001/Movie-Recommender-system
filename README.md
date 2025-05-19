# Movie-Recommender-system
🎬 Movie Recommender App
An intelligent movie recommendation app that helps users discover movies similar to the ones they like. Built using Python, Streamlit, and the OMDb API, the app also fetches useful metadata like plot summaries, genres, posters, and IMDb ratings.

🚀 Features
🎥 Select a movie you like

🎯 Get a list of similar movies using content-based filtering

📝 View detailed info: plot, genre, IMDb rating, and poster

⚡ Fast and interactive UI using Streamlit

🛠 Tech Stack
Python

Pandas

Streamlit

OMDb API

Cosine Similarity (for content-based recommendation)

🔧 Setup Instructions
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/movie-recommender-app.git
cd movie-recommender-app
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Add your OMDb API key
Create a config.json file with the following content:

json
Copy
Edit
{
  "OMDB_API_KEY": "your_api_key_here"
}
Run the app

bash
Copy
Edit
streamlit run app.py

📬 Contact
Feel free to open issues or share feedback. Contributions and suggestions are always welcome.
