import display


def main():
    display.print_table()
    f = open("text_albums_data.txt")
    read = f.read()

    with f as musiclibrary:
        spliting = read.split(",") 
        print(spliting)

   

        


if __name__ == "__main__":
    main()
