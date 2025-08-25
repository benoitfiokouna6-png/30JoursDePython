from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/v1.0/etudiants', methods=['GET'])
def etudiants():
	student_list = [
		{
			'name': 'asabeneh',
			'country': 'Finland',
			'city': 'Helsinki',
			'skills': ['HTML', 'CSS', 'JavaScript']
		},
		{
			'name': 'David',
			'country': 'UK',
			'city': 'London',
			'skills': ['Python', 'MongoDB']
		},
		{
			'name': 'John',
			'country': 'Sweden',
			'city': 'Stockholm',
			'skills': ['Java', 'C#']
		}
	]
	return jsonify(student_list)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, host='0.0.0.0', port=port)
 