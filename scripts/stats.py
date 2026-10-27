"""Render assets/github-stats.svg from live GitHub data.

Counts private contributions too (the public stats cards can't see them).
Run from the repo root:  python3 scripts/stats.py
Needs the GitHub CLI (`gh`) logged in as the profile owner.
"""
import datetime, html, json, subprocess
from collections import Counter

USER = "manthan291999"
QUERY = """
query($login: String!) { user(login: $login) {
  repositories(ownerAffiliations: OWNER, first: 100) { totalCount nodes {
    isPrivate isFork languages(first: 10, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name } } } } }
  contributionsCollection {
    totalCommitContributions totalPullRequestContributions totalIssueContributions
    totalRepositoryContributions restrictedContributionsCount
    contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } } }
}}"""

data = json.loads(subprocess.check_output(
    ["gh", "api", "graphql", "-f", f"query={QUERY}", "-F", f"login={USER}"]))["data"]["user"]
cc = data["contributionsCollection"]
cal = cc["contributionCalendar"]
weeks = [w["contributionDays"] for w in cal["weeks"]]
days = [d for w in weeks for d in w]
repos = data["repositories"]

langs = Counter()
for r in repos["nodes"]:
    if not r["isFork"]:
        for e in r["languages"]["edges"]:
            langs[e["node"]["name"]] += e["size"]
total_bytes = sum(langs.values())
top = langs.most_common(5)
other = total_bytes - sum(v for _, v in top)

best = run = 0
for d in days:
    run = run + 1 if d["contributionCount"] else 0
    best = max(best, run)
active = sum(1 for d in days if d["contributionCount"])
peak = max(d["contributionCount"] for d in days)

# ---- palette: text tokens, single-hue sequential ramp, validated categorical (dark) ----
SURFACE, TEXT, TEXT2, MUTED, LINE = "#0d1117", "#e6edf3", "#c9d1d9", "#8b949e", "#30363d"
ACCENT = "#7ee787"
RAMP = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
CATS = ["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181"]
OTHER = "#6e7681"
FONT = "'JetBrains Mono','SF Mono',Menlo,Consolas,monospace"


def level(n):
    if n == 0:
        return 0
    q = n / peak
    return 1 if q <= 0.25 else 2 if q <= 0.5 else 3 if q <= 0.75 else 4


W, H = 900, 420
o = []
esc = html.escape
today = datetime.date.today()
o.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="GitHub activity: {cal['totalContributions']} contributions in the last year across {repos['totalCount']} repositories">
  <title>GitHub activity for {USER}: {cal['totalContributions']} contributions in the last year, {repos['totalCount']} repositories, {active} active days</title>
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1117"/><stop offset="1" stop-color="#161b22"/></linearGradient></defs>
  <style>text {{ font-family: {FONT}; }} .lbl {{ font-size: 11px; fill: {MUTED}; }}</style>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="url(#bg)" stroke="{LINE}" stroke-width="1.5"/>
  <text x="28" y="34" fill="{MUTED}" style="font-size:12px">github.<tspan fill="{ACCENT}">activity</tspan>(last_12_months)</text>
  <text x="{W-28}" y="34" text-anchor="end" class="lbl">updated {today:%d %b %Y}</text>
''')

# ---- stat tiles ----
tiles = [
    (cal["totalContributions"], "contributions", f"{cc['restrictedContributionsCount']} in private repos"),
    (repos["totalCount"], "repositories", f"{sum(not r['isPrivate'] for r in repos['nodes'])} public"),
    (active, "active days", f"best streak {best} days"),
    (len(langs), "languages", f"most used: {top[0][0]}"),
]
tw, gap, tx = 200, 13, 28
for i, (val, name, sub) in enumerate(tiles):
    x = tx + i * (tw + gap)
    o.append(f'''  <g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{0.15*i:.2f}s" dur="0.6s" fill="freeze"/>
    <rect x="{x}" y="52" width="{tw}" height="84" rx="10" fill="{SURFACE}" stroke="{LINE}"/>
    <rect x="{x}" y="52" width="3" height="84" rx="1.5" fill="{ACCENT}"/>
    <text x="{x+18}" y="90" fill="{TEXT}" style="font-size:30px;font-weight:700">{val}</text>
    <text x="{x+18}" y="110" fill="{TEXT2}" style="font-size:12px;font-weight:700">{esc(name)}</text>
    <text x="{x+18}" y="126" class="lbl">{esc(sub)}</text>
  </g>
