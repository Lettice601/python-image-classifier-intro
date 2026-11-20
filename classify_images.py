from classifier import classifier
import os
from image import Image
correct_total = 0
incorrect_total = 0

images = []

input = input("Enter the path to the image file (or press Enter to use default images): ")
path = "pet_images/" if input == "" else input

for filename in os.listdir(path):
    images.append(Image(os.path.join(path, filename)))

print("Number of images found:", len(images))

#for i in range(10):
#    image = images[i]
#    print(image)

for image in images:
    classifier_label = classifier(image.filename, "alexnet")
    image.set_classifier_label(classifier_label)

    if image.is_correctly_classified:
        correct_total += 1
    else:
        incorrect_total += 1


print("Correct Classifications:", correct_total)
print("Incorrect Classifications:", incorrect_total)
for image in images:
    if not image.is_correctly_classified:
        print(image)