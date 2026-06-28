import requests


def get_github_profile(github_url: str):

    if not github_url:
        return {
            "applicable": False,
            "message": "GitHub profile not provided."
        }

    try:

        username = github_url.rstrip("/").split("/")[-1]

        user_response = requests.get(
            f"https://api.github.com/users/{username}",
            timeout=10
        )

        if user_response.status_code != 200:
            return {
                "applicable": False,
                "message": "GitHub profile not found."
            }

        repos_response = requests.get(
            f"https://api.github.com/users/{username}/repos",
            timeout=10
        )

        repositories = repos_response.json()

        repo_names = []
        languages = set()
        recent_activity = []
        total_stars = 0

        for repo in repositories:

            repo_names.append(repo["name"])

            if repo["language"]:
                languages.add(repo["language"])

            total_stars += repo["stargazers_count"]

            recent_activity.append(
                {
                    "repository": repo["name"],
                    "updated_at": repo["updated_at"]
                }
            )

        return {

            "applicable": True,

            "username": username,

            "public_repositories": len(repositories),

            "repositories": repo_names,

            "languages": list(languages),

            "total_stars": total_stars,

            "recent_activity": recent_activity[:5]

        }

    except Exception as e:

        return {
            "applicable": False,
            "message": str(e)
        }