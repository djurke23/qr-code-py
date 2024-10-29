import qrcode
from PIL import Image

def kreiraj_qr_kod(tekst, naziv_fajla="qr_kod.png", velicina=10, verzija=1):
    """
    Kreira QR kod od datog teksta i čuva ga kao sliku.
    
    Parametri:
    tekst (str): Tekst ili URL koji će biti enkodiran u QR kod
    naziv_fajla (str): Ime izlaznog fajla (default: "qr_kod.png")
    velicina (int): Veličina QR koda (default: 10)
    verzija (int): Verzija QR koda, 1-40 (default: 1)
    """
    
    # Konfigurisanje QR koda
    qr = qrcode.QRCode(
        version=verzija,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=velicina,
        border=4,
    )
    
    # Dodavanje podataka
    qr.add_data(tekst)
    qr.make(fit=True)
    
    # Kreiranje slike
    qr_slika = qr.make_image(fill_color="black", back_color="white")
    
    # Čuvanje slike
    qr_slika.save(naziv_fajla)
    return naziv_fajla

# Primer korišćenja
if __name__ == "__main__":
    # Osnovni primer
    kreiraj_qr_kod("https://www.example.com")
    
    # Primer sa prilagođenim parametrima
    kreiraj_qr_kod(
        "Ovo je neki tekst za QR kod",
        naziv_fajla="moj_qr.png",
        velicina=15,
        verzija=2
    )
