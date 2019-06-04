# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

a = input('Enter the length of side a of the triangle: ')
b = input('Enter the length of side b of the triangle: ')
c = input('Enter the length of side c of the triangle: ')
aa = int(a)
bb = int(b)
cc = int(c)
if aa == bb and bb == cc:
    print(f'A triangle with sides of {aa}, {bb}, & {cc} is an equalateral triangle')
elif aa == bb or aa == cc or bb == cc:
    print(f'A triangle with sides of {aa}, {bb}, & {cc} is a isosceles triangle')
else:
    print(f'A triangle with sides of {aa}, {bb}, & {cc} is a scalene triangle')