import re
from utils import *

class Image:
    list_of_dogs = get_labels("dognames.txt")

    def __init__(self, path):
        self.filename: str = path
        self.true_label: str = self.get_true_label(self.filename)
        self.classifier_label: str = ""
        self.is_correctly_classified: bool = False

        self.is_a_dog: bool = self.is_true_label_dog(Image.list_of_dogs)
        self.classifier_thinks_dog: bool = False

    def __str__(self):
        lines = []
        lines.append(f"file: {self.filename}")
        lines.append(f"\t{'true label:':<20}{'(dog)' if self.is_a_dog else '(not dog)'} {self.true_label}")
        lines.append(f"\t{'classifier label:':<20}{'(dog)' if self.classifier_thinks_dog else '(not dog)'} {self.classifier_label}")
        return(f"{lines[0]}\n{lines[1]}\n{lines[2]}")
        
    def get_true_label(self, text: str):
        text = re.sub(r'^.*(\/|\\)', '', text)
        text = re.sub(r'_\d+\..*$', '', text)
        return re.sub(r'_', ' ', text.lower())

    def set_classifier_label(self, label: str):
        self.classifier_label = label.lower()
        self.is_classifier_label_dog(Image.list_of_dogs)
        self.is_correctly_classified = (self.true_label in self.classifier_label)

    def is_true_label_dog(self, list_of_dogs: list):
        self.is_a_dog = True if self.true_label in list_of_dogs else False
        return self.is_a_dog

    def is_classifier_label_dog(self, list_of_dogs: list):
        self.classifier_thinks_dog = True if self.classifier_label in list_of_dogs else False
        return self.classifier_thinks_dog

if __name__ == "__main__":
    image = Image("pet_images/fox_squirrel_01.jpg")
    image.is_classifier_label_dog(get_labels("dognames.txt"))
    print(image)
    image = Image("pet_images/Basenji_00963.jpg")
    image.is_classifier_label_dog(get_labels("dognames.txt"))
    print(image)