# OuterWorldsWiki
Project to help fill out the OuterWorlds videogame wiki page using ChatGPT

We expect data to be nested in this format:

```
OuterWorlds/
├── Logs/
│   ├── Logs1_Img.jpg
│   └── Logs1_1.jpg
└── Terminals/
    ├── Terminal1_1.jpg
    └── Terminal1_2.jpg
```

# Getting Started
1. Add OpenAI Key to .env (OPENAI_API_KEY)
2. Install dependencies
```
pip install uv
uv sync
```

# How to run
```
cd src
uv run app.py
```