info={
    "Name":"Rahul",
    "Age":22,
    "Mobile No." :868778478,
    "Subject":["cse","ece","mech."]
}

# dict.keys() #use to access all the keys in dictionary
# dict.values() #Returns all the values
# dict.items() #Returns all the key:value pair in tuple
# dict.get("Subject") #Returns the key accoding to value

info.update({"City" : "gurgaon"})
print(list(info.keys()))  # to store all keys in a list
print(list(info.values()))  # to store all values in a list
print(list(info.items()))  # to access all the key value pair in tuple
print(list(info.get("Subject")))  # to store that spcific value of key
print(info["Subject"])
# both of them print value but neeche wala error show karega key present nhi hai to but get waale method agar hum undefined key use krenge to vo none value dega
