# Finding Orientation on a 2D Plane

This project aims to find the orientation difference between two images on a 2D plane using computer vision techniques. It calculates the angle difference between the predominant features in each image.

## Description

The `main.py` script processes two input images, `temp_img.jpg` and `test_image2.jpg`, to determine their orientation difference. It utilizes OpenCV for image processing and matplotlib for visualization.

## Requirements

- Python 3
- OpenCV (`opencv-python-headless`)
- Matplotlib

## Installation

1. **Install Python**: If not already installed, install Python 3 on your system.

2. **Install pip**: Ensure pip, the Python package installer, is installed. You can install it using the following command:

    ```bash
    sudo apt update
    sudo apt install python3-pip
    ```

3. **Install Dependencies**: Install the required Python packages using pip:

    ```bash
    pip3 install opencv-python-headless matplotlib
    ```

## Usage

1. **Clone the Repository**: Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/Finding-Orientation-on-a-2D-plane.git
    ```

2. **Navigate to the Directory**: Change to the directory containing the cloned repository:

    ```bash
    cd Finding-Orientation-on-a-2D-plane
    ```

3. **Add Images**: Place the images you want to process in the same directory as `main.py`. Ensure they are named `temp_img.jpg` and `test_image2.jpg`.

4. **Run the Script**: Execute the `main.py` script to calculate the orientation difference:

    ```bash
    python3 main.py
    ```

5. **View Results**: The script will display the estimated angle difference between the two images along with visualizations.

## Model Comparison


### Using Open Methods 

#### Description:
The model is designed to estimate the angle difference between two images on a 2D plane using computer vision techniques. It preprocesses the input images by applying Gaussian blurring, adaptive thresholding, contour detection, and morphological operations to enhance the features. Then, it calculates the angle difference between the predominant features in each image and visualizes the results.

#### Results:
![Sample Image 1](https://github.com/Shivam-a0621/Finding-Orientation-on-a-2D-plane/blob/main/sampleimages/Screenshot%202024-05-14%20173521.png)
- The best result was provided by the anisotropic diffusion
![Result 2](https://github.com/Shivam-a0621/Finding-Orientation-on-a-2D-plane/blob/main/sampleimages/Screenshot%202024-05-14%20173609.png)
- Final comparios of orientations of two images
- ![Result 3](https://github.com/Shivam-a0621/Finding-Orientation-on-a-2D-plane/blob/main/sampleimages/Screenshot%202024-05-14%20173620.png)


In addition to the orientation difference calculated by the main script, here are the results obtained from other models for comparison.


### U-net and RCNN based Ml algorithms

#### Description:
U-Net is a convolutional neural network (CNN) architecture designed for biomedical image segmentation tasks. It consists of a contracting path to capture context and a symmetric expanding path that enables precise localization. U-Net has gained popularity for its effectiveness in various medical image analysis applications


#### Results:
 ![Result 1](https://github.com/Shivam-a0621/Finding-Orientation-on-a-2D-plane/blob/main/sampleimages/output.png).




### YOLO Model

#### Description:
YOLO (You Only Look Once) is an efficient object detection model known for its real-time performance. I have trained a Yolo segment model on custome datset which I have annotated using roboflow.

#### Results:
![YOLO Result 1](https://github.com/Shivam-a0621/Finding-Orientation-on-a-2D-plane/blob/main/sampleimages/train_batch90.jpg)


### SAM Model

#### Description:
The Segment Anything Model (SAM) is a segmentation model provided by meta , I have also tried this model for segmenting and finding orientation.

#### Results:
![SAM Result 1](https://github.com/Shivam-a0621/Finding-Orientation-on-a-2D-plane/blob/main/sampleimages/SAM.jpg)



## License

This project is licensed under the [MIT License](LICENSE).
