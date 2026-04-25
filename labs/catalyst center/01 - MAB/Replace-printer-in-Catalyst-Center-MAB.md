This is a lab-simulation taken from a real world situation, where I needed to replace a printer to the network. But I did not get the chance to do it in the production network, so I created this lab to test it out in the Devnet Sandbox environment. 
# Replace printer in Catalyst Center with MAB
The printer Printer1 was to be decommissioned and replaced with a new printer, Printer2. The task was to ensure that the new printer would be authenticated via MAB and placed in the correct VLAN (VLAN 30 for printers) in the network, and that this information would be visible in Catalyst Center. The lab was designed to simulate the process of replacing a printer in a network that uses Cisco Identity Services Engine (ISE) for authentication and Cisco Catalyst Center for network management and visibility. Due to the nature of this lab, no pre-configurations is required, all the configurations will be done in the lab itself and some information will be provided in the lab and hardcoded in the walkthrough. 

### Want more labs?
You will find all the labs in the Bitsize series on my Github, link to repo: [CML-bitsize-labs](https://github.com/dannebrob/CML-bitsize-labs/tree/main).

## Learning Objectives
- Identify client devices at the switch level
- Understand MAC address tables and authentication sessions
- Manage endpoints in Cisco ISE
- Create and apply ISE authorization policies
- Assign VLANs via MAB
- Integrate Catalyst Center with ISE
- Troubleshoot the end-to-end NAC flow

## Lab Overview

## Lab Instructions
1. **Setup**: Sign in to the Devnet Sandbox startpage and reserve/launch the "Identity Services Engine 3.4" and the "Catalyst Center Sandbox" sandbox. Once the sandboxes is up and running and accessible, access the Catalyst Center GUI and the ISE GUI using the provided credentials. Review the lab topology and familiarize yourself with the network setup, including the location of the printers and switches involved in the lab.

2. **Configuration**:
Follow the instructions in the Lab Tasks to configure ISE and Catalyst Center. Use the CLI to apply the necessary commands and verify your configuration.
3. **Testing**: After configuring MAB and the necessary policies, test the network connectivity and authentication flow to ensure that the new printer is authenticated correctly and placed in the correct VLAN. Verify that the information is visible in Catalyst Center as expected.

## Lab Tasks
1. **Identify the Networks**: Review the network topology and identify the areas that need to be configured [....]

2. **Configure ISE**: 
printer1: mac address: 1111.1111.1111
printer2: mac address: 2222.2222.2222


3. **Configure Catalyst Center**:

4. **Verify Configuration**: 

5. **Test Connectivity**: 

## Walkthrough
This is a walkthrough of the lab, where you can find the commands and steps to complete the lab tasks. It is recommended to attempt the lab on your own before referring to the walkthrough.

 **Identify the Networks**: Review the network topology and identify the areas that need to be configured [....]

**Configure ISE**:

**Configure Catalyst Center**:

**Verify Configuration**: 

**Test Connectivity**: 

## Resources
- [Cisco OSPF Documentation](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13684-12.html)
- [Cisco OSPF Configuration Guide](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13684-12.html)
- [Cisco OSPF Summarization Documentation](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/13684-12.html)


🔧 Labb: Identifiera skrivare → Verifiera i ISE → MAB i Catalyst Center
01
Identifiera vilken port skrivaren sitter på i building-a_sw1

Du börjar i switchen för att bekräfta att skrivaren är fysiskt ansluten och aktiv.

På switchen: show cdp neighbors eller show lldp neighbors

    Leta efter porten där skrivaren eller dess anslutna patchport visas

    Om skrivaren inte annonserar LLDP/CDP: kör show interfaces status och leta efter en port i connected state

    Notera portnumret, t.ex. Gi1/0/12

02
Hämta MAC-adressen från switchporten

MAC-adressen behövs för att verifiera endpointen i ISE.

På switchen: show mac address-table interface Gi1/0/12

    Notera MAC-adressen i format aaaa.bbbb.cccc

    Bekräfta att endast en MAC syns (skrivare)

    Om flera MAC syns: kontrollera om det sitter en mini-switch eller AP i porten

03
Verifiera MAB-sessionen på switchen

Här ser du om MAB har startat och om VLAN ännu inte är tilldelat.

På switchen: show authentication sessions interface Gi1/0/12 details

    Kontrollera Current Status: Authz Success eller In Progress

    Se Method: MAB

    Notera Server Policies → VLAN (bör vara 30 efter full auth)

    Om VLAN ännu inte är 30: porten är i initialt VLAN

04
Kontrollera endpointen i Cisco ISE

Nu verifierar du att MAC-adressen finns i rätt endpoint-grupp och får rätt policy.

ISE GUI: Administration → Identity Management → Identities → Endpoints

    Sök på MAC-adressen

    Kontrollera att den ligger i gruppen Printers

    Gå till Context Visibility → Endpoints för att se live-session

    Bekräfta att Authorization Rule matchar Printer VLAN 30

05
Verifiera att rätt VLAN skickas från ISE

ISE måste skicka VLAN 30 i Authorization Profile.

ISE GUI: Policy → Policy Sets → [ditt policy set] → Authorization Policy

    Öppna regeln för skrivare

    Bekräfta att Authorization Profile innehåller:

        VLAN = 30

        (valfritt) dACL för skrivare

    Kontrollera Live Logs att rätt regel matchade

06
Kontrollera att Catalyst Center synkar endpointen från ISE

Catalyst Center använder ISE som identitetskälla och måste se skrivaren.

Catalyst Center: System → Settings → External Services → Identity Services Engine

    Bekräfta att pxGrid och ERS är Connected

    Kontrollera att Endpoint Synchronization är aktiverat

    Gå till Clients och sök på MAC-adressen

    Du ska se skrivaren som MAB authenticated

07
Verifiera MAB-hantering i Catalyst Center

Catalyst Center ska visa att skrivaren autentiserats via MAB och placerats i VLAN 30.

Catalyst Center: Assurance → Clients → [MAC-adress]

    Kontrollera Access Type: MAB

    Kontrollera VLAN: 30 (Printers)

    Se vilken switchport (Gi1/0/12) den är ansluten till

    Bekräfta att policyn matchar ISE-regeln

🎯 Vad du tränar i denna labb

    Identifiera klienter på switchnivå

    MAC‑tabeller och auth‑sessioner

    ISE endpoint‑hantering

    ISE authorization policies

    VLAN‑assignment via MAB

    Catalyst Center → ISE integration

    End‑to‑end felsökning av NAC‑flödet

Det här är exakt samma arbetsflöde som i en riktig enterprise‑miljö.