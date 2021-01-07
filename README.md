# FaceRecognitionFlask
 
First, use pip to install requirements.txt (in your virtual environment)
```
pip install -r requirements.txt
```

To run : 
In your chatbot directory
```
rasa run --model models/ --endpoints endpoints.yml --port 5002 --credentials credentials.yml
```
and
```
rasa run actions
```

In your website directory run : 
```
python form_data.py
```

