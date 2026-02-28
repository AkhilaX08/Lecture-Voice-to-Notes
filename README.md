Project Name – Lecture Voice-to-Notes Generator

# Lecture-Voice-to-Notes
Students struggle to take complete notes during lectures. This project converts lecture audio into text using AI speech-to-text, summarizes it into study notes, and generates quizzes & amp; flashcards using generative AI, all in an easy-to-use Streamlit web app.

## **Project Overview**

Students often struggle to take complete notes during lectures because it’s difficult to **listen and write at the same time**. This project solves that problem by using **AI-powered speech-to-text and generative AI** to automatically convert lecture audio into **concise study notes, quizzes, and flashcards**. It provides a **Streamlit web interface** for easy access and use.

---

## **Features**

* Converts lecture audio (mp3/wav) to text automatically
* Summarizes long lectures into **concise study notes**
* Generates **multiple-choice questions (MCQs), short-answer questions, and flashcards**
* User-friendly **web app interface using Streamlit**
* Supports future improvements like multilingual support, emotion detection, and PDF download

---

## **Technology Stack**

* **Frontend & Deployment:** Streamlit
* **Backend & AI Models:** Python, OpenAI Whisper, HuggingFace Transformers (T5/BART)
* **Libraries:**

  ```
  streamlit
  whisper
  transformers
  torch
  nltk
  scikit-learn (optional)
  ```
* **Python Version:** 3.13

---

## **System Requirements**

* Windows / Mac / Linux
* Python 3.10+ (tested on 3.13)
* Minimum 8GB RAM recommended for model inference
* Internet connection for deploying and using API calls (if using OpenAI models)

---

## **How It Works**

1. **Upload Lecture Audio** – User uploads audio in mp3 or wav format
2. **Speech-to-Text Conversion** – OpenAI Whisper transcribes the lecture into text
3. **Text Summarization** – Transformer models like T5/BART summarize long text into concise notes
4. **Quiz & Flashcard Generation** – Key points are converted into MCQs, short answers, and flashcards using generative AI
5. **Output Display** – Summarized notes and quizzes are displayed in the Streamlit web app

---

## **Installation Instructions**

1. Clone the repository:

   ```
   git clone https://github.com/AkhilaX08/Lecture-Voice-to-Notes.git
   ```
2. Navigate to the project folder:

   ```
   cd Lecture-Voice-to-Notes
   ```
3. Install required libraries:

   ```
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:

   ```
   streamlit run app.py
   ```

---

## **Deployment**

* This project can be deployed on **Streamlit Cloud**, **Render**, or **HuggingFace Spaces**.
* For easy capstone deployment, **Streamlit Cloud** is recommended:

  1. Push code to GitHub repository
  2. Connect GitHub repo in Streamlit Cloud
  3. Set `app.py` as the main file and click **Deploy**

---

## **Future Improvements**

* Multilingual lecture support
* Download notes as **PDF**
* Emotion detection from lecture voice
* User login system and personal study dashboard

---

## **Screenshots / Demo**

*(Add screenshots of your app here once deployed)*

---

## **References**

* [OpenAI Whisper](https://github.com/openai/whisper) – Speech-to-Text
* [HuggingFace Transformers](https://huggingface.co/transformers/) – Summarization models (T5/BART)
* [Streamlit](https://streamlit.io/) – Web app framework

---

## **Contact**

* Developed by: **Akhila X**
* GitHub: [https://github.com/AkhilaX08](https://github.com/AkhilaX08)



Features – Key points:

Converts lecture audio to text

Summarizes into notes

Generates quizzes & flashcards

Tech Stack – Python, Streamlit, Whisper, Transformers

How to Run –

Install requirements: pip install -r requirements.txt

Run app: streamlit run app.py
