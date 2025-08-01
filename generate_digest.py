import openai
import feedparser
from datetime import datetime
from pathlib import Path

# Load OpenAI API key from environment variable or config
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the updated system prompt from file
with open("prompts/openai_prompt.txt", "r") as f:
    system_prompt = f.read()

# Load news items (example: from local RSS)
feed = feedparser.parse("watts-up-india-digest.xml")
items = feed.entries[:5]  # You can adjust this based on how many headlines you want

# Prepare raw input for the model
today_news_text = "\n".join([f"- {item.title}: {item.summary}" for item in items])

# Call OpenAI to generate digest
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": today_news_text}
    ],
    temperature=0.7,
    max_tokens=2000
)

# Extract content
digest_output = response['choices'][0]['message']['content']

# Save as XML and HTML
timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H-%M")
html_path = Path(f"newsletter_templates/watts-up-india-{timestamp}.html")
html_path.write_text(digest_output)

# Also optionally print to console
print("Newsletter generated and saved to:", html_path)