
people = [
    {"name":"Yasin","ticket":False, "vip":True },
    {"name":"Isaac","ticket":False, "vip":True }
    ]  # a list, a dictionery{}, tupple (1,2,3)


# Nested loops
for person in people[0]:
    if person["ticket"]:
        if person["vip"]:
            print(person["name"], "Welcome! You are allowed.")
        else:
            print(person["name"],"Welcome regular")
    
    else:
        print(person["name"], "Access Denied")
    
