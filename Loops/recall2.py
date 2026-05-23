# people = [
#     {"name": "Isaac", "ticket": True, "vip": True},
#     {"name": "Brian", "ticket": False, "vip": False},
#     {"name": "Sarah", "ticket": True, "vip": False},
#     {"name": "Dangerous Guy", "ticket": True, "vip": False},
#     {"name": "Mary", "ticket": True, "vip": True}
# ]

# prompt user for some data
name = input("Enter your name: ")
ticket = input("Do you have a ticket? (yes/no): ")
vip = input("Are you VIP? (yes/no): ")


# convert to boolean
ticket = ticket.lower() == "yes"
vip = vip.lower() == "yes"


# append the data to the dictionery
person = {"name": name, "ticket": ticket, "vip": vip}

if not person["ticket"]:
    print(person["name"], "No ticket")
else:
    print(person["name"], "Allowed inside")
