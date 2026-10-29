# -*- coding: utf-8 -*-
"""Sensitivity analyses for the mechanism/outcome dissociation.

Added 2026-10-29 in response to external peer review, which correctly identified
that the published analysis used a lenient dichotomisation (VERIFIED or PARTLY TRUE
= "supported") that was never stated in the manuscript, and never tested.

Run:  python analysis-sensitivity.py
"""
from math import comb, sqrt

V = {"A1":"P","A2":"P","A3":"N","A4":"S","A5":"S","A6":"P","A7":"N","A8":"N",
     "B1":"S","B2":"P","B3":"S","B4":"O","B5":"O","B6":"P","B7":"P","B8":"P","B9":"N","B10":"N","B11":"N",
     "D2":"P","D3":"N","D4":"S","D5":"S","D6":"N","D7":"N",
     "E1":"S","E2":"N","E3":"N","E4":"N","F1":"S"}
MECH = ["A1","A2","A4","A5","A6","B1","B2","B3","B4","B5","B6","B7","B8","B10","D2","D3","D5","E1","E2","E3","F1"]
OUTC = ["A3","A7","A8","B9","B11","D6","D7","E4"]

def hyp(a,b,c,d):
    return comb(a+b,a)*comb(c+d,c)/comb(a+b+c+d,a+c)

def fisher(a,b,c,d):
    obs=hyp(a,b,c,d); r1,r2,c1=a+b,c+d,a+c; p=0.0
    for i in range(0,min(r1,c1)+1):
        j,k=r1-i,c1-i; l=r2-k
        if j<0 or k<0 or l<0: continue
        pr=hyp(i,j,k,l)
        if pr<=obs+1e-12: p+=pr
    return p

def wilson(k,n,z=1.96):
    if n==0: return (0.0,0.0)
    p=k/n; d=1+z*z/n
    c=(p+z*z/(2*n))/d
    h=z*sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return (max(0.0,c-h), min(1.0,c+h))

def table(verdicts, mech, outc, strict):
    def t(ids):
        ok  = sum(1 for i in ids if (verdicts[i]=="S" if strict else verdicts[i] in ("S","P")))
        bad = sum(1 for i in ids if verdicts[i]!="O" and not (verdicts[i]=="S" if strict else verdicts[i] in ("S","P")))
        return ok,bad
    return t(mech), t(outc)

def report(label, verdicts, mech, outc, strict):
    (ms,mn),(os_,on) = table(verdicts,mech,outc,strict)
    p = fisher(ms,mn,os_,on)
    lo,hi = wilson(ms,ms+mn); lo2,hi2 = wilson(os_,os_+on)
    print("%-46s  mech %2d/%-2d (%3.0f%%, CI %2.0f-%2.0f)   outc %d/%-2d (%2.0f%%, CI %2.0f-%2.0f)   p = %.4g"
          % (label, ms,ms+mn,100*ms/(ms+mn),100*lo,100*hi, os_,os_+on,
             100*os_/(os_+on) if os_+on else 0,100*lo2,100*hi2, p))
    return p

print("="*150)
print("1. DICHOTOMISATION SENSITIVITY  (the analysis the reviewer says was never run)")
print("="*150)
report("LENIENT  - supported = VERIFIED or PARTLY TRUE", V, MECH, OUTC, False)
report("STRICT   - supported = VERIFIED only",           V, MECH, OUTC, True)

print()
print("="*150)
print("2. B6 RECODE  (reviewer: audit says 'VERIFIED as citation / NOT TRUE as dominant mechanism';")
print("   the inventoried claim asserts the dominant-mechanism reading, so it should be N, not P)")
print("="*150)
V6 = dict(V); V6["B6"]="N"
report("LENIENT, B6 recoded to NOT TRUE", V6, MECH, OUTC, False)
report("STRICT,  B6 recoded to NOT TRUE", V6, MECH, OUTC, True)

print()
print("="*150)
print("3. A3 SPLIT  (reviewer: A3 bundles six mechanisms, one of which the audit verifies.")
print("   Worst-sub-claim-governs was applied to A3 but best-sub-claim-governs to B2.")
print("   Hostile case: split A3 and credit its one verified sub-claim to the OUTCOME column.)")
print("="*150)
VA = dict(V6); VA["A3a"]="S"
OUTC_A = OUTC + ["A3a"]
report("LENIENT, B6 recoded + A3 split (worst case)", VA, MECH, OUTC_A, False)
report("STRICT,  B6 recoded + A3 split (worst case)", VA, MECH, OUTC_A, True)

