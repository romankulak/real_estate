File = open('realtylinks.txt', 'r')
fo = open('realtylinks9-16.txt', 'w')
fo.seek(0, 2)
seq = File.readlines()[9000:16000]
fo.writelines(seq)
fo.close()
File.close()