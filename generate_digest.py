
from openai import OpenAI
import feedparser
from datetime import datetime
from pathlib import Path
import os

# Use OpenAI SDK v1.x properly with env var
api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

# Load system prompt
with open("prompts/openai_prompt.txt", "r") as f:
    system_prompt = f.read()

# Load RSS feed
feed = feedparser.parse("watts-up-india-digest.xml")
items = feed.entries[:5]  # top 5 headlines

# Format feed content for model input
today_news_text = "\n".join([f"{item.title}: {item.summary}" for item in items])

# Call OpenAI to summarize
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": today_news_text}
    ],
    temperature=0.7,
    max_tokens=2000
)

digest_output = response.choices[0].message.content

# Save to HTML with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
html_path = Path(f"newsletter_templates/watts-up-india-{timestamp}.html")
html_path.write_text(digest_output)

print("✅ Digest generated and saved to", html_path)
