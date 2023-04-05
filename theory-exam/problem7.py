with open('book.txt', 'r') as f:
    books = f.read()
    pages = books.split('--')
    for i,page in enumerate(pages):
        skip_page_number=-1
        if skip_page_number<0 and skip_page_number!=i:
            print(page)
            print('[enter -read more,press q to enter]')
        else:
            skip_page_number=0
            continue
        user_input=input()
        if user_input.isdigit():
            convertNum=int(user_input)
            if convertNum>0:
                skip_page_number=convertNum
        elif user_input=='q':
            break
            

