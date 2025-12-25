# Refactoring – Gilded Rose (Python)

## 🎯 Objectif

Refactorer le code du kata **Gilded Rose** en appliquant des principes de *clean code* et de refactoring incrémental, **sans modifier le comportement existant**, tout en démontrant une démarche professionnelle adaptée à un contexte de code legacy.

---

## 🧠 Démarche suivie

### 1. Analyse du code existant

* Lecture du code pour comprendre son fonctionnement global.
* Identification des parties complexes ou à risque (conditions imbriquées, logique difficile à suivre).

### 2. Mise en place d’un filet de sécurité (Golden Master)

* Mise en place d’**Approval Tests** afin de capturer le comportement actuel du programme.
* Génération d’un fichier de référence (`approved.txt`) servant de base de comparaison.
* Toute modification ultérieure est validée uniquement si le comportement reste strictement identique.

> Cette approche permet de refactorer en toute sécurité, même sans connaître tous les détails métier au départ.

### 3. Nettoyage des tests existants

* Suppression du test `test_foo`, qui n’apportait pas de réelle valeur.
* Ajout d’un test smoke simple pour vérifier que l’application fonctionne correctement dans son ensemble.

### 4. Ajout de tests métier lisibles

* Création de tests unitaires couvrant les règles principales :

  * bornes de qualité (0 à 50)
  * comportement de **Sulfuras**
  * évolution de **Aged Brie**
  * logique des **Backstage passes**
* Le cas **Conjured** est volontairement marqué comme *skipped*, car il n’est pas géré dans la version actuelle du code.

### 5. Refactoring incrémental sécurisé

* Refactorisation par petites étapes, toujours protégée par les tests.
* Extraction de fonctions utilitaires pour améliorer la lisibilité.
* Aucun changement de comportement : tous les tests restent verts à chaque étape.

## 🧩 Résumé des étapes de refactoring

### ✅ Étape 1 — Nettoyage de base et sécurisation (`gilded_rose.py`)

**Objectif :** rendre le code plus lisible sans modifier son comportement.

- Ajout de constantes (`AGED_BRIE`, `BACKSTAGE`, `SULFURAS`) pour éviter les chaînes magiques.
- Clarification des fonctions utilitaires (`_increase_quality`, `_decrease_quality`).

---

### ✅ Étape 2 — Extraction de la logique dans une méthode dédiée (`gilded_rose.py`)

**Objectif :** structurer le code sans en modifier le comportement.

- Extraction de la logique métier dans une méthode `_update_item`.
- La méthode `update_quality()` devient plus lisible et plus expressive.
- Le comportement reste strictement identique (tests inchangés).

---

### ✅ Étape 3 — Simplification des conditions redondantes (`gilded_rose.py`)

**Objectif :** réduire la complexité sans changer le résultat.

- Suppression des vérifications inutiles (`if quality < 50`, `if quality > 0`).
- Ces contrôles sont déjà garantis par `_increase_quality` et `_decrease_quality`.

---

### ✅ Étape 4 — Découpage en méthodes métier (lisibilité + intention) (`gilded_rose.py`)

**Objectif :** rendre la logique facile à comprendre en séparant clairement les responsabilités, sans changer le comportement.

- Découpage de `_update_item` en 3 phases explicites :
  - `_update_quality_before_sell_in(item)`
  - `_decrement_sell_in(item)`
  - `_apply_expired_rules(item)`
- Extraction des règles par type d’item dans des méthodes dédiées :
  - `_update_regular_item(item)`
  - `_update_aged_brie(item)`
  - `_update_backstage(item)`
- Réduction forte de l’imbrication des `if` grâce à des *guard clauses* (`return`), tout en gardant exactement la même logique.

---

### ✅ Étape 5 — Nettoyage et structuration du script de test (`texttest_fixture.py`)

**Objectif :** améliorer la lisibilité et la maintenabilité du script de test sans modifier son comportement ni casser les *approval tests* existants.

- Séparation claire des responsabilités dans le fichier :
  - création des données (`build_items`)
  - gestion des arguments (`parse_days`)
  - affichage des résultats (`print_day`)
- Suppression du code inline dans `main` au profit de fonctions explicites.
- Conservation stricte du format de sortie afin de garantir la compatibilité avec les fichiers d’approbation existants.
- Aucun changement fonctionnel : les résultats produits restent strictement identiques.

---

## 🧪 Tests & vérifications

### Commandes principales

```bash
python -m unittest
python tests/test_gilded_rose_approvals.py
python texttest_fixture.py 10
```

Ces commandes permettent de vérifier :

* l’absence de régression fonctionnelle,
* la cohérence des règles métier,
* la stabilité globale du comportement.

---

## ⚙️ Environnement Python

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🧱 Choix techniques assumés

* **Golden Master** pour sécuriser le refactoring.
* **Refactoring incrémental**, avancement par petites étapes pour limiter les risques.
* **Tests lisibles** servant aussi de documentation.
* **Pas de sur-ingénierie** : priorité à la clarté et à la stabilité.

---

## 🚀 Perspective d’évolution

Une fois le comportement totalement sécurisé, les prochaines étapes possibles seraient :

* mise en place d’une vraie architecture orientée objet par type d’item,
* suppression progressive des conditions complexes,
* ajout d’un support complet pour les items Conjured,
* amélioration globale de la lisibilité et de la maintenabilité.

---

## ⏱️ Temps passé

Environ **2h00**, incluant :

* l’analyse du code existant,
* mise en place des tests,
* refactoring progressif,
* rédaction de la documentation.

---

## ✅ Résultat final

Un code :

* fiable et sécurisé,
* plus lisible et maintenable,
* prêt à évoluer sans risque,
* reflétant une démarche professionnelle de refactoring.
