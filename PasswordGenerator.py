
import random
import string
import time
try:  
    while True:
        def generate_password (length,level,output=[]):
            chars = string.ascii_letters
            if level > 1:
                chars = "{},{}".format(chars,string.digits)
            if level > 1:
                chars = "{},{}".format(chars,string.punctuation)
            #if level > 1:
                #chars = "{},{}".format(chars,string.hexdigits)


            for i in range(length):
                output.append(random.choice(chars))
            
            return"".join(output)
        

        banner = """
        ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗           
        ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗          
        ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║          
        ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║          
        ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝          
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝           
                                                                                    
        ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
        ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
        ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
        ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
        ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
        ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝                                                                          
        """
        print(banner)
        print ("""
        Level 0 = Very Easy
        Level 1 = Easy
        Level 2 = Middle
        Level 3 = Hard
        Level 4 = Very Hard
        """)
        print("Please wait...")
        time.sleep(5)
        password_length = int(input("Length: "))
        password_level = int(input("Level: "))
        password = generate_password(password_length, password_level)
        print("\nYour password is: {}".format(password))
        continue
except KeyboardInterrupt:
    print ("\n Quit & Reset ")
    print ("\n Developer AdamSmithH_")
    time.sleep(3)


