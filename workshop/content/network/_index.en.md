---
date: 2020-06-01
title: "Network - Amazon VPC"  
weight: 100
pre: "<b>1. </b>"
---
  
{{% notice note %}}
In this lab,**VPC Wizard**, create a Public Subnet and a Private Subnet in two Availability Zones (AZ-A, AZ-C), and configure a NAT gateway in one Public Subnet.  
You will then set up a route table to define the traffic flow. This completes the basic networking configuration to create a highly available and scalable Web Services environment in the future.  
{{% /notice %}}
  
{{% notice info %}}
The images inserted into the lab documents are created to help with the lab. Each element you create during the lab (such as VPC, NAT Gateway, and EIP)***Identifier (ID)***may appear differently for different user accounts.  
{{% /notice %}}
  
----
  
## Goal diagram  
The final configuration diagram we would like to build through this lab is as follows.  
![GID-Network-DG](/images/network/gid-network-01.svg)
  
----
  
## Lab Order  
This lab is in the following order:  
  
[1. Creating a VPC](./create_vpc)  
[2. Create additional subnets](./create_subnet)  
[3. Modifying Route Tables](./modify_route)
  
  
  
  
  
