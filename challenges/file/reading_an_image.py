image = open("Ellie.jpg", "rb")
binary_data = image.read()
image.close()
print(f"Binary data: {binary_data}")