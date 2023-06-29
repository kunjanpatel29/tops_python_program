lst = [1200,523,169,1800,7845,9850,2600]
result = []

for num in lst:
    if num >=1000 and num <=9999 and (num % 5 == 0 or num % 8 == 0) and num % 2 == 0:
        result.append(num)

print(result)
