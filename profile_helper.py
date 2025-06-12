import json
import os

PROFILE_PATH = "user_profile.json"

def save_user_profile(profile):
    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f)

def load_user_profile():
    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH, "r") as f:
            return json.load(f)
    return {"full_name": "", "email": "", "role": "", "company": "", "Source of job link": ""}
