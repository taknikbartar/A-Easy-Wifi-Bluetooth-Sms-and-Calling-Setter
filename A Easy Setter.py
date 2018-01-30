import androidhelper
import threading
import time

droid = androidhelper.Android()
stopper = False

def calling(data,phone_number):
        global stopper
        stopper = False
        while True:
            droid.phoneCallNumber(phone_number)
            time.sleep(data)
            if stopper == True:
                break

def sms_sending(address,message,per):
    global stopper
    stopper = False
    while True:                
        if stopper == True:
            break
        time.sleep(per)
        droid.smsSend(address,message)
        
        
def wifi_controler():
    global stopper
    stopper = False
    while True:
        droid.toggleWifiState(True)
        if stopper == True:
            break

def bluetooth_controller():
    global stopper
    stopper = False
    while True:
        droid.toggleBluetoothState(True)
        if stopper == True:
            break
            
def bluetooth_killing():
    global stopper
    stopper = False
    while True:
        droid.toggleBluetoothState(False)
        if stopper == True:
            break

main_menu = """
*****************************
* Ana menuye hosgeldiniz.   *
* Secenekler:               *
*                           *
* arama menusu     (1)      *
* mesaj menusu     (2)      *
* wifi menusu      (3)      *
* bluetooth menusu (4)      *
*****************************
"""
while True:
    permit = input(main_menu)
    
    if permit == '1':
    
        content = """
******************************************
* Ne yapmak istiyorsunuz?                *
*                                        *
* normal bir arama yapmak (1)            *
* belirli bir sure icin surekli arama (2)*
*                                        *
******************************************
"""
                            
        while True:
            sentence = input(content)

            if sentence == '1':
                try:
                    phone_number = input("""Arayacaginiz kisinin telefon numarasi nedir?""")
                    droid.phoneCallNumber(phone_number)
                    print("Araniyor...")
                except ValueError:
                    print("Lutfen sayi degerli bir sey girin!")
                
                turn_option = input("""
ana menu icin a
cikis icin q
devam etmek icin a ve q disinda hergangi bir tus
""")
                if turn_option == 'a':
                    break
                if turn_option == 'q':
                    quit()
                

            if sentence == '2':
                try:
                    phone_number = input("""Arayacaginiz kisinin telefon numarasi nedir?""")
                    process_time = int(input("""{} numarasini kac saniye boyunca arayip durmak istersin?""".format(phone_number)))
                    per = int(input("""Kac saniyede bir arama yspmak istersiniz?"""))
                    caller = threading.Thread(target = calling,args = (per,phone_number))
                    caller.deamon = True
                    caller.start()
                    caller.join(process_time)
                    stopper = True            
                except ValueError:
                    print("Lutfen sayi degerli bir sey girin!")
            turn_option = input("""
ana menu icin a
cikis icin q
devam etmek icin a ve q disinda hergangi bir tus
""")
            if turn_option == 'a':
                break
            if turn_option == 'q':
                quit()
                
