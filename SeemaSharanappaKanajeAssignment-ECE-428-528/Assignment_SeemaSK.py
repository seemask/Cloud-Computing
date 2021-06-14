import csv
from collections import OrderedDict
import os
import cv2
import matplotlib.pyplot as plt
from fer import FER
import requests
# Reading CSV file and arranging their names in alphabetical order
students=[]
n=1
my_dpi = 200
fig = plt.figure(figsize=(30,20), dpi=my_dpi)
class_details=dict()
with open('Masterlist.csv', newline='') as myFile:
    reader = csv.reader(myFile, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        full_name=row[0]+" "+row[1]
        url=row[2]
        class_details.setdefault(full_name,url)

sorted_dict=OrderedDict(sorted(class_details.items()))


response=input("Press 1 to see image gallery of Class Cloud Computing - ECE 428 and 528 \nPress 2 to see emotion of a student's image\nIgnore if any warnings")
# To display Image Gallery
if(response=='1'):
    for i in sorted_dict:
        try:
            image = plt.imread(sorted_dict[i], 'jpg')
            fig.tight_layout()
            ax = fig.add_subplot(18, 3, n)
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_xlabel(i)
            n = n + 1
            ax.imshow(image)

        except:
            print("URL is broken for ", i)
    plt.show()
#On entering name of the student. It displays emotion of the image.
elif(response=='2'):
    val = input("Please enter Name of a person from the class it can be a part of the name or full name")
    print(val)
    folder=r'D:\Winter2021\CloudComputing\pythonProject\Python-Assignment' # Enter folder path of the program
    filename='image_name.png'
    for student_name in sorted_dict:
        if(val in student_name):
            try:

                image_url=sorted_dict[student_name]

                img_data = requests.get(image_url).content
                with open('image_name.png', 'wb') as handler:
                    handler.write(img_data)
                    print("Picture is downloading to the local directory")
                img_emotion = cv2.imread(os.path.join(folder, filename))
                detector = FER(mtcnn=True)

                emotion, score = detector.top_emotion(img_emotion)
                print(student_name+" is "+emotion+" in the image")
            except:
                print("Unable to detect emotions for",student_name)
else:
    print("Invalid Response")






