# dictionary are used to store data key:value pairs
# dictionary are mutable and also unordered
info={
    "Name":"Rahul",
    "Age":22,
    "Mobile No." :868778478,
    "Subject":["cse","ece","mech."]
}
print(info)
print(info["Age"])

info["Name"]="Akshay"
print(info)
# null dictionary create
null_dict={}
print(null_dict)

# nested dictionary
student ={
    "subjects":{
        "phy":89,
        "cse":88,
        "math":90
    }
}

print(student["subjects"]) #for accessing dictionary that is in dictionary
print(student["subjects"]["phy"]) #for accessing only value in nested dictionary