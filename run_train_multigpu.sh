#!/bin/bash

pkill python3
pkill tensorboard

rm -rf ./outdir/logdir/*
#python3 -m multiproc train.py --output_directory=outdir --log_directory=logdir --hparams=distributed_run=True,fp16_run=True &
#python3 -m multiproc train.py --output_directory=outdir --log_directory=logdir --hparams=distributed_run=True,fp16_run=True -c tacotron2_statedict.pt --warm_start&
#python3 -m multiproc train.py --output_directory=outdir --log_directory=logdir --hparams=distributed_run=True,fp16_run=True -c model_zoo/tacotron2_kss2000.pt --warm_start&
tensorboard --logdir=outdir/logdir &
python3 -m multiproc train.py --output_directory=outdir --log_directory=logdir --hparams=distributed_run=True,fp16_run=True -c outdir/checkpoint_0 --warm_start
