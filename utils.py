import re

def get_labels(path: str):
    labels: list[str] = []
    with open(path, 'r') as f:
        for line in f:
            line_labels: list[str] = re.split(r", ", line)
            for label in line_labels:
                labels.append(label.lower().strip())

    return(labels)