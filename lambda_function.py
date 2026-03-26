import json
import sys
import os

# Add src to path so Lambda can find our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from news import get_headlines
from sports import get_scores
from brief import generate_brief
from playlist import create_playlist
from storage import save_brief_to_s3


def lambda_handler(event, context):
    try:
        print("⏳ Pulling today's data...")
        headlines = get_headlines()
        scores = get_scores()

        print("🤖 Generating brief...")
        brief, vibe = generate_brief(headlines, scores)

        print("🎵 Curating playlist...")
        playlist = create_playlist(vibe)

        print("☁️ Saving to S3...")
        save_brief_to_s3(brief, vibe, playlist)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Morning brief generated successfully",
                "vibe": vibe
            })
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }