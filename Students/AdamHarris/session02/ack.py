def ack(m,n):
    """Accepting non-negative inputs for ackermann function, returning Ackermann outputs after calculation"""
    #Testing for correct input types
    if not isinstance(m, int) or not isinstance(n, int):
        return(None)
    elif m<0 or n<0:
        return("Ackermann is undefined when integers are less than zero")
    elif m==0:
        return("Ackermann = ", n+1)
    elif n==0:
        return("Ackermann = ",m-1,1)
    else:
        return("Ackermann = ",m-1, ack(m,n-1))