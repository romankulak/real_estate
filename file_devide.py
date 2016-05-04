File = open('realtylinks.txt', 'r')

for i in range(1000,len(File.readlines()),1000):
    fo = open('realtylinks'+str(i)+'.txt', 'w')
    file2 = open('realtylinks.txt', 'r')
    fo.seek(0, 2)
    seq = file2.readlines()[i-1000:i]
    fo.writelines(seq)
    fo.close()
    file2.close()
    last_ind = i
    fo1 = open('realtylinks' + str(i) + '.txt', 'r')
    print len(fo1.readlines())

lastfile = open('realtylinks'+str(last_ind+1)+'.txt', 'w')
file2 = open('realtylinks.txt', 'r')
lastfile.seek(0, 2)
seq  = file2.readlines()[last_ind:]
lastfile.writelines(seq)

lastfile.close()
file2.close()
File.close()
lastfile2 = open('realtylinks'+str(last_ind+1)+'.txt', 'r')
print len(lastfile2.readlines())
lastfile2.close()