#!/usr/bin/env python3

import vapoursynth as vs
import audiocutter
from subprocess import call
import shutil
import os

core = vs.core
ts_in = r'Zoku_Owarimonogatari/BDMV/STREAM/00010.m2ts'
src = core.lsmas.LWLibavSource(ts_in)

ac = audiocutter.AudioCutter()

vid = ac.split(src, [(24,2183)])

ac.ready_qp_and_chapters(vid)

vid.set_output(0)
if __name__ == "__main__":
    ac.cut_audio('ZokuOwariED_audiocut.m4a', audio_source='Zoku_Owarimonogatari/BDMV/STREAM/00010_Track01.m4a')
