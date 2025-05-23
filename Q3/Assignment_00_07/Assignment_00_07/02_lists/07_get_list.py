def main():
    lst = []  
    
    while True:
        value = input("Enter a value: ") 
        
        if value == "": 
            break
        
        lst.append(value)  

    print("Here's the list:", lst)  

# Required line to run the program
if __name__ == '__main__':
    main()