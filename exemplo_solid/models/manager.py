from .user import User 
class Manager(User):
    def __init__(self, username, email):
        super().__init__(username, email)
    
    @staticmethod
    def members():
        return "voce não tem permissão"
    def work(self):
        return "pagando..."