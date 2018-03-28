# Tower Networking Overview
The networking tool is built with the main goal of allowing users to organize hosts and their relationships in a visual tool. Upon organizing hosts, the user can export these relationships as a YAML file and use that as input to a playbook.

## Usage Manual

### Inventory Creation
The first step in is to create an inventory to be loaded into the network UI. There are no specific credentials or variables necessary to indicate that an inventory can be used in the network UI. The canvas can be used to represent any kind of inventory.

### Network Node Creation
Once the user has created an inventory, the next step is to add hosts to the inventory. This can be done manually or via an inventory source. Regardless of the import method, the host should be configured with a certain set of host varialbes that the network UI will reference when creating visual representations of the nodes. When creating a node that will be used in the network UI, the host variables follow this format:
#### YAML:
```
ansible_topology:
  type: host
```
#### JSON:
```
{
 "ansible_topology": {
  "type": "host",
 }
}
```

This structure denotes that the `type` that the network UI will use when drawing the visual representation of this node in the UI. The options for `ansible_topology` are as follows:

| Key Name               | Value Type                                                  | Description                                                                                                                                                                   |
|------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`                 | `str`                                                       | This will dictate what type of device the network UI will draw. Options are `host`, `switch`, and `router`. If left blank, the UI will denote the node type as `unknown`.     |
| `links`                | `array`                                                     | This array contains objects that will denote what other nodes this particular node is connected to. Each connecting node object requires a `remote_device_name`, a `name`, and a `remote_interface_name`.

Ex: suppose an inventory had three nodes, titled `host-00`, `switch-00`, and `router-00`. To connect `host-00` to the other two hosts, these would be the host variables saved to the host:
```
{
 "ansible_topology": {
  "type": "host",
  "links": [
   {
    "remote_device_name": "router-00",
    "name": "eth0",
    "remote_interface_name": "eth0"
   },
   {
    "remote_device_name": "switch-00",
    "name": "eth1",
    "remote_interface_name": "eth1"
   }
  ]
 }
}

```
Connecting the other two devices to each other, and you would get the following representation in the network UI:
![Example 1](./img/network-example-1.png?raw=true)


### Graphical UI and Restrictions
Once the user has setup their inventory and nodes, they are ready to begin organizing their nodes using the graphical interface. The interface consists of an SVG canvas overlayed with panels that allow the user to drag nodes onto the canvas, as well as the ability to drill-down into the details of the items on the canvas. Below is a breakdown of the panels and their purpose on the interface:
![Example 2](./img/network-example-2.png?raw=true)
1. Toolbox: This panel on the left hand side of the screen will contain all the hosts that are included in the inventory. These are returned from `'/api/v2/inventories/:inventory_id/hosts/'` and therefore are returned in a paginated list. Because of this, the UI will make recursive calls to retrieve the list of hosts. This panel is collapsible using the wrench icon in the toolbar. This panel will scroll vertically with the list of devices.
2. Canvas: The canvas takes up the full screen width and height. The canvas is where the user can drag and drop devices from the toolbox. Once a device is placed on the canvas, it is removed from the toolbox and it can interact with other devices on the canvas. If a device is removed from the canvas, it is not removed from the inventory, it is simply removed from the canvas, and will return to the toolbox
3. Context Menu: When a user clicks on a device for the first time, it selects the device. A second click will activate a context menu with actions for the user. If the user has edit permission on the inventory, they will have the options to view the details of the device, or to remove the device. If the user does not have edit permission, they will only have the option to view the details of the device.
4. Details: The right hand panel displays a read-only form for the device that is currently being inspected by the user. This panel is not shown by default, and is only shown after the user clicks the "Details" button on the context menu for a device. If mutiple devices are displayed on the canvas, the user can select different devices. As the user selects devices, the device detail panel on the right hand side will update with the host data.
5.  Search: The search dropdown is a type-ahead dropdown that has a list of the devices currently on the canvas. It is organized by device type. It should always be in sync with the list of devices on the canvas. Devices on the toolbox will not show up in the search dropdown. Selecting a device from this dropdown will focus the canvas on the device.
6. Toolbar actions: These are actions that are specific to the usability of the network UI. Currently they include the toggle for the toolbox, as well as a cheat sheet of hotkeys that can be used for shortcuts on the network UI.
7. Actions dropdown: These are actions for the content of the network UI. These include "Export YAML" and "Export SVG" which is how a user could export the relationships on the canvas to download for their own use.
8. Zoom Widget: The zoom widget ranges from 0-200%, and controls the zoom of the canvas. The user can also control the zoom using the scroll on their mouse or tracking pad. In future versions of this UI, the zoom will control what level detail they are able to see. But currently the only mode available is for devices in an inventory.
