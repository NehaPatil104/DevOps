name: str = "Neha Patil"
age: int = 22
cgpa: float = 9.5
address: str = 'Pune'
office_address = """
Wadgoan Sheri,
Pune
"""
is_instagram_active: bool = False
is_learning: bool = True

hobbies: list[str] = ["reading", "painting"]
skills: tuple[str] = ("Java", "C++")


from typing import Union

education: dict[str, Union[str, float, int, list]] = {
    "engineering": "JSPM",
    "cppa": 9.6,
    "passout_year": 2024,
    "hobbies": ["reading", "painting"],
    "skills": ("Java", "C++")
}

from typing import TypedDict
class Person(TypedDict):
    age: int
    name: str
    is_hungry: bool



print(name)
print(age)
print(cgpa)
print(address)
print(office_address)
print(is_instagram_active)
print(is_learning)
print(hobbies)
print(skills)
print(education)