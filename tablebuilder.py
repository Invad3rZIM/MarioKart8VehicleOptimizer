
def parseFile(filename):
    lines = open(filename)

    ls = []

    for line in lines:
        li = sanitize(line)

        if len(li) > 0: #ensure line isn't empty before appending it
            ls.append(li)

    return ls

def sanitize(line):
    #removes all <tags></tags>
    while "<" in line:
        startTag = line.index("<")

        if startTag != -1:
            endTag = line.index(">")
            line = line[endTag+1:] if startTag==0 else line[0:startTag] + line[endTag+1:]


    #removes all newline characters
    if "\n" in line:
        line = line[0:line.index("\n")]

    return line.strip() #strips any trailing spaces

def buildTable(data):
    index = 0

    table = []

    datum = []

    index += 1


    while index < len(data):
            datum = [data[index], data[index+1], data[index+2], data[index+3], data[index+4], data[index+5],data[index+6], 0]
            table.append(datum)
            index += 7

            total = 0

            for i in range(1, len(datum)-1):
                datum[i] = numberify(datum[i])
                total += datum[i]

            datum[len(datum)-1]=total

            if data[0] != "Gliders": #gliders is the only dataset that doesn't include a computable total..
                index +=1 

    return table

def numberify(num):
    if type(num) is int:
        return num
    else:
        if num[0] == "+":
            return float(num[1:])
        if num[0] == "0":
            return 0
        if num[0] == "-":
            return -1 * float(num[1:])
        return float(num)

    
    return num
    