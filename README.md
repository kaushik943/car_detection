Car Detection Using OpenCV
This project demonstrates a basic car detection system using OpenCV's Haar Cascade classifier. The system processes a video file to detect and highlight cars in each frame using a pre-trained Haar Cascade classifier.

Prerequisites
Before running the code, ensure you have the following installed:

Python 3
OpenCV (cv2)

Files
haarcascade_car.xml: Haar Cascade classifier file for car detection.
cars.mp4: Input video file containing car footage.
car_detection.py: Main script to run the car detection.

Usage

Download the Haar Cascade for Cars

You can find the haarcascade_car.xml file here. Make sure this file is in the same directory as your script.

Prepare the Video File

Ensure you have a video file named cars.mp4 in the same directory as your script. This video should contain the footage you want to process.

Run the Script

Execute the script using Python : python car_detection.py

Code Explanation

Load Haar Cascade: The CascadeClassifier is loaded with the haarcascade_car.xml file.
Video Capture: Video is captured from the cars.mp4 file.
Frame Processing: Each frame is converted to grayscale, and cars are detected using the detectMultiScale method.
Draw Rectangles: Rectangles are drawn around detected cars.
Display Frame: The processed frame is displayed in a window.
Exit on 'Esc' Key: The loop breaks if the 'Esc' key is pressed, and resources are released.


