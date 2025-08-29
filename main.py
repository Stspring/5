from Examination import CheckingFile

def main():
    file_name = "var7.csv"
    examination = CheckingFile(file_name)
    examination.research_file()
    
if __name__ == '__main__':
    main()