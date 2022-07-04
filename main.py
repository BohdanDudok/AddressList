adr_list = {'Bohdan Dudok': '0996602606',
            'Olena Dudok': '0501732867',
            'Mykola Tsebrov': '0955977202'}


def read_list():
    f = open("addresslist.txt")
    text = f.read()
    print(text)
    f.close()


def ad_cont(name, phone_number):
    name_contact = name
    phone = phone_number
    f = open("addresslist.txt", 'a')
    f.writelines("{0} - {1}\n".format(name_contact, phone))
    f.close()


def del_cont(name):
    name_contact = name
    del adr_list[name_contact]


while True:
    menu = "1 - Address list\n" \
           "2 - Add contact\n" \
           "3 - Delete contact\n"\
           "4 - Exit\n"\
           "---------------------"
    print(menu)
    x = int(input("Select the desired action - "))
    if x == 1:
        read_list()
        quest = input("You can continue? Y/N - ")
        if quest == 'Y' or quest == 'y':
            continue
        if quest == 'N' or quest == 'n':
            break
    if x == 2:
        name_user = input("Please, enter user name - ")
        phone_number = input("Phone number - ")
        ad_cont(name_user, phone_number)
    if x == 3:
        name = input("Enter name - ")
        del_cont(name)
        continue
    if x == 4:
        break
