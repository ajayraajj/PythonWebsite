from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, text
from database import engine

app = Flask(__name__)

categories = [{
    "category": "Fruits",
    "stocks": 250,
    "ratings": 5.5,
    "reviews": 250,
    "items": 20,
}, {
    "category": "Vegetables",
    "stocks": 200,
    "ratings": 4.8,
    "reviews": 180,
    "items": 30,
}, {
    "category": "Meats",
    "stocks": 150,
    "ratings": 4.2,
    "reviews": 120,
    "items": 15,
}, {
    "category": "Dry Fruits",
    "stocks": 180,
    "ratings": 4.9,
    "reviews": 200,
    "items": 25,
}, {
    "category": "Dairy Products",
    "stocks": 300,
    "ratings": 4.7,
    "reviews": 220,
    "items": 40,
}]


def loadProductsFromDb():
  with engine.connect() as conn:
    result = conn.execute(
        text("SELECT category, stocks, ratings, reviews, items FROM product"))
    products = []
    for row in result:
      product_dict = {
          "category":row[0],  
          "stocks":row[1], 
          "ratings": float(row[2]),
          "reviews":row[3], 
          "items": row[4] 
      }
      products.append(product_dict)
    return products


@app.route("/")
def hello():

  result = loadProductsFromDb()
  return render_template('home.html',
                         cat=result,
                         GroceryName="Village super market")


@app.route("/categories")
def CategoryList():
  return jsonify(categories)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
