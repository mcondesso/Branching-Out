import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    return [user for user in users if user["name"].lower() == name.lower()]


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    return [user for user in users if int(user["age"]) == age]


def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    return [user for user in users if user["email"].lower() == email.lower()]


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? ('name', 'age' or 'email'): "
    ).strip().lower()

    users = []
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        users = filter_users_by_name(name_to_search)
    elif filter_option == "age":
        try:
            age_to_filter = int(input("Enter an age to filter users: "))
            users = filter_users_by_age(age_to_filter)
        except ValueError:
            print("The age must be a number.")
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        users = filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")

    if not users:
        print("\nNo users found.")
    else:
        print("\nFound the following users:")
        for user in users:
            print(user)
