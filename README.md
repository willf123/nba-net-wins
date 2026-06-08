# NBA Net Wins Explorer

A full-database career comparison tool built around an original basketball statistic.

🔗 [Live site →](https://willf123.github.io/nba-net-wins)
📬 [Weekly player profiles on Substack →](https://netwins.substack.com)
🎙 [Net Wins Podcast on Substack →](https://netwins.substack.com/podcast)

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

**Step 2 — Team net actions (denominator)**

```
Sum of all positive player net actions on the roster that season
```

Only positive individual net actions count toward the denominator. Players with negative net actions contribute 0 to both numerator and denominator (floor rule), preventing them from artificially inflating a teammate's share.

**Step 3 — Net Wins**

```
Net Wins = (Player net actions ÷ Team net actions) × Team wins
```

A player's share of the team's net statistical margin, multiplied by what that margin produced in the win column.

### Example — Cade Cunningham, 2025-26

| | Value |
|---|---|
| Detroit wins | 60 |
| Team net actions | 9,720 |
| Cade net actions | 1,521 |
| Player share | 15.6% |
| **Net Wins** | **9.39** |

### Edge cases

- **Negative net actions:** Floored at 0 — player contributes nothing to numerator or denominator.
- **Playoff swept teams:** Effective wins set to 1 minimum so Net Wins remain non-zero for players on swept teams.
- **ABA quality:** All ABA regular season and ABA playoff Net Wins are multiplied by a user-adjustable discount (default 90%, slider 50–100%).

---

## Database

**5,018 players · all eras (1946–2026) · NBA + ABA · 148 Hall of Famers tagged**

43,117 player-season rows sourced from public NBA and ABA records, covering:

- NBA regular seasons: 1946-47 through 2025-26 (80 seasons)
- NBA playoffs: all 80 playoff years
- ABA regular seasons: 1967-68 through 1975-76 (9 seasons)
- ABA playoffs: all 9 ABA playoff years

Multi-team rows (2TM/3TM/TOT) are stored but excluded from Net Wins calculations — only individual team stints are used.

### Missing stat handling

| Stat | Missing before | Default assumption | Adjustable |
|---|---|---|---|
| BLK / STL | 1973-74 | 0 per game | Yes — per-player slider |
| TRB | 1950-51 | 4.9 per game | Yes — per-player slider |
| TOV | 1977-78 | League-avg multiplier | Yes — global slider |

Rows with estimated stats are flagged with an orange dot in the explorer. Adjusting a slider recalculates that player's Net Wins and proportionally rebalances all teammates in that season.

### Top 10 by combined Net Wins (reg season + playoffs + ABA × 90%)

| Rank | Player | Combined |
|---|---|---|
| 1 | LeBron James | 335.4 |
| 2 | Kareem Abdul-Jabbar | 288.8 |
| 3 | Tim Duncan | 271.0 |
| 4 | Wilt Chamberlain | 264.0 |
| 5 | Karl Malone | 258.5 |
| 6 | Bill Russell | 229.3 |
| 7 | Shaquille O'Neal | 222.2 |
| 8 | Michael Jordan | 220.4 |
| 9 | Kevin Garnett | 216.1 |
| 10 | Kobe Bryant | 210.1 |

---

## Features

- **Career Comparison Chart** — compare up to 8 players on the same season timeline (Chart.js line chart, reg season Net Wins by year)
- **All-Time Rankings table** — all 5,000+ players, sortable by Combined / Reg Season / Playoffs / Avg per season / Avg top 3 / Peak; filterable by position (G/F/C) and name
- **Player search with chips** — live autocomplete from the full database, quick-add groups by era (GOATs, 80s/90s, Classic era, Role players+, Modern)
- **Explorer table** — search, filter by season / position / type (reg/playoffs/ABA), sort by any stat column, paginated
- **Expandable rows** — team, age, games, MPG, and per-player assumption sliders for flagged seasons
- **ABA discount slider** — adjust ABA season weighting 50–100%, all values update live
- **Pre-1974 BLK/STL sliders** — per-player, per-season estimates that recompute Net Wins and rebalance teammates
- **Pre-1978 TOV correction** — global multiplier slider with sensible default
- **Net Wins only filter** — hide rows where Net Wins couldn't be calculated
- **HOF badges** — throughout the explorer and rankings
- **100% client-side** — no backend, no API, no data sent anywhere, works offline

---

## Data Files

Two standalone JSON files are available in this repo alongside the HTML:

- **`nba_net_wins_data.json`** — all 43,117 player-season rows with column definitions and formula notes
- **`nba_team_wins.json`** — season → team abbreviation → wins lookup (NBA + ABA, reg + playoffs)

---

## Design Decisions

**Why team context is preserved:** A player who produces 1,500 net actions on a team with 10,000 net actions owns 15% of that margin. On a 60-win team, that's 9 Net Wins. On a 20-win team with the same stats, it's fewer — because the team's margin converted to fewer wins. This is intentional: Net Wins rewards players who produced efficiently *and* whose teams turned that production into victories.

**Why personal fouls count as negatives:** Fouls extend possessions for opponents, put them at the free throw line, and remove players from the game. They are a real cost that most metrics ignore.

**Why the denominator uses only positive individual net actions:** Using raw team totals would allow players with negative net actions to inflate the denominator, overstating their teammates' shares. Using only positive contributors ensures the roster exactly sums to team wins.

**ABA discount:** ABA seasons are multiplied by a user-adjustable factor (default 0.90) to reflect the generally accepted view that the ABA was a slightly weaker league. The slider lets you apply your own judgment.

**Pre-1974 estimation:** BLK and STL weren't officially recorded before 1973-74. Affected rows are flagged with an orange dot and carry per-player sliders — adjust and recalculate live.

**Pre-1978 TOV correction:** Turnovers weren't tracked before 1977-78. The correction multiplies the negatives portion of the formula to compensate for missing TOV data. Default derived from post-1977 league-average TOV share.

---

## Built With

- Vanilla JavaScript — no frameworks
- Chart.js for career comparison line charts
- All data compiled from public NBA/ABA records

---

## About

Created by **Will Fiore** as an original analytics project exploring player value through a win-contextualized lens.

- **Live tool:** [willf123.github.io/nba-net-wins](https://willf123.github.io/nba-net-wins)
- **Substack:** [netwins.substack.com](https://netwins.substack.com) — weekly player profiles and formula breakdowns
- **Podcast:** [Net Wins on Substack](https://netwins.substack.com/podcast) — audio companion
- **GitHub:** [github.com/willf123](https://github.com/willf123)

© 2026 Will Fiore. Net Wins formula and all written content are original works. All rights reserved.

Net Wins is an original statistic. Feedback, corrections, and pull requests welcome.
