import time

def how_long(fxn):
    start = time.time()
    def inner (*args):
        return fxn(*args)
    dur = time.time() - start
    print "execution time: " + str(dur)
    return inner

def show_call_info(fxn):
    def inner(*args):
        print fxn.func_name + ": " + str(args)
        return fxn(*args)
    return inner

@how_long
@show_call_info







fibcache = {}
def mem_fib(n):
    if n in fibcache:
        return fibcache[n]
    else:
        fibcache[n] = n if n<2 else fib(n-1) + fib(n-2)
        return fibcache[n]



def memo( fxn ):
    cache = {}
    def inner (x):
        if x not in cache:
            cache[x] = fxn(x)
        return cache[x]
    return inner

@memoize

def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)
                            
