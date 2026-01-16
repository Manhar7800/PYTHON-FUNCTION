db={}#main database

def ragistration(name,email,password,subject,city):
    global db
    sub_dict={}
    sub_dict["name"]=name
    sub_dict["subject"]=subject
    sub_dict["email"]=email
    sub_dict["password"]=password
    sub_dict["city"]=city

    if email in db.keys():
        return "user alredy exists!"
    else:
        db[email]=sub_dict
        return "successfuly ragistration done:"
    
    
def login(email,password):
    global db
    if email in db.keys():
        if password==db[email]["password"]:
            return f"welcome {db[email]["name"]},"
        else:
            return "password does not match !"
    else:
        return "Invalid email and address!"
    
menu="""
          1)ragistration
          2)login
"""

status=True
while status:
    print(menu)
    choice=int(input("enter your choice:"))
    if choice==1:
        name=input("enter your name:")
        email=input("enter your email:")
        password=input("enter your password:")
        subject=input("enter your subject:")
        city=input("enter your city:")

        res=ragistration(name,email,password,subject,city)
        print("responce:",res)

        #print(db)

    else:
        email=input("enter your email:")
        password=input("enter password:")

        res=login(email,password)
        print(res)

        print("------------------------------------")

        choice_exit=input("Do you want to perform more operation? press 'y' or 'n' ")

        if choice_exit=='n' or choice=='no':
            status=False