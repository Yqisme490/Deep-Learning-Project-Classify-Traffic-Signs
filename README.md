# Traffic Sign Classification using Convolutional Neural Networks (CNNs)

**Overview:**

This project focuses on classifying traffic signs by their shape and type using Convolutional Neural Networks (CNNs). The task involves the use of deep learning techniques to accurately identify and classify traffic signs, even in cases where images are of lower quality. We experimented with different neural network architectures, including LeNet and VGG, to improve model performance.

**Key Features:**
* Shape and Type Classification: The project classifies traffic signs based on their shape (round, diamond, hex, etc.) and type (warning, stop, crossing, etc.).
* Baseline Model: A simple neural network is used as a baseline to compare performance with more advanced CNN architectures.
* CNN Architectures: We experimented with LeNet and VGG architectures to improve classification accuracy on both shape and type classes.
* Handling Imbalanced Classes: Techniques were implemented to address the imbalance in the dataset, particularly for underrepresented shapes like hexagonal signs.

**Dataset**
* The dataset contains 446 independent test images and 2,219 training images. The dataset was split into 60% training, 20% validation, and 20% test sets.
* Images were preprocessed by zooming in or cropping to focus on the traffic signs.

**Methodology**
1. Data Preprocessing:
* Images were cleaned and resized to 28x28 pixels.
* Class imbalance was identified, especially for hexagonal and diamond shapes.
  
2. Baseline Model:
* A simple neural network with three layers was trained as the baseline model.
* The baseline model achieved 90% accuracy but struggled with imbalanced classes (e.g., hex shapes).

3. CNN Architectures:
* LeNet CNN: A simple architecture designed for small images (28x28), achieving 99% accuracy in shape classification and effectively capturing features from traffic signs.
* VGG CNN: A more complex architecture that significantly improved performance, especially on independent datasets, with accuracy exceeding 80% on unseen data.
* 
4. Type Classification:
* A separate CNN model was trained to classify traffic signs by type.
* The model achieved high accuracy (99%) in type classification on the training set, but struggled with more complex and diverse sign types in the independent dataset.

**Challenges & Solutions**
* Class Imbalance: Certain traffic sign shapes and types were underrepresented in the training data, which affected model performance. We addressed this by experimenting with different CNN architectures and regularization techniques.
* Generalization Issues: While the models performed well on the training data, they struggled with unseen test images, likely due to data quality issues. Future improvements could include data augmentation to better represent diverse image conditions.
  
**Results**
* Shape Classification: Achieved an accuracy of 99% on the training set and over 80% on the independent test set.
* Type Classification: High accuracy on training data, but some traffic sign types were difficult to classify in the independent test set, suggesting the need for additional training data and augmentation.

**Future Work**
* Data Augmentation: Introducing data augmentation techniques (random cropping, rotation, etc.) to increase dataset diversity and improve model generalization.
* Improved Dataset: Including more diverse and low-quality images to help the model generalize better to real-world scenarios.
* Fine-tuning: Further tuning the CNN models to better handle class imbalances and improve performance on underrepresented traffic sign types.

**Technology Stack**
* Python
* TensorFlow / Keras
* Convolutional Neural Networks (CNNs)
