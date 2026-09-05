def accountFormatter(slot_data):
    print(f"Name: {slot_data["name"]}")
    print(f"\nProfession: {slot_data["profession"]}")
    print(f"\nCountry: {slot_data["country"]}\n")



def accountFormatter_full(data):
    print(f"Name: {data["name"]}")
    print(f"\nProfession: {data["profession"]}")
    print(f"\nCountry: {data["country"]}\n")
    print(f"\nFollowers: {data["followers"]}")