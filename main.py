import os

path = 'file/'


def text_file(path: str):
    file_list = os.listdir(path)
    file_dict = {}
    for f_text in file_list:

        if f_text.rfind('.txt', -4) >= 0:
            with open(os.path.join(path, f_text), 'r', encoding='utf-8') as file:
                file_dict[f_text] = file.readlines()

    with open('new_file.txt', 'w', encoding='utf-8') as file:
        for file_name, rows in sorted(file_dict.items(), key=lambda x: len(x[1])):
            file.write(file_name + '\n')
            file.write(str(len(rows)) + '\n')
            if '\n' not in rows[-1]:
                rows[-1] += '\n'
            file.write(''.join(rows))


text_file(path)
