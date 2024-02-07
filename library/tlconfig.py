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
    tlproc = subprocess.run([TLCONFIG, "%s" % param], stdout=subprocess.PIPE, universal_newlines=True)
    return tlproc.stdout.strip("\n")


def setvalue(param, value, check_mode):
    if not check_mode:
        tlproc = subprocess.run([TLCONFIG, "%s=%s" % (param, value)])
        return tlproc.returncode
    else:
        return 0

def main():
    module = AnsibleModule(argument_spec=dict(param=dict(required=True, type='str'),
                                              value=dict(required=True)),
                           supports_check_mode=True)

    result = {
        "changed": False,
        "param": module.params['param'],
        "value": module.params['value']
    }

    if len(module.params['param']) == 0:
        module.fail_json(msg="Param can't be empty")

    if len(module.params['value']) == 0:
        module.fail_json(msg="Value can't be empty")

    current = getvalue(module.params['param'])
    new = module.params['value']

    if current != new:
        ret = setvalue(module.params['param'], module.params['value'], module.check_mode)

        if ret != 0:
            msg = "Failed setting %s: tl-config returned %d" % (module.params['param'], ret)
            module.fail_json(msg=msg)
        result['changed'] = True

        if module._diff:
            result['diff'] = {
                "before": current,
                "after": new
            }

    module.exit_json(**result)

if __name__ == '__main__':
    main()
