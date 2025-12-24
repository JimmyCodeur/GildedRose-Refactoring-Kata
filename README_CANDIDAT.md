# Refactoring – Gilded Rose (Python)

## 🎯 Objectif
Refactorer le code du kata **Gilded Rose** en appliquant des principes de *clean code* et de refactoring incrémental, **sans modifier le comportement existant**, et en démontrant une démarche professionnelle adaptée à du code legacy.

---

## 🧠 Démarche suivie

1. **Exécution du code existant**
   - Lancement des tests fournis et de la fixture texte afin de comprendre le comportement initial du système.

2. **Mise en place d’un filet de sécurité (Golden Master)**
   - Utilisation d’**Approval Tests** pour figer le comportement actuel du code.
   - Promotion de la sortie générée comme référence officielle (`approved.txt`).
   - Validation systématique du refactor via les approval tests.

3. **Nettoyage des tests existants**
   - Suppression du test placeholder (`test_foo`) non pertinent.
   - Remplacement par un test *smoke* simple validant l’API publique.

4. **Ajout de tests métier lisibles**
   - Tests unitaires couvrant les règles principales :
     - bornes de qualité (0 à 50)
     - comportement de Sulfuras
     - évolution de Aged Brie
     - règles spécifiques des Backstage passes
   - Le cas **Conjured** est volontairement marqué comme *skipped* car non géré dans le comportement legacy actuel.

5. **Refactoring incrémental**
   - Refactor par petits pas, protégés par les tests.
   - Extraction de fonctions helpers :
     - identification des types d’items
     - gestion centralisée de l’augmentation/diminution de la qualité
   - Aucune modification fonctionnelle : tous les tests (unitaires + approval) restent verts.

---

## 🧪 Tests & vérifications

### Commandes principales
```bash
python -m unittest
python tests/test_gilded_rose_approvals.py
python texttest_fixture.py 10
```

Ces commandes permettent de vérifier :

* les règles métier via tests unitaires
* l’absence de régression via le Golden Master
* la conformité de la sortie texte attendue

---

## ⚙️ Environnement Python

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🧱 Choix techniques

* **Refactoring incrémental** : petits changements, commits atomiques.
* **Approval Tests (Golden Master)** pour sécuriser le comportement legacy.
* **Tests métier lisibles** servant de documentation vivante.
* **Aucune réécriture prématurée** : priorité à la sécurité et à la lisibilité.

---

## ⏱️ Temps passé

* Environ **1h30** (incluant analyse, tests, refactor et documentation)

---

## ✅ Résultat

Un code :

* sécurisé par des tests
* plus lisible et maintenable
* prêt à être étendu (ex : ajout futur de Conjured)
* avec un historique de commits reflétant une démarche professionnelle
