from git_hub.client import GithubClient
from repo.parser import RepoParser
from repo.RepoGenerator import ReportsGenerator
from repo.reports.HtmlGenerator import HtmlGenerator
from repo.reports.markdown import MarkdownGenerator
from models.member import Member
from models.manager import Manager


if __name__ == '__main__':
    username = 'rafaelvon1'
    response = GithubClient.get_repos_by_user(username)

    if response["status_code"] == 200:
        parse = RepoParser.parse(response['body'])
        print(ReportsGenerator.build(HtmlGenerator,parse))
        print(ReportsGenerator.build(MarkdownGenerator,parse))
    else:
        print(response['body'])
    
    member = Member("rafael","rafael@gmail.com")
    manager = Manager("rafael-manager","manager@gmail.com")

    print(member.members())
    print(manager.members())