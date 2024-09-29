from os import system
from tables import roles
import db

readme = """
# escambo system #
- [1] Ver Itens
- [0] Sair
"""

class profile:
    def singup():
        system("cls")
        try:
            username = str(input("what is your name?\n> "))
            password = str(input("password\n> "))
            nivel = str(input("nivel\n> "))
        except Exception as e:
            print(f"\nlog [app]\n{e}")
        else:
            system("cls")
            roles.insert_data(username, password, nivel)

    def login():
        system("cls")
        try:
            username = str(input("what is your name?\n> "))
            password = str(input("password\n> "))
            datas = roles.read_data(username, password)
            if not datas:
                print("\n[System] Error Login.")

                
        except Exception as e:
            print(f"\nlog [app]\n{e}")

def main():
    db.create_tables()
    profile.login()


if __name__ == "__main__":
    main()
