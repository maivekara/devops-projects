import json

def get_users():
    users = [
        {"id": 1, "name": "Sefa", "role": "developer"},
        {"id": 2, "name": "Elif", "role": "designer"},
        {"id": 3, "name": "Ahmet", "role": "manager"}
    ]
    return json.dumps(users, indent=2)

if __name__ == "__main__":
    print(get_users())
