# Reddit Bot with AI-Generated Content
This project is a Reddit bot that automatically posts AI-generated content to a subreddit and optionally comments on other posts. The bot uses the Groq AI API for content generation and the Reddit API for interacting with Reddit.

# Features
Automated Posting: Posts AI-generated content to Reddit at regular intervals (e.g., every 1 hour).
AI Integration: Uses Groq AI for generating engaging and insightful posts.
Comment Generation: Optionally generates comments on other posts in a subreddit.
Error Handling: Logs errors for debugging and provides informative logs during execution.
Requirements
Python: Make sure Python 3.8 or above is installed.
APIs:
Groq API: For AI content generation.
Reddit API: For Reddit interaction (posting and commenting).
# Setup Instructions
Clone the Repository:
git clone https://https://github.com/DivyanshYadav12/Reddit_Bot
cd reddit-bot
Install Dependencies: Install required Python packages using requirements.txt:
pip install -r requirements.txt
Set Up API Keys:
Create a .env file or update the code with your credentials:
# Groq API Key: 
Obtain from Groq (https://console.groq.com/keys).
Reddit API Credentials:
# Create an app at Reddit Apps to get 
## (https://www.reddit.com/prefs/apps):
client_id,
client_secret,
username,
password,
user_agent,
