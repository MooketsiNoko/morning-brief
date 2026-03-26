import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_brief(headlines, scores):
    # Format headlines for the prompt
    headlines_text = "\n".join(
        [f"- [{h['topic'].upper()}] {h['title']}: {h['description']}" for h in headlines]
    )

    # Format scores for the prompt
    if scores:
        scores_text = "\n".join(
            [f"- {g['teams']} ({g['status']}): " +
             ", ".join([f"{t}: {s}" for t, s in g['scores'].items()])
             for g in scores]
        )
    else:
        scores_text = "No games for your teams today."

    prompt = f"""
You are a personal morning brief assistant with a Gen Z personality — sassy but masculine sassy, hyped, 
and unfiltered but never mean. You talk like a friend who's way too online. Use casual 
language, light slang, and energy like you just woke up and already know what's good. 
Open with a hype phrase like "we back at it," "rise and grind gang," "up and at em," 
or something in that energy — never just "Morning!" Keep it real, keep it moving.
Based on the news and sports scores below, do two things:

1. Write a short, engaging morning digest (4-6 sentences max). Hit the most 
   interesting headlines and any relevant scores. Make it feel like a smart 
   friend is catching you up, not a news anchor.

2. Based on the overall vibe of today's news and scores, pick ONE mood from 
   this list that best fits the morning and explain in one sentence why:
   - HYPE (big wins, exciting news, good energy)
   - FOCUSED (neutral day, time to lock in)
   - CHILL (slow news day, relaxed vibe)
   - MOTIVATED (losses or setbacks, time to bounce back)
   - CURIOUS (lots of interesting/surprising stories)

Format your response exactly like this:
BRIEF:
<your morning digest here>

VIBE:
<chosen mood in caps>: <one sentence reason>

Here's today's data:

HEADLINES:
{headlines_text}

SCORES:
{scores_text}
"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    response_text = message.content[0].text

    # Parse out the brief and vibe separately
    brief = ""
    vibe = ""

    if "BRIEF:" in response_text and "VIBE:" in response_text:
        brief = response_text.split("BRIEF:")[1].split("VIBE:")[0].strip()
        vibe = response_text.split("VIBE:")[1].strip().split(":")[0].strip()

    return brief, vibe


if __name__ == "__main__":
    from news import get_headlines
    from sports import get_scores

    headlines = get_headlines()
    scores = get_scores()
    brief, vibe = generate_brief(headlines, scores)

    print("=== YOUR MORNING BRIEF ===")
    print(brief)
    print(f"\n=== TODAY'S VIBE: {vibe} ===")