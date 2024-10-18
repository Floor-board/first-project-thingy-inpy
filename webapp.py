import random
from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

#@app.route("/p1")
#def render_page1():
 #   return render_template('page1.html')



seven_ten = [7,8,9,10]

@app.route("/response")
def render_response():
    distance = str(request.args['meters']) 
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if distance == '100m' or distance == '100 meters' or distance == '100':
        n = float(request.args['secounds'])
        min = n * 2 - 0.2
        max = n * 2 + 0.2
        rt = [min, max]
        RandomRt = random.choice(rt)
        print(RandomRt)
    elif distance == '200m' or distance == '200 meters' or distance == '200':
        n = float(request.args['secounds'])
        time = n * 2 + 4
        rt = time
    elif distance == '400m' or  distance == '400 meters' or distance == '400':
        n = float(request.args['secounds'])
        time = n * 2 + random.choice(seven_ten)
        rt = time
    elif distance == '800m' or '800 meters':
        n = float(request.args['secounds'])
        time = n * 2 + random.choice(seven_ten)
        rt = time
    elif distance == '1500' or distance == 'mile' or distance == '1500m' or distance == '1500 meters' or distance == 'one mile':
        n = float(request.args['secounds'])
        time = n * 
    return render_template('index.html', New_Time = rt)
if __name__=="__main__":
    app.run(debug=False)
