MAX_LENGTH = 3  

def shorten(lst):
    while len(lst) > MAX_LENGTH:  
        removed_item = lst.pop() 
        print("Removed:", removed_item)  

def main():
    lst = []  #
    
    # User se list input lena
    n = int(input("Enter number of elements in the list: "))
    for _ in range(n):
        value = input("Enter a value: ")
        lst.append(value)

    print("Original list:", lst) 
    shorten(lst) 
    print("Shortened list:", lst)  


if __name__ == '__main__':
    main()