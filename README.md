# Advancing the interpretation and reconstruction of complex images from fMRI data using AI

## a study on the effect of loss and activation functions in LDM's

### Introduction

This extension builds upon the [MindVis framework](https://doi.org/10.1109/cvpr52729.2023.02175) for decoding human visual stimuli from brain recordings. The primary goal of the extension to the code submitted here is to enable researchers to easily experiment with different loss functions and activation functions in the LDM within the currently SOTA MindVis pipeline.

### Key Features

- Loss Function Control: Add the `--loss_function` parameter to your MindVis workflow to select from a range of supported loss functions (for now, L1 and L2).
- Activation Function Selection: Use the `--activation_function` and `--activation_function_conditioning` parameters to easily switch between common activation functions (for now, 'ReLU' and 'SiLU').
- added FID score as a metric to evaluate the quality of the generated images.

### Getting Started

Download or fork the code from this repository. Then, download the dataset and the pre-trained SC-MBM model used for fMRI encoding from [FigShare](https://figshare.com/s/94cd778e6afafb00946e) and place them in the root directory.

### Usage example:

#### For training the LDM:

    python code/stageB_ldm_finetune.py --loss_function l1 --activation_function relu

Alternatively, you can edit the `code/config.py` file to include the desired loss and activation functions.

#### For the FID score:

    python code/gen_eval.py

For more detailed installation and setup instructions, refer to the original [MindVis repository](https://github.com/zjc062/mind-vis).

### Project Status

Development: Experimental

### Acknowledgments & References

I would like to dedicate this section to acknowledge the authors of MindVis and their incredible ground work.

Chen, Z., Qing, J., Xiang, T., Yue, W. L., & Zhou, J. (2023). Seeing
Beyond the Brain: Conditional Diffusion Model with Sparse Masked
Modeling for Vision Decoding. arXiv. Retrieved from https://doi.org/10.1109/cvpr52729.2023.02175
