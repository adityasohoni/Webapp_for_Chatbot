import json,time
from camera import VideoCamera
from flask import Flask, render_template, request, jsonify, Response
import requests
import base64,cv2


app=Flask(__name__)
output=[]#("message stark","hi")]
# coordinates of NITK Surathkal
lat = 13.001864136351472
lng = 74.80495038765815

def getCoordinates(text):
    firstWord = text.split()[0]
    
    # coordinates of NITK Surathkal
    lat = 13.001864136351472
    lng = 74.80495038765815
    
    if(firstWord == 'Mudrika'):
        lat = 13.008641224563956
        lng = 74.79418828368352
    if( firstWord == 'MainBuilding'):
        lat = 13.06961353476527 
        lng =  74.78629159322206
    if( firstWord == 'OceanPearl'):
        lat = 13.02267735427792
        lng =  74.79054242887052
    if( firstWord == 'Yennar'):
        lat = 13.018314457068078
        lng = 74.81208948121525
    if( firstWord == 'Health'):
        lat = 13.125330866265447
        lng = 74.8011031535809
    if( firstWord == 'Sports'):
        lat = 12.975494928028214
        lng = 74.82307580884962
    if( firstWord == 'SBIBank'):
        lat = 13.077179226201334
        lng = 74.76814417067781
    if( firstWord == 'CCC'):
        lat = 13.066477583824591
        lng = 74.78462366212935
    if( firstWord == 'Central'):
        lat = 13.082529873304695
        lng = 74.79011682594653
    
    return lat,lng
@app.route('/')
def home_page():
    return render_template("IY_Home_page.html",result=output,latitude = lat, longitude = lng)
@app.route('/about')
def about_page():
    return render_template("about.html",result=output)
@app.route('/contact')
def contact_page():
    return render_template("contact.html",result=output)
@app.route('/charts')
def charts_page():
    return render_template("charts.html",result=output)

# @app.route('/cam')
# def sign_page():
#     return render_template("camera.html")


# @app.route('/camera',methods=['POST'])
# def camera():
#     cap=cv2.VideoCapture(0)
#     while True:
#         ret,img=cap.read()
#         img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#         cv2.imwrite("static/cam.png",img)

#         # return render_template("camera.html",result=)
#         time.sleep(0.1)
#         return json.dumps({'status': 'OK', 'result': "static/cam.png"})
#         if cv2.waitKey(0) & 0xFF ==ord('q'):
#             break
#     cap.release()
#     # file="/home/ashish/Downloads/THOUGHT.png"
#     # with open(file,'rb') as file:
#     #     image=base64.encodebytes(file.read())
#     #     print(type(image))
#     # return json.dumps({'status': 'OK', 'user': user, 'pass': password});
#     return json.dumps({'status': 'OK', 'result': "static/cam.png"});

# def gen(camera):
#     while True:
#         data= camera.get_frame()

#         frame=data[0]
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/result',methods=["POST","GET"])
def Result():
    if request.method=="POST":
        print(list(request.form.values()))
        result=list(request.form.values())[0]
        if result.lower()=="restart":
            output.clear()
        else:
            try:
                r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": result})
                print("Bot says, ")
                output.extend([("message parker",result)])
                lat,lng = getCoordinates(r.json()[0]['text'])
                for i in r.json():
                    bot_message = i['text']
                    print(f"{i['text']}")
                    output.extend([("message stark",bot_message)])
            except:
                output.extend([("message parker", result), ("message stark", "We are unable to process your request at the moment. Please try again...")])

        print(output)
        return render_template("IY_Home_page.html",result=output,latitude=lat,longitude = lng)

if __name__=="__main__":
    app.run(debug=True)#,host="192.168.43.161")



