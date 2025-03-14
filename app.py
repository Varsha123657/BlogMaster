import streamlit as st
import google.generativeai as genai
import random

# Configure the API Key (Replace with your actual API Key)
genai.configure(api_key="AIzaSyCpKiNO_xgqZFYi7-zNXT6lFo5QW_Ihb3E")

# Function to generate a blog using AI
def generate_blog(topic, word_count):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")
        response = model.generate_content(f"Write a blog on {topic} in {word_count} words.")
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Function to display a joke while generating the blog
def get_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the Python developer break up? Too many 'if' statements!",
        "Why do Python coders use snake_case? Because it's easy to read!"
    ]
    return random.choice(jokes)

# Streamlit Web App UI
st.title("BlogMaster: AI-Powered Blog Generator")
st.image("Blogmaster.jpg", use_container_width=True)  # Display an image (optional)
st.write("### 🤖 Hello! I’m BlogMaster, your friendly AI assistant. Let’s create a fantastic blog together!")

# User Inputs
user_input = st.text_input("Enter a Blog Topic:")
word_count = st.number_input("Number of words", min_value=100, max_value=5000, value=1000, step=50)

# Generate Blog Button
if st.button("Generate Blog"):
    if user_input and word_count:
        st.write("📝 Generating your blog... Here's a joke while you wait: " + get_joke())
        blog_content = generate_blog(user_input, word_count)
        st.write(blog_content)
    else:
        st.error("Please enter both topic and word count.")

