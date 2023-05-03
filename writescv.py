import sqlite3

# label

def main():
    fileread = open('test.csv','r')

    file_contents=fileread.read()

    fileread.close()

    # print(file_contents)
    file_contents2 = file_contents.split('\n')
    test2=[]

    # lentest = len(file_contents2)
    # for test in file_contents2:
    #     test2 = 'label;'+test
    #     print(test2)

    print(len(file_contents2))
    test3=file_contents2[0:len(file_contents2)-1]
    for i in range(len(file_contents2)-1):
        if i == 0:
            test3[i]= 'label;'+file_contents2[i]
        else:
            test3[i]= ';'+file_contents2[i]
        print(i)



    for test in test3:
        print(str(test))

    
    filewrite = open('filewrite.csv','w')
    for test in test3:
        filewrite.write(test+'\n')
    filewrite.close()

    

    # filewrite = open('filewrite.csv','w')
    # filewrite.write(file_contents)
    # filewrite.close()



if __name__=="__main__":
    main()