from msed2_encrypt import msed2


class Conflation:
    msed3_alg = msed2()

    password = ''

    def read_pwd(self):
        with open('password.txt') as pass_file:
            self.password = str(pass_file.readline())
            print(self.password)

    def merge(self):
        filenames = ['outfile_encrypted.txt_part1.txt', 'outfile_encrypted.txt_part2.txt']
        with open('merged_output_file.txt', 'wb') as outfile:
            for fname in filenames:
                with open(fname, 'rb') as infile:
                    outfile.write(infile.read())

    def run_decrypt(self):
        with open('merged_output_file.txt', 'rb') as in_file, open('outfile_decrypted.txt', 'wb') as out_file:
            self.msed3_alg.decrypt(in_file, out_file, self.password)

    def conflate(self):
        self.read_pwd()
        self.merge()
        self.run_decrypt()


conflation = Conflation()
conflation.conflate()
