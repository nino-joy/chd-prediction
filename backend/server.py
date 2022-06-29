
from typing import final
from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
from tensorflow import keras
import random

app = Flask(__name__)


CORS(app)


@app.route('/api/', methods=["POST"])
def api_post():
    if request.method == 'POST':
        data = request.json
        savedModel = keras.models.load_model('final_model.h5')

        # reqData1 for DNN, reqData2 for FRS

        reqData1 = np.array([data['sex'], int(data['age']), int(data['BP']), int(data['chol']), int(
            data['hdlChol']), data['diabetic'], int(data['wCirc']), int(data['BMI']), int(data['nFat'])])

        # FRS value calculation
        reqData2 = reqData1.tolist()
        x = reqData2

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

        # print(x, "frs=", frs)

        # DNN model predicition
        op = savedModel.predict(reqData1.reshape(1, 9), batch_size=1)
        lst = op.tolist()
        finalop = lst[0][0]

        # FRS and DNN comparison and modification
        if frs <= 0:
            finalop = round(random.uniform(0.03, 0.10), 2)
        elif frs > 0 and frs < 12 and finalop > 0.50:
            finalop = finalop - 0.40
        elif frs >= 12 and frs <= 18 and finalop <= 0.40:
            finalop = round(random.uniform(0.4, 0.6), 2)
        elif frs >= 19:
            if finalop >= 0.00 and finalop < 0.30:
                finalop = finalop + 0.50
            elif finalop >= 0.30 and finalop <= 0.50:
                finalop = finalop + 0.30

        print(finalop)
        print(frs)
        # return op value to frontend
        finalop = str(finalop)
        return jsonify(pred=finalop, frs=frs)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
