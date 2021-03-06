#!/usr/bin/env python3

import vapoursynth as vs
import audiocutter
from subprocess import call
import os

# Note: before cutting
preview = 16688
endcard = 16808
part_b = 16928
epend = 20044

# Note: after cutting
edstart = 15585


core = vs.core
ts_in = r"BDMV/[BDMV][190302][マナリアフレンズ I]/BD/BDMV/STREAM/00009.m2ts"
src = core.lsmas.LWLibavSource(ts_in)

ac = audiocutter.AudioCutter()

vid = ac.split(src, [(24,preview-1),(endcard,endcard+48),(part_b,epend),(preview,part_b)])

ac.ready_qp_and_chapters(vid)

vid.set_output(0)
if __name__ == "__main__":
    ac.cut_audio('ManariaBD_03_ac.m4a', audio_source='BDMV/[BDMV][190302][マナリアフレンズ I]/BD/BDMV/STREAM/00009.m4a')

os.remove("tmp-001.mka")
os.remove("tmp-002.mka")
os.remove("tmp-003.mka")
os.remove("tmp-004.mka")
