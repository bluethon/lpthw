target = open("ex15_sample.txt", 'a')
target.write("sss")

target.truncate()

target.write("aaa\nddddd\nend")

target.read()

target.close()
