def add_8bit(a, b):
    bin_a = f"{a & 0xFF:08b}"
    bin_b = f"{b & 0xFF:08b}"
    
    total = a + b
    bin_total = f"{total & 0xFF:08b}"
    
    overflow = False
    if a > 0 and b > 0 and total > 127:
        overflow = True
    elif a < 0 and b < 0 and total < -128:
        overflow = True

    print(f"Expression: {a} + ({b})")
    print(f"  Operands in Binary: {bin_a} and {bin_b}")
    print(f"  Result in Decimal : {total}")
    print(f"  Result in Binary  : {bin_total}")
    print(f"  Overflow Detected : {overflow}\n")

add_8bit(25, 18)
add_8bit(-25, -18)



def shift(binary_str,steps,direction):
  print("original binary:",binary_str)
  current=binary_str

  for i in range(1,steps+1):
    if direction =="left":
      current=current[1:]+"0"
    else:
      current="0"+current[:-1]
    print(f"step {i}:{current}")
  print()

n=int(input("enter no of binary digits u want to add:"))
for i in range(n):
  binary_str=input("enter the binary:")
  steps=int(input("enter the steps:"))
  direction=input("enter the direction:")
  if direction=="left":
    print("---left shift---")
    shift(binary_str,steps,direction)
  else:
    print("---right shift---")
    shift(binary_str,steps,direction)