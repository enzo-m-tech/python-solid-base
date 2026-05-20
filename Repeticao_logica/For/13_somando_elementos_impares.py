nums = [-2, 5, 8, -1, 10]
soma_impares = 0
for i in range(len(nums)):
     if i % 2 == 1:
         soma_impares +=  nums[i]

print(f"A soma total dos elementos em posições ímpares = {soma_impares} ")

