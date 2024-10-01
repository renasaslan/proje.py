import random

char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenght = int(input("şifreniz kaç karekter olsun?"))
şifre = ""

for i in range(lenght):
    şifre += random.choice(char)
    

print(şifre)
