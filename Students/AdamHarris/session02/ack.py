def ack(m,n):
    """Accepting non-negative inputs for ackermann function, returning Ackermann outputs after calculation"""
    #Testing for correct input types
    if not isinstance(m, int) or not isinstance(n, int):
        return(None)
    elif m < 0 or n < 0:
        return(None)
    elif m == 0:
        return(n+1)
    elif n == 0:
        return(ack(m-1,1))
    else:
        return(ack(m-1, ack(m,n-1)))

if __name__ == "__main__":
    #Validating the function's accuracy.
    mcount = 0
    ncount = 0
    ackcount = 0
    acktestresults = [1,2,3,4,5,2,3,4,5,6,3,5,7,9,11,5,13,29,61,125,0]
    while mcount < 3:
        if ncount == 5: #Resetting the ncount & mcount for further iteration.
            mcount += 1
            ncount = 0
        while ncount < 5:
            if ack(mcount, ncount) != acktestresults[ackcount]:
                print (ack(mcount, ncount), mcount, ncount)
                raise ValueError("Values don't work for the following pair", mcount, ncount, acktestresults[ackcount])
                break
            print (mcount, ncount, acktestresults[ackcount])
            ackcount += 1
            ncount += 1
            if ackcount == 20:
                print("All tests pass.")