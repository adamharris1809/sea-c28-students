import io
import sys

def clean_file(name_fileinput, name_fileoutput):
    f_inlines = io.open(name_fileinput).read()
    #inlines = io.open(name_fileinput).readlines() - test the difference.
    f_outlines = f_input.strip()
    f_outfile = io.open(name_fileoutput, 'w')
    for line in f_outlines:
        f_outfile.write(line"\n")


if __name__ == "__main__":
    filename = sys.argv[1]

"""
#from class example
outfile = io.open('output.txt', 'w')
for i in range(10):
    outfile.write("this is line: %i\n"%i)

#from solutions manual
f_output = map(string.strip, f_input)

"""