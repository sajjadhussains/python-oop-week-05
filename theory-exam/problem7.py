# Define the filename of the book
with open('book.txt', "r") as file:
    pages = file.read().split("--")
    for i, page in enumerate(pages):
        print(page.strip())
        if i < len(pages) - 1:
            choice = input("[enter - read more, press q to quit]")
            if choice.lower() == "q":
                break
