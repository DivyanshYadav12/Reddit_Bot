import os
import time
import logging
from groq import Groq
import praw
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Groq client setup
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# Reddit client setup
reddit = praw.Reddit(
    client_id="0RsxxE_1hCU27gnVUO9JxQ",
    client_secret="xPCgcEcbjrOLhyNVfodWpR0tR3b9Rg",
    username="Advanced_Store_5480",
    password="reddit123",
    user_agent="<console:Advanced_Store_5480:0.0.1>"
)

# subreddit to post in
SUBREDDIT_NAME = "Advanced_Store"
POST_TIME = "12:23"  #(24-hour format)

# content generate function
def generate_content():
    logging.info("Generating content...")
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "user", "content": "Write an engaging Reddit post about AI technology."}
            ],
            model="llama-3.3-70b-versatile"  # Replace with the appropriate model from Groq
        )
        generated_text = response.choices[0].message.content
        logging.info("Content generated successfully.")
        return generated_text
    except Exception as e:
        logging.error(f"Error generating content: {e}")
        return None

# Function to post content on Reddit
def post_to_reddit(content):
    logging.info("Posting content to Reddit...")
    try:
        subreddit = reddit.subreddit(SUBREDDIT_NAME)
        subreddit.submit(title="AI Insights: Exploring the Future of Technology", selftext=content)
        logging.info("Post submitted successfully!")
    except Exception as e:
        logging.error(f"Error posting to Reddit: {e}")

# Define bot
def run_bot():
    logging.info("Reddit bot started. Waiting for the scheduled time...")
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == POST_TIME:
            content = generate_content()
            if content:
                post_to_reddit(content)
            else:
                logging.error("Failed to generate content.")
            time.sleep(60)
        time.sleep(1)

if __name__ == "__main__":
    run_bot()
