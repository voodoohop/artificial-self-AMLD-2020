#!/bin/sh

spell run --machine-type V100_spot --pip-req requirements.txt --apt autossh --apt ffmpeg --apt psmisc --apt build-essential --apt libasound2-dev --apt libjack-dev --apt portaudio19-dev --apt sox -m uploads/chatistics_export:data -- python train.py --run_name run_all_lang --model gpt2 --n_epochs 100