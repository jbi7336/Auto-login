import json

def read_json():
    account = {
        "account": [
        ]
    }

    try:
        with open("../id.json", "r") as f:
            account = json.load(f)
    except:
        print("No file")

    return account

def input_account():
    ty = str(input())
    id = str(input())
    pw = str(input())

    temp = {
        "type": ty,
        "id": id,
        "pw": pw
    }

    return temp


def add_account(jsonObject):
    accountTemp = input_account()
    jsonObject["account"].append(accountTemp)

def remove_account(jsonObject):
    display_account_list(jsonObject)
    index = int(input())

    del(jsonObject["account"][index - 1])

def update_account(jsonObject):
    display_account_list(jsonObject)
    index = int(input())

    newAccount = input_account()
    jsonObject["account"][index - 1] = newAccount

def display_account_list(jsonObject):
    for i in jsonObject['account']:
        print(i)

def make_json(jsonObject):
    with open("../id.json", "w", encoding="utf-8") as f:
        json.dump(jsonObject, f, indent="\t")

def display_menu():
    print()
    print("-------------------")
    print("1. Add    4. Display")
    print("2. Remove 5. Make")
    print("3. Update 6. Exit")
    print("-------------------")

def main():
    jsonObject = read_json()
    while True:
        display_menu()
        playType = input()

        if playType == '1':
            add_account(jsonObject)
        elif playType == '2':
            remove_account(jsonObject)
        elif playType == '3':
            update_account(jsonObject)
        elif playType == '4':
            display_account_list(jsonObject)
        elif playType == '5':
            make_json(jsonObject)
        elif playType == '6': # End Loop
            break
        else:
            print("Wrong Type input")

main()