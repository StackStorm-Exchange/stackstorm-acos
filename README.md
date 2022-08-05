# ACOS Integration Pack
This pack integrates the ACOS-based appliance of A10 Networks which support aXAPI v2.1 or v3.0.

[![CircleCI](https://circleci.com/gh/StackStorm-Exchange/stackstorm-acos.svg?style=shield)](https://circleci.com/gh/StackStorm-Exchange/stackstorm-acos)

## Configuration
You will need to specify set(s) of credentials to connect. Here is an example of the configuration. You can specify multiple credentials in the configuration and distinguish it by the `appliance` parameter of each action.

```yaml
appliance:
  -
    target: 172.31.31.31 # IP address or hostname of appliance to connect
    userid: admin
    passwd: a10
    api_version: v3.0
```

Copy [acos.yaml.example](./acos.yaml.example) to `/opt/stackstorm/configs/acos.yaml` and edit as required.

After making changes to `acos.yaml`, you must tell StackStorm to load the new configuration, with
`sudo st2ctl reload --register-configs`

## Actions
| params                        | description                                                     |
|:------------------------------|:----------------------------------------------------------------|
| add_slb_server                | add a server to the SLB                                    |
| add_slb_server_port           | register a ServerPort to the SLB                                |
| add_slb_service_group_member  | add a server to the ServiceGroup as a member                    |
| add_slb_service_group         | add a ServiceGroup to the SLB                              |
| add_slb_virtual_server        | add a VirtualServer to SLB                                      |
| add_slb_virtual_server_port   | add a VirtualServerPort to the VirtualServer in SLB             |
| create_ip_nat_pool            | create configuration of IP address of NAT pool                  |
| del_slb_server                | remove a server which is registered in SLB                      |
| del_slb_server_port           | remove a ServerPort which is registered in SLB                  |
| del_slb_service_group_member  | remove a server to the ServiceGroup as a member                 |
| del_slb_service_group         | remove a ServiceGroup from SLB                                  |
| del_slb_virtual_server        | remove a VirutlServer from SLB                                  |
| del_slb_virtual_server_port   | remove a VirutlServerPort from the VirtualServer in SLB         |
| delete_ip_nat_pool            | delete configuration of IP address of NAT pool                  |
| get_ip_nat_pool               | get configuration of IP address of NAT pool                     |
| get_slb_server                | get a Server information which is registered in SLB             |
| get_slb_service_group_members | get members information which are belonged to the ServiceGroup  |
| get_slb_service_group         | get a ServiceGroup information which is registered in SLB       |
| get_slb_virtual_server        | get VirtualServer which is registered in the SLB                |
| list_ip_nat_pool              | list configurations of IP address of NAT pool                   |
| list_slb_servers              | lists servers which are registered in SLB                       |
| list_slb_service_groups       | lists ServiceGroup entries which are registered in SLB          |
| list_slb_virtual_servers      | list VirtualServers which are registered in the SLB             |
