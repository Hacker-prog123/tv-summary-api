from flask import Flask, request, jsonify, send_file
from tv_summary import run_tv_summary

app = Flask(__name__)

@app.route('/tvsummary', methods=['POST'])
def process_tv_summary():
    try:
        if 'main_file' not in request.files or 'rr_file' not in request.files:
            return jsonify({"status": "error", "message": "Missing required files: 'main_file' and 'rr_file'"}), 400

        main_file = request.files['main_file'].read()
        rr_file = request.files['rr_file'].read()

        output = run_tv_summary(main_file, rr_file)
        return send_file(output, download_name="TV_Performance_Summary_Output.xlsx", as_attachment=True)

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
