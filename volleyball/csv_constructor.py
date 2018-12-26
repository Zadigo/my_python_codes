import csv

def write_csv(with_titles=False, titles=[], values=[]):
    with open('test.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        if with_titles:
            csv_writer.writerow(titles)
            
        csv_writer.writerow(values)