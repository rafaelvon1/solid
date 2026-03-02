import requests
import json

class GithubClient():

    API = "https://api.github.com"
    # def __init__(self, user):
    #     self.user = user 
    @classmethod
    def get_repos_by_user(self, user):
        response = requests.get(f"{self.API}/users/{user}/repos")
        if response.status_code == 200:
            return {"status_code": 200, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body": "erro"}
      