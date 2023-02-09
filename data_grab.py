import seaborn as sns
import csv
import random

length_of_records = 10

with open('data/crypt_data.csv', mode='w') as file:
    csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['Execution Time'])

    for _ in range(0, length_of_records):
        csv_writer.writerow([random.randrange(310, 350)])