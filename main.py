# Import necessary libraries
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from random import randint
import uuid


# Initialize FastAPI application
app = FastAPI()


# Define a POST endpoint for file upload
@app.post("/upload/")
async def create_upload_file():
