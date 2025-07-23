Cloud Functions and S3 Bucket For Deployment


# 🚀 Deploy Keras `.h5` Model on Google Cloud Functions

This guide explains how to deploy a Keras model as a serverless API using Google Cloud Functions and load the model from Google Cloud Storage.

---

## ✅ Steps to Deploy

### 1. **Prepare Your Project**
- Create a folder with:
  - `main.py` containing your prediction logic.
  - `requirements.txt` listing dependencies.

### 2. **Upload the Model to Cloud Storage**
- Create a GCS bucket.
- Upload your `.h5` model to the bucket (e.g., `gs://your-bucket/models/model.h5`).

### 3. **Grant Permissions**
- Ensure the Cloud Function's service account has `Storage Object Viewer` permission for the bucket.

### 4. **Write Cloud Function Logic**
- In `main.py`, write a function that:
  - Loads the model from GCS (once on cold start).
  - Accepts HTTP POST requests.
  - Returns predictions as JSON.

### 5. **Add Dependencies**
- List required packages in `requirements.txt` (e.g., `tensorflow`, `flask`, `google-cloud-storage`, `numpy`).

### 6. **Deploy the Function**
- Use `gcloud` CLI to deploy your function with HTTP trigger and proper entry point.

### 7. **Test the API**
- Send POST requests with JSON input to your function’s public URL.

### 8. **(Optional) Secure the API**
- Disable unauthenticated access or use an API Gateway/IAM-based access control.

---

## 📌 Notes
- Cloud Functions have a 100MB zipped deployment size limit—load large models from GCS.
- Cloud Functions reuse instances, so loading the model globally is efficient.
