def new_line(txt):
    if txt:
        with open("file.txt", "a", encoding="utf-8") as file:
            file.write(f'{txt}\n')
        new_line(input('Input new line: '))
    else:
        print('The end')


new_line(input('Input new line: '))
