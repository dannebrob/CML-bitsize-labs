import urllib3
urllib3.disable_warnings()

from virl2_client import ClientLibrary

CML_URL = "https://YOUR_IP_TO_CML_SERVER"
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD!"

LAB_NAME = "Enterprice Network Lab"   # ändra till din labb
NODE_NAME = "NewRouter1"    # namnet på noden du vill skapa
NODE_DEFINITION = "iol-xe"    # exempel: iosv, iosvl2, alpine, server, etc.

client = ClientLibrary(
    url=CML_URL,
    username=USERNAME,
    password=PASSWORD,
    ssl_verify=False
)

# Hämta labben
labs = client.all_labs()
lab = None
for l in labs:
    if l.title == LAB_NAME:
        lab = l
        break

if lab is None:
    print(f"Labb '{LAB_NAME}' hittades inte.")
    exit(1)

# Skapa noden
node = lab.create_node(
    label=NODE_NAME,
    node_definition=NODE_DEFINITION,
    x=100,
    y=100
)

lab.sync()

print(f"Node '{NODE_NAME}' skapad i labben '{LAB_NAME}'.")
