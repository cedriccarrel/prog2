from flas improt Flask
app = Flask("Hello World")
@app.route('/hello')
def hello_world():
	return 'Hello, World'

if _name_ == "_main_":
	app.run(debug=True, port=5000)