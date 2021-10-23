import time

k = 1
 
# Initialize sum
s = 0

l = "1"
start = 1.2

start = time.process_time()

def myFunction(s, k, l):
    for i in range(int(l)):
        # even index elements are positive
        if i % 2 == 0:
            s += 4/k
        else:

            # odd index elements are negative
            s -= 4/k

        # denominator is odd
        k += 2
    print(s) 
    print(time.process_time() - start)
    
       

for r in range(1000):
    l = l + "0"
    print(l)
    myFunction(s, k, l)
    start = 0
else: 
    print("finished")
    



     
