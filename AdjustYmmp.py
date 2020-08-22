import configparser
import json
import os
import traceback

path = './Ymmp/'


def do():
    try:
        config = configparser.ConfigParser()
        config.read('./setting.ini', encoding='utf-8')
        lingering = int(config['Serif']['YOIN'])
        interval = int(config['Serif']['INTERVAL'])
        for file in os.listdir(path):
            with open(path + file, 'r', encoding='utf-8') as f:
                ymmp = json.loads(f.read())

            from datetime import time, timedelta

            current_frame = 0
            for item in ymmp['Timeline']['Items']:
                voice_length = item['VoiceLength']
                if voice_length == '00:00:00':
                    continue
                if len(item['VoiceLength']) == 8:
                    voice_length += '.0000000'
                dt = time.fromisoformat(voice_length[:-1])
                seconds = (dt.hour * 3600 + dt.minute * 60 + dt.second + (dt.microsecond / 1000000)) / item[
                    'PlaybackRate'] * 100
                frames = int(seconds / (1 / 30))

                item['Length'] = frames + lingering
                item['Frame'] = current_frame
                current_frame += frames + lingering + interval

            with open('./CompleteYmmp/' + file, 'w', encoding='utf-8') as f:
                data = json.dumps(ymmp, ensure_ascii=False)
                f.write(data)
    except:
        traceback.print_exc()
        input('エラー')


if __name__ == '__main__':
    do()
