from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/info')

def info():
	return jsonify({
		'message': 'Hej Damilola! <3',
		'time': datetime.datetime.today().strftime("%I:%M%p on %d-%m-%Y"),
		'host': socket.gethostname(),
		'deployed_on': 'kubernetes',
		'environment': '${{values.app_env}}',
		'app_name': '${{values.app_name}}'
	})

@app.route('/api/v1/health')

def health():
	return jsonify({
		'status': 'Up'
	})

if __name__ == '__main__':
	app.run(host="0.0.0.0")
