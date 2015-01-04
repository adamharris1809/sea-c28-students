import io
import sys

def clean_file(name_fileinput, name_fileoutput):
    f_inlines = io.open(name_fileinput).readlines()
    f_outlines = map(string.strip, f_input)
    f_outfile = io.open(name_fileoutput, 'w')
    for line in f_outlines:
        f_outfile.write(line+"\n")

def clean_file_LC(name_fileinput, name_fileoutput):
    f_inlines = io.open(name_fileinput).readlines()

    f_outlines = [line.strip()+"\n" for line in f_inlines]

    f_outfile = io.open(name_fileoutput, 'w'), writelines(f_outlines)



"""I don't like the idea of taking credit for leaning entirely on the solutions manual
to understand/write this name = main section below.
"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print help_msg
        sys.exit(1)
    else:
        infilename = sys.argv[1]
    try:
        outfilename = sys.argv[2]
    except IndexError:
        outfilename = infilename

clean_file('home/adamharris/sea-c28-stuff/sea-c28-students/Students/AdamHarris/session04/sherlock.txt',
'home/adamharris/sea-c28-stuff/sea-c28-students/Students/AdamHarris/session04/sherlock1.txt')
#clean_fileLC(name_fileinput, name_fileoutput)

