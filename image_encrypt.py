from PIL import Image


def process_img(choice,key,image_path):
    img = Image.open(image_path)

    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            if choice == 1:
                r, g, b =pixels[x,y]
                r = (r+key) % 256
                g = (g+key+key) % 256
                b = (b+key+key+key) % 256
                pixels[x,y] = r,g,b
            elif choice ==2:
                r, g, b =pixels[x,y]
                r = (r-key) % 256
                g = (g-key-key) % 256
                b = (b-key-key-key) % 256
                pixels[x,y] = r,g,b
    if choice == 1:
        img.save("encrypted_sample.jpg")
        print("Image encrypted as encrypted_sample.jpg")
    elif choice == 2:
        img.save("decrypted_sample.jpg")
        print("Image decrypted as decrypted_sample.jpg")


print("1.Encrypt image")
print("2.Decrypt image")
choice = int(input("Enter your choice: "))
image_path = input("Enter image file name (example: photo.png): ")
key = int(input("Enter key (integer): "))
process_img(choice,key,image_path)
