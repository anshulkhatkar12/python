students = [ "hermi", "harry", "ron"]
for i in students:
    print (i)


students = [ "hermi", "harry", "ron"]
for i in range(len(students)):
    print (i+1,students[i])

students= {
    "hermione": "gryff",
    "harry": "gryff",
    "ron": "gryff",
    "draco": "sylth",
    }
for i in students:
    print(i, students[i], sep= ",")



students=[
    {"name":"herm", "house":"gryff"},
    {"name":"harry", "house":"gryff"},
    {"name":"ron", "house":"gryff"},
    {"name":"draco", "house":"sylth"}
]
for i in students:
    print (i["name"], i["house"], sep=",")