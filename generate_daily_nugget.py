# generate_daily_nugget.py
import datetime

# Simulated post for testing — replace this block with real scraping and formatting
today = datetime.datetime.now().strftime("%Y-%m-%d")
nugget = f"""### {today}
🇮🇳 RE India update:

• NTPC green ammonia wins at ₹51.8/kg  
• Haryana solarizes 2.2 lakh rooftops  
• Renewables +14.4%, hydro +22.4%, coal -4.2%

#IndiaRE #CleanEnergy
"""

with open("content/weekly-nuggets.md", "a") as f:
    f.write("\n" + nugget.strip() + "\n")