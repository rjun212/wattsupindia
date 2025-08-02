
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

# Load latest newsletter file from newsletter_templates
newsletter_dir = Path("newsletter_templates")
html_files = sorted(newsletter_dir.glob("watts-up-india-*.html"), reverse=True)
latest_file = html_files[0]

# Email config
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = os.environ["SMTP_USER"]
smtp_pass = os.environ["SMTP_PASS"]
to_email = "rjun212@gmail.com"

# Read HTML content
html_content = latest_file.read_text()

# Construct email
msg = MIMEMultipart("alternative")
msg["Subject"] = "⚡ Daily Clean Energy Digest"
msg["From"] = smtp_user
msg["To"] = to_email

part = MIMEText(html_content, "html")
msg.attach(part)

# Send email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.sendmail(smtp_user, to_email, msg.as_string())

print("✅ Email sent to", to_email)
