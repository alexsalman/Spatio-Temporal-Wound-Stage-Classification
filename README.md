# Spatio-Temporal Wound Stage Classification
![IEEE Conference Poster](bhi-bsn22-Spatio-Temporal-Wound-Stage-Classification-poster.pdf)

University of California - Santa Cruz

CSE247 Master's Project

**Student: [Alex Salman](https://www.linkedin.com/in/alex-salman/)**

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
See the following .ipynb files in this reposetory:

[2D-CNN+LSTM for Splint Crop](https://github.com/alexsalman/CSE247/blob/59b6b42401ae36755659b7e4153a19035687fd48/2D_CNN%2BLSTM.ipynb)

[2D-CNN+LSTM for Circle Crop](https://github.com/alexsalman/CSE247/blob/main/2D_CNN%2BLSTM_No_Splint.ipynb)

[3D-CNN for Splint Crop](https://github.com/alexsalman/CSE247/blob/main/2D_CNN%2BLSTM_No_Splint.ipynb)

[3D-CNN for Circle Crop](https://github.com/alexsalman/CSE247/blob/main/3D_CNN_No_Splint.ipynb)


## Models Graphs
#### 2D-CNN + LSTM (Splint Crops)
![Splint Crop](https://docs.google.com/drawings/d/e/2PACX-1vQdkgRuHXucM3JMLDEOvPYQPYi01YQ4Lddb1g-UoocV0Fvvk4pkHDjMx5yq2h2FI_znZXz1X3apYf51/pub?w=960&h=720)

#### 2D-CNN + LSTM (Circle Crops)
![Circle Crop](https://docs.google.com/drawings/d/e/2PACX-1vQ_-M67AUWv4VgNnrYJWyl1xsY5DF3g_vMOojR_i0QE1rG420eBksqkTKEhXV4O0EttxFG1id2NOBKC/pub?w=960&h=720)


#### 3D-CNN (Splint Crops)
![Splint Crop](https://docs.google.com/drawings/d/e/2PACX-1vRmwjaPOJckupwg2_d52MeR5WIq6K3GUldA7pMhOTxhD-OLS9-n0IHRGpSDRIiE4Uiwfsq2_x8ef-Ha/pub?w=960&h=720)

#### 3D-CNN (Circle Crops)
![Circle Crop](https://docs.google.com/drawings/d/e/2PACX-1vQR-P19NUnncIXaJenRzYhyfveCEreer0-5KAtdNlw08AD7HYCqZlwN_-uImzPFhFnTDs53LasNWebL/pub?w=960&h=720)


## Saliency_Maps
#### 2D-CNN+LSTM Circle Crop
![2D-CNN+LSTM Circle Crop](https://github.com/alexsalman/CSE247/blob/main/Day%2014_Y8-4-L-VLC15%202dc%20(Saliency%20Maps).png)

#### 3D-CNN Splint Crop
![3D-CNN Splint Crop](https://github.com/alexsalman/CSE247/blob/main/Day%2014_Y8-4-L-VLC15%203ds%20(Saliency%20Maps).png)

## Shell Commands
Installing required packages
``` bash
pip3 install -r requirements.txt
```
