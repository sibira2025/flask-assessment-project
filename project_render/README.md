# Assessment App Template (Flask + Docker + Render)

## Quick Start (Local)
```bash
pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5000
```

## Docker (One Command)
```bash
docker-compose up
# open http://localhost:5000
```

## Deploy to Render
1) Push this folder to a **public GitHub repo**.
2) Ensure `requirements.txt` contains both `flask` and `gunicorn`.
3) Sign in at https://render.com → New → Web Service → Connect your repo.
4) Build Command: `pip install -r requirements.txt`
5) Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
6) Choose **Free** plan → Deploy.
7) Copy the public URL for your demo submission.
