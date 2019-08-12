ThinLinc Server
===============

This role takes care of installing, configuring and starting the
ThinLinc server software. The ThinLinc server software is not included
in this role, and will have to be obtained separately.


License
-------

GPLv3. (See LICENSE)


Contributions
-------------

Pull requests and issues are welcome.


Requirements
------------

 - [ThinLinc Server requirements](https://www.cendio.com/resources/docs/tag/requirements_server.html) - but see `thinlinc-autoinstall-dependencies` below.


Role Variables
--------------

```yaml
thinlinc_accept_eula: "no"
```

By changing this to "yes", you agree to the terms specified in the
ThinLinc End User License Agreement. NOTE: Setting this to yes is a
requirement for installing and using ThinLinc.

```yaml
thinlinc_version: "4.10.0"
thinlinc_build: "6068"
thinlinc_server_bundle_file: "tl-4.10.0-server.zip"
```

ThinLinc version, build number and server bundle names.

```yaml
thinlinc_autoinstall_dependencies: "yes"
```

When set to "yes", this will automatically install any required
dependencies along with the ThinLinc software. If set to "no", the
role assumes that you will take care of it.

```yaml
thinlinc_email: "root@localhost"
```

Administrative email address to receive license warnings.

```yaml
thinlinc_printers: "yes"
```

Whether to install the optional CUPS printer queues for ThinLinc.

```yaml
thinlinc_webadm_password: "$6$7cc31a35e02e55ec$hm.1MsloeBJqNKljx9RH88Z/eRKZCka5ZlabkZGj0nYXh0IaxaiYucsDD.fGJ5sNPthWf63pXkCn9Nu0ua2Ye1"
```

ThinLinc Web Administration password. This default password is
"thinlinc". Generate new hashes with `/opt/thinlinc/sbin/tl-gen-auth`.

```yaml
thinlinc_agent_hostname: null
```

This allows you to modify the hostname reported by the agent server to
the client on connecting. See [ThinLinc in a NAT/Split-DNS
Environment](https://www.cendio.com/resources/docs/tag/network.html#network_nat)
for details. 

Setting `thinlinc_agent_hostname` to null sets this parameter to `ansible_fqdn`.


Examples
--------

This role can be installed through ansible-galaxy with a
`requirements.yml` file. Run `ansible-galaxy install -r
requirements.yml` to install the role:

```yml
---
- src: https:///github.com/cendio/ansible-role-thinlinc-server.git
  scm: git
  name: thinlinc-server
  version: v1.1
```

The role uses three groups - thinlinc-masters, thinlinc-agents and
thinlinc-servers. Here's an example inventory file with one master
server and three agent servers:

```yaml
[thinlinc_masters]
tl-master-01.example.com

[thinlinc_agents]
tl-agent-01.example.com
tl-agent-02.example.com
tl-agent-03.example.com

[thinlinc_servers:children]
thinlinc_masters
thinlinc_agents
```

Now that we got both a role and an inventory, connect the dots by
applying the thinlinc-server role to the thinlinc-servers group with a
`thinlinc.yml` playbook:

```yaml
- hosts: thinlinc-servers
  roles:
    - { role: thinlinc-server, thinlinc_accept_eula: "yes" }
```

The final step is to apply the playbook to the inventory, like this:

`ansible-playbook -i inventory thinlinc.yml`
