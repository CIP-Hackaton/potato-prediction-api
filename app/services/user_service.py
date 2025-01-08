from app.repositories.user_repository import UserRepository

class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: str):
        try:
            user = self.user_repository.get_by_id(user_id)
            return user
        except Exception as e:
            raise Exception(f"Error getting user {user_id}")
    
    def get_user_by_email(self, email: str):
        try:
            user = self.user_repository.get_by_email(email)
            return user
        except Exception as e:
            raise Exception(f"Error getting user {email}")
        
    def create_user(self, user):
        try:
            new_user = self.user_repository.create_user(user)
            return new_user
        except Exception as e:
            raise Exception(f"Error creating user")
        