########################################

    if permit == '2':
        
        content = """
**************************************************
* Ne yapmak istiyorsunuz?                        *                             *
*                                                *
* normal bir sekilde mesaj gondermek (1)         *
* belli bir sure icin surekli mesaj gondermek (2)*
*                                                *
**************************************************
"""


        while True:
            sentence = input(content)
            if sentence == '1':
                address = input("Mesaj atacaginiz kisinin adresi nedir(tel_no seklinde)?")
                message = input("""Mesajiniz nedir?
""")
                droid.smsSend(address,message)
                print("Mesaj gonderildi...")
                turn_option = input("""
ana menu icin a
cikis icin q
devam etmek icin a ve q disinda hergangi bir tus
""")
                if turn_option == 'a':
                    break
                if turn_option == 'q':
                    quit()
                

            if sentence == '2':
                address = input("Mesaj atacaginiz kisinin adresi nedir(tel_no seklinde)?")
                message = input("""Mesajiniz nedir?
""")
                try:
                    data_time = int(input("""Bu mesaji kac saniye boyunca gondermesini istersiniz."""))
                    per = int(input("Bu mesaji kac saniyede bir gondermek istersiniz?"))
                    accepting = input("""Toplam {} tane mesaj gonderilecek.Onaylansin mi(e/E|h/H)?""".format(data_time//per))
                except ValueError:
                    print("Lutfen sayi degerli bir sey girin!")
                data_time_about = data_time // per
                if accepting == 'e' or accepting == 'E':
                    print("İslem baslatildi.")
                    sms_sender = threading.Thread(target = sms_sending,args = (address,message,per))
                    sms_sender.daemon = True
                    sms_sender.start()
                    sms_sender.join(data_time_about * per)
                    stopper = True
                    if data_time % per == 0 and (data_time // per) != 0:
                        droid.smsSend(address,message)
                    time.sleep(data_time - data_time_about)
                    print("Surec bitti...")
                    print("Tum mesajlar gonderildi...")
            
                elif accepting == 'h' or accepting == 'H':
                    print("Menuye donuluyor...")
                else:
                    print("""Lutfen duzgun bir sekilde cevabinizi belirtseydiniz daha iyi olurdu.""")
                    time.sleep(2)
                    print("Menuye donuluyor...")
                turn_option = input("""
ana menu icin a
cikis icin q
devam etmek icin a ve q disinda hergangi bir tus
""")
                if turn_option == 'a':
                    break
                if turn_option == 'q':
                    quit()
                

            else:
                print("Bu programi amacina uygun kullanin lutfen!")
                
########################################################################

    if permit == '3':
        
        content = """
******************************************
* Ne yapmak istiyorsunuz?                  *
*                                          *
* wifiyi normal ac (1)                     *
* wifiyi normal kapat (2)                  *
* wifiyi belli bir sureligine acik tut (3) *
******************************************
"""
                    
        while True:
            try:
                sentences = input(content)
                if sentences == '1':
                    wifi_check = droid.checkWifiState()
                    if wifi_check.result == True:
                        print("Wifiniz zaten acik.")
                    else:  
                        droid.toggleWifiState(True)
                        print("Wifi acildi.")
                    turn_option = input("""
ana menu icin a
cikis icin q
devam etmek icin a ve q disinda hergangi bir tus
""")
                    if turn_option == 'a':
                        break
                    if turn_option == 'q':
                        quit()

                if sentences == '2':
                    wifi_check = droid.checkWifiState()
                    if wifi_check.result == False:
                        print("Wifi zaten kapali.")
                    else:
                        droid.toggleWifiState(False)
                        print("Wifi kapatildi.")
                    turn_option = input("""
ana menu icin a
cikis icin q
devam etmek icin a ve q disinda hergangi bir tus
""")
                    if turn_option == 'a':
                        break
                    if turn_option == 'q':
                        quit()
        
                if sentences == '3':
                    data_time = int(input("Wifiniz kac saniye boyunca acik kalsin?"))                    
                    wifier = threading.Thread(target = wifi_controler )
                    wifier.daemon = True
                    wifier.start()
                    wifier.join(data_time)
                    stopper = True
                    droid.toggleWifiState(False)                               
                    print("Sure dolmustur.Wifi kapatıldı.")
            except ValueError:
                print("Lutfen sayi degerli bir sey girin.")
                
            turn_option = input("""
ana menu icin a
cikis icin q
devam etmek icin a ve q disinda hergangi bir tus
""")
            if turn_option == 'a':
                break
            if turn_option == 'q':
                quit()
                
####################################################################

    if permit == '4':
       
        content = """
********************************************
* Ne yapmak istiyorsunuz?                   *
*                                          *
* Bluetoothu normal ac (1)                 *
* Bluetoothu normal kapat (2)              *
* Bluetoothu belli bir sureligine ac (3)   *
* Bluetoothu belli bir sureligine kapat (4)*
*                                          *
********************************************
"""
        while True:

            sentence = input(content)

            if sentence == '1':
                blue_check = droid.checkBluetoothState()
                if blue_check.result == True:
                    print("Bluetooth zaten acik.")
                else:
                    droid.toggleBluetoothState(True)
                    print("Bluetooth acildi.")
                turn_option = input("""
ana menu icin a
cikis icin q
devam etmek icin a ve q disinda hergangi bir tus
""")
                if turn_option == 'a':
                    break
                if turn_option == 'q':
                    quit()
                    
            if sentence == '2':
                blue_check = droid.checkBluetoothState()
                if blue_check.result == False:
                    print("Bluetooth zaten kapali.")
                else:
                    droid.toggleBluetoothState(False)
                    print("Bluetooth kapatildi.")
                turn_option = input("""
ana menu icin a
cikis icin q
devam etmek icin a ve q disinda hergangi bir tus
""")
                if turn_option == 'a':
                    break
                if turn_option == 'q':
                    quit()

            if sentence == '3':
                data_time = int(input("Bluetoothunuz kac saniye acik kalsin?"))
                droid.toggleBluetoothState(True)
                blueer = threading.Thread(target = bluetooth_controller)
                blueer.deamon = True
                blueer.start()
                blueer.join(data_time)
                stopper = True
                droid.toggleBluetoothState(False)
                print("""Bluetoothunuzun acik kalma suresi bitmistir.Bluetooth kapatildi.""")
                turn_option = input("""
ana menu icin a
cikis icin q
devam etmek icin a ve q disinda hergangi bir tus
""")
                if turn_option == 'a':
                    break
                if turn_option == 'q':
                    quit()

            if sentence == '4':
                data_time = int(input("""Bluetoothunuz kac saniye kapali kalsin?"""))
                last_state = input("""Surec bittiginde bluetooth acilsin mi?(e/E|h/H)""")
                droid.toggleBluetoothState(False)
                blueer = threading.Thread(target = bluetooth_killing)
                blueer.daemon = True
                blueer.start()
                blueer.join(data_time)
                stopper = True
                if last_state == 'e' or last_state == 'E':  
                    droid.toggleBluetoothState(True)
                    print("""Bluetoothunuzun kapali kalma suresi bitmistir.Bluetooth acildi.""")
                if last_state == 'h' or last_state == 'H':
                    droid.toggleBluetoothState(False)
                    print("""Bluetoothunuzun kapali kalma suresi bitmistir.Bluetooth kapali.""")
                turn_option = input("""
ana menu icin a
cikis icin q
devam etmek icin a ve q disinda hergangi bir tus
""")
                if turn_option == 'a':
                    break
                if turn_option == 'q':
                    quit()
