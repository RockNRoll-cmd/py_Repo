import re

#define function to read a file and pick up emailID
def read_func_pick_email(file_path):
    with open(file_path, 'r') as file:
        matches_list = []
        for line in file:
            #get email names
            pattern = r'\b[a-zA-Z0-9]+@+[a-zA-Z]+\.+com\b'
            matches_list.extend(re.findall(pattern, line, re.IGNORECASE))
        for line in matches_list:
            print(line)
        return len(matches_list)
        
def main():
    file_path = "/Users/krishnavinay/Documents/Python_Project/email_list"
    num_matches = read_func_pick_email(file_path)

if __name__ == "__main__":
    main()
