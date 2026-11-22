from flask import Flask, jsonify

def create_app():
	appl = Flask(__name__)
	@appl.get("/health")
	def health():
		return jsonify(
			service="devops-ci-app", 
			version="1.0.0", 
			status="running"
		)

	@appl.get("/")
	def index():
		return jsonify(
			service="devops-ci-app",
			version="1.0.0",
			status="running"
		)
	return appl

app = create_app()
