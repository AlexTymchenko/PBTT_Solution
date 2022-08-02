import hashlib
from draw import summon_an_allien
s = "Python Bootcamp"

hash_variable = hashlib.sha256(s.encode())
output = hash_variable.hexdigest()

summon_an_allien()
print(f"'{output}' - said an allien ")
print(f"'{s}' - said a human ")