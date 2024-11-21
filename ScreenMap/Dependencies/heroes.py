import cv2 as cv
import os

heroes = []

a_templates = os.path.join(os.getcwd(), 'Dependencies/templates')
a_output = os.path.join(os.getcwd(), 'Dependencies/output')
a_initialization = os.path.join(os.getcwd(), 'Dependencies/initialization')

templates = []
for filename in os.listdir(a_templates):
    img = cv.imread(os.path.join(a_templates, filename))
    if img is not None:
        templates.append(img)

output = []
for filename in os.listdir(a_output):
    img = cv.imread(os.path.join(a_output, filename))
    if img is not None:
        output.append(img)
        
initialization = []
for filename in os.listdir(a_initialization):
    img = cv.imread(os.path.join(a_initialization, filename))
    if img is not None:
        initialization.append(img)
        
heroes.append(templates)
heroes.append(output)
heroes.append(initialization)