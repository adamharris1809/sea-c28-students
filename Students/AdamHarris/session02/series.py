"""Creating three functions that build mathematical series and return the nth number inputted by the user."""

def fibonacci(n):
    """Function returns the nth value in the fibonacci series"""
    if not isinstance(n, int) or n<0:
        return(None)
    fibo=[0,1]
    for i in range(n):
        fibo.append(fibo[i]+fibo[i+1])
    print(fibo)
    return(fibo[n-1])

def lucas(n):
    """Function returns the nth value in the lucas series"""
    if not isinstance(n, int) or n<0:
        return(None)
    luc=[2,1]
    for j in range(n):
        luc.append(luc[j]+luc[j+1])
    print(luc)
    return(luc[n-1])

def sum_series(q,*r):
    """Function returns the qth value in a fibonacci-like series beginning with r[0] & r[1]"""
    if not isinstance(q, int) or q<0:
        return(None)
    if not r:
        ss=[0,1]
    else:
        ss=[r[0],r[1]]
    for k in range(q):
        ss.append(ss[k]+ss[k+1])
    print(ss)
    return(ss[q-1])


if __name__ == "__main__":
    """Checking that the 5th result of each series is correct."""
    assert fibonacci(5)==3 #Fibo check
    assert lucas(5)==7 #Lucas check
    assert sum_series(5)==3 #Sum Series without entries
    assert sum_series(5,2,100)==304 #Sum Series with entries