class HtmlGenerator():
    @classmethod
    def build(cls, repos):
        items = ''.join(f"<strong>ID: </strong>{repo.id}\n <strong>name: </strong>{repo.name}\n <strong>star: </strong>{repo.stars}\n" for repo in repos)
        return f'<p>{items}</p>'