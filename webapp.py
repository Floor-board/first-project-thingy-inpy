from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
    
if __name__=="__main__":
    app.run(debug=False)
    
@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    distance = request.args['meters'] 
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if distance == '100m' or distance == '100 meters':
        n = int(request.args['secounds'])
        min = n * 2 - 0.2
        max = n * 2 + 0.2
    elif distance == '200m' or '200 meters':
        n = int(request.args['secounds'])
        time = n * 2 * 1.07
if __name__=="__main__":
    app.run(debug=False)
