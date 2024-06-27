import requests
response = requests.get("https://gitlab.com/api/v4/users/neha.patil-coditas/projects")
my_projects = response.json()

print(my_projects)
print(type(my_projects))

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['http_url_to_repo']}\n")

