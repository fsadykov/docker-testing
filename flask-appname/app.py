from flask import Flask, jsonify
import argparse

## Testing application for kubernetes or docker hosting
## Very useful when you testing loadbalancer

parser = argparse.ArgumentParser(description="Small application to print name of the applcation.")
optional = parser._action_groups.pop()
required = parser.add_argument_group('required arguments')


required.add_argument('-n', '--name', help='Name of the applcation.', required=True)
args = parser.parse_args()

app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello_world():
    data = {'name': args.name, 'message': 'The applcation is up.'}
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
