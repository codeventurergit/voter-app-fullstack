# voter-app-fullstackgi

A full-stack data-driven application designed to analyze and manage voter registration data. This project showcases a modern serverless architecture built with Python and AWS.

## 🚀 Tech Stack
- **Frontend:** React with TypeScript (Modern UI/UX)
- **Backend:** Python (AWS Lambda)
- **Infrastructure:** AWS SAM (Serverless Application Model)
- **Database:** Amazon DynamoDB (NoSQL)
- **CI/CD:** Git/GitHub

## 🏗️ Architecture
The application uses a serverless backend. AWS Lambda handles the business logic and data manipulation, which is exposed via an Amazon API Gateway to the React frontend.

## 🛠️ Project Structure
- `backend/`: Contains the Lambda function logic and data seeding scripts.
- `frontend/`: React application (Integrated via API).
- `template.yaml`: AWS SAM infrastructure-as-code definition.

## 🚦 Getting Started
1. **Build the backend:** `sam build`
2. **Deploy to AWS:** `sam deploy --guided`
3. **Seed the database:** `python backend/scripts/seed_db.py`