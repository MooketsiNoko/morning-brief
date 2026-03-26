from news import get_headlines
from sports import get_scores
from brief import generate_brief
from playlist import create_playlist


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
    create_playlist(vibe)
    print("=" * 50)


if __name__ == "__main__":
    run_morning_brief()