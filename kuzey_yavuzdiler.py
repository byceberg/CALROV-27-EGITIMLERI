import keyboard
import time
import logging
depth_hold_aktif = False
stabilize_aktif= False

logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger("Kullanıcı")

is_running = True
while is_running:
    print ("Program çalışıyor...")
    time .sleep(0.2)
    logging.info("Program çalışıyor...")
    print("Rehber menüsünü görmek için 'r' tuşuna basın.")
    time.sleep(0.2)
    while True:
        if keyboard.is_pressed('r'):
            logging.info("Rehber menüsü açıldı...")
            logging.info("Yukarı gitmek için 'w' tuşuna basın.")
            logging.info("Aşağı gitmek için 's' tuşuna basın.")
            logging.info("Sola gitmek için 'a' tuşuna basın.")
            logging.info("Sağa gitmek için 'd' tuşuna basın.")
            logging.info("Programı kapatmak için 'q' tuşuna basın.")
            logging.info("Stabilize modunu açmak/kapatmak için 'c' tuşuna basın.")
            logging.info("Depth Hold modunu açmak/kapatmak için 'h' tuşuna basın.")
            logging.info("Sistem durumunu görmek için 'i' tuşuna basın.")
            time.sleep(0.2)

        elif keyboard.is_pressed('w'):
            logging.info("Yukarı gidiliyor...")
            time.sleep(0.2)

        elif keyboard.is_pressed('s'):
            logging.info("Aşağı gidiliyor...")
            time.sleep(0.2)
        
        elif keyboard.is_pressed('a'):           
            logging.info("Sola gidiliyor...")
            time.sleep(0.2)

        elif keyboard.is_pressed('d'):          
            logging.info("Sağa gidiliyor...")
            time.sleep(0.2)

        elif keyboard.is_pressed('c'):
            if not stabilize_aktif:
                stabilize_aktif = True
                logging.info("Stabilize moduna geçildi.")
                time.sleep(0.2)
            else:
                stabilize_aktif = False
                logging.info("Stabilize modu kapatıldı.")
                time.sleep(0.2)

        elif keyboard.is_pressed('h'):
            if not depth_hold_aktif:
                depth_hold_aktif = True
                logging.info("Depth Hold moduna geçildi.")
                time.sleep(0.2)
            else:
                depth_hold_aktif = False
                logging.info("Depth Hold modu kapatıldı.")
                time.sleep(0.2)

        elif keyboard.is_pressed('i'):
            if not depth_hold_aktif:
                logging.info("Depth Hold modu aktif değil. Depth Hold modunu açmak için 'h' tuşuna basın.")
                time.sleep(0.2)
            if depth_hold_aktif:
                logging.info("Depth Hold modu aktif. Depth Hold modunu kapatmak için 'h' tuşuna basın.")
                time.sleep(0.2)
            if not stabilize_aktif:
                logging.info("Stabilize modu aktif değil. Stabilize modunu açmak için 'c' tuşuna basın.")
                time.sleep(0.2)
            if stabilize_aktif:
                logging.info("Stabilize modu aktif. Stabilize modunu kapatmak için 'c' tuşuna basın.")
                time.sleep(0.2)
                
        elif keyboard.is_pressed('q'): 
            logging.info("Program kapatılıyor...")
            is_running = False
            break