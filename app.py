from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from random import randint
# initialize our Flask application

app= Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST", "GET"])
@cross_origin()
def sendData():
    randomization1 = randint(0,7)
    randomization2 = randint(7,14)
    if(randomization1==3 and randomization2==11):
        randomLabel = randint(1,5)

        if(randomLabel == 1):
            data =  [(randint(-1885, 2047)) for _ in range(0, 178)]
            return jsonify({
                "Randomization": 1,
                "Label": 1,
                "Data": data,
            })
        elif(randomLabel == 2):
            data =  [(randint(-1147, 2047)) for _ in range(0, 178)]
            return jsonify({
                "Randomization": 1,
                "Label": 2,
                "Data": data,
            })
        elif(randomLabel == 3):
            data =  [(randint(-412, 623)) for _ in range(0, 178)]
            return jsonify({
                "Randomization": 1,
                "Label": 3,
                "Data": data,
            })
        elif(randomLabel == 4):
            data =  [(randint(-424, 360)) for _ in range(0, 178)]
            return jsonify({
                "Randomization": 1,
                "Label": 4,
                "Data": data,
            })
        else:
            data =  [(randint(-288, 294)) for _ in range(0, 178)]
            return jsonify({
                "Randomization": 1,
                "Label": 5,
                "Data": data,
            })
    else:
        data = [135.00, 190.00, 229.00, 223.00, 192.00, 125.00, 55.00, -9.00, -33.00, -38.00, -10.00, 35.00, 64.00, 113.00, 152.00, 164.00, 127.00, 50.00, -47.00, -121.00, -138.00, -125.00, -101.00, -50.00, 11.00, 39.00, 24.00, 48.00, 64.00, 46.00, 13.00, -19.00, -61.00, -96.00, -130.00, -132.00, -116.00, -115.00, -71.00, -14.00, 25.00, 19.00, 6.00, 9.00, 21.00, 13.00, -37.00, -58.00, -33.00, 5.00, 47.00, 80.00, 101.00, 88.00, 73.00, 69.00, 41.00, -13.00, -31.00, -61.00, -80.00, -77.00, -66.00, -43.00, 5.00, 87.00, 129.00, 121.00, 88.00, 12.00, -76.00, -150.00, -207.00, -186.00, -165.00, -148.00, -103.00, -33.00, 40.00, 94.00, 75.00, 8.00, -81.00, -155.00, -227.00, -262.00, -233.00, -218.00, -187.00, -126.00, -65.00, -12.00, 27.00, 61.00, 49.00, 9.00, -46.00, -124.00, -210.00, -281.00, -265.00, -181.00, -89.00, -4.00, 53.00, 53.00, 38.00, 43.00, 31.00, 34.00, 9.00, -7.00, -34.00, -70.00, -84.00, -101.00, -70.00, -11.00, 42.00, 62.00, 66.00, 74.00, 64.00, 59.00, 56.00, 36.00, -11.00, -30.00, -43.00, -23.00, 8.00, 42.00, 77.00, 103.00, 135.00, 121.00, 79.00, 59.00, 43.00, 54.00, 90.00, 111.00, 107.00, 64.00, 32.00, 18.00, -25.00, -69.00, -65.00, -44.00, -33.00, -57.00, -88.00, -114.00, -130.00, -114.00, -83.00, -53.00, -79.00, -72.00, -85.00, -109.00, -98.00, -72.00, -65.00, -63.00, -11.00, 10.00, 8.00, -17.00, -15.00, -31.00, -77.00, -103.00, -127.00, -116.00, -83.00, -51.00]
        return jsonify({
            "Randomization": 0,
            "Label": 0,
            "Data": data,
        })
    


#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=True, port=9797)