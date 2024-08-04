def add(word,definition)
    file1 = open("Words.txt","a")
    file2 = open("Words.txt","a")
    file1.write(word)
    file2.write(definition)
    file1.close()
    file2.close()

