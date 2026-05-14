import json
import os

with open('net-wins-data.json', 'r', encoding='utf-8') as f:
    players = json.load(f)

if not os.path.exists('substack_drafts'):
    os.makedirs('substack_drafts')

for p in players:
    name = p['player']
    # Clean the name thoroughly for Windows filenames
    clean_name = name.lower().replace(' ', '-').replace('.', '').replace("'", "").strip()
    cite_url = f"https://willf123.github.io/nba-net-wins/players/{clean_name}.html"
    
    draft_content = f"# Player Profile: {name}\n\n## The Net Wins Verdict\n{p['ranking_logic']}\n\n[View on Site]({cite_url})"
    
    filepath = f'substack_drafts/{clean_name}-draft.md'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(draft_content)
    print(f"Created: {filepath}") # This will show you the individual files as they are made

print(f"\nDone! Check your folder for {len(players)} files.")