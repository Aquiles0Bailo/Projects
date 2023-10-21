import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

long = int(input("Introduce la longitud de la contraseña: "))

con = ""
for _ in range(long):
    s = random.choice(characters)
    con += s

print("Tu contraseña es:", contraseña)
