from os import system

readme = """
# escambo system #
- [1] Ver Itens
- [0] Sair
"""

def login():
    global username
    system("cls")
    username = str(input("what is username?\n> ")) 
    system("cls")

def menu(username):
    global res
    print(readme)
    res = str(input(f"[{username}]#: "))
    match res:
        case "1":
            view_itens()
        case "0":
            system("cls")
            exit()
        case _:
            return res

def view_itens():
    return

def main():
    if username == None:
        username = "root"
    login(username)
    while True:
        system("cls")
        menu(username)

if __name__ == "__main__":
    main()