# Advanced 01 – Minimal Flask API

Build a tiny JSON API.

## Endpoints

* `/hello` → `{"message":"Hello, World"}`
* `/square/<int:n>` → returns the square of `n`

### Stretch

* `/hello?name=Alice` → personalize message
* Error handling for non‑int input

## Run

```bash
pip install -r requirements.txt
python app.py
```
