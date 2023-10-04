
def process_data(filename):
    try:
        f = open(filename)
    except FileNotFoundError:
        print("File dosen't exist!")
        return 
   
    lines = list()

    for line in f:
        line = line.strip().split(' ')
        lines.append(line)
    f.close()

    return lines


def average_lines(lines):
    avg = []
    for l in lines:
        s = 0
        for num in l:
            s += int(num)
        avg.append(s/3)
    return avg

def output(data, averages):
    for idx in range(len(data)):
        print("Values: {} | Average: {}".format(" ".join(data[idx]), averages[idx]))

def main():
    data = None
    while data == None:
        filename = input("Please enter the name of your file:")
        data = process_data(filename)

    averages = average_lines(data)
    output(data,averages)
main()