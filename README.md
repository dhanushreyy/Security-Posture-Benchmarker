# Security Posture Benchmarker

A full-stack security assessment platform developed during my AI Developer Internship at CampusPe. The application analyzes system security posture, generates benchmark reports, and leverages Large Language Models (LLMs) to provide intelligent security recommendations.

## Overview

Security Posture Benchmarker evaluates security configurations and generates detailed reports with AI-assisted insights. The platform combines backend security analysis with LLM-powered recommendations to help identify vulnerabilities and improve overall security posture.

## Features

- Security posture analysis
- AI-generated vulnerability descriptions
- Intelligent security recommendations
- Security benchmark reporting
- REST API integration
- Input validation and security checks
- Rate limiting for API protection

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask
- REST APIs

### AI
- Groq API
- LLaMA
- Prompt Engineering

### DevOps
- Docker
- Docker Compose

## Project Structure

```
security-posture-benchmarker/
├── ai-service/
├── backend/
├── frontend/
├── docker-compose.yml
├── SECURITY.md
└── README.md
```

## Getting Started

### Clone the repository

```bash
git clone https://github.com/dhanushreyy/Security-Posture-Benchmarker.git
cd Security-Posture-Benchmarker
```

### Install dependencies

Install the required Python packages for the backend and AI service.

### Configure Environment Variables

Create a `.env` file and add the required API keys and configuration values.

### Run the Application

```bash
docker-compose up --build
```

Or start each service individually based on your development setup.

## Key Contributions

- Developed AI-powered microservices using Flask.
- Integrated Groq (LLaMA) APIs for automated security analysis.
- Designed prompt templates to improve the quality and consistency of AI-generated recommendations.
- Implemented input validation, rate limiting, and security protections.
- Collaborated on backend integration, debugging, and application improvements.

## Future Improvements

- User authentication
- Historical assessment reports
- PDF report generation
- Additional security benchmarks
- Cloud deployment

## License

This project is shared for educational and portfolio purposes.
