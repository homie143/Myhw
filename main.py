def read_from_file(filename):
    with open(filename,'r') as file:
        columns = tuple(file.readline().split(','))
        data= []
        for line in file :
            line = file.split(',')
            data.append((int(line[0]), line[1], line[2],int(line[3]), int(line[4]),int(line[5])))
    return columns, data
def write_to_file(filename):
    with open (filename, 'w') as file :
        file.write(','.join(columns)+'\n')
        for line in data :
            line=[str(i) for i in line ]
            file.write(','.join(line)+'\n')
columns=('id','name','lastname','age','haight','weight')
data = [
(1, 'gleb', 'dragov', 15, 178, 67),(2, 'sasha', 'sidorov', 15, 190, 78),(3, 'dima', 'dilanov', 17, 156, 40),]
write_to_file('atbase.csv')