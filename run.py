from waitress import serve
from Myproject.wsgi import application   # <-- replace 'myproject' with your inner folder name if different

if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=8000)
