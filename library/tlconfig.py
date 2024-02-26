#!/usr/bin/python
#
# Ansible interface to tl-config
#
# Copyright 2016- Karl Mikaelsson <derfian@cendio.se> for Cendio AB

import subprocess
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
---
module: tlconfig
short_description: Ansible interface to tl-config
author: "Karl Mikaelsson, @derfian"
requirements:
    - ThinLinc Server

'''

EXAMPLES = '''
- tlconfig: param=/vsmserver/HA/enabled value=1
'''

RETURN = '''
changed:
    type: bool
param:
    type: str
'''

TLCONFIG = "/opt/thinlinc/bin/tl-config"

def getvalue(param):
    tlproc = subprocess.Popen([TLCONFIG, "%s" % param], stdout=subprocess.PIPE,universal_newlines=True)
    stdout, _ = tlproc.communicate()
    return stdout.rstrip()

def setvalue(param, value):
    tlproc = subprocess.Popen([TLCONFIG, "%s=%s" % (param, value)])
    return tlproc.wait()

def main():
    changed = False

    module = AnsibleModule(argument_spec=dict(param=dict(required=True, type='str'),
                                              value=dict(required=True)),
                           supports_check_mode=True)

    if module.check_mode:
        module.exit_json(changed=module.params['value'] != getvalue(module.params['param']))

    if len(module.params['param']) == 0:
        module.fail_json(msg="Param can't be empty")

    if len(module.params['value']) == 0:
        module.fail_json(msg="Value can't be empty")

    if getvalue(module.params['param']) != module.params['value']:
        ret = setvalue(module.params['param'], module.params['value'])

        if ret is not 0:
            msg = "Failed setting %s: tl-config returned %d" % (module.params['param'], ret)
            module.fail_json(msg=msg)
        changed = True

    module.exit_json(changed=changed,
                     param=module.params['param'],
                     value=module.params['value'])

if __name__ == '__main__':
    main()
