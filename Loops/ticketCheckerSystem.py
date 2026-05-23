people = []
# Ask how many people are attending the meeting.
total_people = input("How Many People are attending? ")
# conver total_people to integer
total_people = int(total_people)

# collecting data
for i in range(total_people):
    # print person number
    print("\nPerson", i + 1)

    # Capturing User Input
    name = input("Enter name: ")
    ticket = input("Do you have a ticket? (yes/no): ")
    vip = input("Are you vip? (yes/no): ")

    # conver Data to boolean
    ticket = ticket.lower() == "yes"
    vip = vip.lower() == "yes"

    # Creating Dictionery
    person = {"name": name, "ticket": ticket, "vip": vip}

    # Store the dictionery in the list
    people.append(person)

""" Process all people """
print("\n=============Event Results=============")
for person in people:
    if not person["ticket"]:
        print(person["name"], "Access Denied!!!!")
        continue
    if person["vip"]:
        print(person["name"], "Vip Access Granted")

    else:
        print(person["name"], "Regular Access Granted")
