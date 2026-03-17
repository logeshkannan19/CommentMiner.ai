# 💎 CommentMiner

**Stop guessing what your audience thinks. Start mining the gold in your comments.**

CommentMiner is an AI-powered intelligence layer designed for founders and creators who are tired of scrolling through thousands of YouTube comments. We don't just "show" you sentiment; we surface the actual product insights, requested features, and recurring pain points that are buried in the noise.

## ✨ What it does for you
- **Know the Vibe**: Get an instant, high-level sentiment score without reading a single line.
- **Surface Feature Ideas**: Automatically identify exactly what your users are asking for next.
- **Spot the Friction**: We catch the bugs and complaints before they become dealbreakers.
- **The Bigger Picture**: Summarized themes (like Pricing, UI, or Performance) so you can see the forest, not just the trees.

## 🚀 Built with
- **Frontend**: A minimal, lightning-fast dashboard (HTML/CSS/JS).
- **Backend**: Python's FastAPI—designed for speed and simplicity.
- **Engine**: Powered by OpenAI's GPT-4o-mini for deep contextual understanding.
- **Reality**: Pulls fresh data directly from the YouTube Data API v3.

## 🏁 Get it running in 2 minutes

### 1. Fire up the Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Drop your keys in .env
python main.py
```

### 2. Open the Dashboard
Just open `frontend/index.html` in your favorite browser. It's that simple. No complex builds required.

## 📂 Inside the Box
```text
CommentMiner/
├── backend/            # The brain: FastAPI & AI processing
├── frontend/           # The beauty: Simple, clean dashboard
├── docs/               # The blueprint: Architecture & Guides
└── README.md           # You are here
```

## 📄 License
MIT—Go build something cool with it.
