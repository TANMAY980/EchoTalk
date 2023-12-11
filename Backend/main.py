#uvicorn main:app
#uvicorn main:app --reload

#importing main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

#Custom function imports
#...
from functions.Database import store_messages,reset_messages
from functions.openai_requests import convert_audio_to_text,get_chat_response
from functions.text_to_speech import convert_text_to_speech

#Initate
app = FastAPI()


#CORS-ORIGINS

origins=[
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]

#CORS-Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Check Health

@app.get("/health")
async def root():
    print("tanmay")
    return {"message": "Healthy"}

#reset message

@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "conversation reset"}

#get audio

@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

    #get saved audio
    #audio_input=open("TanmayVoice.mp3","rb")

    #save file from frontend
    with open(file.filename,"wb") as buffer:
        buffer.write(file.file.read())

    audio_input=open(file.filename,"rb")

    #decode audio
    message_decoded=convert_audio_to_text(audio_input)
    
    #gurd: Ensure message decoded
    
    if not message_decoded:
        return HTTPException(status_code=400 ,detail="Failed to decode audio")
    
    #get chatGpt response which is string
    chat_response=get_chat_response(message_decoded)

    #gurd: Ensure message decoded
    
    if not chat_response:
        return HTTPException(status_code=400 ,detail="Failed to get chat response")

    #store messages

    store_messages(message_decoded,chat_response)

    #convert chat response to audio
    print(chat_response)
    audio_output=convert_text_to_speech(chat_response)

    #gurd: Ensure message decoded
    
    if not audio_output:
        return HTTPException(status_code=400 ,detail="Failed to get Eleven labs audio response")
    
    #create a generater that yields chunk of data
    def iterfile():
        yield audio_output
    #return the audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream")
 




#post bot response
#not playing in browser when using post request
#@app.post("/post-audio/")
#async def post_audio(file: UploadFile = File(...)):
#    print("hello")