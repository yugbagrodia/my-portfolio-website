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
    st.image("profile-pic.JPG", width=230)
    st.title("Hi, I'm Yug Bagrodia 👋")
    st.subheader("A Student and Coding Enthusiast from SIT Pune")
    st.write(
        """
        I am a highly motivated and intellectually curious AIML undergraduate at Symbiosis Institute of Technology, Pune, with a forward-thinking mindset and a growing portfolio.
        I am passionate to solve problems and build interesting applications. 
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
    - **Libraries:** Streamlit, Pandas, Basics of NumPy
    - **Databases:** MySQL
    - **Tools:** Git, GitHub, VS Code, Jupyter Notebook
    """
)

# --- PROJECTS ---
st.write("---")
st.subheader("My Projects")
st.write("Here are the projects I built to practice my Python data analysis and visualization skills.")

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
        st.write("[View the dataset on GitHub](https://github.com/fivethirtyeight/data/blob/master/fandango/fandango_score_comparison.csv)")

    except FileNotFoundError:
        st.error("The 'movies.csv' file was not found. Please make sure it's in the same folder as app.py.")

# --- PROJECT 2: A SIMPLE CALCULATOR APP ---
with st.expander("🏆 Project 2: Click here to see the Simple Calculator"):

    st.write(
        """
        - **What I Did:** I built a functional calculator using Streamlit's interactive widgets.
        - **What I Learned:** This project taught me how to handle user input with buttons and number fields, perform calculations, and manage the display of results, including handling potential errors like division by zero.
        """
    )

    # --- CALCULATOR LOGIC ---
    
    # Get user input for two numbers
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)

    # Create four columns for the four operation buttons
    col1, col2, col3, col4 = st.columns(4)

    # Add button
    with col1:
        if st.button("Add (+)"):
            result = num1 + num2
            st.success(f"Result: {num1} + {num2} = {result}")

    # Subtract button
    with col2:
        if st.button("Subtract (-)"):
            result = num1 - num2
            st.success(f"Result: {num1} - {num2} = {result}")

    # Multiply button
    with col3:
        if st.button("Multiply (*)"):
            result = num1 * num2
            st.success(f"Result: {num1} * {num2} = {result}")

    # Divide button
    with col4:
        if st.button("Divide (/)"):
            # Handle the error for division by zero
            if num2 != 0:
                result = num1 / num2
                st.success(f"Result: {num1} / {num2} = {result}")
            else:
                st.error("Error: Cannot divide by zero.")


# --- CONTACT ---
st.write("---")
st.subheader("Get In Touch!")
st.write("You can reach me via email or find me on these platforms:")
st.write("📧 bagrodiayug@gmail.com")
st.write("[LinkedIn](https://www.linkedin.com/in/yug-bagrodia-23671936a/) | [GitHub](https://github.com/yugbagrodia/)")