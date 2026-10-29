import sys, re, json
from math import comb
from collections import Counter

def load(path):
    d={}
    for line in open(path, encoding="utf-8-sig"):
        m = re.match(r"\s*([A-FX]\d{1,2})\s*[:\-]\s*(MECHANISM|OUTCOME|SPECIFICATION|PHYSICS)", line.strip(), re.I)
        if m: d[m.group(1)] = m.group(2).upper()
    return d

def kappa(a, b):
    ids = sorted(set(a) & set(b))
    n = len(ids)
    agree = sum(1 for i in ids if a[i]==b[i])
    po = agree/n
    cats = sorted(set(list(a.values())+list(b.values())))
    pe = sum((sum(1 for i in ids if a[i]==c)/n) * (sum(1 for i in ids if b[i]==c)/n) for c in cats)
    k = (po-pe)/(1-pe) if pe < 1 else 1.0
    return n, agree, po, pe, k, ids

def fisher2x2(a,b,c,d):
    def h(a,b,c,d): return comb(a+b,a)*comb(c+d,c)/comb(a+b+c+d,a+c)
    obs=h(a,b,c,d); r1,r2,c1=a+b,c+d,a+c; p=0.0
    for i in range(0,min(r1,c1)+1):
        j,k2=r1-i,c1-i; l=r2-k2
        if j<0 or k2<0 or l<0: continue
        pr=h(i,j,k2,l)
        if pr<=obs+1e-12: p+=pr
    return p

if __name__ == "__main__":
    A, B = load(sys.argv[1]), load(sys.argv[2])
    n, agree, po, pe, k, ids = kappa(A,B)
    print("=== INTER-RATER RELIABILITY ===")
    print("  claims rated by both : %d" % n)
    print("  exact agreement      : %d/%d = %.1f%%" % (agree, n, 100*po))
    print("  expected by chance   : %.4f" % pe)
    print("  Cohen's kappa        : %.3f" % k)
    print("  interpretation       : %s" % ("almost perfect" if k>=.81 else "substantial" if k>=.61 else "moderate" if k>=.41 else "fair"))
    print("")
    print("  rater A distribution:", dict(Counter(A.values())))
    print("  rater B distribution:", dict(Counter(B.values())))
    dis = [i for i in ids if A[i]!=B[i]]
    print("")
    print("  disagreements (%d): %s" % (len(dis), ", ".join("%s[A=%s/B=%s]"%(i,A[i][:4],B[i][:4]) for i in dis) if dis else "none"))
    if len(sys.argv) > 3:
        json.dump({"A": A, "B": B, "kappa": k, "agreement": po,
                   "disagreements": dis}, open(sys.argv[3], "w"), indent=1)
        print("\n  -> saved %s" % sys.argv[3])

