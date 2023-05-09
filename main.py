from ultralytics import YOLO
from PIL import Image
import cv2
from fastapi import FastAPI
import json
import uvicorn


app = FastAPI()

@app.get('/inference')
async def get_inference():
	model = YOLO('yolov8n.pt')
	results = model('test.jpg')

	return {"inference was succesful!"}
	
@app.get('/')
async def get_index():
	return {"Hello"}

if __name__ == '__main__':
	uvicorn.run("main:app", port=9000, log_level="info")
