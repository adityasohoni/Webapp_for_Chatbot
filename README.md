# Web App for the NITK Chatbot
 
First, use pip to install requirements.txt (in your virtual environment)
```
pip install -r requirements.txt
```

To run (run all commands on separate terminal shells): 
In your chatbot directory

```
rasa run actions & rasa run --model models/ --endpoints endpoints.yml --port 5002 --credentials credentials.yml
```

In your website directory run : 
```
python form_data.py
```

The demo video can be found [here](https://www.youtube.com/watch?v=JudV2MoD2LY)
