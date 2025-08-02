
from openai import OpenAI
import feedparser
from datetime import datetime
from pathlib import Path
import os

# Load OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load system prompt
with open("prompts/openai_prompt.txt", "r") as f:
    system_prompt = f.read()

# Parse feed
feed = feedparser.parse("watts-up-india-digest.xml")
items = feed.entries[:5]  # Adjust number of articles if needed

# Build input for GPT
today_news_text = "\n".join([f"{item.title}: {item.summary}" for item in items])

# Call OpenAI (v1.x format)
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

# Save as HTML
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
html_path = Path(f"newsletter_templates/watts-up-india-{timestamp}.html")
html_path.write_text(digest_output)

print("✅ Digest generated and saved to", html_path)
