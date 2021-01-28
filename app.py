from flask import Flask, render_template, request

app = Flask(__name__)

reviews = []

@app.route('/')
def index():
	title = "Urja Mehta"
	return render_template("index.html", title=title)

@app.route('/subscribe')
def subscribe():
    title = "Subscribe"
    return render_template("subscribe.html", title=title)

@app.route('/form', methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    product_name = request.form.get("product_name")
    review = request.form.get("review")
    reviews.append(f"{first_name} | {product_name} | {review}")
    title = "Thank You"
    return render_template("form.html", title=title, reviews=reviews)


if __name__ == "__main__":
	# db.create_all()
	app.run(debug=True) 