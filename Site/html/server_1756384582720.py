from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='html', static_url_path='')

# Route for the main page (index.html)
@app.route('/')
def serve_index():
    return send_from_directory('html', 'index.html')

# Route for the update page
@app.route('/update')
def serve_update():
    return send_from_directory('html', 'Update Certex VPN Clients.html')

# Route to serve static files from /html and its subdirectories
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('html', filename)

if __name__ == '__main__':
    # Ensure the /html directory exists
    if not os.path.exists('html'):
        raise FileNotFoundError("The 'html' directory does not exist. Please ensure it is in the same directory as server.py")
    app.run(host='0.0.0.0', port=5000, debug=True)