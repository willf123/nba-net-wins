import json
import os

# Load your master data
with open('net-wins-data.json', 'r') as f:
    players = json.load(f)

# Create a folder for your drafts
if not os.path.exists('substack_drafts'):
    os.makedirs('substack_drafts')

for p in players:
    name = p['player']
    filename = name.lower().replace(' ', '-').replace('.', '')
    cite_url = f"https://willf123.github.io/nba-net-wins/players/{filename}.html"
    
    draft_content = f"""
# Player Profile: {name}
    
## The Net Wins Verdict
{p['ranking_logic']}

## Key Metrics
- **Career Net Wins:** {p['net_wins_career']}
- **Peak Season:** {p['peak_performance']}

## Talk to the Data
Copy and paste this into Claude or ChatGPT to discuss this profile:
"Using the data at {cite_url}, explain why {name} ranks where he does in the Net Wins era-normalization model."

[View full interactive chart →](https://willf123.github.io/nba-net-wins/)
    """
    
    # Find this section at the bottom of your script:
with open(f'substack_drafts/{filename}-draft.md', 'w', encoding='utf-8') as f:
    f.write(draft_content)

print(f"Success! 176 Substack drafts generated in /substack_drafts/")