"""Pool compare.py rows (JSON lines) by configuration and run the checks."""
import sys, json, numpy as np
rows = [json.loads(l) for l in open(sys.argv[1])]
checks = []
def check(name, ok):
    checks.append((name, bool(ok))); print(("PASS " if ok else "FAIL ") + name)
groups = {}
for r in rows:
    groups.setdefault(r["file"].rsplit("_s", 1)[0], []).append(r)
out = {}
for g, rs in groups.items():
    a = rs[0]["a"]
    ac = np.array([r["a_count"] for r in rs]); af = np.array([r["a_field"] for r in rs])
    m_c, e_c = ac.mean(), ac.std(ddof=1)/np.sqrt(len(ac)); m_f, e_f = af.mean(), af.std(ddof=1)/np.sqrt(len(af))
    out[g] = (a, m_c, e_c, m_f, e_f)
    print(f"{g}: {len(rs)} causal sets, true a = {a}")
    print(f"   count side  a = {m_c:.2f} +/- {e_c:.2f}   ({m_c/a-1:+.1%})   T = {m_c/(2*np.pi):.3f}")
    print(f"   field side  a = {m_f:.2f} +/- {e_f:.2f}   ({m_f/a-1:+.1%})   T = {m_f/(2*np.pi):.3f}")
    jl = np.mean([r["joint_lnV"] for r in rs]); js = np.mean([r["joint_lnsigma"] for r in rs])
    print(f"   SJ Re W joint regression: ln(local count) {jl:+.4f}, ln(continuum interval) {js:+.4f}; "
          f"field log-slope alpha = {np.mean([r['alpha'] for r in rs]):+.4f} (continuum -1/4pi = {-1/(4*np.pi):+.4f})")
cen, ext = out["sj_6000_a16"], out["sj_4000_a8"]
check("count side recovers the writer's temperature on the causal set, central writer (within 6%)", abs(cen[1]/cen[0] - 1) < 0.06)
check("count side recovers it for the extended writer too (within 4%)", abs(ext[1]/ext[0] - 1) < 0.04)
check("field side (SJ, built from the order alone) recovers it for the central writer (within 6%)", abs(cen[3]/cen[0] - 1) < 0.06)
check("central writer: count-defined and field-defined temperatures agree (within 2 sigma combined)",
      abs(cen[1] - cen[3]) < 2*np.hypot(cen[2], cen[4]))
check("extended writer: the field side departs (>15%) while the count side does not -> the state, not discreteness",
      ext[3]/ext[0] - 1 > 0.15 and abs(ext[1]/ext[0] - 1) < 0.04)
check("the SJ field does NOT track the local interval count alone: continuum interval dominates the joint fit",
      all(abs(r["joint_lnsigma"]) > 2*abs(r["joint_lnV"]) for r in rows))
print(f"\n{sum(o for _, o in checks)}/{len(checks)} checks passed")
