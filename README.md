# NBA Net Wins Analyzer

A career comparison tool built around an original basketball statistic.

🔗 [Live site →](https://willf123.github.io/nba-net-wins)
📬 [Weekly player profiles on Substack →](https://netwins.substack.com)
🎙 [Net Wins Podcast on Substack →](https://netwins.substack.com)

---

## The Statistic

**Net Wins** measures a player's share of their team's net statistical margin, scaled to how many wins that margin actually produced.

Most advanced stats (PER, Win Shares, VORP) measure production in a vacuum. Net Wins anchors a player's positive and negative actions to the team's actual net margin — so the same stat line is worth more on a team that converts its margin efficiently into wins, and less on one that doesn't.

**Important note on methodology:** Net Wins is a contextual share metric, not a causal wins-added stat. It does not isolate individual causation from team quality — a player on a 60-win team earns a share of 60 wins. Team context is preserved by design, not removed. Use avg/season and peak season metrics alongside career totals to compare players across different team environments.

---

## Formula

**Step 1 — Player net actions**

```
Player net actions = (PTS + REB + AST + BLK + STL) − (Missed FG + Missed FT + TOV + PF)
```

**Step 2 — Team net actions**

```
Team net actions = Team positive actions − Team negative actions
(same formula applied to the full roster's season totals)
```

**Step 3 — Net Wins**

```
Net Wins = (Player net actions ÷ Team net actions) × Team wins
```

That's it. A player's share of the team's net statistical margin, multiplied by what that margin produced in the win column.

### Example — Cade Cunningham, 2025-26

| | Value |
|---|---|
| Detroit wins | 60 |
| Team net actions | 9,720 |
| Cade net actions | 1,521 |
| Player share | 15.6% |
| **Net Wins** | **9.39** |

### Edge case handling

For seasons where a team's net actions total falls below 1,000 — fewer than 2% of the 1,818 team-seasons in the database — the season's league-median net actions figure is substituted to prevent division instability. Affected seasons are flagged in the underlying data.

---

## Database

**316 players · all eras (1946–2026) · ABA included · 148 Hall of Famers tagged**

Players span from the BAA/early NBA era through the 2025-26 season. ABA seasons are stored separately and applied with a user-adjustable discount (default 90%, slider 50–100%) to account for league strength differences.

Pre-1974 seasons have BLK and STL set to 0 by default (amber highlight in the UI) — fully editable so you can enter your own estimates and recalculate.

### Top 10 by combined Net Wins (reg season + playoffs + ABA × 90%)

| Rank | Player | Combined |
|---|---|---|
| 1 | LeBron James | 351.8 |
| 2 | Kareem Abdul-Jabbar | 321.2 |
| 3 | Tim Duncan | 287.7 |
| 4 | Karl Malone | 267.9 |
| 5 | Wilt Chamberlain | 255.1 |
| 6 | Kevin Garnett | 231.7 |
| 7 | Dirk Nowitzki | 230.4 |
| 8 | Shaquille O'Neal | 229.3 |
| 9 | Michael Jordan | 220.0 |
| 10 | Kobe Bryant | 210.1 |

---

## Features

- **Career chart** — compare up to 5 players on the same season timeline
- **Season table** — editable BLK/STL for pre-1974 seasons, live recalculation
- **Full library rankings** — 316 players, sortable by combined/reg/playoff/ABA/avg/top-3/peak, filterable by position and era
- **ABA discount slider** — adjust ABA season weighting 50–100%, rankings update live
- **Pre-1977 TOV correction** — slider to adjust for missing turnover data in pre-1977 seasons (default 1.29×, reflects league-average TOV share derived from post-1977 data)
- **Composite weighted ranking** — user-adjustable weights across combined NW, avg/season, top-3 avg, and peak (default: 50/20/20/10). Includes number inputs and sliders, always sums to 100%
- **HOF badge** — Hall of Fame inductees flagged throughout the UI
- **100% client-side** — no backend, no API, works offline

---

## Design Decisions

**Why team context is preserved:** A player who produces 1,500 net actions on a team with 10,000 net actions owns 15% of that margin. On a 60-win team, that's 9 net wins. On a 20-win team with the same stats, it's fewer — because the team's margin converted to fewer wins. This is intentional: Net Wins rewards players who produced efficiently *and* whose teams turned that production into victories.

**Why personal fouls count as negatives:** Fouls extend possessions for opponents, put them at the free throw line, and remove players from the game. They are a real cost that most metrics ignore.

**ABA discount:** ABA seasons are stored separately and multiplied by a user-adjustable factor (default 0.90) to reflect the generally accepted view that the ABA was a slightly weaker league. The slider lets you apply your own judgment.

**Pre-1974 estimation:** BLK and STL weren't officially recorded before 1973-74. Affected cells are highlighted amber and fully editable — enter your own estimates and recalculate to update the career line.

**Pre-1977 TOV correction:** Turnovers weren't tracked before 1977-78, meaning pre-1977 team net actions are missing roughly 23% of negative actions. The correction slider scales the team net actions denominator to compensate, making each recorded negative action cost proportionally more. Default 1.29× reflects the league-average TOV share derived from post-1977 data.

---

## Built With

- Vanilla JavaScript — no frameworks
- Chart.js for career line charts
- All data compiled from public NBA/ABA records and season logs

---

## About

Created by **Will Fiore** as an original analytics project exploring player value through a win-contextualized lens.

- **Live tool:** [willf123.github.io/nba-net-wins](https://willf123.github.io/nba-net-wins)
- **Substack:** [netwins.substack.com](https://netwins.substack.com) — weekly player profiles and formula breakdowns
- **Podcast:** Net Wins on Substack — audio companion to the Substack
- **GitHub:** [github.com/willf123](https://github.com/willf123)

Net Wins is an original statistic. Feedback, corrections, and pull requests welcome.
