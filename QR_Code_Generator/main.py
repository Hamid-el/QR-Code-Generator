import qrCode

text = "https://www.youtube.com/watch?v=pFS4zYWxzNA"
file = "qr_code.png"

qrCode.generateQRCode(text, file)
print(f"QR Code saved to {file}")

