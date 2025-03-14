import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Configure generation settings
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 200,
    "response_mime_type": "text/plain"
}

# Initialize the Gemini Pro model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config
)

print("Model initialized successfully!")

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define the model
model = genai.GenerativeModel("gemini-1.5-pro")

def get_joke():
    """Returns a fun joke to entertain the user."""
    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "What’s a computer’s favorite snack? Microchips!",
        "Why did the AI break up with its girlfriend? It lost its connection!"
    ]
    return random.choice(jokes)

def generate_blog(user_input, word_count):
    """
    Generates a blog based on user input and word count using Gemini Pro LLM.
    Parameters:
        user_input (str): The topic for the blog.
        word_count (int): The desired number of words for the blog.
    Returns:
        str: The generated blog content or an error message.
    """
    st.write("### ⏳ Generating your blog...")
    st.write(f"Here's a little joke while you wait: 😆 **{get_joke()}**")

    # Define the prompt for blog generation
    prompt = f"""
    Write a well-structured blog on the topic: "{user_input}". 
    Ensure the blog is approximately {word_count} words long.
    Include an engaging introduction, detailed explanation, and a strong conclusion.
    """

    try:
        response = model.generate_content([prompt])
        if response and hasattr(response, "text"):
            st.success("🎉 Blog successfully generated!")
            return response.text.strip()
        else:
            return "Error: No response from the model."
    except Exception as e:
        st.error(f"Error generating blog: {e}")
        return None

import random

def get_joke():
    """Returns a random programming-related joke."""
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Python programmers prefer using snake_case? Because it's easier to read!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
        "Why did the programmer get kicked out of the beach? Because he kept using the 'C' language!",
        "Why was the computer cold? It left its Windows open.",
        "What’s a computer’s favorite snack? Microchips!",
        "Why did the AI break up with its girlfriend? It lost its connection!",
        "Why do software developers prefer tea over coffee? Because tea has less Java!",
        "What do you call a group of 8 Hobbits? A byte!",
        "Why do programmers hate nature? Too many bugs.",
        "What is a ghost programmer’s favorite data type? The BOOlean!"
    ]
    
    return random.choice(jokes)

# Example usage
print(get_joke())  # Prints a random joke

import streamlit as st

def main():
    # Streamlit app
    st.title("BlogMaster: AI-Powered Blog Generation")

    # Display the main image and the friendly robot character
    st.image("blogmaster.jpeg", use_container_width=True)  # Adjust the path as needed
    st.write("### 🤖 Hello! I’m BlogMaster, your friendly robot. Let’s create a fantastic blog together!")

import streamlit as st


# Main function to run the Streamlit app
def main():
    st.title("📝 BlogMaster - AI Blog Generator")

    # Get user input
    user_input = st.text_input("Topic", "")
    word_count = st.number_input("Number of words", min_value=100, max_value=5000, value=1000, step=50)

    if st.button("Generate Blog"):
        if user_input and word_count:
            # Call the generate_blog function
            blog_content = generate_blog(user_input, word_count)
            if blog_content:
                st.write(blog_content)
            else:
                st.error("Failed to generate blog. Try again.")
        else:
            st.error("Please provide both the topic and the number of words.")

# Run the app
if __name__ == "__main__":
    main()

