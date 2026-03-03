# 01- Summarization

## Learning Objectives
- Understand the concept of OSPF summarization and its benefits in reducing routing table size and improving network efficiency.
- Learn how to configure OSPF summarization on a router and verify its functionality.
- Analyze the impact of summarization on OSPF routing and network performance.
- Gain hands-on experience with OSPF summarization in a lab environment.
- Develop troubleshooting skills related to OSPF summarization and its effects on network connectivity.


## Lab Overview
(image of the lab topology)[LinkToLabTopology.image]

## Lab Instructions
1. **Setup**: Clone the lab repository and navigate to the `01-summarization` folder. Review the provided startup configurations for the routers in the lab topology.
2. **Configuration**: Import the cml_import.yml file into the CML environment. Follow the instructions in the Lab Tasks to configure OSPF summarization on the appropriate routers. Use the CLI to apply the necessary commands and verify your configuration.
3. **Testing**: After configuring summarization, test the network connectivity and routing tables to ensure that the summarization is working as expected.

## Lab Tasks
1. **Identify the Networks**: Review the network topology and identify the networks that need to be summarized.

R1 is part of area 10 of the OSPF network and is connected to R2 via a transit link. R1 has 3 loopback interfaces (lo1-3) that are part of the ospf area 10 and are advertised into the ospf network. The other loopback interfaces (lo4-6) are part of a external network and are not advertised into the OSPF network.

R1 has the following networks and configurations:
```
Interfaces:
Ethernet0/0: 10.10.0.2/30 #Transit to R2
lo1: 10.10.1.1/30 #Loopback1
lo2: 10.10.2.1/30 #Loopback2
lo3: 10.10.3.1/30 #Loopback3
lo4: 10.11.1.1/30 #Loopback4
lo5: 10.11.2.1/30 #Loopback5
lo6: 10.11.3.1/30 #Loopback6

Ospf:
router-id: 1.1.1.1
Area 10 - lo1, lo2, lo3
External - lo4, lo5, lo6
```

R2:
```
Ethernet0/0: 10.10.0.1/30 #Transit to R1
Ethernet0/1: 10.0.0.1/30 #Transit to R3

ospf:
router-id: 2.2.2.2
area 10 - ethernet0/0
area 0 - ethernet0/1
```

R3:
```
Ethernet0/0: 10.0.0.2/30 #Transit to R2
Ethernet0/1: 10.20.0.2/30 #Transit to R4

ospf:
router-id: 3.3.3.3
area 0 - ethernet0/0
area 20 - ethernet0/1
```

R4:
```
Ethernet0/0: 10.20.0.1/30 #Transit to R3

ospf: 
router-id: 4.4.4.4
area 20 - ethernet0/0
```

2. **Configure Summarization**: On R1, configure OSPF summarization for the loopback interfaces. Use the appropriate OSPF commands to create a summary route that encompasses all the loopback interfaces.

3. **Verify Configuration**: After configuring summarization, verify that the summary route is being advertised correctly. Use OSPF show commands to check the routing tables on R2 and R3 to ensure that they are receiving the summarized route.

find these facts:
<details> 
  <summary>Q1: What is the summary route that R1 is advertising for the loopback interfaces? </summary>
   A1: 10.10.0.0/22 
</details>
<details> 
  <summary>Q2: What is the subnet mask of the summary route? </summary>
   A1: 255.255.252.0
</details>
<details> 
  <summary>Q3: Are the individual loopback interfaces still being advertised, or are they being replaced by the summary route? </summary>
   A1: The individual loopback interfaces are replaced by the summary route.
</details>

- What is the summary route that R1 is advertising for the loopback interfaces?
- 
- 

4. **Test Connectivity**: Test the connectivity from R2 and R3 to the loopback interfaces on R1. Use ping and traceroute commands to verify that the summarized route is functioning correctly and that the individual loopback interfaces are reachable.


## Resources
- [Cisco OSPF Documentation](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13684-12.html)
- [Cisco OSPF Configuration Guide](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13684-12.html)
- [Cisco OSPF Summarization Documentation](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13684-12.html)



<details> 
  <summary>Q1: What is the best Language in the World? </summary>
   A1: JavaScript 
</details>