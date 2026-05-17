import json
import os
from app.models import User

MY_FILE = "save_data.json"

# Data Persistence: Save info to JSON file
def save_to_json(all_users):
    big_dict = {}
    for name, user_obj in all_users.items():
        big_dict[name] = {
            "height": user_obj.height,
            "history": user_obj.history
        }
    with open(MY_FILE, "w") as file:
        json.dump(big_dict, file)

# Load info from JSON file
def load_from_json():
    all_users = {}
    if os.path.exists(MY_FILE):
        with open(MY_FILE, "r") as file:
            try:
                data = json.load(file)
                for name, info in data.items():
                    user_obj = User(name, info["height"])
                    user_obj.history = info["history"]
                    all_users[name] = user_obj
            except json.JSONDecodeError:
                print("Error: File is empty or broken.")
    return all_users