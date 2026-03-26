import anthropic
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

VIBE_DESCRIPTIONS = {
    "HYPE": "high energy rap and hip hop bangers, hype tracks, crowd pleasers",
    "FOCUSED": "lofi hip hop, study beats, calm instrumental, focus music",
    "CHILL": "mellow r&b, chill vibes, laid back hip hop, afternoon grooves",
    "MOTIVATED": "underdog anthems, comeback tracks, motivational rap, grind music",
    "CURIOUS": "genre-blending tracks, new discoveries, eclectic mix, interesting finds",
}

def get_spotify_link(track: str, artist: str) -> str:
    query = urllib.parse.quote(f"{track} {artist}")
    return f"https://open.spotify.com/search/{query}"

def create_playlist(vibe: str):
    vibe_desc = VIBE_DESCRIPTIONS.get(vibe, VIBE_DESCRIPTIONS["FOCUSED"])

    prompt = f"""You are a music curator with incredible taste. 
Generate a playlist of exactly 10 songs that match this vibe: {vibe_desc}

Rules:
- Mix well known and underrated tracks
- Vary the artists, no repeats
- Lean towards hip hop, r&b, and rap but sprinkle in other genres if it fits the vibe
- Return ONLY a numbered list in this exact format, nothing else:
1. Track Name - Artist Name
2. Track Name - Artist Name
(and so on)"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    response_text = message.content[0].text
    lines = [l.strip() for l in response_text.strip().split("\n") if l.strip()]

    print(f"\n🎵 Morning Brief Playlist — {vibe.capitalize()} Vibe\n")
    print("Open any track on Spotify:\n")

    playlist = []
    for line in lines:
        # Strip the number prefix
        if ". " in line:
            track_info = line.split(". ", 1)[1]
            if " - " in track_info:
                track, artist = track_info.split(" - ", 1)
                link = get_spotify_link(track.strip(), artist.strip())
                print(f"  {track.strip()} — {artist.strip()}")
                print(f"  🔗 {link}\n")
                playlist.append({
                    "track": track.strip(),
                    "artist": artist.strip(),
                    "link": link
                })

    return playlist


if __name__ == "__main__":
    create_playlist("CURIOUS")