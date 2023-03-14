from pydoc import visiblename
import flask
from flask import Flask, render_template
import subprocess
import requests
import json
import os
import csv


url = "https://8767-103-169-159-101.in.ngrok.io/api/videos/"
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('index.html')
@app.route('/processing', methods=['GET', 'PATCH'])

def run_script():
    #s = requests.Session()
    response = requests.get(url)
    if response.status_code == 200:
        #self.formatted_print(response.json())
        
        jsonData = response.json()
        """  for i in jsonData:
            if jsonData.index(i) == -1:
                #s = requests.Session()
                response = s.get(url, stream=True)
                jsonData = response.json()
            else:
                jsonData = response.json() """
             
       




  
    for i in jsonData:    
    #if i["is_processed"]==1:
        result = subprocess.run(['/usr/bin/python3', 'track.py', '--source', i["url"], '--vid_id', i["_id"]], capture_output=True)
        vid_id = i["_id"]


  
        with open("./runs/track.txt") as fk:
            contents = fk.read()
            if os.path.getsize("./runs/track.txt") == 0:
                    details = {"totalCrowd": None, "totalCount" : None}
            else:
                count = contents.split(',')
            #x = json.loads(contents)
                totalCrowd = int(count[0])
                totalCount = int(count[1])
                #Need to send dict, not string
                details = {"totalCrowd": totalCrowd, "totalCount" : totalCount}
                #details = json.dumps(details)
                # details = json.load(details)
                with open("./runs/farma.txt") as fy:
                    upadan = fy.read()
                    figure = upadan.split(',')
                    grahok = int(figure[0])
                    pothochari = int(figure[1])

                grahok += totalCrowd
                pothochari  += totalCount
                with open("./runs/farma.txt", 'w') as f:
                    f.write(str(grahok))
                    f.write(str(','))
                    f.write(str(pothochari))
            with open("./runs/trackk.csv", 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([i["createdAt"][0:8], totalCrowd, totalCount])


            #print(totalCrowd)
            #print(type(totalCrowd))
            
            
            
            print(f"{vid_id}")
            print(details)

            
        
            

                    
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
        
        
        
        requests.patch(f"https://8767-103-169-159-101.in.ngrok.io/api/videos/{vid_id}", data = details)
        
            
    
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
    app.run(debug=True) #port=8080