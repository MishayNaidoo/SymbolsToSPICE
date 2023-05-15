import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image
from PyQt5.QtGui import QImage
import PIL
from PIL import Image
import glob
import numpy as np

import random

import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers,models
from keras.preprocessing.image import ImageDataGenerator

loaded_model = models.load_model('ModelGUIV1')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Component Identification")
        
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(400, 400)
        
        self.result_label = QLabel(self)
        
        upload_button = QPushButton("Upload Image", self)
        upload_button.clicked.connect(self.upload_image)
        
        layout = QVBoxLayout()
        layout.addWidget(upload_button)
        layout.addWidget(self.image_label)
        layout.addWidget(self.result_label)
        
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def upload_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)")
        
        if image_path:
            # Process the image
            processed_image = process_image(image_path)
            
            # Display the processed image
            self.display_image(processed_image)
            
            # Identify the component using your machine learning algorithm
            identified_component = identify_component(processed_image)
            
            # Display the result
            self.result_label.setText(f"Identified Component: {identified_component}")
    
    def display_image(self, image):
        image = image.convert("RGBA")  # Convert PIL Image to RGBA mode
        data = image.tobytes("raw", "RGBA")  # Get the image data bytes
        qimage = QImage(data, image.size[0], image.size[1], QImage.Format_RGBA8888)  # Create a QImage from the image data
        pixmap = QPixmap.fromImage(qimage)  # Convert QImage to QPixmap
        self.image_label.setPixmap(pixmap)
    
def process_image(image_path):
    # Implement your image processing logic here
    # You can use libraries like OpenCV or PIL to load and preprocess the image
    # Return the processed image
    
    # Example: Resizing the image to fit the label size
    image = Image.open(image_path)
    image = image.resize((400, 400), Image.ANTIALIAS)
    return image

def identify_component(image):
    # Implement your machine learning algorithm to identify the component in the image
    # Return the identified component
    
    # Example: Randomly select a component
    components = ["Resistor", "Capacitor", "Inductor", "Battery", "Ground"]
    return random.choice(components)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
