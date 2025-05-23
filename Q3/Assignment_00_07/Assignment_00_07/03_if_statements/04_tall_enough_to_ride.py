def main():
    while True:
    
        height = input("How tall are you? ")

        if height == "":
            print("Exiting the program. Have a great day!")
            break

        height = int(height)

        if height >= 50:
            print("You're tall enough to ride!\n")
        else:
            print("You're not tall enough to ride, but maybe next year!\n")

if __name__ == '__main__':
    main()