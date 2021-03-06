#!/usr/bin/env python3
import acsuite as acs
import lvsfunc as lvf
ac = acs.AC()


path = r'BDMV/[BDMV][200220][Kimetsu no Yaiba][Vol.8]/BDMV/STREAM/00007.m2ts'
src = lvf.src(path)

if __name__ == "__main__":
    ac.eztrim(src, [(24, -26)], path[:-4]+"wav", "YaibaBD_NCED_19_cut.wav")
