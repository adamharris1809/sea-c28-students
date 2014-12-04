"""Define the four functions."""

def name():
    """Return a value after working around a NameError"""
    try:
    	print(a)
    except NameError:
	print(1)

def typer():
    """Return a value after working around a TypeError"""
    try:
	print(1+"recycle")
    except TypeError:
	print("recycle")

def sintax():
    """Return a value after working around a SyntaxError"""
    try:
        print('Those guys' taste in beer is terrible.')
    except SyntaxError:
        print("Those guys' taste in beer is terrible.")

def attribute():
    """Return a value after working around a AttributeError"""
        recycle="cans"
    try:
	recycle=recycle.lowr()
    except AttributeError:
	print(recycle.lower()


"""Call the functions."""
name()
typer()
sintax()
attribute()
