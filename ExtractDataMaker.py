import re
import csv
import os

path = './Scenario/'
extract_path = './ExtractData/'


def do():
    for file in os.listdir(path):
        if '.txt' not in file:
            continue

        with open(path + file, 'r', encoding='utf-8') as f:
            base_text = f.read()

        new_text = re.sub('[＜-]', '', base_text)
        while re.findall('\n\n', new_text):
            new_text = re.sub('\n\n', '\n', new_text)

        new_text = re.sub('\n', '$', new_text)
        new_text = re.sub('#.*?#', '', new_text)

        serif_list = []
        character_list = []
        new_text = '$' + new_text
        for text in re.findall('\$(.*?『.*?』)', new_text):
            # background = re.search()
            character = re.search('(.*?)『', text).group().replace('『', '').replace('$', '')
            split_serif = re.search('『(.*?)』', text).group().replace('『', '').replace('』', '').split('$')
            if character not in character_list:
                character_list.append(character)
            for serif in split_serif:
                serif_list.append([character, serif])

        print('--------------------------------------------')
        print(file + 'の処理が完了しました。')
        print('作成されたキャラクタ：' + str(character_list))
        with open(extract_path + file.replace('.txt', '_extract.csv'), 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(serif_list)


if __name__ == '__main__':
    do()
