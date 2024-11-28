import cv2
import pandas as pd

# Function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B, csv):
    minimum = float('inf')
    color_name = ""
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d < minimum:
            minimum = d
            color_name = csv.loc[i, "color_name"]
    return color_name
# Function to handle mouse movement event
def draw_function(event, x, y, flags, param):
    global b, g, r, x_pos, y_pos, clicked, frame, img, capture_from_camera
    if event == cv2.EVENT_MOUSEMOVE:
        x_pos = x
        y_pos = y
        if capture_from_camera:
            b, g, r = frame[y, x]
        else:
            b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        clicked = True
# Function to display menu and get user input
def display_menu():
    print("=== Color Detection Menu ===")
    print("1. Load image from file")
    print("2. Capture image from camera")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice
# Main program
if __name__ == "__main__":
    clicked = False
    r = g = b = x_pos = y_pos = 0
    capture_from_camera = False
    csv_path = 'colors.csv'
    csv = pd.read_csv(csv_path, names=["color", "color_name", "hex", "R", "G", "B"], header=None)

    while True:
        choice = display_menu()

        if choice == '1':
            # Prompt user for image path and load image
            img_path = input("Enter the path to the image file: ")
            img = cv2.imread(img_path)
            if img is None:
                print("Error: Could not load the image from the specified path.")
                continue

            capture_from_camera = False
            window_name = 'image'
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(window_name, img.shape[1], img.shape[0])
            cv2.setMouseCallback(window_name, draw_function)

            while True:
                display_img = img.copy()
                if clicked:
                    # Dynamically set the rectangle size and position based on the image size
                    rect_width = min(750, img.shape[1] - 40)
                    rect_height = 40
                    rect_x1, rect_y1 = 20, 20
                    rect_x2 = rect_x1 + rect_width
                    rect_y2 = rect_y1 + rect_height

                    # Draw rectangle and text
                    cv2.rectangle(display_img, (rect_x1, rect_y1), (rect_x2, rect_y2), (b, g, r), -1)
                    text = get_color_name(r, g, b, csv) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
                    cv2.putText(display_img, text, (rect_x1 + 10, rect_y1 + 30), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

                    if r + g + b >= 600:
                        cv2.putText(display_img, text, (rect_x1 + 10, rect_y1 + 30), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

                cv2.imshow(window_name, display_img)

                # Break the loop when user hits 'esc' key
                if cv2.waitKey(20) & 0xFF == 27:
                    break

            cv2.destroyAllWindows()
            clicked = False  # Reset clicked state

        elif choice == '2':
            # Capture image from camera
            capture_from_camera = True
            window_name = 'image'
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            cap = cv2.VideoCapture(0)
            cv2.setMouseCallback(window_name, draw_function)

            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Failed to capture image from camera.")
                    break

                frame_copy = frame.copy()  # Make a copy to draw on

                if clicked:
                    # Dynamically set the rectangle size and position based on the image size
                    rect_width = min(750, frame.shape[1] - 40)
                    rect_height = 40
                    rect_x1, rect_y1 = 20, 20
                    rect_x2 = rect_x1 + rect_width
                    rect_y2 = rect_y1 + rect_height

                    # Draw rectangle and text
                    cv2.rectangle(frame_copy, (rect_x1, rect_y1), (rect_x2, rect_y2), (b, g, r), -1)
                    text = get_color_name(r, g, b, csv) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
                    cv2.putText(frame_copy, text, (rect_x1 + 10, rect_y1 + 30), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

                    if r + g + b >= 600:
                        cv2.putText(frame_copy, text, (rect_x1 + 10, rect_y1 + 30), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

                cv2.imshow(window_name, frame_copy)

                # Break the loop when user hits 'esc' key
                if cv2.waitKey(20) & 0xFF == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()
            clicked = False  # Reset clicked state

        elif choice == '3':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter a valid option")