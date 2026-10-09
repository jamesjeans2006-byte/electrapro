# ElectraPro — update package for the EXISTING repository

This package is intended to update the existing GitHub repository:
`jamesjeans2006-byte/electrapro` on branch `main`.
It is **not** a new repository and does not require creating a separate website.

## Files in this update
- `app.py` — replaces the existing app interface
- `content/curriculum.py` — subject maps, lesson content, quizzes, glossary and references
- `content/__init__.py` — Python package marker
- `requirements.txt` — Streamlit dependency
- `README.md` — deployment and project notes

## Update the existing repository
1. Download and extract this ZIP on your device.
2. Open the existing repository: https://github.com/jamesjeans2006-byte/electrapro
3. Replace `app.py` with the package's `app.py`.
4. In the repository, create/open the `content` folder and add/replace `curriculum.py` and `__init__.py`.
5. Replace `requirements.txt` and `README.md`.
6. Commit changes to the existing `main` branch.
7. Streamlit Community Cloud should redeploy the existing app. If it does not, open the existing app's Manage app page and reboot it.

Do not delete the old deployed app or create a new repository. Keep a copy of the existing files until the update is verified.

## Local run
`pip install -r requirements.txt`
`streamlit run app.py`

## Scope and accuracy
This release has structured subject maps and 24 authored lessons across the curriculum, including worked examples, key points, questions, practice prompts and references where appropriate. The topic maps show the broader curriculum, but this is not a claim that every advanced subtopic in electrical engineering is exhaustively covered. Expand the lesson library iteratively and validate technical calculations against current standards and manufacturer documentation.

This is educational content, not a substitute for qualified engineering design, official standards, safe-work procedures, certification advice or professional supervision. Copyrighted textbook chapters are not reproduced.
