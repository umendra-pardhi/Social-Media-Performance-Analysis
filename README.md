# 🤖 Social Media Analyzer AI

A pre-hackathon assignment project that analyzes social media engagement data using Langflow and DataStax Astra DB. The project provides insights on post performance across different content types using AI-powered analysis.

## 🎯 Project Overview

This project was developed as part of a pre-hackathon assignment to demonstrate the integration of:
- DataStax Astra DB for data storage
- Langflow for workflow creation
- Groq's Llama-3.1-8b-instant model for generating insights
- Flask for the web application backend

## 🚀 Features

- Fetches and analyzes engagement data from mock social media accounts
- Processes different post types (carousel, reels, static images, stories, IGTV)
- Calculates average engagement metrics for each post type
- Generates AI-powered insights using Llama-3.1-8b-instant model
- Provides a web interface for interaction

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Database**: DataStax Astra DB
- **AI/ML**: Langflow, Groq Llama-3.1-8b-instant
- **Data Generation**: Custom Python script for mock data

## 📊 Data Structure

The project analyzes the following engagement metrics:
- Impressions
- Reach
- Likes
- Comments
- Shares
- Saves
- Engagement Rate

## 🔧 Setup and Installation

1. Clone the repository
```bash
git clone https://github.com/umendra-pardhi/Social-Media-Performance-Analysis.git
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Set up environment variables Create a .env file with:
```bash
LANGFLOW_TOKEN=[Your_Langflow_Token]
```
4. Run the application
```bash
python app.py
```

## 📝 API Endpoints

### Home Route
- `GET /`: Renders the main application interface

### Analysis Route
- `POST /analyze`: 
  - Accepts content for analysis
  - Returns AI-generated insights using Llama model
  - Payload format: `{"content": "user_prompt_here"}`

## 🤝 Contributing

This project is part of a pre-hackathon assignment and was completed as per the specified requirements. Feel free to fork and modify according to your needs.

