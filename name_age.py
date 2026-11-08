from datetime import datetime 

current_year = datetime.now().year

name = input("Enter your name: ")
age = input("Enter your age: ")

birth_year = current_year - int(age)

print(f"Hello {name}! You were born in {birth_year}.")

