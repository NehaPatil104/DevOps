from user import User
from post import  Post

# Object creation
app_user_one = User("neha@gmail.com", "Neha Patil", "Pwd", "Intern")
app_user_one.get_user_info()
app_user_one.change_password("neha@123")

new_post = Post("On a secret mission today", app_user_one.name)
new_post.get_post_info()


