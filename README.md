# AI Podcast Content Assistant

A modular backend REST API built using Flask that generates podcast episode titles, captions, and hashtags.

##  Tech Stack
- Python
- Flask
- REST API Architecture
- Blueprint Routing
- App Factory Pattern
- Environment Configuration

##  Architecture Overview

- App Factory Pattern
- Blueprint-based routing
- Dedicated service layer for business logic
- Structured JSON responses
- Error handling and validation

##  API Endpoints

### Health Check
GET /health

### Generate Content
POST /generate

Request Body:
{
  "topic": "Men's Mental Health"
}

Response:
{
  "success": true,
  "data": {
    "title": "...",
    "caption": "...",
    "hashtags": [...]
  }
}

##  Run Locally

1. Clone repository
2. Create virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Run:
   python run.py

##  Future Improvements
- MySQL integration
- Real AI API integration
- Authentication layer
- Docker containerization