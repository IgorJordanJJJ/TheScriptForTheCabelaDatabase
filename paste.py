
def main():
    file = open('websearch_in.csv','r')

    file_contents=file.read()

    file.close()

    print(file_contents)


if __name__=="__main__":
    main()