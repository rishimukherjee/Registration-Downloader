from tempfile import TemporaryFile
from xlwt import Workbook
import re
f = open(r'D:\backup\fest.txt', 'r+')
line = f.readline()
attributes = {'Name':0, 'College':1, 'E-mail':2, 'Phone':3, 'Select Your Events':4}
book = Workbook()
sheet1 = book.add_sheet('Sheet 1')
for i in range(5):
    sheet1.col(i).width = 10000
sheet1.write(0,0,'Name')
sheet1.write(0,1,'College Name')
sheet1.write(0,2,'Phone No')
sheet1.write(0,3,'E-mail ID')
sheet1.write(0,4,'Select Your Events')
c = 1
while line:
    line = line.strip()
    line = re.sub(r'\s', '', line)
    line = re.sub(r'\n', '', line)
    for z in range(5):
        if ':' in line:
            found_at = line.index(':')
            key = line[:found_at]
            value = line[found_at+1:]
            row = sheet1.row(c)
            if 'Name' in key:
                row.write(0, value)   
            if 'College' in key:
                row.write(1, value)
            if 'Phone' in key:
                row.write(2, value)
            if 'E-mail' in key:
                row.write(3, value)
            if 'Select Your Events' in key:
                row.write(4, value)
        line=f.readline()
    c+=1
    line = f.readline()
book.save('simple.xls')
book.save(TemporaryFile())
f.close()