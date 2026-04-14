#!/usr/bin/env python3
import os

cookies = {}
raw = os.environ.get("HTTP_COOKIE", "")
for part in raw.split(";"):
    part = part.strip()
    if "=" in part:                          # ← bug corrigé (était désaligné)
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
<html lang="fr">
<head>
  <meta charset="UTF-8"/>
  <style>
    body {{
      background-image: url({bg_img});
      background-color: {bg};
      background-position: center;
      background-size: cover;
      background-repeat: no-repeat;
      background-attachment: fixed;
      color: {fg};
      font-family: sans-serif;
      text-align: center;
      padding: 4rem;
    }}
    button {{
      background: {fg};
      color: {bg};
      border: none;
      padding: 1rem 2rem;
      font-size: 1.2rem;
      cursor: pointer;
      margin: 1rem;
    }}

    /* Bouton Top 5 Siths */
    .btn-top5 {{
      display: inline-block;
      margin-top: 2.5rem;
      padding: 1rem 2.5rem;
      background: transparent;
      border: 2px solid #c0392b;
      color: #ff4444;
      font-size: 1.1rem;
      font-weight: bold;
      cursor: pointer;
      letter-spacing: 2px;
      text-decoration: none;
      transition: background 0.3s, color 0.3s, box-shadow 0.3s;
      box-shadow: 0 0 12px #c0392b55;
    }}
    .btn-top5:hover {{
      background: #c0392b;
      color: #fff;
      box-shadow: 0 0 28px #c0392baa;
    }}
    .btn-top5-label {{
      display: block;
      margin-top: 0.5rem;
      font-size: 0.85rem;
      color: #888;
      font-style: italic;
    }}
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

  <!-- Bouton vers le Top 5 des Siths -->
  <div style="margin-top: 2rem;">
    <a href="/cgi-bin/top5.py" class="btn-top5">⚔ TOP 5 DES SITHS ⚔</a>
    <span class="btn-top5-label">Clique sur les Siths pour découvrir leur fiche</span>
  </div>

</body>
</html>""")