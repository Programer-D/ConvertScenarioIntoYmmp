from Util.Ymmp import *
import os


def do():
    with open('./Base/base.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())

    exist_character_list = load_ymm_character_setting_json('../YukkuriMovieMaker4/user/setting/')

    path = './PronunciationData/'
    ymmp_path = './Ymmp/'

    for file in os.listdir(path):
        if 'pronunciation' not in file:
            continue

        serif_list, character_list = load_pronunciation_data(path + file)

        new_voice_list = []
        frame = 10

        for index, serif in enumerate(serif_list):
            new_voice_list.append(make_voice_item(serif, frame, exist_character_list))
            frame += 1

        new_character_list = make_new_character_list(character_list, exist_character_list)

        data['Timeline']['Items'] = new_voice_list
        data['Characters'] = new_character_list

        with open(ymmp_path + file.replace('_pronunciation.csv', '.ymmp'), 'w', encoding='utf-8') as f:
            ymmp_data = json.dumps(data, ensure_ascii=False)
            f.write(ymmp_data)


if __name__ == '__main__':
    do()
