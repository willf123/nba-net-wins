# NBA Net Wins Analyzer

**A career comparison tool built around an original basketball statistic.**

🔗 **[Live site →](https://willf123.github.io/nba-net-wins)**

---

## The Statistic

**Net Wins** measures a player's contextual contribution to their team's wins and losses — normalizing individual performance against what it actually costs a team to win or lose that season.

Most advanced stats (PER, Win Shares, VORP) measure production in a vacuum. Net Wins ties a player's positive and negative actions directly to the team's actual win/loss record, so the same stat line means more on a dominant team and less on a losing one.

### Formula

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
| **Player wins** | **10.36** |
| Detroit losses | 22 |
| Team negative actions | 7,333 |
| Team loss rate | 333.3 per loss |
| Cade negative actions | 1,145 |
| **Player losses** | **3.44** |
| **Net Wins** | **6.92** |

---

## Features

- **64 players** across all eras (1950–2026)
- Career chart — compare up to 5 players on the same timeline
- Season table — editable BLK/STL for pre-1974 seasons (blocks and steals weren't tracked before 1973-74)
- Rankings tab — sort selected players by career net wins, avg per season, or peak season
- Full library rankings — filter by position, era, or sort metric
- 100% client-side — no backend, no API calls, works offline

---

## Design Decisions

**Why team context matters:** A player who scores 30 points on a team that scores 120 per game has contributed less proportionally than one who scores 25 on a team that scores 95. Net Wins captures this by anchoring each player's output to what their specific team needed to win.

**Why personal fouls count as negatives:** Fouls extend possessions for opponents, put them at the line, and remove players from the game. They're a real cost — though tactical fouls in specific situations could be refined further.

**Pre-1974 estimation:** BLK and STL weren't officially recorded before the 1973-74 season. Cells for those seasons are highlighted in amber and fully editable — you can enter your own estimates (e.g., Bill Russell at 6 blocks/game × 70 games = 420) and hit Recalculate to update the entire career line.

---

## Player Library

| Era | Players |
|---|---|
| Early NBA (1950–1969) | Bob Cousy, Bob Pettit, Elgin Baylor, Bill Russell, Wilt Chamberlain, Willis Reed, Jerry West, Oscar Robertson |
| 1970s | John Havlicek, Kareem Abdul-Jabbar, Julius Erving, George Gervin, Pete Maravich, Rick Barry, Moses Malone, Elvin Hayes |
| 1980s–90s | Magic Johnson, Larry Bird, Michael Jordan, Isiah Thomas, Charles Barkley, Patrick Ewing, Karl Malone, John Stockton, Scottie Pippen, Hakeem Olajuwon, David Robinson, Clyde Drexler, Kevin McHale, Dominique Wilkins, Gary Payton, Reggie Miller, Allen Iverson |
| 2000s | Kobe Bryant, Tim Duncan, Shaquille O'Neal, Kevin Garnett, Dirk Nowitzki, Dwyane Wade, Jason Kidd, Steve Nash, Ray Allen, Tony Parker, Carmelo Anthony, Chris Paul |
| Modern | LeBron James, Stephen Curry, Kevin Durant, Giannis Antetokounmpo, Nikola Jokic, James Harden, Russell Westbrook, Kawhi Leonard, Anthony Davis, Joel Embiid, Luka Dončić, Damian Lillard, Jayson Tatum, Kyrie Irving, Paul George, Jimmy Butler, Klay Thompson, Dwight Howard, Cade Cunningham |

---

## Built With

- Vanilla JavaScript — no frameworks
- Chart.js for the career line chart
- All data compiled from public NBA records and team season logs

---

## About

Created by **Will Fiore** as an original analytics project exploring player value through a win-contextualized lens.

- GitHub: [github.com/willf123](https://github.com/willf123)
- Portfolio: [github.com/willf123/dbt-analytics-portfolio](https://github.com/willf123/dbt-analytics-portfolio)

---

*Net Wins is an original statistic. Feedback, corrections, and pull requests welcome.*
