import subprocess
import random
import sys
import os
from selenium import webdriver
import time
import os
from colorama import Fore,init
import datetime
import requests

init()
clear = lambda: os.system('cls')
clear()
random_banner = random.randint(1,7)
if random_banner == 1:
      print(Fore.GREEN,"""                                                                                                                                                       
               :           :                                                                                                                              
        .,    t#,         t#,                                                                                 L.                     ,;         .        .
       ,Wt   ;##W.       ;##W.             i                     i                                        t   EW:        ,ft       f#i         ;W       ;W
      i#D.  :#L:WE      :#L:WE            LE                    LE              ..                        Ej  E##;       t#E     .E#t         f#E      f#E
     f#f   .KG  ,#D    .KG  ,#D          L#E                   L#E             ;W,      ,##############Wf.E#, E###t      t#E    i#W,        .E#f     .E#f 
   .D#i    EE    ;#f   EE    ;#f        G#W.                  G#W.            j##,       ........jW##Wt   E#t E#fE#f     t#E   L#D.        iWW;     iWW;  
  :KW,    f#.     t#i f#.     t#i      D#K.                  D#K.            G###,             tW##Kt     E#t E#t D#G    t#E :K#Wfff;     L##Lffi  L##Lffi
  t#f     :#G     GK  :#G     GK      E#K.                  E#K.           :E####,           tW##E;       E#t E#t  f#E.  t#E i##WLLLLt   tLLG##L  tLLG##L 
   ;#G     ;#L   LW.   ;#L   LW.    .E#E.                 .E#E.           ;W#DG##,         tW##E;         E#t E#t   t#K: t#E  .E#L         ,W#i     ,W#i  
    :KE.    t#f f#:     t#f f#:    .K#E                  .K#E            j###DW##,      .fW##D,           E#t E#t    ;#W,t#E    f#E:      j#E.     j#E.   
     .DW:    f#D#;       f#D#;    .K#D                  .K#D            G##i,,G##,    .f###D,             E#t E#t     :K#D#E     ,WW;   .D#j     .D#j     
       L#,    G#t         G#t    .W#G                  .W#G           :K#K:   L##,  .f####Gfffffffffff;   E#t E#t      .E##E      .D#; ,WK,     ,WK,      
        jt     t           t    :W##########Wt        :W##########Wt ;##D.    L##, .fLLLLLLLLLLLLLLLLLi   E#t ..         G#E        tt EG.      EG.       
                                :,,,,,,,,,,,,,.       :,,,,,,,,,,,,,.,,,      .,,                         ,;.             fE           ,        ,         
                                                                                                                           ,                           """)
elif random_banner == 2:
    print(Fore.RED,""" ▄████▄   ▒█████   ▒█████   ██▓        ██▓    ▄▄▄      ▒███████▒ ██▓ ███▄    █ ▓█████   ██████   ██████ 
▒██▀ ▀█  ▒██▒  ██▒▒██▒  ██▒▓██▒       ▓██▒   ▒████▄    ▒ ▒ ▒ ▄▀░▓██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▒██    ▒ 
▒▓█    ▄ ▒██░  ██▒▒██░  ██▒▒██░       ▒██░   ▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██▒▓██  ▀█ ██▒▒███   ░ ▓██▄   ░ ▓██▄   
▒▓▓▄ ▄██▒▒██   ██░▒██   ██░▒██░       ▒██░   ░██▄▄▄▄██   ▄▀▒   ░░██░▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒  ▒   ██▒
▒ ▓███▀ ░░ ████▓▒░░ ████▓▒░░██████▒   ░██████▒▓█   ▓██▒▒███████▒░██░▒██░   ▓██░░▒████▒▒██████▒▒▒██████▒▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░   ░ ▒░▓  ░▒▒   ▓▒█░░▒▒ ▓░▒░▒░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
  ░  ▒     ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░   ░ ░ ▒  ░ ▒   ▒▒ ░░░▒ ▒ ░ ▒ ▒ ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░
░        ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░        ░ ░    ░   ▒   ░ ░ ░ ░ ░ ▒ ░   ░   ░ ░    ░   ░  ░  ░  ░  ░  ░  
░ ░          ░ ░      ░ ░      ░  ░       ░  ░     ░  ░  ░ ░     ░           ░    ░  ░      ░        ░  
░                                                      ░       """)

