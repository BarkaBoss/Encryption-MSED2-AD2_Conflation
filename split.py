import os
import math

class Split:

    def split_alpha_beta(file_name):
        file_size = os.path.getsize(file_name)


        print(file_size)
        CHUNK_SIZE = int(math.ceil(file_size/2))
        file_number = 1
        with open(file_name,'rb') as f:
            chunk = f.read(CHUNK_SIZE)
            while chunk:
                with open(file_name+'_part' + str(file_number)+'.txt', 'wb') as chunk_file:
                    chunk_file.write(chunk)
                file_number += 1
                chunk = f.read(CHUNK_SIZE)