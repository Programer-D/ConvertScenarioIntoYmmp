import csv
import os
import json
import re
from CONSTANT import VOICE_ITEM_BASE, CHARACTER_BASE


def get_character_image_base_from_character_list(character_list, name):
    for character in character_list:
        if character['name'] == name:
            return character['base']
    return None


def load_pronunciation_data(file_path):
    serif_list = []
    character_name_list = []
    color_list = ['#ABDDF4', '#aff6d2', '#b8f6ac', '#e4f6a7', '#F6DEA3', '#F6BCA2',
                  '#F6A8DD', '#CAABF6', '#919BF6', '#76C8F6', '#F4EBCB', '#F4BEBE',
                  '#F49292', '#F4C892', '#F4EE92', '#72FFC9', '#72C2FF', '#7279FF']

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            character = row[0]
            character_name_list.append(character)
            serif_list.append({'character': character, 'text': row[1], 'pronunciation': row[2]})

    character_list = []
    character_name_list = list(set(character_name_list))
    for index, character in enumerate(character_name_list):
        character_list.append({'name': character, 'color': color_list[index]})

    return serif_list, character_list


def make_voice_item(serif, frame, exist_character_list):
    voice_base = VOICE_ITEM_BASE.copy()
    character_name = serif['character']

    character = None
    for exist_character in exist_character_list:
        if exist_character['Name'] == character_name:
            character = exist_character
    voice_base['CharacterName'] = character_name

    if character:
        voice_base['Volume'] = character['Volume']
        playback_rate = character['PlaybackRate']
        voice_base['PlaybackRate'] = playback_rate
        voice_base['VoiceParameter'] = character['VoiceParameter']

    voice_base['Serif'] = serif['text']
    voice_base['Hatsuon'] = serif['pronunciation']
    voice_base['Frame'] = frame
    voice_base['Length'] = 1

    return voice_base


def make_new_character_list(character_list, exist_character_list):
    new_character_list = []
    for index, character in enumerate(character_list):
        exist_flag = False
        for exist_character in exist_character_list:
            exist_flag = False
            if exist_character['Name'] == character['name']:
                exist_flag = True
                new_character_list.append(exist_character)
                break

        if not exist_flag:
            character_base = CHARACTER_BASE.copy()
            character_base['Name'] = character['name']
            character_base['Color'] = character['color']
            new_character_list.append(character_base)
    return new_character_list


def load_ymm_character_setting_json(ymm_setting_path):
    latest_version_num = 0
    latest_version = ''
    for version in os.listdir(ymm_setting_path):
        version_num = int(re.sub('\.', '', version))
        if latest_version_num < version_num:
            latest_version_num = version_num
            latest_version = version

    with open(ymm_setting_path + latest_version + '/YukkuriMovieMaker.Settings.CharacterSettings.json',
              'r', encoding='utf-8') as f:
        return json.loads(f.read())['Characters']
