import io
import sys

def clean_file(name_fileinput, name_fileoutput):
    f_inlines = io.open(name_fileinput).readlines()
    f_outlines = map(string.strip, f_input)
    f_outfile = io.open(name_fileoutput, 'w')
    for line in f_outlines:
        f_outfile.write(line"\n")

def clean_file_LC(name_fileinput, name_fileoutput):
    f_inlines = io.open(name_fileinput).readlines()
    f_outlines = [line"\n".strip() for line in f_inlines]
    f_outfile = io.open(name_fileoutput, 'w'), write(f_outlines)

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