class MarkdownGenerator():
    @classmethod
    def build(cls, repos):
        items = ''.join(f"**ID:** {repo.id}\n **name:** {repo.name}\n **star:** {repo.stars}\n" for repo in repos)
        return f'## Repos: \n\n{items}'