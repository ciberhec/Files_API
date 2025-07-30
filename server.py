from flask import Flask, send_from_directory
app = Flask(
    __name__,
    static_folder='../',
    static_url_path='',
)
@app.route('/')
def home():
    return send_from_directory('../html', 'index.htm')
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('../', path)

if __name__ == '__main__':
    app.run(debug=True)
    