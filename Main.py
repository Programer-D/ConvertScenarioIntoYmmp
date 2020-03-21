try:
    import traceback
    import ExtractDataMaker
    import PronunciationMaker
    import YmmpMaker
    import AdjustYmmp
    import os


    def delete_file(dir):
        for file in os.listdir(dir):
            os.remove(dir + file)


    while True:
        print(
            '##########################################################################################################################')
        print('1:Scenarioフォルダ内にある。「.txt」ファイル全てを処理対象とし、ExtractDataフォルダにセリフを抽出したファイルを生成します。')
        print(
            '2:ExtractDataフォルダ内にある、_extract.csvという文字を含んだファイルを対象にYMMを用いて発音を付与した後、PronunciationDataフォルダに発音を付与したファイルを生成します。')
        print('3:PronunciationDataフォルダ内にある、_pronunciation.csvという文字を含んだファイルを対象に、Ymmpフォルダにゆっくりムービメーカーで読み込み可能なファイルを生成します。')
        print('4:Ymmpフォルダ内のファイルを対象に、CompleteYmmpフォルダにアイテムの長さを修正したymmpファイルを生成します。')
        print('5:コピペイラーズ内のBase,CompleteYmmpを除く、『全てのフォルダ』内に入っているファイルを削除します。')
        number = input('メインメニューです。番号を入力すると該当の処理が作動します。\n')

        if number == '1':
            try:
                ExtractDataMaker.do()

                print('----------------------------------')
                print('処理が完了しました。')
                print('----------------------------------')
            except:
                traceback.print_exc()
                print('エラーが発生しました。サポートを希望する場合は上記のエラーメッセージを開発者に提供してください。')

        elif number == '2':
            try:
                PronunciationMaker.do()
                print('----------------------------------')
                print('処理が完了しました。')
                print('----------------------------------')
            except:
                traceback.print_exc()
                print('エラーが発生しました。サポートを希望する場合は上記のエラーメッセージを開発者に提供してください。')

        elif number == '3':
            try:
                YmmpMaker.do()
                print('----------------------------------')
                print('処理が完了しました。')
                print('----------------------------------')
            except:
                traceback.print_exc()
                print('エラーが発生しました。サポートを希望する場合は上記のエラーメッセージを開発者に提供してください。')

        elif number == '4':
            try:
                AdjustYmmp.do()
                print('----------------------------------')
                print('処理が完了しました。')
                print('----------------------------------')
            except:
                traceback.print_exc()
                print('エラーが発生しました。サポートを希望する場合は上記のエラーメッセージを開発者に提供してください。')
        elif number == '5':
            try:
                print('!!!!!!!!!!!!!!!!!!')
                print('!!!!!!!!!!!!!!!!!!')
                print('Scenario,ExtractData,PronunciationData,Ymmp内のファイルを全て削除します。')
                print('復元は出来ません。必ず元台本はバックアップがある状態で行ってください。')
                print('実行準備が整ったら「Delete」と入力してエンターキーを押してください。')
                print('キャンセルしたい場合は「Delete」以外の文字(未入力含む)を入力してエンターキーを押してください。')
                print('!!!!!!!!!!!!!!!!!!')
                print('!!!!!!!!!!!!!!!!!!')
                delete_check = input('')

                if delete_check == 'Delete':
                    delete_file('./Scenario/')
                    delete_file('./ExtractData/')
                    delete_file('./PronunciationData/')
                    delete_file('./Ymmp/')
                    print('処理が完了しました。')
                else:
                    print('削除を中止しました。')


            except:
                traceback.print_exc()
                print('エラーが発生しました。サポートを希望する場合は上記のエラーメッセージを開発者に提供してください。')
except:
    traceback.print_exc()
    print('エラーが発生しました。サポートを希望する場合は上記のエラーメッセージを開発者に提供してください。')
    input('エンターキーで終了します。')
