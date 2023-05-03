import sqlite3

# label



def main():
    fileread = open('test.csv','r')
    file_contents=fileread.read()
    fileread.close()

    file_contents2 = file_contents.split('\n')

    test3=file_contents2[0:len(file_contents2)-1]
    for i in range(len(file_contents2)-1):
        if i == 0:
            test3[i]= 'label;'+file_contents2[i]
        else:
            # print(file_contents2)
            # print('\n')
            # print(file_contents2[0]+'\n')
            a = file_contents2[i].split(";")
            # print(a)
            # print(a[7][0])
            # b = a[0].split(',')
            # print(b)
            # print(file_contents2[i][0]+'\n')
            test3[i]= a[7][0]
            if a[8] == 'Magnet Yoke':
                test3[i]=test3[i]+'MR'
            else:
                test3[i]=test3[i]+a[8][0:2]
            test3[i]=test3[i]
            if len(a[9])==1:
                test3[i]=test3[i]+'0'+a[9]
            else:
                test3[i]=test3[i]+a[9]
            test3[i]=test3[i]+"R"+a[0][0]+a[1]+a[2][0]
            if len(a[3])==1:
                test3[i]=test3[i]+'0'+a[3]
            else:
                test3[i]=test3[i]+a[3]

            if a[4] == 'Thermostabilizzation':
                test3[i] = test3[i]+'TS'
            elif a[4] == 'TPC centerl membrane':
                test3[i] = test3[i]+'CM'
            elif a[4] == 'Sensors':
                test3[i] = test3[i]+'SN'
            elif a[4] == 'ROC Chamber':
                test3[i] = test3[i]+'RC'
            elif a[4] == 'DAQ':
                test3[i] = test3[i]+'DQ'
            else:
                b = a[4].split()
                test3[i] = test3[i]+b[0][0]+b[1][0]
            if len(a[5])==1:
                test3[i]=test3[i]+'00'+a[5]
            elif len(a[5])==2:
                test3[i]=test3[i]+'0'+a[5]
            else:
                test3[i]=test3[i]+a[5]
            test3[i]=test3[i]+ ';'+file_contents2[i]



    # for test in test3:
    #     print(str(test))

    
    filewrite = open('filewrite.csv','w')
    for test in test3:
        filewrite.write(test+'\n')
    filewrite.close()

    

    # filewrite = open('filewrite.csv','w')
    # filewrite.write(file_contents)
    # filewrite.close()



if __name__=="__main__":
    main()