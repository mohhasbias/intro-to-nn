def is_nonnegative(n):
   if n >= 0:
      return 1
   else:
      return 0
   
input = [5, 10, 2.5, 0.01, 0, -3, -7.8]

for i in input:
    classification = is_nonnegative(i)
    print(f"Input: {i:>10}, Classification: {classification}")
