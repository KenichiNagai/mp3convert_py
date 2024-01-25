import glob
import os
from pydub import AudioSegment
# import pydub

AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = "C:\\ffmpeg\\bin\\ffprobe.exe"

# ファイルが存在するか確認
print(os.path.exists('C:\\ffmpeg\\bin\\ffmpeg.exe'))
print(os.path.exists('C:\\ffmpeg\\bin\\ffprobe.exe'))

def main():
    folder_path = r"C:\Users"
    file_paths_m4a = glob.glob(folder_path + '\\*.m4a')
    file_paths_opus = glob.glob(folder_path + '\\*.opus')

    print(file_paths_m4a)

    # 出力フォルダがなければ作成する
    output_folder_path = folder_path + r"\output"
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)

    for file_path_m4a in file_paths_m4a:
        print('path')
        print(file_path_m4a)
        # ファイルの存在確認
        print(os.path.exists(file_path_m4a))

        # ボイスメモで収録したm4aファイルを読み込む
        sounds = AudioSegment.from_file(file_path_m4a, 'm4a')

        # 基本情報の表示
        print(f'channel: {sounds.channels}')
        print(f'frame rate: {sounds.frame_rate}')
        print(f'duration: {sounds.duration_seconds} s')
        exit()
    
    
        convert_from_m4a_to_mp3(file_path_m4a, output_folder_path + '\\' + os.path.basename(file_path_m4a) + '.mp3')
    


    for file_path_opus in file_paths_opus:
        print('path')
        print(file_path_opus)
        convert_from_opus_to_mp3(file_path_opus, output_folder_path + '\\' + os.path.basename(file_path_opus) + '.mp3')

    print('finished')


def convert_from_m4a_to_mp3(input_file, output_file):
    sound = AudioSegment.from_file(input_file, format="m4a")
    sound.export(output_file, format="mp3", bitrate="192k")  # 例: 192kbpsのビットレート


def convert_from_opus_to_mp3(input_file, output_file):
    sound = AudioSegment.from_file(input_file, format="opus")
    sound.export(output_file, format="mp3", bitrate="192k")  # 例: 192kbpsのビットレート



if __name__ == '__main__':
    main()
