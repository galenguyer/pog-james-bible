import re
import json

# https://stackoverflow.com/a/24894475
def rep(text, word, replacement):
    def func(match):
        g = match.group()
        if g.islower(): return replacement.lower()
        if g.istitle(): return replacement.title()
        if g.isupper(): return replacement.upper()
        return replacement      
    return re.sub(word, func, text, flags=re.IGNORECASE)

raw = {}
with open('raw.json', 'r') as fd:
    raw = json.loads(fd.read())

bible = {}
for key, value in raw.items():
    book = key.rsplit(' ', 1)[0]
    if book not in bible:
        bible[book] = {}
    chapter = key.rsplit(' ', 1)[1].split(':')[0]
    verse = key.rsplit(' ', 1)[1].split(':')[1]
    if chapter not in bible[book]:
        bible[book][chapter] = []
    if len(bible[book][chapter]) == 0 or value.startswith('#'):
        bible[book][chapter].append({})
    val = rep(value, "^# ", "")
    val = rep(val, "in us", "among us")
    val = rep(val, "\\bsin\\b", "cringe")
    val = rep(val, "\\bsins\\b", "cringes")
    val = rep(val, "\\bsinner\\b", "cringer")
    val = rep(val, "\\bsinners\\b", "cringers")
    val = rep(val, "\\bsinned\\b", "cringed")
    val = rep(val, "\\bsinneth\\b", "cringeth")
    val = rep(val, "\\bsinfun\\b", "cringeful")
    bible[book][chapter][len(bible[book][chapter])-1][verse] = val

with open('bible.json', 'w') as fd:
    fd.write(json.dumps(bible, indent=2))
