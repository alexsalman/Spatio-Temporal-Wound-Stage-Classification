# Spatio-Temporal Wound Stage Classification

University of California - Santa Cruz

CSE247 Master's Project

**A project by [Alex Salman](mailto:aalsalma@ucsc.edu)**

Last modified: June 3, 2022

## Project Description
This project proposes an architecture for classifying wound healing stages of a series of wound images. We generate a series of consecutive wound image frames and feed them to a 2D convolutional neural network combined with long short-term memory unit and a 3D convolutional neural network to learn spatio-temporal features associated with the healing trajectory. We also visualize the saliency maps to identify features the model is extracting. Both models can extract visual features related to wound healing and have relatively high classification accuracy.

## Project Features
1. Generate videos from images using openCV
2. Pad different length generated videos to have the same length (16 frames)
3. Name vidoe after the name of the last frame appended
4. Normalize array of frames to values between 0-1
5. Split data to 75% training, 12.5% validation, and 12.5% test
6. Learn spatio-temporal features using 2D-CNN+LSTM and 3D-CNN
7. Has two versions for each model for high and low resolution images
8. Visualize features extracted using saliency maps

## Dataset
[Wound image dataset](https://datadryad.org/stash/dataset/doi:10.25338/B84W8Q)

[Processed dataset repository](https://drive.google.com/drive/u/0/folders/1VRzXupLR9Xct_8Fuph-HqbAAj95qLnU4)

## Labels
Hemostasis, Inflammatory, Proliferative, and Maturation

## Models
#### 2D-CNN + LSTM (Splint Crops)
![Splint Crop](https://docs.google.com/drawings/d/e/2PACX-1vQdkgRuHXucM3JMLDEOvPYQPYi01YQ4Lddb1g-UoocV0Fvvk4pkHDjMx5yq2h2FI_znZXz1X3apYf51/pub?w=960&h=720)
![Circle Crop](https://docs.google.com/drawings/d/e/2PACX-1vQ_-M67AUWv4VgNnrYJWyl1xsY5DF3g_vMOojR_i0QE1rG420eBksqkTKEhXV4O0EttxFG1id2NOBKC/pub?w=960&h=720)


#### 3D-CNN


## Shell Commands
Installing required packages
``` bash
pip3 install -r requirements.txt
```
