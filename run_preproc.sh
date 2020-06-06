#!/bin/bash

#	--file_list=filelists/kss_audio_text_train_filelist.txt,filelists/kss_audio_text_val_filelist.txt \

python3 preprocess_audio.py \
	--file_list=filelists/kss_audio_text_val_filelist.txt \
        --silence_mel_padding=0
