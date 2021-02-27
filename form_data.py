import json,time
from flask import Flask, render_template, request, jsonify, Response
import requests
import base64,cv2
from map_embedding import embed


app=Flask(__name__)
output=[]


map = []

def defaultCoordinates():
    
    
    map.append(embed["NITKSurathkal"])

defaultCoordinates()

def getCoordinates(location):
    
    
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
        
        return render_template("IY_Home_page.html",result=output,embed_map = map[-1])

if __name__=="__main__":
    app.run(debug=True)#,host="192.168.43.161")



