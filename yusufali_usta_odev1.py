import logging
import msvcrt
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)


class Uygulama():

    def __init__(self):
        self.is_running = True
        self.mode = "Manuel"

    def menu_goster(self):
        print("\n=== KONTROL PANELİ ===")
        print("W, A, S, D : Hareket")
        print("C : Stabilize Modu")
        print("H : Depth Hold Modu")
        print("I : Durum Bilgisi")
        print("Q : Çıkış")
        print(f"Aktif Mod : {self.mode}")
        print("======================\n")

    def tus_isle(self, tus):
        if tus == "w" or tus == "W":
            logging.info("Yukarı hareket edildi")
        elif tus == "s" or tus == "S":
            logging.info("Aşağı hareket edildi")
        elif tus == "a" or tus == "A":
            logging.info("Sola hareket edildi")
        elif tus == "d" or tus == "D":
            logging.info("Sağa hareket edildi")
        elif tus == "c" or tus == "C":
            self.mode = "Stabilize Modu"
            logging.info(f"Mod değişti -> {self.mode}")
        elif tus == "h" or tus == "H":
            self.mode = "Depth Hold Modu"
            logging.info(f"Mod değişti -> {self.mode}")
        elif tus == "i" or tus == "I":
            logging.info(f"Program Çalışıyor | Aktif Mod: {self.mode}")
        elif tus == "q" or tus == "Q":
            logging.info("Program kapatılıyor...")
            self.is_running = False
        else:
            logging.warning(f"Geçersiz tuş basıldı!: '{tus}'")

    def calistir(self):
        self.menu_goster()

        while self.is_running:
        
            if msvcrt.kbhit():
                tus = msvcrt.getch().decode("utf-8")
                self.tus_isle(tus)

            time.sleep(0.1)

if __name__ == "__main__":
    app = Uygulama()
    app.calistir()

