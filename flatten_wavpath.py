'''
IntFlow Co., Ltd.
Develped by Kwang Myung Jeon, 2020-06-06
'''

import numpy as np
import argparse
import warnings
import os
from shutil import copyfile
warnings.filterwarnings("ignore")

def preprocess_audio(file_list, target_folder):

    #Make Target Folder
    os.makedirs(target_folder, exist_ok=True)

    f = open(file_list, encoding="utf-8")
    R = f.readlines()
    f.close()
    print('='*5+file_list+'='*5)

    for i, r in enumerate(R):
        wav_file = r.split('|')[0]
        src = wav_file
        wav_file_pathes = wav_file.split('/')[1:]
        
        dst = target_folder + '/'
        for j, W in enumerate(wav_file_pathes):
            if j == 0:
                dst += W
            else:
                dst = dst + '_' + W
        print(src)
        print(dst)
        copyfile(src, dst)

if __name__ == "__main__":
    """
    usage
    python preprocess_audio.py -f=filelists/nam-h_test_filelist.txt,filelists/nam-h_train_filelist.txt,filelists/nam-h_val_filelist.txt -s=3
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_list', type=str, default='./filelists/skylife_audio_text_val_filelist.txt',
                        help='file list to preprocess')
    parser.add_argument('-tf', '--target_folder', type=str, default='./datasets/skylife/val',
                        help='target folders for flatten')
    args = parser.parse_args()
    file_list = args.file_list
    target_folder = args.target_folder
    preprocess_audio(file_list, target_folder)
