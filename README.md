# Serveur-Django-rest — API REST du catalogue Skstore

API REST en lecture seule réalisée avec **Django REST Framework** pour exposer le catalogue de la boutique de sneakers [Skstore](https://github.com/EdNganji/Skstore) : marques, articles et stocks par magasin.

## Endpoints

| Méthode | URL | Description |
|---|---|---|
| GET | `/api/Brand/` | Liste des marques |
| GET | `/api/Brand/<id>/` | Détail d'une marque |
| GET | `/api/Item/` | Liste des articles |
| GET | `/api/Item/<id>/` | Détail d'un article |
| GET | `/api/Stock/` | Stocks par magasin |
| GET | `/api/Stock/<id>/` | Détail d'un stock |

L'interface d'administration est disponible sur `/admin/` et la connexion à l'API navigable sur `/api-auth/`.

## Modèle de données

| Modèle | Champs |
|---|---|
| `Brand` | nom, image, courriel du fournisseur, numéro |
| `Item` | nom, image, prix, marque |
| `Shop` | nom, adresse, articles (via `Stock`) |
| `Stock` | magasin, article, quantité |

## Technologies

- Python, Django 3.2
- Django REST Framework
- SQLite, Pillow (images)

## Installation

```bash
python -m venv venv
source venv/bin/activate          # Windows : venv\Scripts\activate
pip install "django>=3.2,<4" djangorestframework pillow
python manage.py migrate
python manage.py runserver
```

Puis ouvrir http://127.0.0.1:8000/api/Item/

> Le fichier `skstore/serializers.py` (sérialiseurs `BrandSerializer`, `ItemSerializer`, `StockSerializer`) doit être présent pour que l'API démarre.

## Auteur

**Daniel Nganjip** — projet réalisé en 2023.
