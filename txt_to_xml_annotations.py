"""
Script to convert ExDark Dataset to a format that Darkflow can use
"""
import cv2
import os

IMG_DIR = 'ExDark/Car/'
DATA_DIR = 'ExDark_Anno/Car/'
RESULTS_DIR = 'ExDark_Custom_Anno/Car/'
for filename in os.listdir(DATA_DIR):
    print("On file ", filename)
    img = cv2.imread(IMG_DIR + filename.split(".txt")[0])
    img_width = img.shape[1]
    img_height = img.shape[0]

    with open(DATA_DIR + filename, "r") as in_f:
        data = in_f.readlines()[1]
        data = data.split()
        label = data[0]
        top_left_x = data[1]
        top_left_y = data[2]
        width_bbox = data[3]
        height_bbox = data[4]

        if label == "Car":
            with open(RESULTS_DIR + filename.split(".jpg.txt")[0] + ".xml", "w") as out_f:
                out_f.writelines(["<annotation>\n",
                                  "<folder>ExDark/Car</folder>\n"
                                  "<filename>" + str(filename).split('.txt')[0] + "</filename>\n",
                                  "<path>" + str(IMG_DIR + filename.split('.txt')[0]) + "</path>\n",
                                  "<source>\n",
                                  "<database>Unknown</database>\n",
                                  "</source>\n",
                                  "<size>\n",
                                  "<width>" + str(img_width) + "</width>\n",
                                  "<height>" + str(img_height) + "</height>\n",
                                  "<depth>3</depth>\n",
                                  "</size>\n",
                                  "<segmented>0</segmented>\n",
                                  "<object>\n",
                                  "<name>car</name>\n",
                                  "<pose>Unspecified</pose>\n",
                                  "<truncated>0</truncated>\n",
                                  "<difficult>0</difficult>\n",
                                  "<bndbox>\n",
                                  "<xmin>" + str(top_left_x) + "</xmin>\n",
                                  "<ymin>" + str(top_left_y) + "</ymin>\n",
                                  "<xmax>" + str(int(int(top_left_x) + int(width_bbox))) + "</xmax>\n",
                                  "<ymax>" + str(int(int(top_left_y) + int(height_bbox))) + "</ymax>\n",
                                  "</bndbox>\n",
                                  "</object>\n",
                                  "</annotation>\n"])
