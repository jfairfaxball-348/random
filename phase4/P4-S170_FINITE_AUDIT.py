#!/usr/bin/env python3
"""P4-S170 local finite-word prefix-code sanity; NOT a proof or hosted CI."""
from itertools import product

def P(s):
    n=s.find("1")
    if n<0 or n+1>=len(s):
        return None
    return s[n+1] + "0"*n + "1" + s[n+2:]

def main():
    total=0
    for L in range(2,12):
        dom=["".join(t) for t in product("01",repeat=L) if P("".join(t)) is not None]
        images=[P(s) for s in dom]
        target={"".join(t) for t in product("01",repeat=L) if "1" in "".join(t)[1:]}
        assert len(dom)==2**L-2
        assert len(set(images))==len(images)
        assert set(images)==target
        total+=len(dom)
    assert total==4072
    print("PASS LOCAL FINITE SANITY",total)

if __name__=="__main__":
    main()
