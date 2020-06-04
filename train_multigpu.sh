#!/bin/bash

pkill python3
python3 -m multiproc train.py --output_directory=outdir --log_directory=logdir --hparams=distributed_run=True,fp16_run=True &
tensorboard --logdir=outdir/logdir
