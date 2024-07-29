##User Management:
# Implement classes for user registration, login, and authentication.
# Manage user profiles and permissions, including different user roles (e.g., Admin, User).
# Implement password encryption for secure authentication.


class User:
    def __init__(self, user_name, user_password, user_email, user_role):
        self.user_name = user_name
        self.user_password = user_password
        self.user_email = user_email
        self.user_role = user_role


class UserManager:
    def __init__(self):
        self.users = []
        self.logged_in_user = None

    def register(self, user_name, user_password, user_email, user_role):
        for user in self.users:
            if user.user_name == user_name:
                return "Username already exists."
        new_user = User(user_name, user_password, user_email, user_role)
        self.users.append(new_user)
        return "User registered successfully."

    def login(self, user_name, user_password):
        for user in self.users:
            if user.user_name == user_name and user.user_password == user_password:
                self.logged_in_user = user
                return "Login successful."
        return "Invalid username or password."

    def authenticate_user(self, user_email, user_password):
        for user in self.users:
            if user.user_email == user_email and user.user_password == user_password:
                print("Authenticate user")
                return True
        print("User email or password is invalid")
        return False

    def update_profile(self, user_name, user_new_role):
        for user in self.users:
            if user.user_name == user_name:
                if user_new_role:
                    user.user_role = user_new_role
                return "Profile updated successfully."
        return "User not found."

user_manager = UserManager()
print(user_manager.register("admin", "adminpass", "admin@example.com", "Admin"))
print(user_manager.login("admin", "adminpass"))

print(user_manager.authenticate_user("admin@gmail.com.com", "admin123"))


print(user_manager.update_profile("admin", "Admin2"))