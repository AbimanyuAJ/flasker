from flask import Flask, render_template


#Creating a Flask instance
app=Flask(__name__)

#Create a route decorator
@app.route('/')

def index():
	first_name='ABI'
	favorite_pizza=["pepporoni","cheese","onion",41]
	return render_template("index.html",
		first_name=first_name,
		favorite_pizza=favorite_pizza)

#localhost:5000/user/Abi
@app.route('/user/<name>')

def user(name):
	return render_template("user.html",name=name)

#creating error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404


#Internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"),500



if __name__ == '__main__':
    app.run(debug=True)
