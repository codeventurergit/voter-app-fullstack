# voter-app-fullstack

A full-stack data-driven application designed to analyze and manage voter registration data. This project showcases a modern serverless architecture built with Python and services are deployed to AWS using SAM Configuration as Code. The frontend demo link is hosted on Vercel.  The backend demo links are hosted on Render.

## 🚀 Tech Stack
- **Frontend:** React with TypeScript (Modern UI/UX)
- **Backend:** Python (AWS Lambda)
- **Infrastructure:** AWS SAM (Serverless Application Model)
- **Database:** Amazon DynamoDB (NoSQL)
- **CI/CD:** Git/GitHub

## 🏗️ Architecture

The application uses a serverless backend. AWS Lambda handles the business logic and data manipulation, which is exposed via an Amazon API Gateway to the React frontend.
This project is built using a modern, scalable stack:

*   **Frontend:** React.js (Data Visualization & Insights Dashboard)
*   **Backend:** FastAPI (Python) - High-performance asynchronous API
*   **Database:** AWS DynamoDB (NoSQL) - Scalable cloud storage
*   **Deployment:** Render (Automated CI/CD)
*   **Integration:** Boto3 for secure AWS SDK communication

  ## 🛠️ Project Structure
- `backend/`: Contains the Lambda function logic and data seeding scripts.
- `frontend/`: React application (Integrated via API).
- `template.yaml`: AWS SAM infrastructure-as-code definition.

## 🚀 Live Demo & Technical Review

Because this demo is hosted on a free-tier environment, the services may "sleep" during periods of inactivity. Please follow these steps for the best experience:

### 1. Initialize the Environment (Warm-Up)
**Click here first:** https://voter-insights-backend.onrender.com 
*If the page takes ~30 seconds to load, the server is spinning up. Once you see the "API is live" message, the system is fully operational.*

### 2. Explore the Implementation
*   **Interactive API Docs (Swagger):** https://voter-insights-backend.onrender.com//docs  
    *Use this to test the strategy engine directly. You can enter any Voter ID (e.g., `V-1001`) in the POST endpoint to see the logic generate a unique insight about a voter.*
*   **Insights Dashboard:**  https://voter-app-fullstack-riyrdi046-codeventurergits-projects.vercel.app/
    *View the real-time visualization of voter demographics and interests.*

### 3. Data Resilience (Optional)
If the dashboard appears empty, I have provided a utility endpoint to re-seed the live database:
1. Navigate to the **Swagger UI** link above.
2. Locate the `POST /dev/seed` endpoint.
3. Click **"Try it out"** and then **"Execute"**. This will populate your session with 50 unique AWS DynamoDB records.

## 🧠 Core Features & Design Patterns

*   **Deterministic Strategy Mapping:** The backend utilizes a seed-based logic to ensure unique, repeatable insights for every voter ID, demonstrating how business logic can be applied to raw data.
*   **Graceful Degradation:** The system is architected to handle arbitrary inputs, providing generated fallback strategies to ensure a seamless user experience even for new data points.
*   **Security & Identity:** Utilizes AWS IAM (Identity and Access Management) for secure, programmatic access to cloud resources.
*   **CORS-Enabled Architecture:** Configured for secure cross-origin communication between disparate frontend and backend hosting environments.

## 🛠️ Local Development

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Configure AWS Credentials in your environment variables.
4. Run the development server: `uvicorn main:app --reload`
