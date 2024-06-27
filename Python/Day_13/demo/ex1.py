url = 'wwww.google.com/chat?name="Neha"&color="blue'
def convert_to_dict(url):
    url = url.split("?")
    url = url[1]
    parameters = {}
    word = ""
    for ch in url:
        if ch == '=':
            key = word
            word = ""
        elif ch == '&':
            value = word
            parameters[key] = value
            key = ""
            value = ""
            word = ""
        else:
            word = word + ch
    return parameters

print(convert_to_dict(url))

products_dict = {
    "name" : "xyz",
    "color": "blue",
    "size": "S",
    "price": "123"
}

user = {
    "name": "xyz",
    "password" : "admin"
}

def products(name, color, size, price):
    print(name, color, size, price)

def users(name, password):
    print(name, password)


def controller(url_from_user):
    url_from_user = url_from_user.split("/")
    url_from_user = url_from_user[1].split("?")
    endpoint = url_from_user[0]
    print(endpoint)
    
    convert_to_dict(url)

    if endpoint == "user":
        users(user["name"], user["password"])
    elif endpoint == "products":
        products(**products_dict)

controller(url)

admin = {
    "name": "XYZ",
    "role": "admin"
}

intern = {
    "name": "XYZ",
    "role": "Intern"
}


permissions = {
    "HR": "yes",
    "TA": "yes",
    "Intern": "no",
    "SDE": "no",
    "Tech Lead" : "no"
}

def delete_profile(permission):
    return permission == "yes" and "Deleting profile..." or "Contact your administrator to delete this profile..."

print(delete_profile(permissions[intern["role"]]))
