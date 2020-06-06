'''
IntFlow Co., Ltd.
Develped by Kwang Myung Jeon, 2020-06-06
'''

from scipy.io.wavfile import write
import librosa
import numpy as np
from scipy import signal
import argparse
import warnings
warnings.filterwarnings("ignore")

sr = 22050
max_wav_value=32768.0
trim_fft_size = 1024
trim_hop_size = 256
trim_top_db = 23

#Creation of the filter
cutOff = 100 # Cutoff frequency
nyq = 0.5 * sr
N  = 8    # Filter order
fc = cutOff / nyq # Cutoff frequency normal
b, a = signal.butter(N, fc, btype='highpass')

def preprocess_audio(file_list, silence_audio_size):
    for F in file_list:
        f = open(F, encoding="utf-8")
        R = f.readlines()
        f.close()
        print('='*5+F+'='*5)

        for i, r in enumerate(R):
            wav_file = r.split('|')[0]
            print(wav_file)
            data, sampling_rate = librosa.load(wav_file)

            #Apply the filter
            data = signal.filtfilt(b,a, data)

            data = data / np.abs(data).max() *0.999
            # get the noisy interval
            #non_silent_interval = librosa.effects.split(data, top_db=trim_top_db, hop_length=trim_hop_size)
            #print(non_silent_interval)
            data_= librosa.effects.trim(data, top_db= trim_top_db, frame_length=trim_fft_size, hop_length=trim_hop_size)[0]
            data_ = data_*max_wav_value
            data_ = np.append(data_, [0.]*silence_audio_size)
            data_ = data_.astype(dtype=np.int16)
            write(wav_file, sr, data_)
            #print(len(data),len(data_))
            if(i%100 == 0):
                print (i)

if __name__ == "__main__":
    """
    usage
    python preprocess_audio.py -f=filelists/nam-h_test_filelist.txt,filelists/nam-h_train_filelist.txt,filelists/nam-h_val_filelist.txt -s=3
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_list', type=str, default='./filelists/kss_audio_text_test_filelist.txt',
                        help='file list to preprocess')
    parser.add_argument('-s', '--silence_mel_padding', type=int, default=0,
                        help='silence audio size is hop_length * silence mel padding')
    args = parser.parse_args()
    file_list = args.file_list.split(',')
    silence_audio_size = trim_hop_size * args.silence_mel_padding
    preprocess_audio(file_list, silence_audio_size)
