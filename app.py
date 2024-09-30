from os import system, name
from getpass import getpass
from tables import roles
import db

class profile:
    @staticmethod
    def singup():
        try:
            system("cls" if name == "nt" else "clear")
            username = input("Sing-Up: ")
            password = getpass("Password: ")
            nivel = input("Nivel\n> ")

            system("cls" if name == "nt" else "clear")
            roles.insert_data(username, password, nivel)

        except Exception as e:
            print(f"\nlog [singup]\n{e}")

    @staticmethod
    def login():
        try:
            system("cls" if name == "nt" else "clear")
            username = input("Login: ")
            password = getpass("Password: ")

            system("cls" if name == "nt" else "clear")
            datas = roles.read_data(username, password)

            if datas and isinstance(datas, list) and len(datas) > 0:
                id_value = datas[0][0] 

            return 200 if datas else 400
        
        except Exception as e:
            print(f"\nlog [login]\n{e}")

class sys:
    @staticmethod
    def user():
        try:
            if profile.login() == 400:
                print("It looks like you are not registered, do you want to register (y/n)?")
                log = input("")

                if log == 'y':
                    profile.singup()
                elif log == 'n':
                    system("cls" if name == "nt" else "clear") 
                    exit()
                else:
                    return sys.user()

        except Exception as e:
            print(f"\nlog [user]\n{e}")

    @staticmethod
    def menu():
        itens = ["Sair", "Ver itens"]
        print("# escambo system #")
        for index, item in enumerate(itens):
            print(f"- [{index}] {item}")

        try:
            choise = input("\n>")
            match choise:
                case '0':
                    system("cls" if name == "nt" else "clear")         
                    exit()
                case '1':
                    print(200)
                case _:
                    return sys.menu()
                
        except Exception as e:
            print(f"\nlog [menu]\n{e}")


def main():
    db.create_tables() 
    sys.user()
    sys.menu()


if __name__ == "__main__":
    main()
