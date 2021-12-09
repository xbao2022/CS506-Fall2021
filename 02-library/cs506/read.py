def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    file = open(filename, "r")

    X = []
    for line in file:
        each_line = line.strip()
        each_list = each_list.split(",")
        X.append(each_list)

    file.close()

    return X
