from enum import Enum

class Gender(str, Enum):
    man = "man"
    women = "women"


g = Gender("man")

print(g) # Gender.man
print(g.value) # man
print(g.man.value) # man
print(g.women.value) # women