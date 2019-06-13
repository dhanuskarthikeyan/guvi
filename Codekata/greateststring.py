ab=raw_input().split()
if len(ab[0])==len(ab[1]):
    print ab[0]
elif len(ab[0]) > len(ab[1]):
    print ab[0]
else:
    print ab[1]
