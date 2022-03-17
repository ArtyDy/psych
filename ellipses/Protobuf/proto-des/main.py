#%%
import sys
from typing import List, Any, Union
import os

import path_pb2 as proto
from google.protobuf.internal.decoder import _DecodeVarint32
import google


if __name__ == "__main__":
    pathf = 'E:/Manip/Psych/psych/ellipses/results'

    filenames = os.listdir(pathf)
    for f in filenames:
        print(f)
        # read all file as a string
        #if len(sys.argv) == 1:
         #for i in range (1,30)
          #  data = open("32.protobuf", "rb").read()
        #else:
         #   data = open(sys.argv[1], "rb").read()
        data = open(pathf+'/'+f, "rb").read()


        decoder = _DecodeVarint32

        path, pos = 0, 0

        aaa = f.split('.')

        output = open('E:/Manip/FE/Ellipses/output/'+aaa[0]+'.txt', 'w')


        next_pos, pos = 0, 0

        while pos < len(data):
            msg = proto.Path()
            next_pos, pos = decoder(data, pos)
            msg.ParseFromString(data[pos:pos + next_pos])

            # use parsed message
            output.write(
                'startParameter:\t{}\nendParameter:\t{}\ndecimalPrecision:\t{}\npoints:\t{}\nstrokeWidths:\t{}\nstrokeColor:\t{}\n\n'.format(
                msg.startParameter,
                msg.endParameter,
                msg.decimalPrecision,
                msg.points,
                msg.strokeWidths,
                msg.strokeColor
            ))

            # go to next pos
            pos += next_pos

        output.close()

# %%
