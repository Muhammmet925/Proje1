import hashlib

# Bilinen virüslerin hash imzaları (Örnektir)
VIRUS_DATABASE = {
    "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8": "Truva Atı Tespit Edildi!",
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855": "Spyware Tespit Edildi!"
}

def dosya_tara(dosya_yolu):
    with open(dosya_yolu, "rb") as f:
        dosya_icerigi = f.read()
        dosya_hash = hashlib.sha256(dosya_icerigi).hexdigest()
        
    if dosya_hash in VIRUS_DATABASE:
        return f"TEHLİKE: {VIRUS_DATABASE[dosya_hash]}"
    else:
        return "Dosya Temiz."