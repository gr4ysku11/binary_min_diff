#!/usr/bin/env python

import sys

# exit if two args not passed in via argv
if sys.argv.count != 2:
    print("[USAGE] binary_min_diff.py <original file> <fuzzed crash file>")
    exit()

orig_file = open(sys.argv[1], 'rb')
fuzz_file = open(sys.argv[2], 'rb')

# parse file extension
# assumes original file has extension and fuzz/crash files do not
# as is the case with afl, afl++, winafl, etc...
ext_i = orig_file.name.rfind(".")
ext = orig_file.name[ext_i+1:]

orig_bytes = orig_file.read()
fuzz_bytes = fuzz_file.read()

# abort if file sizes differ
if (len(orig_bytes != fuzz_bytes)):
    print("[ABORT] file lengths do not match!")
    exit()

# loop over byte arrays and detect differences
i = 0
while(i < len(orig_bytes)):

    # if bytes differ, find next identical byte index
    if orig_bytes[i] != fuzz_bytes[i]:

        diff_file = open("{0}_offset{1}.{2}".format(fuzz_file.name,i,ext), 'wb')

        # copy original bytes up to difference
        diff_file.write(orig_bytes[0:i])

        # find next identical match
        for j in range(i+1, len(orig_bytes)):

            # if bytes match
            if orig_bytes[j] == fuzz_bytes[j]:

                # write fuzzed bytes into diff file
                diff_file.write(fuzz_bytes[i:j])

                # write remaining original bytes
                diff_file.write(orig_bytes[j:])
                diff_file.close()

                i = j
                break
    i += 1