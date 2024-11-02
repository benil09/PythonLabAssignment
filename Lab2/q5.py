"""
Write a program to find the roots of a quadratic equation when the
coefficients a, b and c are given ( assume that a, b and c are integers)
 Hint: find the discriminant d= b2 − 4ac
 
If d = 0, the equation has one real repeated root (both roots are the same:
    R1= R2 = -b/(2a)
    
If d > 0, the equation has two distinct real roots.
    R1= (-b + sqrt(d))/2a
    R2= (-b - sqrt(d))/2a
If d < 0, the equation has two complex roots.
real_part = -b / (2 * a)
imaginary_part = math.sqrt(-discriminant) / (2 * a)

"""