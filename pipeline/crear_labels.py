import requests
import time

GITHUB_TOKEN = "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"
REPO = "marolyrb-valorp/proj-rionegro-capacidades"

API = f"https://api.github.com/repos/{REPO}/labels"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

LABELS = [
    {"name": "clasificación:FUNDAMENTAL", "color": "d73a4a"},
    {"name": "clasificación:IMPORTANTE", "color": "f9a825"},
    {"name": "clasificación:COMPLEMENTARIA", "color": "0075ca"},
    {"name": "clasificación:REFERENCIA", "color": "cccccc"},
    {"name": "celda:analítica-individual", "color": "1f77b4"},
    {"name": "celda:analítica-organizacional", "color": "1f77b4"},
    {"name": "celda:analítica-sistémico", "color": "1f77b4"},
    {"name": "celda:operativa-individual", "color": "ff7f0e"},
    {"name": "celda:operativa-organizacional", "color": "ff7f0e"},
    {"name": "celda:operativa-sistémico", "color": "ff7f0e"},
    {"name": "celda:política-individual", "color": "2ca02c"},
    {"name": "celda:política-organizacional", "color": "2ca02c"},
    {"name": "celda:política-sistémico", "color": "2ca02c"},
    {"name": "comparabilidad:alta", "color": "0e8a16"},
    {"name": "comparabilidad:media", "color": "fbca04"},
    {"name": "comparabilidad:baja", "color": "e4e669"},
    {"name": "comparabilidad:nula", "color": "cccccc"},
    {"name": "estado:pendiente", "color": "ffffff"},
    {"name": "estado:ficha-generada", "color": "c2e0c6"},
    {"name": "estado:revisada", "color": "0075ca"},
    {"name": "estado:integrada", "color": "0e8a16"},
    {"name": "P1:incluir", "color": "0e8a16"},
    {"name": "P2:marco-teórico", "color": "1f77b4"},
    {"name": "P3:metodología", "color": "ff7f0e"},
    {"name": "P4:indicadores", "color": "9467bd"},
]

print(f"Creando {len(LABELS)} labels...")
for label in LABELS:
    resp = requests.post(API, headers=HEADERS, json=label)
    if resp.status_code == 201:
        print(f"  ✓ {label['name']}")
    elif resp.status_code == 422:
        print(f"  - {label['name']} (ya existe)")
    else:
        print(f"  ✗ {label['name']} — Error: {resp.status_code}")
    time.sleep(0.5)

print("Listo!")