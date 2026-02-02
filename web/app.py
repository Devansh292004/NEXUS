from flask import Flask, render_template, request, jsonify
import os
import sys
import uuid

# Add parent directory to path to import nexus
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from nexus.orchestrator import NexusOrchestrator

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    # Create a unique session directory for this request
    session_id = str(uuid.uuid4())
    session_dir = os.path.join(app.config['UPLOAD_FOLDER'], session_id)
    os.makedirs(session_dir, exist_ok=True)

    specification = ""

    # Handle PDF or Text file upload
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            path = os.path.join(session_dir, file.filename)
            file.save(path)
            specification = path

    # Handle raw text if no file
    if not specification and 'spec' in request.form:
        specification = request.form['spec']

    if not specification:
        return jsonify({"error": "No specification provided"}), 400

    # Change current working directory or pass it to orchestrator
    # For simplicity, we'll tell the orchestrator where to work
    orchestrator = NexusOrchestrator()
    try:
        # Run the pipeline, passing the unique session directory
        result = orchestrator.run_pipeline(specification, base_path=session_dir)

        # Structure results for frontend
        return jsonify({
            "status": "success",
            "session_id": session_id,
            "certification": result.get("certification"),
            "code": result.get("code"),
            "documentation": result.get("documentation"),
            "build_info": result.get("build_info")
        })
    except Exception as e:
        print(f"Server Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
