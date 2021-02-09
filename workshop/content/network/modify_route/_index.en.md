---
date: 2020-06-30
title: "Modifying Route Tables"  
weight: 130
pre: "<b>1-3. </b>"
---
  
{{% notice note %}}
**Routing Table**to view all route tables created, and you can change the route table or associate a subnet with that route table. In this case, we will associate the appropriate route table for the two newly created subnets.  
{{% /notice %}}
  
----
  
## **Public Subnets**Modifying Route Tables  
  
1. Click**Route Tables** on the left side of the VPC menu. Click in the middle search bar and select **VPC** in the resource properties, then select the `VPC-LAB's***VPC ID***and set the filter.  
![gid-network-20](/images/network/gid-network-20.png)
  
2. After filtering, you will see two route tables. once**Explicit subnet**Let's start with the route table that has subnets attached to. When you click on the corresponding route table, the details will be displayed below. Verify that it belongs to `VPC-lab` again.  
![gid-network-21](/images/network/gid-network-21.png)
  
3. bottom**Routes**tab to view the settings of this route table.  
![gid-network-22](/images/network/gid-network-22.png)
- Destination***10.0.0.0/16 (inside VPC)***If**Local Gateway (local)**route traffic to the  
- Destination***Other***, traffic to all destinations (0.0.0.0/0)**Internet Gateway (igw-xxx)**Route to.  
-**Communicate directly with the Internet**is a possible routing configuration, so**Public Subnets**is the route table that should be applied to the  
  
4. To determine which subnets the corresponding route table conditions are associated with**Subnet Association**tab.  
![gid-network-23](/images/network/gid-network-23.png)
-**10.0.10.0/24**only `Public subnet A` which has the address space of is associated with that route table.  
- the newly created `Public subnet C` also depends on the rules of that route table**0.0.0.0/0**to the Internet gateway.  
-**Edit subnet relations**to connect `Public Subnet C` to that route table as well.  
  
5.***Edit subnet relations***If you look at the Subnet ID field in the middle of the window, you will see that `Public subnet C` is not selected. `Public subnet C`**Left check box**to set up the connection, then click**Save**button.  
![gid-network-24](/images/network/gid-network-24.png)
  
6. You can now see that the route table has `Public subnet A` (10.0.10.0/24) and `Public subnet C` (10.0.20.0/24) attached.  
![gid-network-25](/images/network/gid-network-25.png)
  
7. In order to avoid further crosstalk,**Name**field and name the route table `Public route`.  
![gid-network-26](/images/network/gid-network-26.png)
  
8. The route table `Public route` setup for the public subnet is complete.  
![gid-network-27](/images/network/gid-network-27.png)
  
----
  
## **Private Subnets**Modifying Route Tables  
  
1. Let's modify the route table for the private subnets.  
Of the two route tables currently visible,**Route table without name**, and then click**Routes**tab.  
![gid-network-28](/images/network/gid-network-28.png)
  
2. bottom**Routes**tab to view the settings of this route table.  
![gid-network-29](/images/network/gid-network-29.png)
- Destination***10.0.0.0/16 (inside VPC)***If**Local Gateway (local)**route traffic to the  
- Destination***Other***, traffic to all destinations (0.0.0.0/0)**NAT Gateway (nat-xxx)**Route to.  
-**NAT Gateway**because it is a subnet that uses**Private Subnets**is the route table that should be applied to the  
  
3. To associate a private subnet with a route table,**Subnet**Let's tap on the tab.  
![gid-network-30](/images/network/gid-network-30.png)
- If you check the subnet connection, no subnets are connected.  
- Unconnected `Private subnet A` (10.0.100.0/24), `Private subnet C` (10.0.200.0/24) subnets will be visible at the bottom.  
-**Edit subnet relations**to connect `Private Subnet A` and `Private Subnet C` to the corresponding route table.  
  
4.***Edit subnet relations***In the middle of the window, the subnet ID of `Private subnet A` (10.0.100.0/24), `Private subnet C` (10.0.200.0/24)**Left check box**to set up the connection, then click**Save**button.  
![gid-network-31](/images/network/gid-network-31.png)
  
5. Verify that the two private subnets are well connected to the corresponding route table, and then click**Name**field to name the route table `Private route`.  
![gid-network-32](/images/network/gid-network-32.png)
  
6. The route table `Private route` setup for the private subnet is complete.  
![gid-network-33](/images/network/gid-network-33.png)
  
{{% notice info %}}
Now, the basic network configuration is complete.  
{{% /notice %}}
  
----
  
## Architectures to date  
Conceptually, the resources that you have configured to date are displayed in the drawing as shown below.  
![gid-network-01](/images/network/gid-network-01.svg)
