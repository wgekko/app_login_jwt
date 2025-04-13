def authenticate(username, password):
    users = {
        "admin": {"password": "admin123", "role": "admin"},
        "usuario1": {"password": "user123", "role": "usuario1"},
        "usuario2": {"password": "user234", "role": "usuario2"},
    }
    user = users.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None