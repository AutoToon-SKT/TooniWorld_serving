from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI



app = FastAPI()


class AllStoryRequest(BaseModel):
    allStory: str

@app.post("/{userId}/{infoId}/allstory")
def read_item(userId: int, infoId: int, request: AllStoryRequest):  
    print("userId " + str(userId))  
    print("infoId " + str(infoId))  
    print("allStory " + request.allStory)
    return {"userId": userId, "infoId": infoId, "allStory": request.allStory}



