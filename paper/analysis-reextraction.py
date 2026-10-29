# -*- coding: utf-8 -*-
"""Re-run the ordinal test with A3 decomposed as two independent extractors decomposed it."""
from math import comb
from itertools import combinations

V = {"A1":"P","A2":"P","A3":"N","A4":"S","A5":"S","A6":"P","A7":"N","A8":"N",
     "B1":"S","B2":"P","B3":"S","B4":"O","B5":"O","B6":"P","B7":"P","B8":"P","B9":"N","B10":"N","B11":"N",
     "D2":"P","D3":"N","D4":"S","D5":"S","D6":"N","D7":"N",
     "E1":"S","E2":"N","E3":"N","E4":"N","F1":"S"}
MECH = ["A1","A2","A4","A5","A6","B1","B2","B3","B4","B5","B6","B7","B8","B10","D2","D3","D5","E1","E2","E3","F1"]
OUTC = ["A3","A7","A8","B9","B11","D6","D7","E4"]
RANK = {"S":2,"P":1,"N":0}

def ordinal(mech, outc, verd):
    m=[RANK[verd[i]] for i in mech if verd[i]!="O"]
    o=[RANK[verd[i]] for i in outc if verd[i]!="O"]
    pool=m+o; n=len(pool); k=len(o); obs=sum(o)
    cnt=tot=0
    for idx in combinations(range(n),k):
        tot+=1
        if sum(pool[j] for j in idx)<=obs: cnt+=1
    return sum(m)/len(m), (sum(o)/len(o) if o else 0), 2*cnt/tot

def hyp(a,b,c,d): return comb(a+b,a)*comb(c+d,c)/comb(a+b+c+d,a+c)
def fisher(a,b,c,d):
    obs=hyp(a,b,c,d); r1,r2,c1=a+b,c+d,a+c; p=0.0
    for i in range(0,min(r1,c1)+1):
        j,k=r1-i,c1-i; l=r2-k
        if j<0 or k<0 or l<0: continue
        pr=hyp(i,j,k,l)
        if pr<=obs+1e-12: p+=pr
    return p
def dicho(mech,outc,verd,strict):
    def t(ids):
        ok=sum(1 for i in ids if (verd[i]=="S" if strict else verd[i] in ("S","P")))
        bad=sum(1 for i in ids if verd[i]!="O" and not (verd[i]=="S" if strict else verd[i] in ("S","P")))
        return ok,bad
    (ms,mn),(os_,on)=t(mech),t(outc)
    return ms,mn,os_,on,fisher(ms,mn,os_,on)

def show(label, mech, outc, verd):
    mm,om,p=ordinal(mech,outc,verd)
    ms,mn,os_,on,pl=dicho(mech,outc,verd,False)
    _,_,os2,on2,ps=dicho(mech,outc,verd,True)
    ms2=dicho(mech,outc,verd,True)[0]
    print("%-52s ord %.2f/%.2f p=%-9.4g | lenient %2d/%-2d vs %d/%-2d p=%-9.4g | strict %2d/%-2d vs %d/%-2d p=%.4g"
          % (label, mm, om, p, ms, ms+mn, os_, os_+on, pl, ms2, ms2+dicho(mech,outc,verd,True)[1], os2, os2+on2, ps))

print("="*185)
print("A3 DECOMPOSED AS TWO INDEPENDENT, HYPOTHESIS-BLIND EXTRACTORS DECOMPOSED IT")
print("Extractor 1: C007 C008 C009 C018 C026   |   Extractor 2: C076 C077 C078 C079 C080")
print("Both produced the same five boundaries. Neither isolated renal sodium retention.")
print("="*185)
show("ORIGINAL (A3 as one claim)", MECH, OUTC, V)

# Decomposition. Verdicts from INTEGRITY_AUDIT.md's own A3 sub-claim table.
#   a3a GLUT4 forced against thermodynamic gradient        -> mechanism, no basis as framed
#   a3b vascular proliferation + endothelial dysfn + ather -> outcome, bundles PARTLY(endoth) + NOT(ather)
#   a3c beta-cell apoptosis                                -> outcome, NOT TRUE (backwards: beta-cell rest preserves)
#   a3d reverse electron transport at Complex I            -> mechanism, OPEN (same content as B4/B5)
#   a3e smooth muscle hypertrophy + calcification + renal Na -> outcome, bundles NOT + VERIFIED(renal Na)
BASE = dict(V); del BASE["A3"]
M5 = [i for i in MECH]; O5 = [i for i in OUTC if i!="A3"]

# (i) worst-sub-claim-governs, the rule stated in Methods
Vw = dict(BASE); Vw.update({"a3a":"N","a3b":"N","a3c":"N","a3d":"O","a3e":"N"})
show("decomposed, worst-governs (stated rule)", M5+["a3a","a3d"], O5+["a3b","a3c","a3e"], Vw)

# (ii) best-sub-claim-governs on the bundle containing the verified mechanism
Vb = dict(BASE); Vb.update({"a3a":"N","a3b":"P","a3c":"N","a3d":"O","a3e":"S"})
show("decomposed, best-governs on a3b and a3e", M5+["a3a","a3d"], O5+["a3b","a3c","a3e"], Vb)

# (iii) maximally hostile: all five to OUTCOME, best-governs
show("MAX HOSTILE: all 5 to outcome, best-governs", M5, O5+["a3a","a3b","a3c","a3d","a3e"], Vb)

# (iv) the reviewer's construction: renal sodium retention isolated as its own VERIFIED outcome claim
#      (no independent extractor actually did this)
Vr = dict(BASE); Vr.update({"a3a":"N","a3b":"N","a3c":"N","a3d":"O","a3e":"N","a3f":"S"})
show("reviewer's split (NOT reproduced by extractors)", M5+["a3a","a3d"], O5+["a3b","a3c","a3e","a3f"], Vr)

print()
print("="*185)
print("EXTRACTION INSTABILITY (pre-registered measure)")
print("="*185)
orig, e1, e2 = 61, 258, 237
print("  author              : %3d claims" % orig)
print("  extractor 1         : %3d claims   d vs author = %.2f" % (e1, abs(e1-orig)/orig))
print("  extractor 2         : %3d claims   d vs author = %.2f" % (e2, abs(e2-orig)/orig))
print("  extractor 1 vs 2    : difference %d, %.1f%% of their mean" % (abs(e1-e2), 100*abs(e1-e2)/((e1+e2)/2)))
print()
print("  Pre-registered threshold was d > 0.30 for 'granularity is unstable'. Both exceed it by")
print("  an order of magnitude. The two extractors agree closely with EACH OTHER, so this is not")
print("  definitional noise: the author's extraction was systematically coarse.")
