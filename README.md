# Color-Detection with Python and OpenCV
This project uses Python and OpenCV to detect colors in images or via a live camera feed. It provides the color name and RGB ratio for any selected point.

Features
- **Detect colors in static images or live camera feed.**
- **Displays color name and RGB values.**


Follow these steps to run the program:
1)1. Install Dependencies:
You need Python and the required libraries to run the program. Use the following steps to set up the environment.
```commandline
pip install opencv-python pandas
```

2. Configure the Color CSV File:
The program relies on a CSV file to match RGB values to their respective color names. Ensure that the CSV file colors.csv is in the same directory as the script or provide the correct path in the script.

3. Run the Program:
Load Image from File:

 - **Choose option 1 to load an image from your local storage.**
    - **You’ll be prompted to provide the path of the image file.**
    - **The program will display the image, and you can hover over the image to view the RGB values and the name of the closest matching color.**
- **Capture Image from Camera:**
    - **Choose option 2 to start the camera feed.**
    - **Hover your mouse over the live video to see the RGB values of the pixel you're pointing at.**

4. Example Menu:
Once the program runs, you'll see a menu like this:
=== Color Detection Menu ===
1. Load image from file
2. Capture image from camera
3. Exit
Enter your choice: 

5)Exit the Program:

To exit, simply choose option 3, and the program will terminate.


Contributing:
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.



