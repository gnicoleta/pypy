x = int(input("Enter number: "))

fn2 = 0 #fn-2 is 0 for f0
fn1 = 1 #fn-1 is 1 for f1

print("Fibonacci sequence until %d:"%(x))
for i in range(0, x):
    print(fn2)
    sum = fn1+fn2
    fn2 = fn1
    fn1 = sum