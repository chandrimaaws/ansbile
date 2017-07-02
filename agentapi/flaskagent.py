from flask import Flask
from flask_httpauth import HTTPBasicAuth
import os
from flask import  render_template, url_for, json
from flask import jsonify , json
from flask import request


app = Flask(__name__)

@app.route("/create", methods=["POST"])
def do_something():

     data_jsondata = request.get_json()

     f = open('/etc/ansible/playbooks/home/group_vars/all','w')
     f.write('http_port: 8080\n')
     f.write('https_port: 8443\n')
     f.write('# AWS specific variables\n')
     f.write('ec2_access_key: \n')
     f.write('ec2_secret_key: \n')
     f.write('ec2_region: us-east-1\n')
     f.write('ec2_zone:\n')
     f.write('ec2_image: ami-643b1972\n')
     f.write('ec2_instance_type: ')
     f.write( data_jsondata['serviceSpecificConfigurations']['flavorName']+"\n")
     f.write('ec2_keypair: \n')
     f.write('ec2_security_group: launch-wizard-1\n')
     f.write('ec2_instance_count: 1\n')
     f.write('ec2_tag: demo\n')
     f.write('ec2_tag_name_prefix: dj\n')
     f.write('ec2_hosts: all\n')
     f.write('wait_for_port: 22\n')
     f.write('machine_name: demo\n')


     f.close()

     os.system("ansible-playbook /etc/ansible/playbooks/home/launch_aws.yml")
     os.system("ansible-playbook /etc/ansible/playbooks/home/start_deployment.yml --private-key='/home/ec2-user/sayan-aws.pem' ")


     site_root = os.path.realpath(os.path.dirname(__file__))
     json_url = os.path.join(site_root,'log/logansible.json')
     data = json.load(open(json_url))
     return jsonify(data)


if __name__ == '__main__':
   app.run('0.0.0.0',8089,debug = True)
