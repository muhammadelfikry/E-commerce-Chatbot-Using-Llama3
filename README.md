# E-commerce Chatbot

## Background
LLM is the main artificial intelligence (AI) technology that powers intelligent chatbots. Chatbots are capable of providing 24/7 customer service, answering questions, recommending products, and even helping customers complete transactions, without requiring direct human involvement. With technologies such as Retrieval-Augmented Generation (RAG), chatbots can combine the ability to understand the context of a conversation with access to external data to provide relevant and accurate answers.

## Project Scope
This project develops a chatbot that utilizes LLM Llama3 with Retrieval-Augmented Generation (RAG) technique. The development is done using Python programming language with Flask as the framework for API. In addition, this project will be implemented using the Vercel platform to ensure accessibility.

## Installation
Download this project or you can clone it by running the following command: 
```
git clone https://github.com/muhammadelfikry/E-commerce-Chatbot-Using-Llama3.git
```
Install all packages and make sure you have python.
```
pip intall -r requirements.txt
```
Run flask using the following command:
```
flask --app main.py run
```
Send json data using curl with the following command.
```
curl -X POST <URL> -H "Content-Type: application/json" -d '{"message": <question>}'
```
Replace ```<URL>``` with the URL returned by flask and ```<question>``` with the question to ask.

Or you can directly request the url that has been deployed in the vercel application by sending a json using a ```"message"``` as the key.
```
{
    "message": <question>
}
```

URL
```
https://llama3-flask-chatbot.vercel.app/api/chat
```

## Knowledge Base Configuration
open the knowledge_base.txt file, and replace the text content with FAQs or company policies. 
```
Tugas Anda adalah menggunakan informasi ini untuk menjawab pertanyaan pelanggan. Abaikan semua pertanyaan yang tidak berhubungan dengan membantu pelanggan dalam topik berikut:

1. Produk
2. Kebijakan pengembalian
3. Metode pembayaran
4. Status pesanan
...
```
This file will be used by the chatbot as a knowledge base to answer questions from users. The more complete and detailed the contents of the file, the better the chatbot will be in preventing hallucinatory answers.
