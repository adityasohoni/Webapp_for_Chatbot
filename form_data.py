import json,time
from flask import Flask, render_template, request, jsonify, Response
import requests
import base64,cv2
from map_embedding import embed


app=Flask(__name__)
output=[]


map = []

def defaultCoordinates():
    lat.append(13.010992210852605)
    lng.append(74.79431669717836)
    # coordinates of NITK Surathkal
    
    map.append(embed["NITKSurathkal"])

defaultCoordinates()

def getCoordinates(location):
    
    map = {
        
        "Amul" : [13.008990937415803,74.79676318694564],
        "Nescafe" : [13.007456649901386, 74.79686072103866],
        "Nandini" : [13.012629093163248, 74.79609699793872],
        "Mudrika" : [13.008615710447698, 74.79415678177236],
        "MainBuilding" : [13.010816520025335, 74.79430667015167],
        "OceanPearl" : [13.008555277616512, 74.79518139773533],
        "Yennar" : [13.008662050867967, 74.79410813883005],
        "HealthCareCentre" : [13.009520241237365, 74.79624759779159],
        "SportsComplex" : [13.009854915350024, 74.79811174202523],
        "SBIBank" : [13.008954404207831, 74.79411792717062],
        "CCC" : [13.009407250859917, 74.79579061551671],
        "CentralLibrary" : [13.010511730820618, 74.79436580937538],

        "ITDepartment" : [13.01096341447703, 74.7921926013909],
        "CSEDepartment" : [13.01277483761104, 74.79135221551678],
        "ECEDepartment" : [13.011635697504223, 74.79215169770643],
        "EEEDepartment" : [13.0109677794616, 74.79231137590178],
        "MECHDepartment" : [13.012189357491657, 74.79591750645949],
        "MNDepartment" : [13.011766176141933, 74.7939723577556],
        "METADepartment" : [13.010431655743487, 74.79498642708732],
        "CVDepartment" : [13.01224358420148, 74.79399369205241],
        "CHEMDepartment" : [13.011187633263118, 74.79623468581308]
        
    }

    lat.append(map[location][0])
    lng.append(map[location][1])
    map.append(embed[location])
    
    

    
@app.route('/')
def home_page():
    return render_template("IY_Home_page.html",result=output,embed_map = map[-1])
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
                output.extend([("message user",result)])

                for i in r.json():
                    if('custom' in i):
                        bot_message = i['custom']['text']
                        print(f"{i['custom']['text']}")
                        output.extend([("message bot",bot_message)])

                        getCoordinates(i['custom']['title'])

                    else:
                        
                        if('text' in i):
                            bot_message = i['text']
                            print(f"{i['text']}")
                            output.extend([("message bot",bot_message)])
                        if('image' in i):
                            image_link = i['image']
                            output.extend([("image",image_link)]) 

                   
            except:
                output.extend([("message user", result), ("message bot", "We are unable to process your request at the moment. Please try again...")])
        print(lat) 
        print(output)
        return render_template("IY_Home_page.html",result=output,embed_map = map[-1])

if __name__=="__main__":
    app.run(debug=True)#,host="192.168.43.161")



