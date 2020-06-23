# python3
# flask

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-port',  '--port', nargs="?", help='Server port')

argv = parser.parse_args()

if argv.port is not None:

    from flask import Flask, render_template, request
    import process
    app = Flask(__name__)
        
    @app.route("/")
    def index():

        proc = process.Process()
        proc.start()
        q = proc.queue
        data = []
        for i in range(q.qsize()):
            data.append(q.get())

        return render_template("home.html", data = data)

    if __name__ == "__main__":
        app.run(debug=False, host='localhost', port=argv.port)
else:
    parser.print_help()
