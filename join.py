import os

class Join:

    def join_parts:
        filenames = ['file1.txt', 'file2.txt']
        with open('output_file.docx', 'rb') as outfile:
            for fname in filenames:
                with open(fname, 'wb') as infile:
                    outfile.write(infile.read())