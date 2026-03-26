import requests

# Your teams — edit these to whatever you follow
MY_TEAMS = ["Manchester City", "Dallas Cowboys", "Manchester United", "Los Angeles Lakers"]

def get_scores():
    results = []

    url = "https://site.api.espn.com/apis/site/v2/sports"
    leagues = [
        ("basketball", "nba"),
        ("football", "nfl"),
        ("soccer", "eng.1")
    ]

    for sport, league in leagues:
        response = requests.get(f"{url}/{sport}/{league}/scoreboard")
        data = response.json()

        for event in data.get("events", []):
            competitors = event["competitions"][0]["competitors"]
            team_names = [c["team"]["displayName"] for c in competitors]

            # Only keep games involving your teams
            if any(team in team_names for team in MY_TEAMS):
                scores = {c["team"]["displayName"]: c["score"] for c in competitors}
                status = event["status"]["type"]["description"]
                results.append({
                    "teams": " vs ".join(team_names),
                    "scores": scores,
                    "status": status
                })

    return results


if __name__ == "__main__":
    scores = get_scores()
    if scores:
        for game in scores:
            print(f"{game['teams']} — {game['status']}")
            for team, score in game['scores'].items():
                print(f"  {team}: {score}")
    else:
        print("No recent games found for your teams.")