elif random_banner == 3:
    print(Fore.BLUE,"""                                                                                                                  
      # ###                     ###        ###                                                                      
    /  /###  /                   ###        ###                        #                                            
   /  /  ###/                     ##         ##                       ###                                           
  /  ##   ##                      ##         ##                        #                                            
 /  ###                           ##         ##                                                                     
##   ##          /###     /###    ##         ##      /###     ###### ###   ###  /###     /##       /###     /###    
##   ##         / ###  / / ###  / ##         ##     / ###  / /####### ###   ###/ #### / / ###     / #### / / #### / 
##   ##        /   ###/ /   ###/  ##         ##    /   ###/ /      ##  ##    ##   ###/ /   ###   ##  ###/ ##  ###/  
##   ##       ##    ## ##    ##   ##         ##   ##    ##         /   ##    ##    ## ##    ### ####     ####       
##   ##       ##    ## ##    ##   ##         ##   ##    ##        /    ##    ##    ## ########    ###      ###      
 ##  ##       ##    ## ##    ##   ##         ##   ##    ##       ###   ##    ##    ## #######       ###      ###    
  ## #      / ##    ## ##    ##   ##         ##   ##    ##        ###  ##    ##    ## ##              ###      ###  
   ###     /  ##    ## ##    ##   ##         ##   ##    /#         ### ##    ##    ## ####    /  /###  ## /###  ##  
    ######/    ######   ######    ### /      ### / ####/ ##         ## ### / ###   ### ######/  / #### / / #### /   
      ###       ####     ####      ##/        ##/   ###   ##        ##  ##/   ###   ### #####      ###/     ###/    
                                                                    /                                               
                                                                   /                                                
                                                                  /                                                 
                                                                 /         """)
elif random_banner == 4:
    print(Fore.YELLOW,"""  ******                     **        **                  **                                 
  **////**                   /**       /**                 //                                  
 **    //   ******   ******  /**       /**  ******   ****** ** *******   *****   ******  ******
/**        **////** **////** /**       /** //////** ////** /**//**///** **///** **////  **//// 
/**       /**   /**/**   /** /**       /**  *******    **  /** /**  /**/*******//***** //***** 
//**    **/**   /**/**   /** /**       /** **////**   **   /** /**  /**/**////  /////** /////**
 //****** //****** //******  ***       ***//******** ******/** ***  /**//****** ******  ****** 
  //////   //////   //////  ///       ///  //////// ////// // ///   //  ////// //////  //////  """)

elif random_banner == 5:
    print(Fore.GREEN,"""  #####                                                                             
 #     #  ####   ####  #         #        ##   ###### # #    # ######  ####   ####  
 #       #    # #    # #         #       #  #      #  # ##   # #      #      #      
 #       #    # #    # #         #      #    #    #   # # #  # #####   ####   ####  
 #       #    # #    # #         #      ######   #    # #  # # #           #      # 
 #     # #    # #    # #         #      #    #  #     # #   ## #      #    # #    # 
  #####   ####   ####  ######    ###### #    # ###### # #    # ######  ####   ####  
                                                                                 """)
elif random_banner == 6:
    print(Fore.WHITE,"""________  ________  ________  ___               ___       ________  ________  ___  ________   _______   ________   ________      
|\   ____\|\   __  \|\   __  \|\  \             |\  \     |\   __  \|\_____  \|\  \|\   ___  \|\  ___ \ |\   ____\ |\   ____\     
\ \  \___|\ \  \|\  \ \  \|\  \ \  \            \ \  \    \ \  \|\  \\|___/  /\ \  \ \  \\ \  \ \   __/|\ \  \___|_\ \  \___|_    
 \ \  \    \ \  \\\  \ \  \\\  \ \  \            \ \  \    \ \   __  \   /  / /\ \  \ \  \\ \  \ \  \_|/_\ \_____  \\ \_____  \   
  \ \  \____\ \  \\\  \ \  \\\  \ \  \____        \ \  \____\ \  \ \  \ /  /_/__\ \  \ \  \\ \  \ \  \_|\ \|____|\  \\|____|\  \  
   \ \_______\ \_______\ \_______\ \_______\       \ \_______\ \__\ \__\\________\ \__\ \__\\ \__\ \_______\____\_\  \ ____\_\  \ 
    \|_______|\|_______|\|_______|\|_______|        \|_______|\|__|\|__|\|_______|\|__|\|__| \|__|\|_______|\_________\\_________\
                                                                                                           \|_________\|_________|
                                                                                                      """)
