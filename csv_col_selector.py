import csv

if __name__ == '__main__':

    # input your wanted columns below
    wanted_cols = ['d', 'c']
    # input file
    input_file = 'test.csv'

    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        header = True
        header_to_index = {}
        output = []
        for row in reader:
            new_row = []
            if header:
                for i, col in enumerate(row):
                    if col in wanted_cols:
                        header_to_index[col] = i

                for col in wanted_cols:
                    new_row += [row[header_to_index[col]]]
                header = False
            else:
                for col in wanted_cols:
                    new_row += [row[header_to_index[col]]]

            output += [new_row]

        for row in output:
            print(','.join(row))

