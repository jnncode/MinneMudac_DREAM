def date_format_help(file):
    """
    Change date format from xxxxxxxx to xxxx-xx-xx. Dumps data into new file. 
    :param file: RevisedData.csv
    :return: None
    """
    in_file = open(file, 'r')
    out_file = open("GameLogsCSV\DateFormat.csv", "w")
    out_file.write(in_file.readline())

    for line in in_file:
        data = line.split(',')
        data[0] = '{0}-{1}-{2}'.format(data[0][:4], data[0][4:6], data[0][6:])
        out_file.write(",".join(data))

    in_file.close()
    out_file.close()

def main():
    file_path = "GameLogsCSV\RemovedDuplicates.csv"
    date_format_help(file_path)

if __name__ == "__main__":
    main()
