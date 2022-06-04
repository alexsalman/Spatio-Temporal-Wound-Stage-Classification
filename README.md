# Spatio-Temporal Wound Stage Classification

University of California - Santa Cruz

CSE247 Master's Project

**A project by [Alex Salman](mailto:aalsalma@ucsc.edu)**

Last modified: June 3, 2022

## Project Description
With the increasing usage of neural networks and deep learning in the medical field, this work proposes an architecture for classifying wound healing stages of a series of wound images. We generate a series of consecutive wound image frames and feed them to a 2D convolutional neural network combined with long short-term memory unit and a 3D convolutional neural network to learn spatio-temporal features associated with the healing trajectory. We also visualize the saliency maps to identify features the model is extracting. Both models can extract visual features related to wound healing and have relatively high classification accuracy.

## Dataset
[Wound image dataset](https://datadryad.org/stash/dataset/doi:10.25338/B84W8Q)

[Processed dataset repository](https://drive.google.com/drive/u/0/folders/1VRzXupLR9Xct_8Fuph-HqbAAj95qLnU4)

## Shell Commands
Installing required packages
``` bash
pip3 install -r requirements.txt
```
