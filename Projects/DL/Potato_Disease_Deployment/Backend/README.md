# Requirements
tensorflow==2.5.0
fastapi
uvicorn
python-multipart
pillow
tensorflow-serving-api==2.5.0
matplotlib
numpy

# Running FAST API .py file
uvicorn main:app --reload


# Setting up pip3 and python 
using virtual environment
- python3 -m venv venv
- source venv/bin/activate

# Loading Model 
- Step1: direct.py file mein tf.load_model(path) keras model loaded 
    - use model.predict fucntion
-Step2: tf serving -> model -> docker run and create a Ednpoint for predciting
    - use response.endpoint call to get response from docker tf _serving port
    - docker run --platform=linux/amd64 -t --rm -p 8501:8501 \
  -v "/Users/shubhamkeshari/Documents/ML_DL_AI/ML_With_Python_GoogleColab/Projects/DL/API Backend/potatoModel:/models/potato_model" \
  -e MODEL_NAME=potato_model \
  tensorflow/serving