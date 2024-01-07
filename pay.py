def Person_init(num:int, person:list):
    expenses = {}

    num_people = num

    for i in range(num):
        # person = input(f"請輸入第{i+1}個人的名字：")
        expenses[person[i]] = None

    for person in expenses.keys():
        expenses[person] = {item: 0 for item in expenses.keys() if item != person}

    return expenses


 
def PayList(paylist,num):

    paylist = {name: sum(int(money) for person, money in items.items()) / num for name, items in paylist.items()}

    # paylist = {name: sum(int(money) / num) for name, items in paylist.items() for person, money in items.items()}
    print(paylist)

    return paylist



# person = Person_init(num,person)  
# pay = PayList(len(person.keys()))
def result(person,pay):
    for item in pay.keys():
        # print(f"每個人給{item} {pay[item]}元")
        for person_key in person.keys():
            # print(f"--{person_key}--")

            if item != person_key:
                person[person_key][item] = person[person_key][item] + pay[item]
                # print(person)
            else:
                person[item] = {person: items - pay[item] for person, items in person[person_key].items()}
                # print(person)

    result = ""
    for person_key in person:
        result += f"{person_key}\n"
        for p,item in person[person_key].items():
            if item > 0:
                result += f"需給 {p} : {abs(item)}元\n"
            elif item < 0:
                result += f"跟 {p} 拿 : {item}元\n"

        result += "\n\n"
    return result
    print(result)