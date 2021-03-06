#!/usr/bin/env python3
import acsuite as acs
import lvsfunc as lvf
ac = acs.AC()


path = r'BDMV/[BDMV] HONZUKI/HONZUKI_2/BDMV/STREAM/00013.m2ts'
src = lvf.src(path)

if __name__ == "__main__":
    ac.eztrim(src, [(24, -24)], path[:-4]+"wav", "BookwormBD_NCED1_cut.wav")
