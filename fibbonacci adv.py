import time
def fib(m,d):
                if m in d:
                                return d[m]
                else:
                                v=fib(m-1,d)+fib(m-2,d)
                                d[m]=v
                                return v
d={0:1,1:1}
start=time.time()
print(700,d)
print(time.time()-start,"secs")
