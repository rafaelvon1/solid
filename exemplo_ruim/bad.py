import requests
import json

class ListRepository():

    API = "https://api.github.com"
    def __init__(self, user):
        self.user = user 
    def get_repos_by_user(self):
        response = requests.get(f"{self.API}/users/{self.user}/repos")
        if response.status_code == 200:
            return {"status_code": 200, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body": "erro"}
        
    def parse_response(self):
        response = self.get_repos_by_user()
        body = response["body"]
        if response["status_code"] == 200:
            for i in range(len(body)):
                print(f'{body[i]["id"]} - {body[i]["name"]} - {body[i]["stargazers_count"]}')

p =ListRepository("rafaelvon1")
p.parse_response()