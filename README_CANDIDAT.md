# Refactoring - Gilded Rose (Python)

## Objectif
Refactorer le code du kata **Gilded Rose** en appliquant des principes de clean code, tout en conservant **strictement** le comportement existant.

## Demarche
1. Lecture des regles metier (README du kata)
2. Mise en place d'un filet de securite via tests (Approval / Golden Master)
3. Refactoring incremental (petits pas, tests verts)
4. Nettoyage et documentation

## Environnement Python (venv)
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Approche
- Lecture des regles et comprehension du comportement actuel.
- Mise en place/usage d'un golden master (ApprovalTests).
- Refactoring en petits pas avec tests verts.

## Commandes
```bash
python -m unittest
python tests/test_gilded_rose_approvals.py
python texttest_fixture.py 10
```

## Temps passe
- XX minutes (placeholder)
