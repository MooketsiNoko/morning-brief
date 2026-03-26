from news import get_headlines
from sports import get_scores
from brief import generate_brief
from playlist import create_playlist
from storage import save_brief_to_s3


def run_morning_brief():
    print("⏳ Pulling today's data...\n")
    headlines = get_headlines()
    scores = get_scores()

    print("🤖 Generating your morning brief...\n")
    brief, vibe = generate_brief(headlines, scores)

    print("=" * 50)
    print("🌅 YOUR MORNING BRIEF")
    print("=" * 50)
    print(brief)
    print(f"\n🎯 TODAY'S VIBE: {vibe}")
    print("=" * 50)

    print("\n⏳ Curating your playlist...\n")
    playlist = create_playlist(vibe)
    print("=" * 50)

    print("\n☁️  Saving to AWS S3...\n")
    save_brief_to_s3(brief, vibe, playlist)


if __name__ == "__main__":
    run_morning_brief()