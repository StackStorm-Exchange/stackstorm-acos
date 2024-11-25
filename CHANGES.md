# Changelog

## v1.8.0
* Enabled to set health_check parameter at the add_slb_server action.

## v1.7.0
* Added an action (update_slb_virtul_server) to update SLB virtual-server.

## v1.6.0

* Added "member_state" parameter at the "acos.acos_slb_service_group_member" action
  for setting registered member state.

* Added an action "acos.update_slb_service_group_member" to change slb service-group
  member's configuration that have already been registered.

## v1.5.0

* Enabled to pass parameters how to connect ACOS appliance

## v1.4.0

* Added actions to get slb template lists.

## v1.3.0

* Add `specified_target` parameter to all actions.
* Fixed failed action of list slb on v2.1

## v1.2.0

* Added actions to operate IP address of NAT pool

## v1.1.0

* Update acos_client, which this pack depends on, version from v1.4.6 to v2.6.0
  or later to be able to compatible with ACOS version up to v5.2.1 (#20)

## v1.0.0

* Drop Python 2.7 support.

## v0.2.6

* Update acos-client dependency to 1.4.6 from 1.4.1
* Add explicit support for Python 2 and 3

## v0.2.5

* Bump to fix git tagging issue. No code changes

## v0.2.4

* Change runner type  from `run-python` to `python-script`

## v0.2.3

* Following acos-client v1.4.1 to operate SLB ServerPort through the AxAPI v3.0

## v0.2.2

* Added actions to add/delete VirtualServerPort on the VirtualServer in the SLB

## v0.2.1

* Added actions to operate ServerPort in the SLB

## v0.2.0

* Enabled to set multiple appliance informations to manage in the configuration file

## v0.1.0

* Added actions to operate SLB functions
