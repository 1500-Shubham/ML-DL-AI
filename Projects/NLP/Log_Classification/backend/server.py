import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
import io
from classify import classify

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Log Classification API"}

@app.post("/classify/")
async def classify_logs(file: UploadFile):

    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV.")
    
    try:
        # Read the uploaded CSV
        df = pd.read_csv(file.file)
        if "source" not in df.columns or "log_message" not in df.columns:
            raise HTTPException(status_code=400, detail="CSV must contain 'source' and 'log_message' columns.")

        # Perform classification
        predicted_lables = classify(list(zip(df["source"], df["log_message"])))
        df["target_label"] = predicted_lables
        print("Dataframe:",df.to_dict())

        output_file = "/Users/shubhamkeshari/Documents/ML_DL_AI/ML-DL-AI/Projects/NLP/Log_Classification/backend/outputAPICall.csv"
        df.to_csv(output_file, index=False)
        print("File saved to output.csv")
        return FileResponse(output_file, media_type='text/csv')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))