#!/usr/bin/env python3
import os

# --- Lecture des cookies ---
cookies = {}
raw = os.environ.get("HTTP_COOKIE", "")
for part in raw.split(";"):
    part = part.strip()
    if "=" in part:
        k, v = part.split("=", 1)
        cookies[k.strip()] = v.strip()

side = cookies.get("side", "none")

# Couleurs selon le camp
if side == "sith":
    bg, fg, accent = "#0a0000", "#ff4444", "#cc0000"
elif side == "jedi":
    bg, fg, accent = "#00001a", "#44aaff", "#0055cc"
else:
    bg, fg, accent = "#111", "#eee", "#c0392b"

# --- Données du Top 5 ---
siths = [
    {
        "rank": 5,
        "name": "Dark Vador",
        "img": "/images/darkvador.gif",
        "desc": "Ancien Jedi devenu le bras droit de l'Empereur. Respiration légendaire, casque iconique, main mécanique. Le père de tous les méchants de cinéma.",
        "fun": "Il a construit C-3PO enfant. Oui vraiment."
    },
    {
        "rank": 4,
        "name": "Dark Maul",
        "img": "/images/Dark_Maul_face.webp",
        "desc": "Double sabre laser, visage tatoué rouge et noir, agilité surhumaine. Il est revenu d'entre les morts juste pour avoir sa revanche.",
        "fun": "A survécu à être coupé en deux. Respect."
    },
    {
        "rank": 3,
        "name": "Le Shit Web",
        "img": "/images/rastagwer.jpg",
        "desc": "Seigneur des erreurs 404, maître du HTML tordu et du CSS qui foire sur Firefox. Il a été invoqué lors d'un test de serveur web qui a mal tourné. Depuis, il hante les logs Apache et plante les requêtes des Jedis non avertis.",
        "fun": "Son seul pouvoir Force : faire crasher un serveur avec un seul GET mal formé."
    },
    {
        "rank": 2,
        "name": "Post Malone",
        "img": "/images/post_malone.jpg",
        "desc": "Personne ne sait comment il a atterri sur ce serveur web. Il était là, entre deux tests de routes HTTP, tatoué, chapeau de cowboy, bière à la main. Certains pensent qu'il EST le côté obscur. D'autres pensent que c'est juste une image de test qui a pris trop de place.",
        "fun": "Son endpoint préféré : POST /malone. Retourne toujours un 200 OK, même quand tout est en feu."
    },
    {
        "rank": 1,
        "name": "Les Siths aux cookies",
        "img": "/images/cookies.png",
        "desc": "Ces Siths légendaires ont raccroché leur sabre laser pour se consacrer à l'art suprême : faire des cookies au chocolat dans la salle du trône.",
        "fun": "Même Yoda admet que leurs cookies sont imbattables."
    },
]

