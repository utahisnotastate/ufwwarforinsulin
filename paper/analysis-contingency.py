from math import comb
# verdicts from the audit
V = {"A1":"P","A2":"P","A3":"N","A4":"S","A5":"S","A6":"P","A7":"N","A8":"N",
     "B1":"S","B2":"P","B3":"S","B4":"O","B5":"O","B6":"P","B7":"P","B8":"P","B9":"N","B10":"N","B11":"N",
     "D2":"P","D3":"N","D4":"S","D5":"S","D6":"N","D7":"N",
     "E1":"S","E2":"N","E3":"N","E4":"N","F1":"S"}
# blinded consensus (D4 adjudicated to SPECIFICATION = rater A, majority of the two on form)
MECH = ["A1","A2","A4","A5","A6","B1","B2","B3","B4","B5","B6","B7","B8","B10","D2","D3","D5","E1","E2","E3","F1"]
OUTC = ["A3","A7","A8","B9","B11","D6","D7","E4"]
def tally(ids):
    sup = sum(1 for i in ids if V[i] in ("S","P"))
    nos = sum(1 for i in ids if V[i]=="N")
    opn = sum(1 for i in ids if V[i]=="O")
    return sup,nos,opn
ms,mn,mo = tally(MECH); os_,on,oo = tally(OUTC)
print("  MECHANISM (n=%d): supported %d, not supported %d, open %d" % (len(MECH),ms,mn,mo))
print("  OUTCOME   (n=%d): supported %d, not supported %d, open %d" % (len(OUTC),os_,on,oo))
print("")
print("  2x2 (open excluded):")
print("                supported   not supported")
print("    mechanism      %2d            %2d" % (ms,mn))
print("    outcome        %2d            %2d" % (os_,on))
def fisher(a,b,c,d):
    def h(a,b,c,d): return comb(a+b,a)*comb(c+d,c)/comb(a+b+c+d,a+c)
    obs=h(a,b,c,d); r1,r2,c1=a+b,c+d,a+c; p=0.0
    for i in range(0,min(r1,c1)+1):
        j,k=r1-i,c1-i; l=r2-k
        if j<0 or k<0 or l<0: continue
        pr=h(i,j,k,l)
        if pr<=obs+1e-12: p+=pr
    return p
p = fisher(ms,mn,os_,on)
print("")
print("    mechanism supported: %d/%d = %.0f%%" % (ms,ms+mn,100*ms/(ms+mn)))
print("    outcome   supported: %d/%d = %.0f%%" % (os_,os_+on,100*os_/(os_+on) if os_+on else 0))
print("    Fisher's exact, two-sided p = %.3e" % p)
print("")
print("  vs. UNBLINDED v2 claim: 13/14 (93%) vs 0/13 (0%), p = 7.5e-07")
