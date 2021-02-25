import json,time
from flask import Flask, render_template, request, jsonify, Response
import requests
import base64,cv2


app=Flask(__name__)
output=[]#("message stark","hi")]

lat = []
lng = []


def defaultCoordinates():
    # coordinates of NITK Surathkal
    lat.append(13.001864136351472)
    lng.append(74.80495038765815)
defaultCoordinates()
def getCoordinates(location):
    
    map = {
        
        "Mudrika" : [13.008641224563956,74.79418828368352],
        "MainBuilding" : [13.06961353476527,74.78629159322206],
        "OceanPearl" : [13.02267735427792,74.79054242887052],
        "Yennar" : [13.018314457068078,74.81208948121525],
        "HealthCareCentre" : [13.125330866265447,74.8011031535809],
        "SportsComplex" : [12.975494928028214,74.82307580884962],
        "SBIBank" : [13.077179226201334,74.76814417067781],
        "CCC" : [13.066477583824591,74.78462366212935],
        "CentralLibrary" : [13.082529873304695,74.79011682594653],
        
    }

    lat.append(map[location][0])
    lng.append(map[location][1])
    
    
@app.route('/')
def home_page():
    return render_template("IY_Home_page.html",result=output,latitude = lat[-1], longitude = lng[-1])
@app.route('/about')
def about_page():
    return render_template("about.html",result=output)
@app.route('/contact')
def contact_page():
    return render_template("contact.html",result=output)
@app.route('/charts')
def charts_page():
    return render_template("charts.html",result=output)


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

                for i in r.json():
                    if('custom' in i):
                        bot_message = i['custom']['text']
                        print(f"{i['custom']['text']}")
                        output.extend([("message stark",bot_message)])

                        getCoordinates(i['custom']['title'])

                    else:
                        
                        if('text' in i):
                            bot_message = i['text']
                            print(f"{i['text']}")
                            output.extend([("message stark",bot_message)])
                        if('image' in i):
                            image_link = i['image']
                            output.extend([("image",image_link)]) 

                   
            except:
                output.extend([("message parker", result), ("message stark", "We are unable to process your request at the moment. Please try again...")])
        print(lat) 
        print(output)
        return render_template("IY_Home_page.html",result=output,latitude=lat[-1],longitude = lng[-1])

if __name__=="__main__":
    app.run(debug=True)#,host="192.168.43.161")



