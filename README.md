# starknetd_discord_bot
A discord bot to get the status of the Starknet Node

Get the Discord Secret Key from here https://discord.com/developers/applications
Paste it at discord_bot.py file where you will my token

create a virtual environment and activate it 
than run the command "pip install requirements.txt" without inverted commas



To run the script with systemd 
create a xyx.service file at /etc/systemd/system/
 paste the below code at xyz.service file and save it
 
 
[Unit]
Description=Discord Bot

[Service]
Type=simple
User=nehat
WorkingDirectory=path where your discord script is
ExecStart= /path to your directory where you have created virtual environment  /path to your discord bot bot file
Restart=always

[Install]
WantedBy=multi-user.target

Than enable the scipt with "sudo systemctl enable xyz.service"
than start the service with "sudo systemctl start xyz.service"

and you are goofd to go. 