''')

# ---- contribution heatmap ----
cs, step = 11, 14
hx, hy = (W - len(weeks) * step) // 2 + 12, 178
for wi, week in enumerate(weeks):
    first = datetime.date.fromisoformat(week[0]["date"])
    if first.day <= 7 and wi < len(weeks) - 1:
        o.append(f'  <text x="{hx + wi*step}" y="{hy-8}" class="lbl">{first:%b}</text>\n')
    for d in week:
        dow = (datetime.date.fromisoformat(d["date"]).weekday() + 1) % 7  # Sunday = 0
        lv = level(d["contributionCount"])
        o.append(f'  <rect x="{hx + wi*step}" y="{hy + dow*step}" width="{cs}" height="{cs}" rx="2.5" fill="{RAMP[lv]}">'
                 f'<title>{d["contributionCount"]} on {d["date"]}</title></rect>\n')
for dow, name in [(1, "Mon"), (3, "Wed"), (5, "Fri")]:
    o.append(f'  <text x="{hx-10}" y="{hy + dow*step + 9}" text-anchor="end" class="lbl">{name}</text>\n')
ly = hy + 7 * step + 16
breakdown = (f"{cc['totalCommitContributions']} public commits · {cc['totalRepositoryContributions']} repos created · "
             f"{cc['totalPullRequestContributions']} PRs · {cc['restrictedContributionsCount']} private")
o.append(f'  <text x="{hx}" y="{ly+9}" class="lbl">{esc(breakdown)}</text>\n')
lx = W - 28 - (len(RAMP) * 14 + 70)
o.append(f'  <text x="{lx}" y="{ly+9}" class="lbl">Less</text>\n')
for i, c in enumerate(RAMP):
    o.append(f'  <rect x="{lx + 34 + i*14}" y="{ly}" width="{cs}" height="{cs}" rx="2.5" fill="{c}"/>\n')
o.append(f'  <text x="{lx + 34 + len(RAMP)*14 + 4}" y="{ly+9}" class="lbl">More</text>\n')

# ---- languages: stacked bar, 2px surface gaps, direct labels ----
by = ly + 46
o.append(f'  <text x="28" y="{by-12}" fill="{TEXT2}" style="font-size:12px;font-weight:700">languages <tspan class="lbl" style="font-weight:400">by code size, all repos</tspan></text>\n')
bw = W - 56
segs = [(n, v, CATS[i]) for i, (n, v) in enumerate(top)] + ([("Other", other, OTHER)] if other else [])
x = 28.0
for i, (n, v, c) in enumerate(segs):
    w = bw * v / total_bytes - (2 if i < len(segs) - 1 else 0)
    o.append(f'  <rect x="{x:.1f}" y="{by}" width="{max(w,2):.1f}" height="12" rx="3" fill="{c}"/>\n')
    x += w + 2
lx = 28
for n, v, c in segs:
    label = f"{n} {100*v/total_bytes:.1f}%"
    o.append(f'  <circle cx="{lx+5}" cy="{by+33}" r="5" fill="{c}"/>'
             f'<text x="{lx+15}" y="{by+37}" fill="{TEXT2}" style="font-size:12px">{esc(n)} <tspan fill="{MUTED}">{100*v/total_bytes:.1f}%</tspan></text>\n')
    lx += 15 + len(label) * 7.6 + 22

o.append("</svg>\n")
open("assets/github-stats.svg", "w").write("".join(o))
print(f"wrote assets/github-stats.svg · {cal['totalContributions']} contributions, {repos['totalCount']} repos")
