from flask import Flask, jsonify
from kubernetes import config
import argparse
import os



## Testing application for kubernetes or docker hosting
## Very useful when you testing loadbalancer

parser = argparse.ArgumentParser(description="Small application to print name of the applcation.")
optional = parser._action_groups.pop()
required = parser.add_argument_group('required arguments')

required.add_argument('-n', '--name', help='Name of the applcation.', required=True)
required.add_argument('-ns', '--namespace', help='Name of the applcation.', required=True)
args = parser.parse_args()

def generateVariables():
    data = {
    'name': args.name,
    'message': 'The applcation is up.',
    'userinfo' : []}
    deployment = deployPod(args.name)
    if deployment:
        data['deployMessage'] = 'Deployment was success!!'
    else:
        data['deployMessage'] = 'Deployment was not success!!'
    if 'TEST' in os.environ:
        data['testing'] = True

    if 'PASSWORD' in os.environ and 'USERNAME' in os.environ:
        item = { "password" : os.environ.get('PASSWORD'), 'username' : os.environ.get('USERNAME') }
        data['userinfo'].append(item)

    if 'MESSAGE' in os.environ:
        data['messageFromEnv'] = os.environ.get('MESSAGE')

    return data




def deployPod(name):
    deployPodTemplate = {'apiVersion': 'v1',
    'kind': 'Pod', 'metadata': {'name': f'{name}-deploy',
    'labels': {'app': f'{name}-deploy'}},
    'spec': {'containers': [
    {'name': f'{name}-deploy',
    'image': 'fsadykov/docker-testing',
    'args': ['--name', 'kube-testing']}]}}
    try:
        config.load_incluster_config()
        v1.create_namespaced_pod(args.namespace, body=deployPodTemplate)
        return True
    except:
        return False

app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello_world():
    data = generateVariables()
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
