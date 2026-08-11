# ML From Scratch

A hands-on journey through Machine Learning by implementing algorithms from scratch.

The goal of this repository is to understand the mathematics, intuition, and implementation behind machine learning algorithms rather than relying entirely on high-level libraries.

Every algorithm in this repository will be implemented from scratch using Python and fundamental tools such as NumPy.

---

## Goals

- Understand the mathematical foundations behind ML algorithms
- Implement algorithms from scratch
- Understand how models learn from data
- Implement optimization techniques manually
- Compare implementations with established ML libraries
- Build a strong foundation for Deep Learning, Generative AI, and LLMs

---

## Algorithms

### 1. Linear Regression
- [ ] Simple Linear Regression
- [ ] Multiple Linear Regression
- [ ] Mean Squared Error
- [ ] Ordinary Least Squares
- [ ] Gradient Descent
- [ ] Batch Gradient Descent
- [ ] Stochastic Gradient Descent
- [ ] Mini-Batch Gradient Descent

### 2. Logistic Regression
- [ ] Sigmoid Function
- [ ] Binary Classification
- [ ] Binary Cross-Entropy Loss
- [ ] Gradient Descent
- [ ] Multiclass Logistic Regression

### 3. Regularization
- [ ] L1 Regularization
- [ ] L2 Regularization
- [ ] Elastic Net

### 4. k-Nearest Neighbors
- [ ] KNN Classification
- [ ] KNN Regression
- [ ] Distance Metrics

### 5. Naive Bayes
- [ ] Gaussian Naive Bayes
- [ ] Multinomial Naive Bayes
- [ ] Bernoulli Naive Bayes

### 6. Decision Trees
- [ ] Entropy
- [ ] Information Gain
- [ ] Gini Impurity
- [ ] Classification Tree
- [ ] Regression Tree

### 7. Ensemble Learning
- [ ] Random Forest
- [ ] Bagging
- [ ] AdaBoost
- [ ] Gradient Boosting
- [ ] XGBoost

### 8. Support Vector Machines
- [ ] Linear SVM
- [ ] Hinge Loss
- [ ] Kernel Trick
- [ ] Polynomial Kernel
- [ ] RBF Kernel

### 9. Clustering
- [ ] K-Means
- [ ] K-Means++
- [ ] Hierarchical Clustering
- [ ] DBSCAN
- [ ] Gaussian Mixture Models

### 10. Dimensionality Reduction
- [ ] Principal Component Analysis (PCA)
- [ ] Linear Discriminant Analysis (LDA)
- [ ] t-SNE

### 11. Model Optimization
- [ ] Gradient Descent
- [ ] Momentum
- [ ] RMSProp
- [ ] Adam
- [ ] Learning Rate Scheduling

### 12. Neural Networks
- [ ] Perceptron
- [ ] Activation Functions
- [ ] Forward Propagation
- [ ] Backpropagation
- [ ] Loss Functions
- [ ] Multilayer Perceptron
- [ ] Neural Network from Scratch

### 13. Convolutional Neural Networks
- [ ] Convolution
- [ ] Padding
- [ ] Stride
- [ ] Pooling
- [ ] CNN from Scratch

### 14. Recurrent Neural Networks
- [ ] Vanilla RNN
- [ ] Backpropagation Through Time
- [ ] LSTM
- [ ] GRU

### 15. Attention and Transformers
- [ ] Attention Mechanism
- [ ] Self-Attention
- [ ] Scaled Dot-Product Attention
- [ ] Multi-Head Attention
- [ ] Positional Encoding
- [ ] Transformer Encoder
- [ ] Transformer Decoder
- [ ] Transformer from Scratch

### 16. Generative Models
- [ ] Autoencoders
- [ ] Variational Autoencoders (VAE)
- [ ] Generative Adversarial Networks (GAN)
- [ ] GAN from Scratch

### 17. Natural Language Processing
- [ ] Bag of Words
- [ ] TF-IDF
- [ ] Word Embeddings
- [ ] Word2Vec
- [ ] Skip-Gram
- [ ] CBOW

### 18. Large Language Models
- [ ] Tokenization
- [ ] Byte Pair Encoding (BPE)
- [ ] Language Modeling
- [ ] Causal Language Modeling
- [ ] GPT Architecture
- [ ] GPT from Scratch
- [ ] Fine-Tuning
- [ ] LoRA
- [ ] Retrieval-Augmented Generation (RAG)

---

## Tools

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn (mainly for comparison and validation)
- PyTorch (for later deep learning implementations)

The core algorithms will be implemented manually wherever practical.

---

## Learning Approach

For every algorithm, the goal is to follow this process:

1. Understand the intuition
2. Understand the mathematics
3. Implement it from scratch
4. Test it on data
5. Visualize the results where useful
6. Compare it with a standard library implementation
7. Document what I learned

The purpose is not to recreate libraries such as Scikit-learn or PyTorch.

The purpose is to understand what happens underneath them.

---

## Structure

```text
ml-from-scratch/
│
├── linear-regression/
├── logistic-regression/
├── regularization/
├── knn/
├── naive-bayes/
├── decision-trees/
├── ensemble-learning/
├── svm/
├── clustering/
├── dimensionality-reduction/
├── optimization/
├── neural-networks/
├── cnn/
├── rnn/
├── transformers/
├── generative-models/
├── nlp/
└── llms/
