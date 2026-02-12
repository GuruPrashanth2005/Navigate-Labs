a=int(input(""))
b=int(input(""))
print("sum:", a + b) #addition
print("difference:", a - b) #subtraction
print("product:",a * b) #multiplication
print("quotient:",a / b) #division
print("integer division:", a // b) #floor division
print("modulus:",a % b) #modulus
print("exponentiation:", a ** b) #exponentiation

#relational operators
print("a == b:", a == b) #equal to
print("a != b:", a != b) #not equal to
print("a > b:", a > b) #greater than
print("a < b:", a < b) #less than
print("a >= b:", a >= b) #greater than or equal to
print("a <= b:", a <= b) #less than or equal to


#logical operators
print("a > 0 and b > 0:", a > 0 and b > 0) #logical and
print("a > 0 or b > 0:", a > 0 or b > 0) #logical or
print("not (a > 0):", not (a > 0)) #logical not


#bitwise operators
print("a & b:", a & b) #bitwise and     
print("a | b:", a | b) #bitwise or
print("a ^ b:", a ^ b) #bitwise xor
print("~a:", ~a) #bitwise not
print("a << 1:", a << 1) #left shift
print("a >> 1:", a >> 1) #right shift


#assignment operators
c = a + b
print("c = a + b:", c)  #simple assignment
c += a
print("c += a:", c)     #add and assign     
c -= a
print("c -= a:", c)     #subtract and assign
c *= a
print("c *= a:", c)     #multiply and assign    
c /= a
print("c /= a:", c)     #divide and assign
c %= a
print("c %= a:", c)     #modulus and assign
c **= a
print("c **= a:", c)    #exponentiation and assign
c //= a
print("c //= a:", c)    #floor division and assign
