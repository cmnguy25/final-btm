import cv2
import numpy as np

def detect_and_mark_tree(image_path, output_path):
    # Load image
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define range for brown color in HSV (assuming trees are mostly brown in winter)
    lower_brown = np.array([10, 100, 20])
    upper_brown = np.array([20, 255, 200])
    
    # Threshold the HSV image to get only brown colors
    mask = cv2.inRange(hsv, lower_brown, upper_brown)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Adjust the threshold area as needed
            M = cv2.moments(contour)
            if M["m00"] != 0:
                center_x = int(M["m10"] / M["m00"])
                center_y = int(M["m01"] / M["m00"])
                # Draw a larger dot in a brighter color (red) in the center of the detected tree
                cv2.circle(image, (center_x, center_y), 10, (0, 0, 255), -1)

    # Save the image with the marked tree
    cv2.imwrite(output_path, image)
    # Show the image with the marked tree
    cv2.imshow("Image with detected tree", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
detect_and_mark_tree('images/DJI_20240425075720_0004_V.JPG', 'images/DJI_20240425075720_0004_V_marked.JPG')

