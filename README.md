# Simple FastAPI Project

This is a minimal FastAPI application you can run locally or containerize for AWS (ECS/App Runner/Elastic Beanstalk).

## Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

Run the server:
```
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000 (docs: /docs).

## API Endpoints

- GET /healthz : Health check (returns {"status":"ok"})
- GET / : Returns {"hello": "world"}
- GET /items/{item_id} : Returns item details
- GET /login : HTML login page (template)
- POST /login : Form submit (try admin/admin)

## Docker (easy for AWS)

Build and run:
```
docker build -t fastapi-sample .
docker run --rm -p 8000:8000 fastapi-sample
```

Then push the image to ECR and run it on ECS/Fargate or App Runner.
