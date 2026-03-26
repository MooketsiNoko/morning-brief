import boto3
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

BUCKET_NAME = "morning-brief-mooketsi"  # update if you named it differently


def save_brief_to_s3(brief: str, vibe: str, playlist: list):
    s3 = boto3.client("s3")

    today = datetime.now().strftime("%Y-%m-%d")

    data = {
        "date": today,
        "vibe": vibe,
        "brief": brief,
        "playlist": playlist
    }

    filename = f"briefs/{today}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=json.dumps(data, indent=2),
        ContentType="application/json"
    )

    print(f"✅ Brief saved to S3: s3://{BUCKET_NAME}/{filename}")
    return filename


def get_brief_from_s3(date: str = None):
    s3 = boto3.client("s3")

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    filename = f"briefs/{date}.json"

    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=filename)
        data = json.loads(response["Body"].read().decode("utf-8"))
        return data
    except s3.exceptions.NoSuchKey:
        print(f"No brief found for {date}")
        return None


if __name__ == "__main__":
    # Test it with dummy data
    test_playlist = [{"track": "Mortal Man", "artist": "Kendrick Lamar", "link": "https://spotify.com"}]
    save_brief_to_s3("This is a test brief", "CURIOUS", test_playlist)

    # Read it back
    result = get_brief_from_s3()
    print("Retrieved from S3:", result)