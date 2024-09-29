from tables import roles
from app import readme

class Profile:
    @staticmethod
    def singup():
        try:
            username = input("What is your name?\n> ")
            password = input("Password\n> ")
            nivel = input("Nivel\n> ")
            system("cls")
            roles.insert_data(username, password, nivel)
        except Exception as e:
            print(f"\nlog [app]\n{e}")

    @staticmethod
    def login():
        try:
            username = input("What is your name?\n> ")
            password = input("Password\n> ")
            datas = roles.read_data(username, password)
            if datas:
                system.menu()
            else:
                print("\nlog [login]\nThere is no user in the database")
        except Exception as e:
            print(f"\nlog [app]\n{e}")

class system:
    @staticmethod   
    def user():
        print(200)

    @staticmethod   
    def menu():
        system("cls")
        print(readme)
        print(200)
