import requests

token = "add your github token here"
username = "your github user name"
version = "1.0.8-final"

headers = {
    "Authorization": f"token {token}"
}

print(f"Loading Repdelete version {version}")
print("-------------------------------------")
print(" ")

repos_to_delete = ["add your repo's here!"]

for repo in repos_to_delete:
    url = f"https://api.github.com/repos/{username}/{repo}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Successfully deleted {repo}")
    else:
        print(
            f"Failed to delete {repo}. Status code: {response.status_code}, Response: {response.text}")
