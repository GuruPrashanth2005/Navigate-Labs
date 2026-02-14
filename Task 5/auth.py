class Auth:
    def login(self):
        pass

class PasswordAuth(Auth):
    def login(self):
        print("Password Verified")

a = PasswordAuth()
a.login()
