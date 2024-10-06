from os import system, name
from getpass import getpass
from tables import roles
import mysql09 as db

class profile:
    @staticmethod
    def singup():
        system("cls" if name == "nt" else "clear")
        try:
            username = input("Sing-Up: ")
            password = getpass("Password: ")
            nivel = input("Nivel\n> ")
            system("cls" if name == "nt" else "clear")

            roles.insert_data(username, password, nivel)
        except Exception as e:
            print(f"\nlog [app/singup]: {e}")
            exit()

    @staticmethod
    def login():
        global username
        system("cls" if name == "nt" else "clear")
        try:
            username = input("Login: ")
            password = getpass("Password: ")
            system("cls" if name == "nt" else "clear")
            
            datas = roles.read_data(username, password)
            if datas and isinstance(datas, list) and len(datas) > 0:
                id_value = datas[0][0]
                # print(id_value)
                return
            else: 
                400
        except Exception as e:
            print(f"\nlog [app/login]: {e}")
            exit()

class sys:
    @staticmethod
    def user():
        print("It looks like you are not registered, do you want to register (y/n)?")
        try:
            if profile.login() == 400:
                log = input("")
                if log == 'y':
                    profile.singup()
                elif log == 'n':
                    system("cls" if name == "nt" else "clear") 
                    exit()
                else: return sys.user()
        except Exception as e:
            print(f"\nlog [app/user]: {e}")
            exit()

    def adm():
        return

    @staticmethod
    def menu():
        itens = ["Sair", "Ver itens"]
        print("# escambo system #")
        for index, item in enumerate(itens):
            print(f"- [{index}] {item}")
        try:
            choise = input(f"\n[{username}]>")
            match choise:
                case '0':
                    system("cls" if name == "nt" else "clear")         
                    exit()
                case '1':
                    print(200)
                case _: return sys.menu()
        except Exception as e:
            print(f"\nlog [app/menu]: {e}")
            exit()

def main():
    db.connection()
    sys.user()
    sys.menu()

if __name__ == "__main__":
    main()
