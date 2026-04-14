#!/usr/bin/env python3

import os

cookies = {}
raw = os.environ.get("HTTP_COOKIE", "")
for part in raw.split(";"):
    part = part.strip()
    if "=" in part:
        k, v = part.split("=", 1)
        cookies[k.strip()] = v.strip()

side = cookies.get("side", "none")

if side == "sith":
    bg_img, bg, fg, title = "/images/Dark_Maul_face.webp", "#1a0000", "#ff4444", "🔴 Bienvenue, Seigneur Sith"
elif side == "jedi":
    bg_img, bg, fg, title = "/images/obiwankenobite.webp", "#00001a", "#4af", "🔵 Que la Force soit avec toi, Jedi"
else:
    bg_img, bg, fg, title = "/images/galaxie.jpg", "#111", "#eee", "⚔️ Choisis ton camp"

print("Content-Type: text/html")
print()
print(f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8"/>
  <style>
    body {{ background-image: url({bg_img}); background-color: {bg};
            background-position: center;
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: {fg}; font-family: sans-serif; text-align: center; padding: 4rem; }}
    button {{ background: {fg}; color: {bg}; border: none; padding: 1rem 2rem; font-size: 1.2rem; cursor: pointer; margin: 1rem; }}
  </style>
</head>
<body>
  <h1>{title}</h1>
  <form action="/cgi-bin/enterDarkSide.php" method="get">
    <button type="submit">Rejoins le côté obscur de la Force</button>
  </form>
  <form action="/cgi-bin/enterBrightSide.py" method="get">
    <button type="submit">Rejoins le côté lumineux de la Force</button>
  </form>
  <form action="/cgi-bin/resetSide.py" method="get">
    <button type="submit">Redevenir un honnête citoyen</button>
  </form>
</body>
</html>""")
