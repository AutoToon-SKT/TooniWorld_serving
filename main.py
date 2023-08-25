from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

import uvicorn

app = FastAPI()


class AllStoryRequest(BaseModel):
    allStory: str

@app.post("/{userId}/{infoId}/allstory")
def read_item(userId: int, infoId: int, request: AllStoryRequest):  
    print("userId " + str(userId))  
    print("infoId " + str(infoId))  
    print("allStory " + request.allStory)
    return {"userId": userId, "infoId": infoId, "allStory": request.allStory}



if __name__ == '__main__':
    app_str = 'main:app'
    uvicorn.run(app_str, host='0.0.0.0', port=8000, reload=True, workers=1)