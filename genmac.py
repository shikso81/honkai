import os
import random

COLOR_CODE = {
    "GREEN": "\033[0;32m",
    "RESET": "\033[0m",
}

os.system("cls")
print(f'''{COLOR_CODE["GREEN"]}     
                                                                                                                                                                                                                                                                                                                                        
        ,----,                        ,----,                             
      ,/   .`|     ,----..          ,/   .`|                      ____   
    ,`   .'  :    /   /   \       ,`   .'  :     ,---,.         ,'  , `. 
  ;    ;     /   /   .     :    ;    ;     /   ,'  .' |      ,-+-,.' _ | 
.'___,/    ,'   .   /   ;.  \ .'___,/    ,'  ,---.'   |   ,-+-. ;   , || 
|    :     |   .   ;   /  ` ; |    :     |   |   |   .'  ,--.'|'   |  ;| 
;    |.';  ;   ;   |  ; \ ; | ;    |.';  ;   :   :  |-, |   |  ,', |  ': 
`----'  |  |   |   :  | ; | ' `----'  |  |   :   |  ;/| |   | /  | |  || 
    '   :  ;   .   |  ' ' ' :     '   :  ;   |   :   .' '   | :  | :  |, 
    |   |  '   '   ;  \; /  |     |   |  '   |   |  |-, ;   . |  ; |--'  
    '   :  |    \   \  ',  /      '   :  |   '   :  ;/| |   : |  | ,     
    ;   |.'      ;   :    /       ;   |.'    |   |    \ |   : '  |/      
    '---'         \   \ .'        '---'      |   :   .' ;   | |`-'       
                   `---`                     |   | ,'   |   ;/           
                                             `----'     '---'        
                                                                                                                                                                                    
                          ''')                                            

def generate_mac():
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    return ':'.join(map(lambda x: "%02x" % x, mac))

mac_addresses = [generate_mac() for _ in range(1000)]

for mac in mac_addresses:
    print(mac)