import io

def clean_file(fileinput, fileoutput):
    f_input = io.open('').read()
    #inlines = io.open(f_input).readlines() - test the difference.
    f_output = f_input.strip()


    f_output = io.open(fileoutput, 'w')
    for line in f_output:
        f_output.write(line "\n")


#from class example
outfile = io.open('output.txt', 'w')
for i in range(10):
    outfile.write("this is line: %i\n"%i)

#from solutions manual
f_output = map(string.strip, f_input)