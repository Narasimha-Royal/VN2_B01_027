print("--------Data Structures--------")
print("------1)STRINGS------")
state = "Andhra Pradesh"
print(state,type(state))
print("Value at 2nd Index:--", state[2])  # Index
print("Value at -7 Index:--", state[-7])  # Index
print("Partial name between two index numbers:--", state[2:6])  # Slicing
print("Partial name between two index numbers:--", state[4:])   # Slicing
print("Partial name between two index numbers:--", state[:9])   # Slicing
print("Partial name between two index numbers:--", state[-12:-2])  # Slicing
print("Partial name between two index numbers:--", state[:-3])  # Slicing
print("Partial name between two index numbers:--", state[-13:])  # Slicing

print("------2) LIST and Nested List------")
list = [1,5.6,"Royal",[4,7.3,"Narasimha"],True,(9,3.5)]
print(list)
print(type(list))
print("Value at 3nd Index:--", list[2])  # Index
print("Value at -5 Index:--", list[-5])  # Index
print("Slicing between two index numbers:--", list[1:4])  # Slicing
print("Slicing between two index numbers:--", list[2:])  # Slicing
print("Slicing between two index numbers:--", list[:5])  # Slicing
print("Indexing In Nested List:",list[3])  # Index
print("Indexing In Nested List:",list[3][2])  # Index
print("Indexing In Nested List:",list[3][2][5])  # Index

print("------3) TUPLE and Nested Tuple------")
tuple = (1,5.6,"Royal",(4,7.3,"Narasimha"),True,[9,3.5])
print(tuple)
print(type(tuple))
print("Value at 3nd Index:--", tuple[2])  # Index
print("Value at -5 Index:--", tuple[-5])  # Index
print("Slicing between two index numbers:--", tuple[1:4])  # Slicing
print("Slicing between two index numbers:--", tuple[2:])  # Slicing
print("Slicing between two index numbers:--", tuple[:5])  # Slicing
print("Indexing In Nested Tuple:",tuple[3])  # Index
print("Indexing In Nested Tuple:",tuple[3][2])  # Index
print("Indexing In Nested Tuple:",tuple[3][2][5])  # Index

print("------4) Dictionary------")
dict = {
    "id": 27,
    "name": "Narasimha",
    "gender": "Male",
    "locations": ["Bangalore","Kurnool"]
}
print(dict)
print(type(dict))
print(dict["id"])
print(dict["name"])
print(dict["locations"])

print("------5) Sets------")
set = {1,5.6,"Charan",True}
print(set)
print(type(set))
