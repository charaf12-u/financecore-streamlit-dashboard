# 📊 FinDash — Financial Analytics Dashboard

> **Turning Financial Data into Decisions**

FinDash est un tableau de bord analytique multipage développé avec **Streamlit**, connecté à une base de données **PostgreSQL**. Il permet aux décideurs financiers de visualiser les performances des transactions, d'analyser les risques clients et d'exporter les données filtrées — le tout en temps réel.

---

## 📸 Aperçu du Projet

### 🔹 Executive View — Vue Générale des Performances

| KPIs & Transactions | Segmentation & CA | Export & Summary |
|---|---|---|
| ![exec1](asset/images/image_project/Capture%20d’écran%202026-04-17%20154424.png) | ![exec2](asset/images/image_project/Capture%20d’écran%202026-04-17%20154515.png) | ![exec3](asset/images/image_project/Capture%20d’écran%202026-04-17%20154537.png) |

### 🔸 Risk Analysis — Analyse des Risques Clients

| Heatmap Corrélation | Scatter Plot Risques | Top Clients à Risque |
|---|---|---|
| ![risk1](asset/images/image_project/Capture%20d’écran%202026-04-17%20154601.png) | ![risk2](asset/images/image_project/Capture%20d’écran%202026-04-17%20154621.png) | ![risk3](asset/images/image_project/Capture%20d’écran%202026-04-17%20154639.png) |

---

## 🏗️ Architecture du Projet

```
dashboard_analytics_multipages/
│
├── app.py                          # Point d'entrée principal de l'application
├── requirements.txt                # Dépendances Python
├── .env                            # Variables d'environnement (non versionné)
├── .gitignore                      # Fichiers exclus du versioning Git
│
├── pages/
│   ├── ExecutiveView_page.py       # Page 1 : Vue Executive (KPIs + graphiques)
│   └── RiskAnalysis_page.py        # Page 2 : Analyse des risques clients
│
├── core/
│   ├── db_connection.py            # Connexion SQLAlchemy à PostgreSQL
│   ├── queries.py                  # Requête SQL principale (JOIN multi-tables)
│   ├── filters.py                  # Logique de filtrage des données
│   ├── kpis.py                     # Calcul des indicateurs clés (KPIs)
│   └── risk_engine.py              # Moteur de classification des risques
│
├── components/
│   ├── kpi_cards.py                # Affichage des cartes métriques
│   ├── charts.py                   # Graphiques Executive View (line, bar, pie)
│   └── risk_chart.py               # Graphiques Risk Analysis (heatmap, scatter)
│
├── utils/
│   ├── data_processing.py          # Pipeline ETL : chargement, nettoyage, features
│   └── logger.py                   # Système de logging centralisé
│
├── asset/
│   ├── styles.css                  # CSS personnalisé du dashboard
│   └── images/
│       ├── findash_logo.png        # Logo principal
│       ├── icon.png                # Icône de l'onglet navigateur
│       └── image_project/          # Captures d'écran du projet
│
├── .streamlit/
│   └── config.toml                 # Configuration du thème Streamlit
│
├── logs/                           # Fichiers de logs générés automatiquement
└── json_planification/
    └── plan.json                   # Fichier de planification du projet
```

---

## ⚙️ Prérequis

Avant de lancer le projet, assurez-vous d'avoir installé :

| Outil | Version recommandée |
|---|---|
| Python | ≥ 3.9 |
| PostgreSQL | ≥ 13 |
| pip | Dernière version |

---

## 🚀 Guide d'Installation et d'Utilisation

### Étape 1 — Cloner le dépôt

```bash
git clone https://github.com/votre-username/dashboard_analytics_multipages.git
cd dashboard_analytics_multipages
```

---

### Étape 2 — Créer un environnement virtuel

```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement (Windows)
venv\Scripts\activate

# Activer l'environnement (macOS / Linux)
source venv/bin/activate
```

---

### Étape 3 — Installer les dépendances

```bash
pip install -r requirements.txt
```

Les bibliothèques installées :

| Bibliothèque | Rôle |
|---|---|
| `streamlit` | Framework web du dashboard |
| `plotly` | Visualisations interactives |
| `pandas` | Manipulation des données |
| `sqlalchemy` | ORM pour la connexion à la base de données |
| `psycopg2-binary` | Driver PostgreSQL pour Python |

---

### Étape 4 — Configurer la base de données PostgreSQL

Assurez-vous que votre base de données PostgreSQL est lancée et que le schéma `financecore_db` existe avec les tables suivantes :

