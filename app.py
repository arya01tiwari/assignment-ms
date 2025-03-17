from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flask Server is Running!</h1><p>Visit <a href='/htop'>/htop</a> to see system info.</p>"

@app.route('/htop')
def htop():
    import os
    import datetime
    import subprocess

    name = "Arya Tiwari"  
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")

    
    htop_output = subprocess.getoutput("top -b -n 1")

    response = f"""
    <pre>
    Name: {name}
    Username: {username}
    Server Time (IST): {server_time}

    TOP output:
    {htop_output}
    </pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)