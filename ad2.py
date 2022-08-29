from msed2_encrypt import msed2
import os
import math

class AD2:

    msed2_alg = msed2()
    #msed2_alg
    password = '' 
    def read_pwd(self):
        with open('password.txt') as pass_file:
            self.password = str(pass_file.readline())
            print(self.password)
    
    def run_encrypt(self):
        with open('infile.txt', 'rb') as in_file, open('outfile_encrypted.txt', 'wb') as out_file:
            self.msed2_alg.encrypt(in_file, out_file, self.password)
    
    def split_alpha_beta(self, file_name):
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
    
    def ad2(self):
        check = ['Consequently,','time', 'cool', 'Note']
        with open('infile.txt', encoding="utf8") as pnl:
            for line in pnl:
                for word in line.split():
                    #print(word)
                    for i in range(len(check)):
                        #print(word, " == ",check[i])
                        if word == check[i]:
                            #break
                            print('found ', check[i])
                            self.read_pwd()
                            self.run_encrypt()
                            self.split_alpha_beta('outfile_encrypted.txt')
                        else:
                            print('not found')
                        break

ad2 = AD2()
ad2.ad2()