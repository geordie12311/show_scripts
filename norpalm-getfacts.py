#python script utilising nornir_napalm plugin "napalm_get"
#script will get facts from all devices in nornir host file
#and output the details to the screen. Note: this will work on
#all supported devices (such as Cisco,Juniper, Arista etc.)

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
#importing napalm_get from nornir_napalm
nr = InitNornir(config_file="config.yaml")

def pull_info(task):
    facts = task.run(task=napalm_get, getters=["get_facts"])
    task.host["facts"] = facts.result
#function is using the getters syntax to get_facts from the hosts
results = nr.run(task=pull_info)
print_result(results)
<<<<<<< HEAD:nornir-napalm-scripts/norpalm-getfacts.py

import ipdb
ipdb.set_trace()
=======
>>>>>>> 8e5eb719ec2f21c81f09090b97fae5e6b4f842e0:norpalm-getfacts.py
