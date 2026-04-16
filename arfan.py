a = 132  # 0b10000100
b = 45   # 0b00101101

# Formatting styles
fmt0 = '{:<10}'              # Left-aligned, 10 spaces
fmt1 = '0b{:08b}  ({:3})'    # Binary with 8 leading zeros, decimal 3 spaces wide
n = 30

# Bitwise AND
print("Bitwise AND:")
print(fmt0.format('a'), fmt1.format(a, a))
print(fmt0.format('b'), fmt1.format(b, b))
print('_' * n)
print(fmt0.format('a & b'), fmt1.format(a & b, a & b))

# Bitwise OR
print("Bitwise OR:")
print(fmt0.format('a'), fmt1.format(a, a))
print(fmt0.format('b'), fmt1.format(b, b))
print('_' * n)
print(fmt0.format('a | b'), fmt1.format(a | b, a | b))

# Bitwise XOR
print("Bitwise XOR:")
print(fmt0.format('a'), fmt1.format(a, a))
print(fmt0.format('b'), fmt1.format(b, b))
print('_' * n)
print(fmt0.format('a ^ b'), fmt1.format(a ^ b, a ^ b))

# Bitwise NOT (with mask to show 8-bit result)
print("Bitwise NOT:")
print(fmt0.format('a'), fmt1.format(a, a))
print('_' * n)
print(fmt0.format('~a'), fmt1.format(~a & 0xFF, ~a & 0xFF))
