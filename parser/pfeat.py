# print perf headers

def print_feat(feat):
    print(("# Measured on %s (%s)" % (
            feat.hostname.hostname,
            feat.osrelease.osrelease)))
    print(("# %s, %s" % (
            feat.cpudesc.cpudesc,
            feat.cpuid.cpuid)))
    print(("# %s" % (" ".join([x.cmdline for x in feat.cmdline.cmdline]))))
