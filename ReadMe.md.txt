# 🤖 AI Multimodal Customer Support Chatbot

## 📌 Project Overview

This project is an advanced **AI-powered customer support chatbot** built during my internship. It combines multiple AI capabilities such as:

* Question Answering (Q&A)
* Image-based understanding
* Medical RAG (Retrieval-Augmented Generation)
* PDF document understanding
* Sentiment Analysis
* Multilingual communication

The chatbot is designed to simulate real-world intelligent customer support systems.

---

## 🎯 Objectives

* Build a smart chatbot using AI/ML techniques
* Enhance chatbot with multiple real-world capabilities
* Improve user experience using sentiment-aware responses
* Enable multilingual support
* Implement document-based question answering

---

## 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* FAISS
* Google Gemini API
* NLP (Natural Language Processing)

---

## 🚀 Features / Tasks Implemented

### ✅ Task 1: Basic Q&A Chatbot

* Answers general user queries

### ✅ Task 2: Image-based Chatbot

* Understands and responds based on images

### ✅ Task 3: Medical RAG Chatbot

* Uses medical dataset (MedQuAD)
* Retrieves accurate answers using vector search

### ✅ Task 4: PDF Q&A Chatbot

* Reads PDF documents
* Answers questions from uploaded files

### ✅ Task 5: Sentiment Analysis Chatbot

* Detects user sentiment (Positive/Negative/Neutral)
* Responds accordingly

### ✅ Task 6: Multilingual Chatbot

* Supports multiple languages
* Automatically detects user language

---

## 📂 Project Structure

```
AI-Multimodal-Customer-Support-Chatbot
│
├── src
├── data
├── images
│   ├── 1.chatbot_Interface.png
│   ├── 2.multimodel_chatbot Output.png
│   ├── 2.1 Multimodel_chatbot Image_based Output.png
│   ├── 2.2 Chatbot_image_based Output.png
│   ├── 3. Medical_chatbot_Output.png
│   ├── 4. Pdf_Chatbot_Output.png
│   ├── 5. Sentiment_Output.pdf
│   └── 6. Multilingual_Output.pdf
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### Step 1: Clone Repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Step 2: Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```
pip install -r requirements.txt
```

### Step 4: Run Chatbots

```
streamlit run src/qa_chatbot.py
streamlit run src/image_chatbot.py
streamlit run src/medical_rag_chatbot.py
streamlit run src/pdf_qa_chatbot.py
streamlit run src/sentiment_chatbot.py
streamlit run src/multilingual_chatbot.py
```

---

## 🔑 Environment Variables

Create a `.env` file and add your API key:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## 📊 Project Demonstration

### 🧠 Chatbot Interface

![Chatbot Interface](images/1.chatbot_Interface.png)

---

### 🤖 Multimodal Chatbot Output

![Multimodal Chatbot](images/2.multimodel_chatbot Output.png)

---

### 🖼️ Image-based Chatbot

![Image Chatbot](images/2.1 Multimodel_chatbot Image_based Output.png)

![Image Chatbot Output](images/2.2 Chatbot_image_based Output.png)

---

### 🏥 Medical Chatbot (RAG)

![Medical Chatbot](images/3. Medical_chatbot_Output.png)

---

### 📄 PDF Chatbot

![Chatbot](images/4. Pdf_Chatbot_Output.png)

---

### 😊 Sentiment Analysis Output

![Sentiment Output](images/5. Sentiment_Output.pdf)

---

### 🌍 Multilingual Chatbot Output

![Multilingual Output](images/6. Multilingual_Output.pdf)

---

## 📈 Results

* Successfully implemented all 6 chatbot features
* Achieved accurate responses using RAG approach
* Improved interaction using sentiment detection
* Enabled multilingual communication

---

## 💡 Future Improvements

* Add voice-based interaction
* Deploy chatbot on cloud
* Improve UI/UX
* Add more datasets for better accuracy

---

## 👨‍💻 Author

**Dipesh Dubey**
BSc Computer Science | Aspiring Data Scientist

---

## ⭐ Conclusion

This project demonstrates the integration of multiple AI technologies into a single chatbot system, making it more intelligent, interactive, and practical for real-world applications.