- `transaction` — Données des transactions financières
- `client` — Informations clients (score crédit, taux d'intérêt, catégorie risque)
- `segment_client` — Segments des clients
- `produit` — Produits financiers
- `categorie_produit` — Catégories de produits
- `agence` — Agences bancaires
- `devise` — Devises utilisées
- `statut_transaction` — Statuts des transactions
- `type_operation` — Types d'opérations bancaires
- `anomalie` — Détection d'anomalies

---

### Étape 5 — Configurer les variables d'environnement

Créez un fichier `.env` à la racine du projet avec vos identifiants de connexion :

```env
DB_USER=postgres
DB_PASSWORD=votre_mot_de_passe
DB_HOST=localhost
DB_PORT=5432
DB_NAME=financecore_db
```

> ⚠️ **Important** : Ne partagez jamais ce fichier `.env` ! Il est déjà exclu via `.gitignore`.

---

### Étape 6 — Lancer l'application

```bash
streamlit run app.py
```

L'application sera accessible dans votre navigateur à l'adresse :

```
http://localhost:8501
```

---

## 🖥️ Fonctionnalités du Dashboard

### 🔹 Sidebar — Filtres Globaux

La barre latérale permet de filtrer **toutes les visualisations** simultanément :

| Filtre | Type | Description |
|---|---|---|
| **AGENCE** | Multiselect | Filtrer par agences bancaires |
| **SEGMENT CLIENT** | Multiselect | Filtrer par segment de clientèle |
| **PRODUIT** | Multiselect | Filtrer par type de produit financier |
| **YEAR** | Slider | Sélectionner une plage d'années |

---

### 📊 Page 1 — Executive View

Vue synthétique des performances financières globales.

#### 🔢 KPIs Affichés en Temps Réel
- **TRANSACTION** — Nombre total de transactions uniques
- **REVENUE (€)** — Chiffre d'affaires total en euros
- **CLIENTS ACTIFS** — Nombre de clients uniques actifs
- **MARGE MOYENNE** — Marge calculée via `montant × taux_interet`

#### 📈 Graphiques
| Graphique | Description |
|---|---|
| **Évolution des Transactions** | Line chart : CA mensuel par type d'opération |
| **Segmentation Clients** | Pie chart : Répartition des clients par segment |
| **CA par Agence** | Bar chart : Chiffre d'affaires par agence |
| **CA par Produit** | Bar chart : Chiffre d'affaires par produit |

#### 💾 Export des Données
- Bouton **"Download CSV"** pour télécharger le dataset filtré
- Nom du fichier exporté : `financecore_filtered_data.csv`

#### 📝 Executive Summary
- Affiche automatiquement une indication de tendance financière :
  - 📈 *Positive financial trend detected* — si la moyenne est positive
  - ⚠️ *Negative financial trend detected* — si la moyenne est négative

---

### 🔸 Page 2 — Risk Analysis

Analyse approfondie du risque financier des clients.

#### ⚡ Moteur de Classification des Risques
Chaque client est classé automatiquement selon la règle suivante :

| Condition | Niveau de Risque |
|---|---|
| `score_credit < 400` ET `montant_eur > 5000` | 🔴 **High Risk** |
| `score_credit < 700` | 🟡 **Medium Risk** |
| Sinon | 🟢 **Low Risk** |

#### 📊 Graphiques
| Graphique | Description |
|---|---|
| **Heatmap de Corrélation** | Corrélation entre `score_credit`, `montant_eur` et `taux_interet` |
| **Risk Scatter Plot** | Nuage de points : score_credit vs montant, coloré par type de transaction |

#### 🏆 Top 10 Clients à Risque
Tableau interactif affichant les 10 clients les plus à risque, triés par :
- Montant le plus élevé (décroissant)
- Score crédit le plus bas (croissant)

Colonnes affichées : `client_id`, `score_credit`, `montant_eur`, `categorie_risque`

---

## 🔄 Pipeline de Données (ETL)

Le flux de traitement des données suit ce pipeline :

```
PostgreSQL DB
     │
     ▼
load_data()          → Exécute la requête SQL (JOIN 9 tables)
     │
     ▼
clean_data()         → Conversion dates, gestion nulls, suppression doublons
     │
     ▼
feature_engineering() → Création colonnes : year, month, transaction_type
     │
     ▼
validate_data()      → Vérification shape, logs des anomalies
     │
     ▼
@st.cache_data       → Mise en cache Streamlit (évite les rechargements)
     │
     ▼
Dashboard            → Affichage interactif
```

---

## 📁 Système de Logs

L'application génère automatiquement des logs dans le dossier `logs/` :

```
logs/
├── app_YYYY-MM-DD.log
├── pages/
│   └── ...
```

Types de logs utilisés :
- `log_info()` — Informations de fonctionnement normal
- `log_warning()` — Avertissements (données vides, valeurs nulles)
- `log_error()` — Erreurs critiques avec traceback

---

## 🛠️ Technologies Utilisées

| Technologie | Usage |
|---|---|
| **Python 3.9+** | Langage principal |
| **Streamlit** | Framework web & interface utilisateur |
| **Plotly Express** | Visualisations interactives |
| **Pandas** | Manipulation & analyse des données |
| **SQLAlchemy** | Connexion ORM à PostgreSQL |
| **psycopg2** | Driver natif PostgreSQL |
| **PostgreSQL** | Base de données relationnelle |

---

## 👤 Auteur

**Charaf** — Formation Data Analyst @ Simplon  
Projet réalisé dans le cadre du parcours de formation **Data Analytics**

---

> *FinDash — Turning Financial Data into Decisions* 🚀
