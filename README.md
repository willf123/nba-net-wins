# NBA Net Wins Analyzer

A career comparison tool built around an original basketball statistic.

**[🔗 Live site →](https://willf123.github.io/nba-net-wins)**  
**[📬 Weekly player profiles on Substack →](https://netwins.substack.com)**

---

## The Statistic

Net Wins measures a player's contextual contribution to their team's wins and losses — normalizing individual performance against what it actually costs a team to win or lose that season.

Most advanced stats (PER, Win Shares, VORP) measure production in a vacuum. Net Wins ties a player's positive and negative actions directly to the team's actual win/loss record, so the same stat line means more on a dominant team and less on a losing one.

**Important note on methodology:** Net Wins is a contextual efficiency metric, not a causal wins-added stat. It does not isolate individual causation from team quality — a player on a 60-win team is measured against a 60-win context. This is intentional. Use avg/season and peak season metrics alongside career totals to compare players across different team environments.

---

## Formula

**Step 1 — Team win rate (positive)**
```
Team positive actions = PTS + REB + AST + BLK + STL
Win rate = Team positive actions ÷ Wins
```

**Step 2 — Team loss rate (negative)**
```
Team negative actions = Missed FG + Missed FT + Turnovers + Personal Fouls
Loss rate = Team negative actions ÷ Losses
```

**Step 3 — Player wins**
```
Player positive actions = PTS + REB + AST + BLK + STL
Player wins = Player positive actions ÷ Team win rate
```

**Step 4 — Player losses**
```
Player negative actions = Missed FG + Missed FT + Turnovers + Personal Fouls
Player losses = Player negative actions ÷ Team loss rate
```

**Step 5 — Net Wins**
```
Net Wins = Player Wins − Player Losses
```

### Example — Cade Cunningham, 2025-26

| | Value |
|---|---|
| Detroit wins | 60 |
| Team positive actions | 15,540 |
| Team win rate | 259.0 per win |
| Cade positive actions | 2,666 |
| Player wins | 10.36 |
| Detroit losses | 22 |
| Team negative actions | 7,333 |
| Team loss rate | 333.3 per loss |
| Cade negative actions | 1,145 |
| Player losses | 3.44 |
| **Net Wins** | **6.92** |

---

## Database

**226 players · all eras (1946–2026) · ABA included · 143 Hall of Famers tagged**

Players span from the BAA/early NBA era through the 2025-26 season. ABA seasons are stored separately and applied with a user-adjustable discount (default 90%, slider 50–100%) to account for league strength differences.

Pre-1974 seasons have BLK and STL estimated at 0 by default (amber highlight in the UI) — fully editable so you can enter your own estimates and recalculate.

### Top 10 by combined Net Wins (reg season + playoffs + ABA × 90%)

| Rank | Player | Combined |
|------|--------|----------|
| 1 | Kareem Abdul-Jabbar | 144.0 |
| 2 | Tim Duncan | 143.5 |
| 3 | LeBron James | 126.7 |
| 4 | Larry Bird | 106.1 |
| 5 | Magic Johnson | 103.6 |
| 6 | Shaquille O'Neal | 101.7 |
| 7 | Karl Malone | 97.7 |
| 8 | Tony Parker | 96.9 |
| 9 | Bill Russell | 93.5 |
| 10 | Scottie Pippen | 93.4 |

---

## Features

- **Career chart** — compare up to 5 players on the same season timeline
- **Season table** — editable BLK/STL for pre-1974 seasons
- **Full library rankings** — 226 players, sortable by combined/reg/playoff/ABA/avg/top-3/peak, filterable by position and era
- **ABA discount slider** — adjust ABA season weighting 50–100%, rankings update live
- **HOF badge** — Hall of Fame inductees flagged throughout the UI
- **Composite ranking** — equal-weight score across combined NW, avg/season, and top-3 avg
- **100% client-side** — no backend, no API, works offline

---

## Design Decisions

**Why team context matters:** A player who scores 30 points on a team that scores 120 per game contributes less proportionally than one who scores 25 on a team that scores 95. Net Wins captures this by anchoring each player's output to what their team needed to win.

**Why personal fouls count as negatives:** Fouls extend possessions for opponents, put them at the line, and remove players from the game. They're a real cost that most metrics ignore.

**ABA discount:** ABA seasons are stored separately and multiplied by a user-adjustable factor (default 0.90) to reflect the generally accepted view that the ABA was a slightly weaker league. The slider lets you apply your own judgment.

**Pre-1974 estimation:** BLK and STL weren't officially recorded before 1973-74. Affected cells are highlighted amber and fully editable — enter your own estimates and recalculate to update the career line.

---

## Built With

- Vanilla JavaScript — no frameworks
- Chart.js for career line charts
- All data compiled from public NBA/ABA records and team season logs

---

## About

Created by Will Fiore as an original analytics project exploring player value through a win-contextualized lens.

- **Live tool:** [willf123.github.io/nba-net-wins](https://willf123.github.io/nba-net-wins)
- **Substack:** [netwins.substack.com](https://netwins.substack.com) — weekly player profiles and formula breakdowns
- **GitHub:** [github.com/willf123](https://github.com/willf123)

Net Wins is an original statistic. Feedback, corrections, and pull requests welcome.
