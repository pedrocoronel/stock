from os import system as os
import system

import db

readme = """
# escambo system #
- [1] Ver Itens
- [0] Sair
"""

def main():
    os("cls")
    db.create_tables() 
    system.user()
    system.menu()


if __name__ == "__main__":
    main()
