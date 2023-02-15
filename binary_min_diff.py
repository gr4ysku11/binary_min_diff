#!/bin/python

import sys

# TODO
# exit if two args not passed in via argv

orig_file = open(sys.argv[1], 'rb')
fuzz_file = open(sys.argv[2], 'rb')

# TODO
# abort if both file sizes differ

# TODO
# parse file extension, if present

orig_bytes = orig_file.read()
fuzz_bytes = fuzz_file.read()

# loop over byte arrays and detect differences
i = 0
while(i < len(orig_bytes)):

    # if bytes differ, find next identical byte index
    if orig_bytes[i] != fuzz_bytes[i]:
        diff_file = open("{0}_offset{1}".format(fuzz_file.name,i), 'wb')

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