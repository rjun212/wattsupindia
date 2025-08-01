import datetime

rss_template = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Watts Up India – Daily Digest</title>
    <link>https://humanofcleantech.substack.com</link>
    <description>Automated daily digest on clean energy.</description>
    <pubDate>{pub_date}</pubDate>
    <item>
      <title>Watts Up India – Daily Digest {pub_date}</title>
      <link>https://humanofcleantech.substack.com</link>
      <guid>{guid}</guid>
      <pubDate>{pub_date}</pubDate>
      <description><![CDATA[
<h2>Indian Power Sector News</h2>
<h3>## Market & Industry</h3>
<ul>
  <li><b>Tesla taps LG Energy for next–gen battery module for India</b></li>
  <li><b>Greenko plans $2B investment in pumped hydro and wind hybrid facility</b></li>
</ul>
<h3>## Policy & Regulation</h3>
<ul>
  <li><b>MNRE launches state solar portal compliance guidelines</b></li>
</ul>
<h3>## Research & Analysis</h3>
<ul>
  <li><b>CEEW report finds grid-scale storage 30% cheaper by 2030</b></li>
</ul>
<h3>## Upcoming Events</h3>
<ul>
  <li>Renewables India Expo, Aug 15–17, Greater Noida</li>
</ul>
]]></description>
    </item>
  </channel>
</rss>
"""

now = datetime.datetime.utcnow()
pub_date = now.strftime("%a, %d %b %Y %H:%M:%S +0000")
guid = str(int(now.timestamp() * 1000))

xml_output = rss_template.format(pub_date=pub_date, guid=guid)

with open("watts-up-india-digest.xml", "w", encoding="utf-8") as f:
    f.write(xml_output)

print("✅ RSS digest generated.")
