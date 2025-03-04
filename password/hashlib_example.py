import hashlib

password = "nombreMascota"
hash = hashlib.sha256(password.encode()).hexdigest()

print(password)
print(hash)

