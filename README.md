# Morning Brief AI

A fully automated Gen Z toned personal morning assistant that runs every day at 6AM 
on AWS — no manual input required. Pulls live news and sports scores, 
generates an AI-written daily digest, curates a mood-matched playlist, 
and saves everything to the cloud.

## Architecture
```
CloudWatch (6AM daily)
        ↓
   AWS Lambda
        ↓
  ┌─────┴─────┐
  │           │
NewsAPI    ESPN API
  │           │
  └─────┬─────┘
        ↓
  Anthropic Claude
  (brief + vibe detection)
        ↓
  Anthropic Claude
  (playlist curation)
        ↓
     AWS S3
  (stores daily brief)
```

## What it does

- 📰 Fetches top headlines across tech and sports via NewsAPI
- 🏀 Pulls live and recent scores for your teams via ESPN's API
- 🤖 Uses Claude (Anthropic) to write a personalized morning digest
  and determine the day's vibe
- 🎵 Generates a 10-track mood-matched playlist with direct Spotify links
- ☁️ Saves each day's brief as JSON to AWS S3
- ⏰ Runs automatically every morning via CloudWatch + Lambda

## Tech Stack

- **Python** — core logic
- **AWS Lambda** — serverless compute
- **AWS S3** — cloud storage for daily briefs
- **AWS CloudWatch** — daily schedule trigger
- **Anthropic Claude API** — brief generation + vibe detection + playlist curation
- **NewsAPI** — live headlines
- **ESPN API** — real-time scores (no key required)
- **Spotipy + Spotify API** — playlist generation
- **python-dotenv** — environment variable management

## Project Structure
```
morning-brief/
├── src/
│   ├── news.py            # fetches live headlines
│   ├── sports.py          # fetches live scores
│   ├── brief.py           # AI generates digest + detects vibe
│   ├── playlist.py        # AI curates mood-matched playlist
│   ├── storage.py         # saves brief to AWS S3
│   └── main.py            # runs everything locally
├── lambda_function.py     # AWS Lambda entry point
├── trust-policy.json      # IAM role policy
├── .env                   # API keys (not committed)
└── README.md
```

## Running Locally

1. Clone the repo
```bash
   git clone https://github.com/MooketsiNoko/morning-brief.git
   cd morning-brief
```

2. Create a virtual environment and install dependencies
```bash
   python -m venv venv
   venv\Scripts\activate
   pip install requests python-dotenv anthropic spotipy boto3
```

3. Create a `.env` file with your API keys
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

## AWS Deployment

The app is deployed as a Lambda function triggered daily by CloudWatch Events.
API keys are stored as Lambda environment variables.
Each brief is saved to S3 at `s3://morning-brief-mooketsi/briefs/YYYY-MM-DD.json`

## Example Output
```
🌅 YOUR MORNING BRIEF
Rise and grind gang, we got some juicy stuff today! Lakers cooked the 
Pacers 137-130 last night — that offense was absolutely unhinged. 
Marvel Rivals confirmed for Switch 2, devs said "bet." Joe Flacco back 
with the Bengals because that man simply refuses to retire.

🎯 TODAY'S VIBE: HYPE

🎵 Morning Brief Playlist — Hype Vibe
  DNA. — Kendrick Lamar
  Sicko Mode — Travis Scott
  Big Energy — Latto
  ...
```