elif random_banner == 7:
    print(""" ██████╗ ██████╗  ██████╗ ██╗         ██╗      █████╗ ███████╗██╗███╗   ██╗███████╗███████╗███████╗
██╔════╝██╔═══██╗██╔═══██╗██║         ██║     ██╔══██╗╚══███╔╝██║████╗  ██║██╔════╝██╔════╝██╔════╝
██║     ██║   ██║██║   ██║██║         ██║     ███████║  ███╔╝ ██║██╔██╗ ██║█████╗  ███████╗███████╗
██║     ██║   ██║██║   ██║██║         ██║     ██╔══██║ ███╔╝  ██║██║╚██╗██║██╔══╝  ╚════██║╚════██║
╚██████╗╚██████╔╝╚██████╔╝███████╗    ███████╗██║  ██║███████╗██║██║ ╚████║███████╗███████║███████║
 ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝""")

while True:
  print(Fore.GREEN,"""\n      ┌─┐┌─┐┌─┐┌─┐┬  
  1── │ ┬│ ││ ┬├┤ │                   //         
      └─┘└─┘└─┘└─┘┴─┘                             
      ┌─┐┌┬┐┌┬┐
  2── │  │││ ││                      //       
      └─┘┴ ┴─┴┘   
      ┌┬┐┬┌┬┐┌─┐
  3___ │ ││││├┤                    //                ?
       ┴ ┴┴ ┴└─┘

       ┌─┐┌─┐┌┬┐┬  ┬┌─┐┬─┐  ┌─┐┬┌─┐┬ ┬┌─┐┌┐┌
 4____ │  │ ││││└┐┌┘├┤ ├┬┘  └─┐│└─┐├─┤├┤ │││     
       └─┘└─┘┴ ┴ └┘ └─┘┴└─  └─┘┴└─┘┴ ┴└─┘┘└┘
 """)
  key = input(Fore.RED+"\n{X_X} ?...→ :>>  ")

  if key == "0":
    sys.exit()
  elif key == "1":
      clear = lambda: os.system('cls')
      clear()
      print(Fore.RED,"\n..................... gogel website ......................................")
      print(Fore.BLUE,"""\n\t\t [1] instagram.com  /  [2] facebook.com  /  [3] tiktok.com 
                 [4] github.com     \  [5] youtube.com   \  [6] touter.com
                 [7] reddit.com     /  [8] netflix.com   /  [0] back
                 [00] exit  |""")
      geg = 1
      while geg == 1:
        gogel = input("\nYou r website ?? ")
        driver = webdriver.Firefox()
        if gogel == "1":
            username_instagram = input("ok! please you r user name instagram: ")
            password_instagram = input("password instagram : ")
            driver.get("http://www.instagram.com")
            user_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
            user_insta.send_keys(username_instagram)
            passwd_insta = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
            passwd_insta.send_keys(password_instagram)
            driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
        elif gogel == "2":
          driver.get('http://facebook.com/')
        elif gogel == "3":
          driver.get('http://tiktok.com/')
        elif gogel == "4":
          driver.get('http://github.com/')
        elif gogel == "5":
          driver.get('http://youtube.com/')
        elif gogel == "6":
          driver.get('http://touter.com/')
        elif gogel == "7":
          driver.get('http://reddit.com/')
        elif gogel == "8":
          driver.get('\http://netflix.com/')
        elif gogel == "0":
             geg += 1
        elif gogel == "00":
          sys.exit()
        else:
          print("Not Website!")

  elif key == "2":
    clear = lambda: os.system('cls')
    clear()
    print(Fore.GREEN,"""\n\t\t  :'######::'##::::'##:'########::
                '##... ##: ###::'###: ##.... ##:
                ##:::..:: ####'####: ##:::: ##:
                ##::::::: ## ### ##: ##:::: ##:
                ##::::::: ##. #: ##: ##:::: ##:
                ##::: ##: ##:.:: ##: ##:::: ##:
                . ######:: ##:::: ##: ########::
                :......:::..:::::..::........:::""")
    print(Fore.RED,"""
    1) run python;
    2) off pc;
    3) new file;
    4) rmove  file;
    5) list file to dairedtiry;
    6) addres pwd;
    7) ip;
    0) back to ...
    00) exit()
    +_+ & +_+ 
    """)
    p = 1
    while p == 1:
      cmd = input(Fore.WHITE+"plese You Comand CMD $_ ")
      if cmd == "1":
        os.system('python')
      elif cmd == "2":
        uu = input("you r pc dune !(y & n) ")
        if uu == "y":
          os.system("shutdown /s /t 1")
      elif cmd == "3":
        file = input("addres :: ")
        os.chdir(file)
        new = input("name you, r file+(txt,py ...) > ")
        open(new, 'a')
        print("ok new file", file)
      elif cmd == "4":
        file = input("addres :: ")
        os.chdir(file)
        nm = input("rmove file :^ ")
        os.listdir()
        os.remove(nm)
        print("ok rmove!")
        os.listdir()
      elif cmd == "5":
        close = lambda: os.system('cls')
        close()
                          
        cwd = os.getcwd()
        print(Fore.GREEN+"""
                                                                            * File:
                                                                            ---------------------------------------------------------
                                                                            [----------------------     !    ----------------------------]""")
        for dir_path, dir_names, file_names in os.walk(cwd):
              for f in file_names:
                  print("\n      [2021] ~ ",f)

      elif cmd == "6":
        yp = os.getcwd()
        print(yp)
      elif cmd == "7":
        ip = subprocess.getoutput("ipconfig")
        print(ip)
      elif cmd == "0":
        p += 3
      elif cmd == "00":
        sys.exit()
      else:
        print("please try agin! ")

  elif key == "3":
    clear = lambda: os.system('cls')
    clear()
    print("<1> <hurs> , <2> <tim aig> , <0> <back to > , <00> <exit>")
    ss =1
    while ss == 1:
       y = input("\nwhats timing #")
       if y == "2":
          o = input("time start :")
          oo = input("time stop .")
          for i in range(o,oo):
            print(i)
            time.sleep(1)
       elif y == "1":
        w = time.time()
        print(w)
       elif y == "00":
         sys.exit()
       elif y == "0":
         ss += 1
  elif key == "4":
    clear = lambda: os.system('cls')
    clear()
    print(Fore.GREEN,"""\n:::       :::  ::::::::  :::::::::  :::    ::: :::::::::: :::::::::  
:+:       :+: :+:    :+: :+:    :+: :+:   :+:  :+:        :+:    :+: 
+:+       +:+ +:+    +:+ +:+    +:+ +:+  +:+   +:+        +:+    +:+ 
+#+  +:+  +#+ +#+    +:+ +#++:++#:  +#++:++    +#++:++#   +#+    +:+ 
+#+ +#+#+ +#+ +#+    +#+ +#+    +#+ +#+  +#+   +#+        +#+    +#+ 
 #+#+# #+#+#  #+#    #+# #+#    #+# #+#   #+#  #+#        #+#    #+# 
  ###   ###    ########  ###    ### ###    ### ########## ######### """)

    print("""
   #1 Machine!
   #0 back!
   #00 exit!""")
    m = 1
    while m == 1:
      h = input("\nYOU key ")
      if h == "1":
        num1 = input("Plese insert the first number:  ")
        num2 = input("Plese insert the first number:  ")
        operation = input("Please insert your desired operation among: + - * / ")

        if operation == "+":
              result = float(num1) + float(num2)

        elif operation == "-":
              result = float(num1) - float(num2)

        elif operation == "*":
              result = float(num1) * float(num2)

        elif operation == "/":
              result = float(num1) / float(num2)
        else:
              result = "The operation by the user is wrong!"


        print(result)

      elif h == "0":
        m+=1
      elif h == "00":
        sys.exit()
      



    

    
      
    
