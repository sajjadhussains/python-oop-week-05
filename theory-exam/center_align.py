with open('demo_text.txt','r+') as file:
    lines = file.readlines()
    file.truncate(0)
    file.close()
with open('demo_text.txt','w') as file:
    white_space=7
    first_length=len(lines[0])
    for i,line in enumerate(lines):
        if i==0:
            white_space=10
        elif len(line)>first_length:
            white_space=5
            first_length=len(line)
        elif len(line)<first_length:
            white_space=15
            first_length=len(line)
        file.write(line.strip().center(len(line)+white_space)+'\n')