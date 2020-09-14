
users = [(0, "Bob", "password"),
         (1, "Rolf", "passgood"),
         (2, "Jose", "passold"),
         (3, "username", "passwordtoo")
         ]

username_mapping = {user[1]: user for user in users}
print(username_mapping["Bob"])
username_input = input("Enter your user name: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password == password_input:
    print("your username and password are correct")
else:
    print("your username and password are not correct")

