n = int(input("Nhập số nguyên dương n: "))

is_lucky_number = True

while n > 0:
    digit = n % 10
    if (digit!=6 and digit!=8):
        is_lucky_number = False
        break
    n //= 10

if is_lucky_number:
	print(n, "là số may mắn")
else:
	print(n, "KHÔNG phải số may mắn")
