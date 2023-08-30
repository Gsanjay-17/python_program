import qrcode

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

data = "https://docs.google.com/forms/d/e/1FAIpQLSf8dL_v7kyRphRfzN2qAtlAyWFxac1l0EatC3KJZ7wTXTSo8Q/viewform?usp=sf_link"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color="white")
img.save("test.png")