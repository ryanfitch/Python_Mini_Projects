# Write a Python program that accept an integer (n) and computes
# the value of n+nn+nnn

n = int(input("Give me an input: "))
n1 = int( "%s" % n )
n2 = int( "%s%s" % (n,n) )
n3 = int( "%s%s%s" % (n,n,n) )
print (n1+n2+n3)
