minimum = int(input("enter minimum: "))
maximum = int(input("enter maximum: "))

perfectnums = []

def perfectnumber(n): #find each perfect number
    if n < 1:
        return False
    
    perfectsum = 0
    for i in range(1, n):
        if n % i == 0: 
            perfectsum+=i # i gets added to what df needs to add up to
    return perfectsum == n

basenumber = maximum
print("all perfect numbers from %d to %d are " %(minimum, maximum))
for i in range(1, basenumber + 1):
    if perfectnumber(i):
        perfectnums.append(i)
print(perfectnums)

#it does, now checking if edits sync to vs2019
