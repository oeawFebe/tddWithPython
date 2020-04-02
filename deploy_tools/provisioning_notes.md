how to set up a new instance (Amazon Lightsail)

1 Choose Linux/Unix
1 Choose Ubuntu 16.04 LTS
1 Choose $3.5 Plan
1 Type "identify your instance" Ubuntu-{{%forloop count%}}
1 Hit Create Instance
2 Go to "Networking"
2 Hit Create Static IP
2 Select an instance - choose "Ubuntu - {{forloop count}}"
2 Identify your static IP (leave it as it is e.g. StaticIp-{{forloop count}}
2 Hit Create
2 Write down your static IP (this time 34.199.74.50) (not the private ip172.26.12.84)
3 Go to Aws
3 Go to Route53
3 Go to Hosted zones in Dashboard
3 Create Hosted Zone (?) and/or Create Record Set (?)
3 choose(type?) name and insert the static IP to "value"
3 other settings are as is
3 Hit "save record set"
4 Click the ... to "Manage" the Ubuntu-{{forloop count}}
4 Hit the tab "network" and add HTTPS443 RDP3389 Custom8000 Custom8080
4 Save the setting
5 go to the "you can download your default private key from the account page"
5 download the pem file (this time /c/Users/Owner/Downloads/LightsailDefaultKey-us-east-1.pem)
6 Connect to the VPS (Ubuntu-{{count}}) and install python3.7 by

username@server:$ sudo add-apt-repository ppa:deadsnakes/ppa
press ENTER
username@server:$ sudo apt update
username@server:$ sudo apt install python3.7 python3.7-venv
type "Y"


