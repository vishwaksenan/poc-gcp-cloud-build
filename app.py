from flask import Flask
app = Flask(__name__)

@app.route('/feature3/')
def feature3():
	return "Hello World! From Playpen Demo Testing Feature 3\n"

@app.route('/feature2/')
def feature2():
	return "Hello World! From Playpen Demo Testing Feature 2 Cert\n"

@app.route('/')
def hello():
	return "Test from Demo Demo change 3\n"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)