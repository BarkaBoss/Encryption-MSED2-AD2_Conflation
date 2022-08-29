check = ['fine', 'cool']

with open('outfile.docx', 'rb') as pnl:
    for line in pnl:
        for word in line.split():
            for i in range(len(check)):
                if word == check[i]:
                    print('found ', check[i])