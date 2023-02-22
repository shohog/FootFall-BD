from pydoc import visiblename
import flask
from flask import Flask, render_template
import subprocess
import requests
import json
import os

""" from bs4 import BeautifulSoup as Soup

html = 
<html>
<head>
<title>Test Page</title>
</head>
<body>
<div>test</div>
</html>

soup = Soup(html)

title = soup.find('title')
meta = soup.new_tag('meta')
meta['content'] = "text/html; charset=UTF-8"
meta['http-equiv'] = "Content-Type"
title.insert_after(meta) """


url = "https://0300-103-169-159-101.in.ngrok.io/api/videos"
app = Flask(__name__)



@app.route('/')
def home():
   return render_template('index.html')
@app.route('/analyzing')

def run_script():
    s = requests.Session()
    response = s.get(url, stream=True)
    if response.status_code == 200:
        #self.formatted_print(response.json())
        
        jsonData = response.json()
        for i in jsonData:
            if jsonData.index(i) == -1:
                s = requests.Session()
                response = s.get(url, stream=True)
                jsonData = response.json()
            else:
                jsonData = response.json()
             
       




        
        for i in jsonData:    
        #if i["is_processed"]==1:
            result = subprocess.run(['/usr/bin/python3', 'track.py', '--source', i["url"], '--vid_id', i["_id"]], capture_output=True)
            vid_id = i["_id"]
            #print(vid_id)
            with open("./runs/track.txt") as fk:
                contents = fk.read()
                if os.path.getsize("./runs/track.txt") == 0:
                        details = {"totalCrowd": None, "totalCount" : None}
                else:
                    count = contents.split(',')
                    print("clear")
                #x = json.loads(contents)
                    totalCrowd = int(count[0])
                    totalCount = int(count[1])
                    details = {"totalCrowd": totalCrowd, "totalCount" : totalCount}
                #print(totalCrowd)
                #print(type(totalCrowd))
                
                
            #if list(x.keys())[0] == i["_id"]:
                #tp = x[vid_id]
            #else:
                #tp = 0
                

                #"totalCrowd" = i["totalCrowd"]
                vid_id = int(vid_id)
                print(vid_id)
                # print(totalCrowd, totalCount)
                # print(type(totalCrowd))
                # print(type(totalCount))
                # print(f"https://0300-103-169-159-101.in.ngrok.io/api/files/{vid_id}")

                
            
                

                        
                # with open("./runs/track" + '.txt', 'w') as f:
                    #json.dump(details, f)
            
            #print(tp)
                
            """ with open("./runs/track.txt") as fk:
                contents = fk.read()
                y = json.loads(contents)
                print(y) """


            """  z = {
                "totalCount": y[vid_id]
            } """
            #print(type(tp))
            
            
            s.patch(f"https://0300-103-169-159-101.in.ngrok.io/api/videos/{vid_id}", data= details)
            #s.get(r.url)
            f = open("./runs/track.txt", 'r+')
            f.truncate(0)

        # result = subprocess.run(
        #     ['/usr/bin/python3', 'track.py', '--source', 'JsonData['url']'],
        # capture_output=True)
        
         #else:
            #print("error")
        # result = subprocess.run(
        # ['/usr/bin/python3', 'track.py', '--source', 'url'],
        # capture_output=True)

        #   Get the output as a string
        # output = result.stdout.decode('utf-8')
        # file = open(r'track.py --source od3.mp4 --yolo-weights yolov5n.pt --img 640 --class 0', 'r').read()
        # return exec(file)
        return "Done"



if __name__ == "__main__":
    app.run(debug=True)