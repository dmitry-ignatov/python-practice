import requests


def get_repository_response(repo_full_name):
    response = requests.get(
        f"https://api.github.com/repos/{repo_full_name}",
        timeout=10
    )

    return response


result = get_repository_response("psf/requests")
if result.status_code == 200:
    repository_data = result.json()
    print(repository_data["name"])
    print(repository_data["full_name"])
    print(repository_data["description"])
else:
    print(f"код ошибки {result.status_code}")