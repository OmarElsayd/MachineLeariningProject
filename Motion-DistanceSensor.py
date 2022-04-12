import csv
if __name__ == "__main__":
    file = open('HumanResource.csv')
    Data = csv.reader(file)
    head = Data[:1]
    print (head)