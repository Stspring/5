from Examination import CheckingFile

def main():
    file_name = "aaa.csv"
    handler = CheckingFile(file_name)
    handler.research_file()
    
if __name__ == '__main__':
    main()