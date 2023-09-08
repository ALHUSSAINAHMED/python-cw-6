# write your code here
person = {
           "name": "hussain" ,
            "age" : "15" ,
           "hobbies" : "police"
       }
print(person["name"])
print(person["age"])






person["age"] = "16"
person["country"] = "Portugal"




print(f"hi my name is {person['name']}, iam {person['age']}, iam from {person['country']}, i hobe to be a {person['hobbies']} ")
print(f"{person}")






person.get("Sciences")

def check_hobbies(person):
    if person["hobbies"] >= 3 :
        print("wow you are amazing")
