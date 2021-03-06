#!/usr/bin/env python3

import vapoursynth as vs
import audiocutter
from subprocess import call

core = vs.core
ts_in = r"../Fate Grand Order -First Order-/BDROM/BDMV/STREAM/00000.m2ts"
src = core.lsmas.LWLibavSource(ts_in)

ac = audiocutter.AudioCutter()

vid = ac.split(src, [(24,103912)])

ac.ready_qp_and_chapters(vid)

vid.set_output(0)
if __name__ == "__main__":
    ac.cut_audio(r'CMs/FGO_FO01_cut.flac', audio_source=r'../Fate Grand Order -First Order-/BDROM/BDMV/STREAM/00000.flac')
