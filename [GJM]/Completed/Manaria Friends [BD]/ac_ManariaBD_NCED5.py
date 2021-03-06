#!/usr/bin/env python3

import vapoursynth as vs
import audiocutter
from subprocess import call
import os

core = vs.core
ts_in = r"BDMV/[BDMV][190402][マナリアフレンズ II]/BD/BDMV/STREAM/00012.m2ts"
src = core.lsmas.LWLibavSource(ts_in)

ac = audiocutter.AudioCutter()

vid = ac.split(src, [(24,982+23)])

ac.ready_qp_and_chapters(vid)

vid.set_output(0)
if __name__ == "__main__":
    ac.cut_audio('ManariaBD_NCED5_ac.m4a', audio_source='BDMV/[BDMV][190402][マナリアフレンズ II]/BD/BDMV/STREAM/00012.m4a')
