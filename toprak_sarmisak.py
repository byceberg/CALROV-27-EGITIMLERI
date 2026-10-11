import msvcrt
import logging

logger = logging.getLogger("Calrov27")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
logger.addHandler(handler)

def Tusalma():
    karakter = msvcrt.getch()
    try:
        return karakter.decode("utf-8")
    except UnicodeDecodeError:
        return karakter

print("Hoşgeldiniz, belirli komutları çalıştırmak için aşağıdaki rehbere bakınız.\nW = İleri Gitmek\nA = Sola Gitmek\nS = Aşağı Gitmek\nD = Sağa Gitmek\nZ = Armed Moduna Geçmek\nX = Disarmed Moduna Geçmek\nC = Stabilize Moduna Geçmek\nH = Depth Hold Moduna Geçmek\nV = Mevcut Durumu Görüntülemek\nQ = Çıkış")

MitArmoderNicht = "Disarmed"
Xkoordinat = 0
Ykoordinat = 0
Mod = "Etkin mod yok"

while(1):
    girdi = Tusalma()
    
    match girdi:
        case "W" | "w":
            if MitArmoderNicht == "Armed":
                logger.info("İleri gidildi.")
                Ykoordinat += 1
            else:
                logger.warning("Aracı ilk önce Armed moduna geçiriniz.")
        case "A" | "a":
            if MitArmoderNicht == "Armed":
                logger.info("Sola gidildi.")
                Xkoordinat -=1
            else:
                logger.warning("Aracı ilk önce Armed moduna geçiriniz.")
        case "S" | "s":
            if MitArmoderNicht == "Armed":
                logger.info("Geri gidildi.")
                Xkoordinat -=1
            else:
                logger.warning("Aracı ilk önce Armed moduna geçiriniz.")
        case "D" | "d":
            if MitArmoderNicht == "Armed":
                logger.info("Sağa gidildi")
                Xkoordinat +=1
            else:
                logger.warning("Aracı ilk önce Armed moduna geçiriniz.") 
        case "Z" | "z":
                if MitArmoderNicht == "Disarmed":
                    logger.info("Armed moduna geçildi.")
                    MitArmoderNicht = "Armed"
                else: 
                    logger.info("Araç zaten Armed modunda.")
        case "X" | "x":
                if MitArmoderNicht == "Disarmed":
                    logger.info("Araç zaten Disarmed modunda.")
                else: 
                    logger.info("Disarmed moduna geçildi") 
                    MitArmoderNicht = "Disarmed" 
        case "C" | "c":
                if Mod != "Stabilize":
                    logger.info("Stabilize moduna geçildi.")
                    Mod = "Stabilize"
                else: 
                    logger.info("Stabilize modu devre dışı bırakıldı.") 
                    Mod = "Etkin mod yok"       
        case "H" | "h":
                if Mod != "Depth Hold":
                    logger.info("Depth Hold moduna geçildi.")
                    Mod = "Depth Hold"
                else: 
                    logger.info("Depth Hold modu devre dışı bırakıldı.") 
                    Mod = "Etkin mod yok"                 
        case "V" | "v":
              logger.info("=" * 35 + f"\nDurum = Çalışıyor\nKoordinat = {Xkoordinat},{Ykoordinat}\n{MitArmoderNicht}\nMod = {Mod}\n" + "=" * 35)
        case "Q" | "q":
              logger.info("Program başarılı bir şekilde sonlandırılıyor")
              break
        
              
            