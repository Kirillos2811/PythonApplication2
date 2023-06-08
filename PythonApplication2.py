import collections

pets = {

    1:

        {

            "Мухтар": {

                "Вид питомца": "Собака",

                "Возраст питомца": 9,

                "Имя владельца": "Павел"

            },

        },

    2:

        {

            "Каа": {

                "Вид питомца": "желторотый питон",

                "Возраст питомца": 19,

                "Имя владельца": "Саша"

            },

        },

}

def get_pet(ID):
    if ID in pets.keys():
        return pets[ID]
    return False

def get_suffix(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 1 < age % 10 < 5:
        return "года"
    else:
        return "лет"


def create(pet_name, pet_species, pet_age, pet_owner_name):
    last_id = collections.deque(pets, maxlen=1)[0]
    pets[last_id + 1] = {pet_name: {"Вид питомца": pet_species, "Возраст питомца": pet_age, "Имя владельца": pet_owner_name}}
    print("SUCCESS")


def read(ID):
    pet = get_pet(ID)
    if not pet:
        print(None)
        return
    pet_name = list(pet.keys())[0]
    print(f'''Это {pet[pet_name]['Вид питомца']} по кличке "{pet_name}".'''
          + f'''Возраст питомца: {pet[pet_name]['Возраст питомца']} {get_suffix(pet[pet_name]['Возраст питомца'])}.'''
          + f'''Имя владельца: {pet[pet_name]['Имя владельца']}''')

def update(ID, pet_name, pet_species, pet_age, pet_owner_name):
    pet = get_pet(ID)
    if not pet:
        print("Pet not found")
        return
    pet_old_name = list(pet.keys())[0]

    if pet_name == "":
        pet_name = pet_old_name
    if pet_species == "":
        pet_species = pet[pet_old_name]['Вид питомца']
    if pet_age == "":
        pet_age = pet[pet_old_name]['Возраст питомца']
    if pet_owner_name == "":
        pet_owner_name = pet[pet_old_name]['Имя владельца']

    pets[ID] = {pet_name: {"Вид питомца": pet_species, "Возраст питомца": pet_age, "Имя владельца": pet_owner_name}}
    print("SUCCESS")

def delete(ID):
    pet = get_pet(ID)
    if not pet:
        print("Pet not found")
        return
    pets.pop(ID)
    print("SUCCESS")

def pets_list():
    last_id = collections.deque(pets, maxlen=1)[0]
    for i in range(1, last_id + 1):
        print(f"{i}:")
        read(i)

command = None
while command != "stop":
    command = input()
    if command == "CREATE":
        pet_name = input("Имя питомца: ")
        pet_species = input("Вид питомца: ")
        pet_age = int(input("Возраст питомца: "))
        pet_owner_name = input("Имя владельца: ")

        create(pet_name, pet_species, pet_age, pet_owner_name)
    elif command == "READ":
        ID = int(input("ID: "))
        read(ID)
    elif command == "UPDATE":
        print("Input the values or leave them blank if you don't want to change them")
        ID = int(input("ID: "))
        pet_name = input("Имя питомца: ")
        pet_species = input("Вид питомца: ")
        pet_age = input("Возраст питомца: ")
        if pet_age != "":
            pet_age = int(pet_age)
        pet_owner_name = input("Имя владельца: ")

        update(ID, pet_name, pet_species, pet_age, pet_owner_name)
    elif command == "DELETE":
        ID = int(input("ID: "))
        delete(ID)
    elif command == "PETS LIST":
        pets_list()
    elif command == "stop":
        pass
    else:
        print("Undefined command")