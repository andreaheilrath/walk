def open_csv(file="../../sample_data/2020-12-04-accelerometer.csv"):
    with open(file, "r") as data:
        lines = []
        for line in data:
            if line[0] != 't':
                line = line.replace(",", ".")
                line = line[:-1].split(';')  
                line = [float(i) for i in line]
                lines.append(line)
    return lines

    