print()
print("="*150)
print("4. BLOCK-STRATIFIED EXACT TEST  (reviewer M10: stratum is confounded with document block.")
print("   Is the dissociation present WITHIN blocks, or only between them?)")
print("="*150)
def blk(i): return i[0]
for strict in (False, True):
    print("\n  %s coding:" % ("STRICT" if strict else "LENIENT"))
    print("    block   mech supported    outc supported")
    num=den=0.0; obs_a=0; exp_a=0.0; var_a=0.0
    for b in sorted(set(blk(i) for i in MECH+OUTC)):
        m=[i for i in MECH if blk(i)==b]; o=[i for i in OUTC if blk(i)==b]
        (ms,mn),(os_,on)=table(V,m,o,strict)
        n=ms+mn+os_+on
        if n==0: continue
        print("      %s       %2d/%-2d              %d/%-2d" % (b,ms,ms+mn,os_,os_+on))
        if ms+mn and os_+on:
            # Mantel-Haenszel accumulation
            obs_a += ms
            r1=ms+mn; r2=os_+on; c1=ms+os_; c2=mn+on
            exp_a += r1*c1/n
            if n>1: var_a += r1*r2*c1*c2/(n*n*(n-1))
    if var_a>0:
        chi=(abs(obs_a-exp_a)-0.5)**2/var_a
        # survival function of chi2 with 1 df via erfc
        from math import erfc
        p_cmh = erfc(sqrt(chi/2))
        print("    Cochran-Mantel-Haenszel (continuity-corrected): chi2 = %.3f, 1 df, p = %.4g" % (chi,p_cmh))
    else:
        print("    CMH not estimable: no block contains both arms with variance")

print()
print("="*150)
print("5. EXACT ODDS RATIO BOUND  (reviewer M17: OR is infinite; report the one-sided lower bound)")
print("="*150)
for strict,lab in ((False,"LENIENT"),(True,"STRICT")):
    (ms,mn),(os_,on)=table(V,MECH,OUTC,strict)
    # one-sided lower 95% bound: largest psi with P(X >= ms | psi) >= 0.05
    def pcond(ms_,r1,r2,c1,psi):
        tot=0.0; num=0.0
        lo=max(0,c1-r2); hi=min(r1,c1)
        for i in range(lo,hi+1):
            w=comb(r1,i)*comb(r2,c1-i)*(psi**i)
            tot+=w
            if i>=ms_: num+=w
        return num/tot
    r1,r2,c1=ms+mn,os_+on,ms+os_
    lo_b, hi_b = 1e-6, 1e6
    for _ in range(200):
        mid=sqrt(lo_b*hi_b)
        if pcond(ms,r1,r2,c1,mid) >= 0.05: hi_b=mid
        else: lo_b=mid
    print("  %-8s  conditional MLE odds ratio = infinity;  one-sided 95%% lower bound = %.2f" % (lab, sqrt(lo_b*hi_b)))

print()
print("="*150)
print("6. BONFERRONI  (reviewer M17: six pairwise comparisons among four strata)")
print("="*150)
for strict,lab in ((False,"LENIENT"),(True,"STRICT")):
    (ms,mn),(os_,on)=table(V,MECH,OUTC,strict)
    p=fisher(ms,mn,os_,on)
    print("  %-8s  p = %.4g   Bonferroni x6 = %.4g   %s at alpha=0.05"
          % (lab,p,min(1,p*6), "SURVIVES" if p*6<0.05 else "DOES NOT SURVIVE"))

print()
print("="*150)
print("7. ORDINAL TEST  (no dichotomisation required)")
print("   The dependence on a cut point is itself the reviewer's objection. An exact")
print("   permutation test on the ordinal verdict scale VERIFIED(2) > PARTLY TRUE(1) >")
print("   NOT TRUE/NO BASIS(0) uses all the information and chooses no cut.")
print("="*150)
from itertools import combinations
RANK = {"S":2,"P":1,"N":0}
def ordinal_perm(mech, outc, verdicts):
    m=[RANK[verdicts[i]] for i in mech if verdicts[i]!="O"]
    o=[RANK[verdicts[i]] for i in outc if verdicts[i]!="O"]
    pool=m+o; n=len(pool); k=len(o)
    obs=sum(o)
    # exact: enumerate all C(n,k) assignments of which items fall in the outcome arm
    cnt=0; tot=0
    for idx in combinations(range(n),k):
        s=sum(pool[j] for j in idx)
        tot+=1
        if s<=obs: cnt+=1
    return obs, sum(m)/len(m), sum(o)/len(o) if o else 0, cnt/tot, tot
obs,mmean,omean,p1,tot = ordinal_perm(MECH,OUTC,V)
print("  mean verdict rank  mechanism = %.2f   outcome = %.2f   (scale 0-2)" % (mmean,omean))
print("  exact one-sided permutation p = %.4g  (%d permutations enumerated)" % (p1,tot))
print("  two-sided (doubled)          = %.4g" % min(1,2*p1))
V6b=dict(V); V6b["B6"]="N"
_,mm2,om2,p2,_ = ordinal_perm(MECH,OUTC,V6b)
print("  with B6 recoded to NOT TRUE: mech mean %.2f, one-sided p = %.4g, two-sided = %.4g" % (mm2,p2,min(1,2*p2)))
VA2=dict(V6b); VA2["A3a"]="S"
_,mm3,om3,p3,_ = ordinal_perm(MECH,OUTC+["A3a"],VA2)
print("  with B6 recoded AND A3 split (worst case): one-sided p = %.4g, two-sided = %.4g" % (p3,min(1,2*p3)))
