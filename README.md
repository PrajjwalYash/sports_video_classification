# Sports Video Recognition using CNN + LSTM

## Overview
This project focuses on recognizing actions in videos using a combination of CNNs and LSTM networks. The goal is to leverage the strengths of convolutional networks for spatial feature extraction and LSTM networks for capturing temporal dynamics. This approach ensures that the temporal information in video sequences is not lost, leading to better action recognition.

## Approaches Considered

### 1. Simple CNN Models
- **Approach:** Started with traditional CNN models applied directly to video frames. Take a moving average of the output.
- **Issue:** While CNNs effectively capture spatial features, they lack the capability to preserve and analyze temporal information across frames, which is crucial for accurate action recognition.

### 2. 2+1D Convolution
- **Approach:** Applied 2D convolutions followed by 1D convolutions separately to capture temporal and spatial information.
- **Analysis:** This approach is inspired by models like MobileNet, where separable convolutions are used to reduce computational complexity. However, in the context of action recognition, convolution alone might not effectively capture the sequence of movements (temporal dynamics) necessary for accurate predictions.

### 3. CNN Followed by LSTM (Final Approach)
- **Approach:** Used a combination of CNN to extract spatial features from each frame, followed by an LSTM to capture temporal dependencies between these frames.
- **Reasoning:** This method simplifies the model while effectively capturing temporal relationships using feature vectors derived from a time-distributed CNN. The LSTM layer then processes these sequences of feature vectors to make predictions about the action being performed.
