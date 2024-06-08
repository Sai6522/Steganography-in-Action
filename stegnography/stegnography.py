import cv2
import os

image_path = input("Enter the path to the image file: ")


img = cv2.imread(image_path)



msg = input("Enter secret message: ")
password = input("Enter a passcode: ")


d = {}
c = {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)


n = 0
m = 0
z = 0


for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    if m == img.shape[1]:
        m = 0
        if n == img.shape[0]:
            raise ValueError("Message is too long to be encoded in this image.")
        n += 1
        z = (z + 1) % 3


output_image_path = "encrypted_Image.jpg"
cv2.imwrite(output_image_path, img)
os.startfile(output_image_path)


message = ""
n = 0
m = 0
z = 0


pas = input("Enter passcode for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        if m == img.shape[1]:
            m = 0
            if n == img.shape[0]:
                raise ValueError("Decryption went out of bounds.")
            n += 1
            z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("You are not authenticated")
