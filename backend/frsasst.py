import pandas as pd
import numpy as np


str = (input("Enter a list element separated by space:'sex','age','bp','chol','hdl','diab','wc','bmi','N_FAT':-"))
x = str.split(',')
x = [int(i) for i in x]


# for i in range(len(x)):
frs = 0
if x[5] == 1:
    frs = frs+4
if x[7] >= 30:
    frs = frs+2


if x[0] == 1:

    if x[4] < 40:
        frs = frs+2
    elif x[4] >= 40 and x[4] <= 49:
        frs = frs+1
    elif x[4] >= 60:
        frs = frs-1

    if x[1] >= 20 and x[1] <= 34:
        frs = frs-9
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+4
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+7
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+9
        elif x[3] >= 280:
            frs = frs+11

    elif x[1] >= 35 and x[1] <= 39:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+4
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+7
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+9
        elif x[3] >= 280:
            frs = frs+11
        frs = frs-4
    elif x[1] >= 40 and x[1] <= 44:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+3
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+5
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+6
        elif x[3] >= 280:
            frs = frs+8
        frs = frs-0
    elif x[1] >= 45 and x[1] <= 49:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+3
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+5
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+6
        elif x[3] >= 280:
            frs = frs+8
        frs = frs+3
    elif x[1] >= 50 and x[1] <= 54:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+2
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+3
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+4
        elif x[3] >= 280:
            frs = frs+5
        frs = frs+6
    elif x[1] >= 55 and x[1] <= 59:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+2
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+3
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+4
        elif x[3] >= 280:
            frs = frs+5
        frs = frs+8
    elif x[1] >= 60 and x[1] <= 64:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+1
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+1
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+2
        elif x[3] >= 280:
            frs = frs+3
        frs = frs+10
    elif x[1] >= 65 and x[1] <= 69:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+1
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+1
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+2
        elif x[3] >= 280:
            frs = frs+3
        frs = frs+11
    elif x[1] >= 70 and x[1] <= 90:
        if x[3] >= 240 and x[3] <= 279:
            frs = frs+1
        elif x[3] >= 280:
            frs = frs+1
        frs = frs+12

    if x[2] >= 120 and x[2] <= 129:
        frs = frs+0
    elif x[2] >= 130 and x[2] <= 139:
        frs = frs+1
    elif x[2] >= 140 and x[2] <= 159:
        frs = frs+2
    elif x[2] >= 160:
        frs = frs+4


elif x[0] == 2:
    if x[4] < 40:
        frs = frs+2
    elif x[4] >= 40 and x[4] <= 49:
        frs = frs+1
    elif x[4] >= 60:
        frs = frs-1
    if x[1] >= 20 and x[1] <= 34:
        frs = frs-7
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+4
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+8
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+11
        elif x[3] >= 280:
            frs = frs+13

    elif x[1] >= 35 and x[1] <= 39:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+4
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+8
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+11
        elif x[3] >= 280:
            frs = frs+13
        frs = frs-3
    elif x[1] >= 40 and x[1] <= 44:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+3
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+6
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+8
        elif x[3] >= 280:
            frs = frs+10
        frs = frs-0
    elif x[1] >= 45 and x[1] <= 49:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+3
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+6
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+8
        elif x[3] >= 280:
            frs = frs+10
        frs = frs+3
    elif x[1] >= 50 and x[1] <= 54:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+2
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+4
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+5
        elif x[3] >= 280:
            frs = frs+7
        frs = frs+6
    elif x[1] >= 55 and x[1] <= 59:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+2
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+4
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+5
        elif x[3] >= 280:
            frs = frs+7
        frs = frs+8
    elif x[1] >= 60 and x[1] <= 64:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+1
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+2
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+3
        elif x[3] >= 280:
            frs = frs+4
        frs = frs+10
    elif x[1] >= 65 and x[1] <= 69:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+1
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+2
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+3
        elif x[3] >= 280:
            frs = frs+4
        frs = frs+12
    elif x[1] >= 70 and x[1] <= 90:
        if x[3] >= 160 and x[3] <= 199:
            frs = frs+1
        elif x[3] >= 200 and x[3] <= 239:
            frs = frs+1
        elif x[3] >= 240 and x[3] <= 279:
            frs = frs+2
        elif x[3] >= 280:
            frs = frs+2
        frs = frs+15

    if x[2] >= 120 and x[2] <= 129:
        frs = frs+2
    elif x[2] >= 130 and x[2] <= 139:
        frs = frs+3
    elif x[2] >= 140 and x[2] <= 159:
        frs = frs+4
    elif x[2] >= 160:
        frs = frs+6


print(x, "frs=", frs)
