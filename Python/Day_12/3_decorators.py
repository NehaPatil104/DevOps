# check if user has enough permissions

def authorize(authorized_roles):
    def lt(func):
        def check_permission(*args, **kwargs):
            if args[0] in authorized_roles:
                return func(*args, **kwargs)
            return f"You don't have permissions to delete the user as a {args[0]}!"
        return check_permission
    return lt

@authorize(["Admin", "HR"])
def delete_profile(user_name):
    return f"Profile deleted by {user_name}!"

print(delete_profile("Admin")) 