print("Content-Type: text/html")
print()
print(f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Top 5 des Siths</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Crimson+Text:ital,wght@0,400;1,400&display=swap');

    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    body {{
      background-color: {bg};
      color: {fg};
      font-family: 'Crimson Text', serif;
      min-height: 100vh;
      padding: 40px 20px 60px;
    }}

    h1 {{
      font-family: 'Cinzel Decorative', serif;
      text-align: center;
      font-size: clamp(1.5rem, 5vw, 3rem);
      color: {accent};
      text-shadow: 0 0 20px {accent}99, 0 0 60px {accent}44;
      letter-spacing: 4px;
      margin-bottom: 8px;
    }}

    .subtitle {{
      text-align: center;
      color: #888;
      font-style: italic;
      margin-bottom: 40px;
      letter-spacing: 2px;
    }}

    /* Grille des mini images cliquables */
    .grid {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 20px;
      max-width: 900px;
      margin: 0 auto 50px;
    }}

    .card {{
      width: 150px;
      cursor: pointer;
      text-align: center;
      transition: transform 0.25s ease;
    }}

    .card:hover {{ transform: translateY(-8px); }}

    .card:hover .mini-img {{
      box-shadow: 0 0 0 3px {accent}, 0 0 25px {accent}88;
    }}

    .mini-img {{
      width: 150px;
      height: 150px;
      object-fit: cover;
      border-radius: 4px;
      border: 2px solid {accent}55;
      transition: box-shadow 0.25s ease;
      display: block;
      background: #1a1a2e;
    }}

    .mini-img-fallback {{
      width: 150px;
      height: 150px;
      border-radius: 4px;
      border: 2px solid {accent}55;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 3rem;
      background: linear-gradient(135deg, #1a0000, #2a0a0a);
      transition: box-shadow 0.25s ease;
    }}

    .card:hover .mini-img-fallback {{
      box-shadow: 0 0 0 3px {accent}, 0 0 25px {accent}88;
    }}

    .rank-badge {{
      font-family: 'Cinzel Decorative', serif;
      font-size: 0.85rem;
      color: {accent};
      margin-top: 8px;
      letter-spacing: 1px;
    }}

    .card-name {{
      font-size: 0.95rem;
      color: {fg};
      margin-top: 4px;
      line-height: 1.3;
    }}

    /* Panneau de détail */
    .detail-panel {{
      max-width: 620px;
      margin: 0 auto;
      background: rgba(255,255,255,0.04);
      border: 1px solid {accent}44;
      border-left: 4px solid {accent};
      border-radius: 3px;
      padding: 28px 32px;
      display: none;
      animation: fadeIn 0.3s ease;
    }}

    .detail-panel.visible {{ display: block; }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(10px); }}
      to   {{ opacity: 1; transform: translateY(0); }}
    }}

    .detail-panel h2 {{
      font-family: 'Cinzel Decorative', serif;
      font-size: 1.5rem;
      color: {accent};
      margin-bottom: 14px;
      text-shadow: 0 0 10px {accent}66;
    }}

    .detail-panel p {{
      font-size: 1.1rem;
      line-height: 1.7;
      color: #ccc;
      margin-bottom: 14px;
    }}

    .fun-fact {{
      font-style: italic;
      color: {accent}cc;
      font-size: 1rem;
      border-top: 1px solid {accent}33;
      padding-top: 12px;
      margin-top: 4px;
    }}

    .back-btn {{
      display: inline-block;
      margin-top: 40px;
      padding: 12px 32px;
      background: transparent;
      border: 1px solid {accent};
      color: {accent};
      font-family: 'Cinzel Decorative', serif;
      font-size: 0.85rem;
      letter-spacing: 2px;
      text-decoration: none;
      border-radius: 2px;
      transition: all 0.3s ease;
      text-align: center;
      display: block;
      max-width: 260px;
      margin: 40px auto 0;
    }}

    .back-btn:hover {{
      background: {accent};
      color: #fff;
      box-shadow: 0 0 20px {accent}66;
    }}
  </style>
</head>
<body>

<h1>⚔ TOP 5 DES SITHS ⚔</h1>
<p class="subtitle">Clique sur un Sith pour découvrir sa fiche</p>

<div class="grid">
""")

# Données encodées en JS pour le panneau dynamique
sith_data_js = "const siths = {\n"
for s in siths:
    name_js = s['name'].replace("'", "\\'")
    desc_js = s['desc'].replace("'", "\\'")
    fun_js  = s['fun'].replace("'", "\\'")
    sith_data_js += f"  {s['rank']}: {{ name: '{name_js}', desc: '{desc_js}', fun: '{fun_js}' }},\n"
sith_data_js += "};"

# Cartes cliquables
for s in siths:
    rank = s['rank']
    name_html = s['name']
    img = s['img']
    label = f"Top {rank}" if rank > 1 else "🏆 Top 1"
    print(f"""  <div class="card" onclick="showSith({rank})">
    <img class="mini-img" src="{img}" alt="{name_html}"
         onerror="this.style.display='none';this.nextElementSibling.style.display='flex'"/>
    <div class="mini-img-fallback" style="display:none">⚔️</div>
    <div class="rank-badge">{label}</div>
    <div class="card-name">{name_html}</div>
  </div>
""")

print(f"""</div>

<div class="detail-panel" id="detail">
  <h2 id="detail-name"></h2>
  <p id="detail-desc"></p>
  <p class="fun-fact" id="detail-fun"></p>
</div>

<a href="/" class="back-btn">← Retour au classement</a>

<script>
{sith_data_js}

function showSith(rank) {{
  const s = siths[rank];
  if (!s) return;
  document.getElementById('detail-name').textContent = 'Top ' + rank + ' — ' + s.name;
  document.getElementById('detail-desc').textContent = s.desc;
  document.getElementById('detail-fun').textContent = '💡 ' + s.fun;
  const panel = document.getElementById('detail');
  panel.classList.remove('visible');
  void panel.offsetWidth; // reset animation
  panel.classList.add('visible');
  panel.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
}}
</script>

</body>
</html>""")