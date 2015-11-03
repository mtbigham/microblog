from app import app

@app.route('/')
@app.route('/index')
def indes():
	return "Hello, world!"