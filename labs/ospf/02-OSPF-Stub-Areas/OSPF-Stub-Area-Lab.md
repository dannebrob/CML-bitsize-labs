[Introduction]
# OSPF Stub Areas
You will find all the labs in the Bitsize series on my Github, link to repo: [CML-bitsize-labs](https://github.com/dannebrob/CML-bitsize-labs/tree/main).

## Learning Objectives
- Implement OSPF Stub Areas in a network topology.
- Implement Virtual Links in OSPF to connect non-backbone areas to the backbone area.
- Configure non-OSPF areas for LANs and ensure connectivity with the rest of the network.
- Implement route summarization in OSPF to optimize routing tables.
- Verify OSPF Stub Area configurations.
- Document the OSPF Stub Area configuration in the Lab notebook text file.

## Lab Overview
I'm glad you are here, in this lab we will be configuring OSPF Stub Areas in a network topology. We will also be implementing Virtual Links to connect non-backbone areas to the backbone area, and configuring non-OSPF areas for LANs while ensuring connectivity with the rest of the network. Additionally, we will implement route summarization in OSPF to optimize routing tables and verify our configurations.

If you need to brush up on the concepts, I have some study notes that you are more than welcome to review, heres the [link](https://github.com/dannebrob/CCNP-study-notes), im sure it will help you in your journey towards mastering OSPF Stub Areas.

## Lab Instructions
1. **Setup**: Clone the lab repository and navigate to the `02-OSPF-Stub-Areas` folder. Review the provided startup configurations for the routers in the lab topology.
2. **Configuration**: Import the `02-OSPF_Stub_Areas_Lab.yaml` file into the CML environment. 
Follow the instructions in the Lab Tasks to configure OSPF Stub Areas on the appropriate routers. Use the CLI to apply the necessary commands and verify your configuration.
3. **Testing**: After configuring stub areas, test the network connectivity and routing tables to ensure that the stub areas are working as expected.

## Lab Tasks
0. **Review the Lab Environment**: Familiarize yourself with the lab environment and the routers involved.
1. **Configure OSPF Stub Areas**: Configure the appropriate routers to be part of the stub areas, ensuring that they are correctly connected to the backbone area (Area 0). One of the areas should be a normal area (not stub), one should be a totally stubby area, and one should be a normal stub area.

2. **Configure Virtual Links**: If necessary, configure virtual links to connect non-backbone areas to the backbone area.
3. **Configure HR and IT LANS**: Configure the HR and IT LANs to be non-ospf areas, and ensure that they can communicate with the rest of the network through the appropriate routers.
4. **Configure Route Summarization**: Implement route summarization on the appropriate routers to optimize the OSPF routing tables.
5. **Verify Configuration**: Use OSPF commands to verify that the stub areas are correctly configured and that the routers are advertising the correct routes.

6. **Test Connectivity**: Test the connectivity between different areas of the network to ensure that the OSPF Stub Areas are functioning correctly.

## Walkthrough
0. **Review the Lab Environment**: 
We have a total of 6 routers in this lab, R1, R2, R3, R4, R5 and R6. R1 and R2 will be connected to the backbone area (Area 0), while R3, R4 and R5 will be connected to Area 1. R5 and R6 will be connected to Area 2. The HR LAN is connected to R3, and wil be part of Area 10, and the IT LAN is connected to R6, will be part of Area 20.
Non of the routers are configured with OSPF, but they have at least ip addresses and subnet masks configured on their interfaces. The interfaces connecting the routers are using p2p links (/30).
The HR and IT LANs are not configured in any other way, they are just connected to the appropriate routers and are assigned ip addresses and subnet masks.

1. **Configure OSPF Stub Areas**
- backbone area (Area 0): R1 and R2
<br>
We first need to configure OSPF on R1 and R2, and assign them to Area 0. We will also configure R1 to be the DR for Area 0, and R2 to be the BDR for Area 0.
Open up the CLI for R1 and R2 and enter the following commands:
<br>
```
R1:
router ospf 1
network 10.10.10.0 0.0.0.3 area 0

R2:
router ospf 1
network 10.10.10.0 0.0.0.3 area 0
```

- Now we need to configure R3, R4 and R5 to be part of Area 1, We will configure Area 1 to be a normal area, and in a bit we will configure Area 2 to be a totally stubby area.
Open up the CLI for R2, R3, R4 and R5 and enter the following commands:
<br>
```
R2:
router ospf 1
network 10.20.20.0 0.0.0.3 area 1
network 10.20.20.4 0.0.0.3 area 1

R3:
router ospf 1
network 10.20.20.8 0.0.0.3 area 1

R4:
router ospf 1
network 10.20.20.12 0.0.0.3 area 1

R5:
router ospf 1
network 10.20.20.8 0.0.0.3 area 1
network 10.20.20.12 0.0.0.3 area 1

```
- Now we need to configure R5 and R6 to be part of Area 2, and we will configure Area 2 to be a totally stubby area.
Open up the CLI for R5 and R6 and enter the following commands:
```
R5:
router ospf 1
network 10.30.30.0 0.0.0.3 area 2
area 2 stub no-summary
R6:
router ospf 1
network 10.30.30.0 0.0.0.3 area 2
area 2 stub no-summary
```


2. **Configure Virtual Links**: If necessary, configure virtual links to connect non-backbone areas to the backbone area.


Since area 20 is a totally stubby area, it cannot be directly connected to the backbone area (Area 0). We will need to configure a virtual link between R5 and R2 to connect Area 20 to Area 0.
Open up the CLI for R5 and R2 and enter the following commands:
```
R5:
router ospf 1
area 2 virtual-link
R2:
router ospf 1
area 1 virtual-link
```
This will create a virtual link between R5 and R2, allowing Area 20 to be connected to Area 0 through Area 1. Its easy to think of it as a tunnel between R5 and R2, allowing OSPF to exchange routing information between the two areas.
Without this tunnel R5 would not be able to exchange routing information with R1 and R2, and the HR and IT LANs would not be able to communicate with the rest of the network.

3. **Configure HR and IT LANS**: Configure the HR and IT LANs to be part of area 10 and area 20, and ensure that they can communicate with the rest of the network through the appropriate routers. The HR LAN should be a stub area, and the IT LAN should be a totally stubby area.
4. **Configure Route Summarization**: Implement route summarization on the appropriate routers to optimize the OSPF routing tables.
5. **Verify Configuration**: Use OSPF commands to verify that the stub areas are correctly configured and that the routers are advertising the correct routes.

6. **Test Connectivity**: Test the connectivity between different areas of the network to ensure that the OSPF Stub Areas are functioning correctly.