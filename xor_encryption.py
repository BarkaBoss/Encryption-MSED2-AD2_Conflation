import random

class XOR:
    punct = (".", ";", "!", "?", ",")
    count = 0
    new_word = ""

    def scramble(self):
        with open("infile.txt", 'r', encoding='utf-8') as fin:
            for line in fin.readlines():  # Read line by line in txt file

                for word in line.split():  # Read word by word in each line

                    if len(word) > 2:  # If word length >3

                        if word.endswith(self.punct):
                            word1 = word[1:-2]
                            word1 = random.sample(word1, len(word1))
                            word1.insert(0, word[0])
                            word1.append(word[-2])
                            word1.append(word[-1])

                        else:
                            word1 = word[1:-1]
                            word1 = random.sample(word1, len(word1))
                            word1.insert(0, word[0])
                            word1.append(word[-1])
                            self.new_word = self.new_word + ''.join(word1) + " "

                else:
                    self.new_word = self.new_word + word + " "


        with open("data/XOR.txt", 'a+') as fout:
            fout.write(self.new_word + "\n")

        self.new_word = ""


xor = XOR()
xor.scramble()
