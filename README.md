# Morning Brief AI

A personal morning assistant that pulls live news and sports scores, 
generates an AI-written daily digest in your tone, and curates a 
mood-matched playlist — all in one run.

## What it does

- 📰 Fetches top headlines across tech and sports via NewsAPI
- 🏀 Pulls live and recent scores for your teams via ESPN's API
- 🤖 Uses Claude (Anthropic) to write a personalized morning digest 
  and determine the day's vibe
- 🎵 Generates a 10-track mood-matched playlist with direct Spotify links

## Tech Stack

- **Python** — core logic
- **Anthropic Claude API** — brief generation + vibe detection + playlist curation
- **NewsAPI** — live headlines
- **ESPN API** — real-time scores
- **Spotipy + Spotify API** — playlist generation
- **python-dotenv** — environment variable management

## Setup

1. Clone the repo
```bash
   git clone https://github.com/MooketsiNoko/morning-brief.git
   cd morning-brief
```

2. Create a virtual environment and install dependencies
```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install requests python-dotenv anthropic spotipy
```

3. Create a `.env` file in the root with your API keys
```
   NEWS_API_KEY=your_news_api_key
   ANTHROPIC_API_KEY=your_anthropic_api_key
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
```

4. Customize your teams in `src/sports.py`
```python
   MY_TEAMS = ["Oklahoma City Thunder", "Dallas Cowboys", "Manchester City"]
```

5. Run it
```bash
   python src/main.py
```

## Example Output
```
🌅 YOUR MORNING BRIEF
Rise and grind gang, we got some juicy stuff today! Lakers are cooking 
the Pacers right now, up 126-113. Mo Salah officially leaving Liverpool 
after 9 years — emotional damage. Apple dropped iOS 26.4 with actually 
decent updates for once.

🎯 TODAY'S VIBE: CURIOUS

🎵 Morning Brief Playlist — Curious Vibe
  Mortal Man — Kendrick Lamar
  Broken Clocks — SZA
  Cellophane — FKA twigs
  ...
```

## Project Structure
```
morning-brief/
├── src/
│   ├── news.py        # fetches live headlines
│   ├── sports.py      # fetches live scores
│   ├── brief.py       # AI generates digest + detects vibe
│   ├── playlist.py    # AI curates mood-matched playlist
│   └── main.py        # runs everything together
├── .env               # API keys (not committed)
└── README.md
```
