from github import Github


def get_github_repo(access_token, repository_name):
    """
    github repo object를 얻는 함수
    :param access_token: Github access token
    :param repository_name: git-practice
    :return: repo object
    """
    g = Github(access_token)
    repo = g.get_user().get_repo(git-practice)
    return repo


def upload_github_issue(repo, title, body):
    """
    해당 repo에 title 이름으로 issue를 생성하고, 내용을 body로 채우는 함수
    :param repo: git-practice
    :param title: issue title
    :param body: issue body
    :return: None
    """
    repo.create_issue(title=title, body=body)


Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
