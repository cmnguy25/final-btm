# Detecting and Mapping Tree Coordinates and Brown-Tailed Moth Nests Using Drone Imaging

## Introduction
This project is a continuation of the work initiated by Henry Landay in collaboration with Professor Chowdhury at Colby College’s Davis AI Institute. Over the past few months, I have worked with Professor Klepach from Colby College’s Science, Technology, and Society (STS) department to utilize machine learning techniques for detecting brown-tailed moth (BTM) nests from drone imagery.

## Task 1: Detecting and Mapping Tree Coordinates from Drone Imaging

### Introduction  
The first phase of the project involved mapping tree coordinates from drone imagery. Previously, there was no way to directly identify individual trees in the images, which presented a significant challenge.

### Methodology  
A Python script, `metadata.py`, was developed to extract critical metadata from the drone images, including altitude and the camera's field of view. This metadata was used to calculate the distances between image edges. The YOLO library was utilized to detect tree locations within the drone images using a pre-trained model.

However, the metadata lacked directional information (e.g., North, East, South, West), complicating the task of mapping tree coordinates. To overcome this, a function was implemented using the `detecttrees.py` script to rotate the marked images 360 degrees around their center, attempting to align detected trees with pre-existing tree coordinates.

### Results  
The workaround achieved acceptable accuracy, allowing for the mapping of all photographed trees in the `metadata.ipynb` file. However, this method's success is contingent on the availability of an existing coordinate dataset. Without such data, the method is less reliable and involved a degree of guesswork and trial-and-error. Collecting clear and accurate data is strongly recommended for future efforts.

### Future Research  
Future drone operators should capture images directly above the trees, with the drone parallel to the ground and its view perpendicular to the ground. Recording the drone’s direction would simplify the calculation of coordinates using basic mathematical and physical principles. This approach would also enable coordinate calculations without pre-existing datasets, enhancing project scalability.

Additionally, I recommend exploring alternatives to the YOLO library for tree detection, as YOLO includes extraneous information and has non-optimal runtimes. The size of the YOLO library also presents challenges for uploading to GitHub.

## Task 2: Training a Machine Learning Model to Detect Brown-Tailed Moth Nests from Drone Imaging

### Introduction  
The second phase of the project focused on developing a machine learning algorithm to detect brown-tailed moth nests from drone imagery. The goal was to reduce the time and cost associated with conducting BTM surveys, potentially saving resources and enabling more frequent surveys.

### Methodology  
The initial plan involved training the machine learning model using infrared (IR) images, as these were expected to show clear contrasts between nests and their surroundings due to temperature differences. However, most IR photos were too blurry to be useful, and the remaining images did not display discernible IR contrasts. Consequently, I reverted to using RGB images, which presented significant challenges due to the similarities between BTM nests and tree buds.

For the RGB analysis, I constructed a Convolutional Neural Network (CNN) using TensorFlow. The data was augmented by dividing each image into 49 smaller images, maintaining the same ratio and classifying them as either “nests” or “no_nests.” To balance the classes, images without nests were randomly removed until the dataset contained approximately 80 images evenly divided between the two classes. The model was trained with an 80-20 training-validation split, a batch size of 16, and 10 epochs.

### Results  
The current model's accuracy hovers around 60%, with limited avenues for improvement due to the insufficient quantity and quality of data. The model effectively detects clear and obvious BTM nests but struggles with more subtle cases, despite attempts at data augmentation.

### Future Research  
Future research should prioritize the collection of higher-quality data, particularly IR images captured during colder months to enhance contrast between nests and their surroundings. Drone operators should capture high-resolution, non-blurry images that clearly depict trees. I believe that a CNN with TensorFlow remains a sound approach for this task.

## File directory and explanation
BTM
- **`dataset/`** - Dataset used to train the model. Divided into nests and no nests.
- **`images/`** - Unimportant.
- **`images2/`** - Unimportant.
- **`images3/`** - Unimportant.
- **`images4/`** - Unimportant.
- **`images5/`** - Unimportant.
- **`__pycache__/`** - Unimportant.
- **`.gitattributes`** - Unimportant.
- **`.gitignore`** - Unimportant.
- **`btmnotes.txt`** - Unimportant.
- **`coco.names`** - Unimportant.
- **`delete_extra.py`** - Deletes half the files in the no_nests subfolder. No longer important.
- **`detecttrees.py`** - Detects trees using the YOLO library.
- **`detect_btm.ipynb`** - The BTM detection model and algorithm.
- **`image.py`** - Unimportant.
- **`map.html`** - Unimportant.
- **`metadata.ipynb`** - Tree mapping and detection implementation.
- **`metadata.py`** - Processes the metadata and many other things.
- **`move_files.py`** - Unimportant.
- **`random_points_map.html`** - Unimportant.
- **`README.md`** - This file.
- **`split_images.py`** - Unimportant.
- **`split_multiple_images.py`** - Used to split images into smaller ones. Can change variables to split into more or fewer images.
- **`trees.csv`** - Unimportant.
- **`yolov3.cfg`** - Unimportant.



## Acknowledgements  
- Professor Klepach  
- Linh Tong  
- Tahiya Chowdhury  
- Henry Landay  
- Sam Trafton