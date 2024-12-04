# Website Categorization Using an RNN

This project implements a **Recurrent Neural Network (RNN)** to classify websites into predefined categories based on their content. The primary workflow involves fetching the title of a webpage from its URL, processing it, and predicting its category using a pre-trained model.

---

## Features

### 1. **RNN-based Classification**
   - Utilizes an RNN with pre-trained embeddings for efficient and accurate text categorization.

### 2. **HTML Parsing**
   - Automatically fetches and processes webpage titles using the **BeautifulSoup** library.

### 3. **Imbalanced Dataset Handling**
   - Balances training data for top categories to improve model generalization.

### 4. **Pre-trained Embeddings**
   - Leverages **GloVe embeddings** for enhanced word representation.

### 5. **Transfer Learning**
   - Fine-tuned for better performance on the provided dataset.

---

For a detailed walkthrough, check out the full article on Medium:  
[**Website Classifier using RNN**](https://medium.com/pythoneers/rnn-project-website-classifier-51ddd8ea29af)
