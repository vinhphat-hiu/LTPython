n = int(input("Nhập số nguyên dương n: "))

max = -1

while n > 0:
    digit = n % 10
    if digit > max:
        max=digit
    n //= 10

print("Max:", max)