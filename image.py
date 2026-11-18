import re

class Image:
    def __init__(self, path):
        self.filename: str = path
        self.true_label: str = self.get_true_label(self.filename)
        self.classifier_label: str = ""
        self.is_correctly_classified: bool = False

    def __str__(self):
        return f"Image(filename: {self.filename}, true label: {self.true_label}, classifier label: {self.classifier_label})"

    def get_true_label(self, text):
        text = re.sub(r'^.*/', '', text)
        text = re.sub(r'_\d+\..*$', '', text)
        return re.sub(r'_', ' ', text.lower())

    def set_classifier_label(self, label):
        self.classifier_label = label
        self.is_correctly_classified = (self.true_label in self.classifier_label)

if __name__ == "__main__":
    image = Image("pet_images/fox_squirrel_01.jpg")
    print(image)