from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Set up Flask
app = Flask(__name__)

# Connect to Mongo using PyMongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
    # app.config["MONGO_URI"] : tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL.
    # "mongodb://localhost:27017/mars_app" : is the URI we'll be using to connect our app to Mongo. 
mongo = PyMongo(app)


# Set up App Route 
@app.route("/")
def index():
    mars = mongo.db.mars.find_one() 
    # uses PyMongo to find the "mars" collection in our database, which we will create when we convert our Jupyter scraping code to Python Script.
    return render_template("index.html", mars=mars)
    # tells Flask to return an HTML template using an index.html file.
    
    
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)
    
    
if __name__ == "__main__":
    app.run()