with open('book.txt', "r") as file:
    pages = file.read().split("--")
    current_page = 0
    while current_page < len(pages):
        print(pages[current_page].strip())
        user_input = input("[enter - read more, press q to quit]")
        if user_input.lower() == "q":
            break
        elif user_input.isdigit():
            skip_pages = int(user_input)
            current_page += skip_pages
        elif user_input=='-1':
            current_page-=1
        else:
            current_page += 1
