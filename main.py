import cv2 
import numpy as np
import matplotlib.pyplot as plt

def preprocessing(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh_img = cv2.adaptiveThreshold(blurred_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
    aniso_img = cv2.filter2D(thresh_img, -1, np.ones((3,3),np.uint8))
    contours, _ = cv2.findContours(aniso_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    min_contour_area = 300  # Adjust this threshold as needed
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
    contour_mask = np.zeros_like(aniso_img)
    cv2.drawContours(contour_mask, filtered_contours, -1, 255, thickness=cv2.FILLED)
    filtered_img = cv2.bitwise_and(aniso_img, contour_mask)
    final_img = cv2.GaussianBlur(filtered_img, (5, 5), 0)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    bin_img = cv2.morphologyEx(final_img, cv2.MORPH_OPEN, kernel, iterations=2)
    
    return bin_img

def angle_difference(img1, img2):
    final_img1 = preprocessing(img1.copy())
    final_img2 = preprocessing(img2.copy())

    contours1, _ = cv2.findContours(final_img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(final_img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours1) > 0 and len(contours2) > 0:
        cnt1 = max(contours1, key=cv2.contourArea)
        cnt2 = max(contours2, key=cv2.contourArea)

        M1 = cv2.moments(cnt1)
        cx1 = int(M1["m10"] / M1["m00"] if M1["m00"] != 0 else 0)
        cy1 = int(M1["m01"] / M1["m00"] if M1["m00"] != 0 else 0)

        M2 = cv2.moments(cnt2)
        cx2 = int(M2["m10"] / M2["m00"] if M2["m00"] != 0 else 0)
        cy2 = int(M2["m01"] / M2["m00"] if M2["m00"] != 0 else 0)

        dx = cx2 - cx1
        dy = cy2 - cy1

        angle1 = np.arctan2(dy, dx)
        angle1_deg = np.degrees(angle1)

        angle_diff_deg = abs(angle1_deg)
        if angle_diff_deg > 180:
            angle_diff_deg = 360 - angle_diff_deg

        rgb_img1 = cv2.cvtColor(final_img1, cv2.COLOR_BGR2RGB)
        rgb_img2 = cv2.cvtColor(final_img2, cv2.COLOR_BGR2RGB)

        fig, (ax1, ax2) = plt.subplots(1, 2)

        ax1.imshow(rgb_img1)
        ax1.axis('off')

        ax2.imshow(rgb_img2)
        ax2.axis('off')  

        fig.suptitle(f'Estimated Angle Difference: {angle_diff_deg:.2f} degrees')

        plt.show()

        return angle_diff_deg

def main():
    img1 = cv2.imread("temp_img.jpg")
    img2 = cv2.imread("test_image2.jpg")
    angle_diff = angle_difference(img1, img2)

if __name__ == "__main__":
    main()
