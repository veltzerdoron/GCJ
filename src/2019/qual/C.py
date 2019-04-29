import sys

def gcd(a, b):
  while b:
    a, b = b, a%b
  return a

t = int(input())
for i in range(t):
  N, L = list(map(int, input().split()))
  nums = list(map(int, input().split()))

  # get first and last primes
  primes = set()
  # get gcd for all pairs of consecutive multiplications
  for a, b in zip(nums, nums[1:]):
    if a != b:
      g = gcd(a,b)
      primes.add(a // g)
      primes.add(b // g)
  
  if len(primes) < 26:
    for a, b in zip(nums, nums[1:]):
      if a == b:
        for prime in primes:
          if a % prime == 0:
            primes.add(a // prime)

  assert (len(primes) == 26)
  primes = sorted(list(primes))

  y = ""

  # get first prime
  prime = 1
  c = 1
  for a, b, k in zip(nums, nums[1:], range(len(nums))):
    if a != b:
      g = gcd(a,b)
      if k % 2 == 0:
        prime = a // g 
      else:
        prime = g
      break

  for num in nums:
    y += chr(ord('A') + primes.index(prime))
    prime = num // prime
  y += chr(ord('A') + primes.index(prime))
    
  print("Case #{n}: {y}".format(n=i + 1, y=y))
