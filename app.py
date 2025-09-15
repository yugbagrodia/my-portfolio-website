import streamlit as st
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# --- HERO SECTION ---
# Using columns to layout the image and text side-by-side
col1, col2 = st.columns(2)

with col1:
    # You can upload an image to your folder and change "profile-pic.png"
    st.image("profile-pic.jpg", width=200)
    st.title("Hi, I'm [Yug Bagrodia] 👋")
    st.subheader("A Student and Coding Enthusiast from SIT Pune")
    st.write(
        """
        I am passionate about using Python to solve problems and build interesting applications. 
        This portfolio is my first venture into web development, built entirely with Python!
        """
    )

with col2:
    # This column is intentionally left blank or you can add an image here
    st.write(" ") # Add some space

# --- SKILLS ---
st.write("---") # A horizontal divider
st.subheader("My Skills")
st.write(
    """
    - **Programming:** Python
    - **Libraries:** Pandas, NumPy
    - **Databases:** MySQL
    - **Tools:** Git, GitHub, VS Code
    """
)

# --- PROJECTS ---
st.write("---")
st.subheader("My Projects")
st.write("Here is a project I built to practice my Python data analysis and visualization skills.")

# Create an expander for the project
with st.expander("🏆 Project 1: Click here to see the Interactive Movie Visualizer"):
    # All of the project code is now INDENTED inside the expander
    try:
        # Load the data from the CSV file
        df = pd.read_csv('movies.csv', index_col='title')

        # Create a slider to select the number of top movies to display
        top_n = st.slider('Select number of top movies to display:', min_value=5, max_value=25, value=10)

        # Get the top N movies based on IMDB rating
        top_movies = df.nlargest(top_n, 'imdb_rating')

        st.write(f"Displaying the Top {top_n} Movies by IMDB Rating")

        # Create a bar chart
        st.bar_chart(top_movies['imdb_rating'])

        st.write(
            """
            - **What I Did:** I used the Pandas library to load and process a dataset of top-rated movies.
            - **What I Learned:** This project taught me how to handle data with Pandas, create interactive widgets with Streamlit (like this slider!), and visualize data with charts.
            """
        )
        st.write("[View the dataset on GitHub](https://github.com/fivethirtyeight/data/tree/master/imdb)")

    except FileNotFoundError:
        st.error("The 'movies.csv' file was not found. Please make sure it's in the same folder as app.py.")

# --- CONTACT ---
st.write("---")
st.subheader("Get In Touch!")
st.write("You can reach me via email or find me on these platforms:")
st.write("📧 bagrodiayug@gmail.com")
st.write("[LinkedIn](https://www.linkedin.com/in/yug-bagrodia-23671936a/) | [GitHub](https://github.com/yugbagrodia/)")