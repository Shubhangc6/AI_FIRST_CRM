# 🤖 AI First CRM

An AI-powered Customer Relationship Management (CRM) application built using modern frontend, backend, and LangGraph-based AI tools. The application helps manage customer information, automate CRM workflows, and provide intelligent assistance through AI agents.

---

# 📌 Project Overview

AI First CRM is designed to simplify customer relationship management by combining traditional CRM features with AI-powered automation.

The system provides:

- Customer management
- Lead tracking
- AI-powered assistance
- Automated CRM workflows
- Intelligent data handling
- Interactive user interface

The project contains:

- Frontend application for user interaction
- Backend API for business logic
- LangGraph AI agent with multiple tools for automation

---

# 🏗️ Project Architecture


AI_FIRST_CRM
│
├── frontend
│ ├── Components
│ ├── Pages
│ ├── Services
│ └── UI Components
│
├── backend
│ ├── app
│ │ ├── config.py
│ │ ├── database.py
│ │ ├── models
│ │ ├── routes
│ │ ├── services
│ │ └── langgraph
│ │
│ ├── requirements.txt
│ └── main.py
│
├── .gitignore
└── README.md


---

# 🚀 Features

## Frontend Features

- User-friendly CRM dashboard
- Customer information management
- Lead management interface
- API integration with backend
- Responsive UI design


## Backend Features

- REST API services
- Database integration
- Customer CRUD operations
- Authentication handling
- AI agent integration


## AI Features (LangGraph)

The project uses LangGraph to create an AI workflow agent with multiple tools.

Implemented tools:

### 1. Customer Search Tool

- Searches customer information from the database
- Retrieves customer details based on user queries


### 2. Customer Creation Tool

- Creates new customer records
- Saves customer details into the database


### 3. Customer Update Tool

- Updates existing customer information
- Modifies customer records dynamically


### 4. Customer Delete Tool

- Removes customer records safely
- Handles deletion requests through AI workflow


### 5. Customer Analytics Tool

- Provides customer-related insights
- Generates useful summaries from CRM data


---

# 🛠️ Technology Stack

## Frontend

- React.js
- JavaScript
- HTML5
- CSS3

## Backend

- Python
- FastAPI / Flask
- REST APIs
- SQL Database

## AI Framework

- LangGraph
- LangChain
- LLM Integration

## Database

- MySQL / SQLite

## Development Tools

- GitHub
- VS Code
- Postman

---

# ⚙️ Installation Guide

## Step 1: Clone Repository

```bash
git clone https://github.com/Shubhangc6/AI_FIRST_CRM.git

cd AI_FIRST_CRM