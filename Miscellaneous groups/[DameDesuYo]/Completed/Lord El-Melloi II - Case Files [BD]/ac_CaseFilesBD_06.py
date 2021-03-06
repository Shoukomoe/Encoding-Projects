#!/usr/bin/env python3
import acsuite as acs
import lvsfunc as lvf
ac = acs.AC()


path = r'BDMV/[BDMV][191106][Lord El-Melloi II-sei no Jikenbo][Vol.03]/BDROM/BDMV/STREAM/00002.m2ts'
src = lvf.src(path)

if __name__ == "__main__":
    ac.eztrim(src, [(24, -24)], path[:-4]+"wav", "CaseFilesBD_06_cut.wav")
