# Echo
Echo ChatGpt AI voice chatbot using OpenAi Chat model-gpt-3.5-turbo  Audio model-whisper-1  text-to-speech-Elevenlabs Rachel AI voice 
#full architecture of the project

![full application Architecture](https://github.com/TANMAY980/EchoTalk/assets/65010491/83bdbcde-786e-4428-9285-bf4805912bd5)
#sending my voice to openai whisper-1 to decode voice in text
![voice to whisper-1](https://github.com/TANMAY980/EchoTalk/assets/65010491/8da9daa6-f78c-4b85-9457-4a4858f773ac)

#sending post request through fasapi
![sending post request through fasapi](https://github.com/TANMAY980/EchoTalk/assets/65010491/fc212ba4-99cb-42f7-9378-adc91d3fde49)
#getting succesfully response
![getting succesfully response](https://github.com/TANMAY980/EchoTalk/assets/65010491/a2496a8a-9752-473d-b79b-88a8a1765a1a)

#usage of openai whisper after sending audio file and giving back response
![usage of whisper](https://github.com/TANMAY980/EchoTalk/assets/65010491/0cf23ad0-bc79-4953-a7c9-69b98d6a97ff)
#caution- in these screenshot you might see the name of the voice Ai chatbot is different during development time i set the name of the chatbot is EchoTalk and after development while testing faces some issue with the name during testing like when i say EchoTalk Whisper consfused with pronunciation so i changed it to Echo light word with clear pronunciaton althoug here also i m getting issue with the name but it recognize few times
you can see it's correct me by saying "I am EchoTalk" currently i am getting response as a text not audio we can see in commandline
![response from whisper](https://github.com/TANMAY980/EchoTalk/assets/65010491/bf119425-1f14-470d-9c5c-216ed97915cb)
#in fastapi document which is builtin in fasiapi here we can see the audio file 
![audio in fastapidoc](https://github.com/TANMAY980/EchoTalk/assets/65010491/bff02b71-8b5c-4bc2-a46d-9d540c367cc1)

#all the responses from eleven labs text to speech
![elvenlabs text voice to](https://github.com/TANMAY980/EchoTalk/assets/65010491/ef11672c-4351-4f1d-8fc0-153223729b6e)
#complete frontend ui
before starting the conversation we can see there is a message bouncing ask echo with your voice and in the background json file there is no messages stored. and recoding status showing idle
![Screenshot (482)](https://github.com/TANMAY980/EchoTalk/assets/65010491/5f8cc2e3-6399-4d3a-a052-e76ca712198f)
#now after my voice recorded it send to the backend it is showing that let me answer your question and recording button status showing stopped.you can see that stored_message.json file is empty because there is no message at this point
![Screenshot (483)](https://github.com/TANMAY980/EchoTalk/assets/65010491/ca3a065a-35e1-42db-8c2b-553c866504db)
#after record  pass to the backend and message stored into the database file the we getting the audio file in the frontent we can play and download our audio file we have now both audio file mine and echo voice audio file and echo's reply is automatically being played as a response 
![Screenshot (485)](https://github.com/TANMAY980/EchoTalk/assets/65010491/c5bf8400-1cfa-435b-8df9-d88043af8abb)

#now further conversation we can see all the conversation using scroll down and up
![Screenshot (486)](https://github.com/TANMAY980/EchoTalk/assets/65010491/eb318ad5-22be-457e-9d78-0aefd9b9143d)
#now we have reset our messages
before reseting our database file
![Screenshot (478)](https://github.com/TANMAY980/EchoTalk/assets/65010491/0526c45c-0f58-4e4b-8f68-24c3461d85bc)
while reseting
![Screenshot (479)](https://github.com/TANMAY980/EchoTalk/assets/65010491/19ab91fd-ddb3-42ed-9087-8b9c8726ba4c)
#frontend view after reseting the chat 
![Screenshot (480)](https://github.com/TANMAY980/EchoTalk/assets/65010491/080a091d-9bb3-4ab8-a42b-caeac7b877f7)
#after reseting the chat stored_data.json file
![Screenshot (481)](https://github.com/TANMAY980/EchoTalk/assets/65010491/4e9d1d3b-0658-4bb2-a46c-cc5f7b0ac974)



![Screenshot (487)](https://github.com/TANMAY980/EchoTalk/assets/65010491/634734bf-774e-4a3b-9fc9-e12b6c0a56e8)





Backend
Technologies-python,FastApi,chatGpt model,elvenLabs
steps in Backend-
Imports
CORS-cross origin resource sharing frontend to Backend
Health Entrypoint-
    API Route EndPoint
    1)save the audio input
    2)convert audio to text
    3)get chatbot response
    4)add to chat history
    5)convert text to speech
![Backend](https://github.com/TANMAY980/EchoTalk/assets/65010491/904e227f-f4e7-4558-9cea-727e29e9b2b4)

#Extentions
Auto Close Tag, Auto Rename Tage, ES7-React/redux snippets(for creating react function), isort, prettier-code formatter,Python,Tailwind Css intellisense(suggesting of color and code),Pylance 

#Folder Setup
Create a folder with name mine is EchoTalk and inside create two folder Frontend,Backend

#verify Your installation 
open your cmd  and type python --version or python3 --version (required python 3.6.6 or above) and install python package manager by using
py -m ensurepip --upgrade or py get-pip.py if you have pip then check the version pip3 --version or pip --version
check Node version  node --version use semi-recent version of node
we need yarn check the version opf the yarn --version we can install npm install --global yarn 
Ts-node install using npm i -g ts-node if we @version we can get the exact version (type script node) can check using ts-node --version

#information about npm npx yarn
npm is the default package manager for Node. js, npx allows running packages without installation, and Yarn provides enhanced performance and additional features compared to npm.

#install the packages for Backend (Python,FastApi)
so change the folder to the Backend and create Python virtual environment  (python3 or python -m venv venv) it will create the venv folder inside Backend folder now activate the virtual environment makesure you are inside in Backend folder in windows use (venv\scripts\activate)
command to activate the virtual environment

install openAi package using pip3 install openAi==0.27.0
pip3 install python-decouple==3.8 python-multipart==0.0.6 requests==2.28.2 fastapi==0.92.0
install uvicorn using pip3 install "uvicorn[standard]" to work as the server. https://fastapi.tiangolo.com/tutorial/
create main.py by using echo>main.py in windows
copy the code which is given https://fastapi.tiangolo.com/tutorial/first-steps/ and paste it main.py
from fastapi import FastAPI

#main.py 
allow us to check that Everything has installed and is working for the fastapi

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

to check run uvicorn main:app --reload (--reload for developing  it means detected changes so if i running this in a production env or hosting we would run uvicorn main:app) we will see
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
in localhost:8000 {'message':'Hello World'} that means everything is working fine.

#Frontend JSON Script
{
  "name": "frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "start": "vite preview"
  },
  "dependencies": {
    "axios": "^1.3.4",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-media-recorder": "^1.6.6"
  },
  "devDependencies": {
    "@types/react": "^18.0.27",
    "@types/react-dom": "^18.0.10",
    "@vitejs/plugin-react": "^3.1.0",
    "autoprefixer": "^10.4.13",
    "postcss": "^8.4.21",
    "tailwindcss": "^3.2.7",
    "typescript": "^4.9.3",
    "vite": "^4.1.0"
  }
}
#React Frontend preparation and package installation
creating React project swith to the frontend folder 
npx create-vite . (vite is builder (.) is in the directory)
select framework React and select Typescript
installing all the packages which is presented in package.json folder using yarn --exact
to test run yarn dev we will get http://localhost:5137/

#Tailwind  css integration(https://tailwindcss.com/docs/guides/vite)
npx tailwindcss init -p it will create tailwind.config.cjs and in this file replace the content with
 content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],

under src folder goto index.css add  at the top
@tailwind base;
@tailwind components;
@tailwind utilities;
remove everything except body

go to the App.tsx remove extra div tag
function App() {

  return (
  
      <div className="">
       Hello
      </div>
  );
}

export default App
build using yarn build then yarn start for not dev mode its production mode
http:\\localhost:4137\

#Set The API key
#CAUTION

Eleven Labs: https://beta.elevenlabs.io/subscription

Click on profile image > Profile

Open AI API Key: https://platform.openai.com/account/api-keys

Just create a key and copy it
Open AI Org: https://platform.openai.com/account/org-settings

Just copy your org id

#Setting Env Variables(it's way to keep secret key and private things to private so people can't access 
creating .env file using echo>.env in Backend
open .env file create varable
OPEN_AI_API_KEY=enter you key
OPEN_AI_ORG_KEY=enter you key
ELEVEN_LABS_KEY=enter you key

Backend
steps in Backend-
Imports-
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config(this going to allow us to bring in the environment variable that we saved in the environment setup
import openai

#Initate
app = FastAPI()

CORS-CORS is a node. js package for providing a Connect/Express middleware that can be used to enable CORS with various options.cross origin resource sharing frontend to Backend (what app going to allow we have backend running on DomainApi.com need to accept any request from echo.com this is where we can
dictate what domain urls you will accept in your backend)
origins=[
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]
#CORS-Middleware- This middleware provides a comprehensive, configurable implementation of the CORS (Cross Origin Resource Sharing) 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, (allow originis that allow origins)
    allow_credentials=True,(allowing credentials by setting True)
    allow_methods=["*"],(allowing all methods using *)
    allow_headers=["*"],(allowing all headers using *)
)

Health Entrypoint-
    API Route EndPoint
    1)save the audio input
    2)convert audio to text
    3)get chatbot response
    4)add to chat history
    5)convert text to speech

#About Docs and Endpoints
FastApi Provides built in documentation
test our endpoint using Documentation which is provided by Fastapi i dont have to write any API Documentation
main endpoint sending a post request from react application (PostEndpoint) sending an audio file with data to an endpoint not playing the audio in the Browser in POST endpoint

@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)): (sending file into the Fastapi on the Backend)


#convert Voice to Text with Whisper
create a function in functions folder in Backend

import openai
from decouple import config
#Retrieve ENV variables
openai.organization=config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

#open_ai -whisper
#convert audio to text

def convert_audio_to_text(audio_file):
    try:
        transcript=openai.Audio.transcribe("whisper-1",audio_file) 
        message_text=transcript["text"](returning the result of transcript as text object)
        return message_text
    except Exception as e:
        print(e)
        return
        
transcript=openai.Audio.transcribe("whisper-1",audio_file) 

openai: This is likely an instance of the OpenAI Python library. The library provides a convenient way to interact with OpenAI's APIs.

Audio.transcribe: This is a method or function provided by the OpenAI library for transcribing audio. It's used to convert spoken language in the audio file into text.

"whisper-1": This is the model identifier or name. In this case, it appears to be using a model called "whisper-1." Models in the OpenAI API often have specific characteristics or are trained for certain tasks.

audio_file: This is the path or content of the audio file that you want to transcribe. It could be a local file path or the actual audio content.

The purpose of this code is to transcribe the speech from the given audio file using the specified OpenAI model ("whisper-1"). The transcribed text is the output of this operation and can be used for various natural language processing tasks or applications where you need the spoken content converted into written text.

now import this function in main.py
from functions.openai_requests import convert_audio_to_text,get_chat_response

@app.post("/post-audio-get/")
async def post_audio(file: UploadFile = File(...)):

#get saved audio
    audio_input=open("TanmayVoice.mp3","rb")

#decode audio
    message_decoded=convert_audio_to_text(audio_input)


convert_audio_to_text(audio_input)

so above the function we open the audio input and read it as read bytes and calling the function with the audio input and passing to the whisper-1 and as a result we return the text as object we are geting the output as a text .so in open ai docs post-audio-get execute the endpoint.

#PROMPT ENGINEERING(https://platform.openai.com/docs/guides/text-generation/chat-completions-api)
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

using prompt engineering telling the sysytem that what it is here i did a Technical interviewer for software developer junior engineer post.
Build up database for chat log un json file.

setup Database.py here we going to create get recent message function this is going to essentially build whatever converstion going to feed into chatgpt in latest conversation.

#defining the file name where message gonna store
file_name="stored_data.json"
    #confining the ai trying to tell ai what exactly you expect this is called promt engineering
    learn_instruction={
        "role":"system",
        "content":"you are interviewing the user for a job as a software Engineer .Ask short questions that are relevant to the junior position.Your name is Echo.The user name is Tanmay keep your answer under 30 words ."
    }

#initializing messages
 messages = []

#adding random  for making interesting prompt engineering giving ai humour

 x=random.uniform(0,1)

#making 50% chance of chatgpt humour 

if x<0.5:
        learn_instruction["content"] = learn_instruction["content"] + "your response will include some dry humour."
    else:
        learn_instruction["content"] = learn_instruction["content"] + "your respose will include a rather challenging question."
 #append the instruction to messages    
    messages.append(learn_instruction)

#creating function for adding the data into stored_data.json from messages
try:
    with open(file_name) as user_file:
        #opening the json file
        data = json.load(user_file)
        #appending the last 5 items of data
        if data:
            if len(data) < 5:
                for item in data:
                    messages.append(item)
            else:
                for item in data[-5:]:
                    messages.append(item)
except  Exception as e:
    print(e)
    pass
#return messages
return messages

#GETTING RESPONSE FROM CHATGPT
in open_ai_request.py

def get_chat_response(message_input):
#this get_recent_messages coming from database.get the recent messages
    messages = get_recent_messages()
    #latest message
    user_message = {
        "role":"user",
        #message_input is recent audio message which is decoded and passes into the get_chat_response function
        "content":message_input
    }
    messages.append(user_message)
    print(messages)
    #calling openai
    try:
        #getting resopnse from chatGpt
        response=openai.ChatCompletion.create(
            #chatgpt model
            model="gpt-3.5-turbo",
            #whole row user content
            messages=messages
        )
        #message we get from chatgpt
        message_text = response["choices"][0]["message"]["content"]
        return message_text
    except Exception as e:
        print(e)
        return


creating function to get the response from chatgpt passing the decoded message to the function and now we are calling the get_recent_messages_function so import this function in to this file now user message={"role":"user", "message":("decoded message" text cinverted from audio)message_input} that will be our latest message to our chatgpt and then append the user_message to messages now call open ai to get response=openai.ChatCompletion.create(mosel="gpt-3.5-turbo" messages=messages) now message_text=response["choices"]we getting object from chatgpt it will be the 1st item and message and message content returns from chatgpt now get that chat response and  passing messagr decoded 

import get chatresponse in main.py

#STORING THE MESSAGES IN DATABASE

def store_messages(request_message,response_message): 

    #define the file name
    file_name="stored_data.json"
    #Get recent messages excluded 1st messages
    messages=get_recent_messages()[1:]
    #add messages to the data
    user_message ={"role":"user","content":request_message}
    assistant_message={"role":"assistant","content":response_message}
    messages.append(user_message)
    messages.append(assistant_message)
    with open(file_name,"w")as f:
        json.dump(messages,f)
    

here excluding the 1st message learn_instruction={"role":"assistant","content":"interviewer"}this message we exclude that added in the message list at the begining. opening and saving the message in to the json file. now in main.py call the functions   store_messages(message_decoded,chat_response)


#CREATING RESET FUNCTION

def reset_message():

    #open the file and overwrite with nothing
    open("stored_data.json,"w")
go to the main.py and add the endpoint
@app.get("/reset")
async def reset_conversation();
    reset_message()
    return{"message":"conversation reset"}

#TEXT_TO_SPEECH CONVERT USING ELVEN LABS

import requests
from decouple import config

ELEVEN_LABS_API_KEY=config("ELEVEN_LABS_API_KEY")

#ELeven labs
#convert Text to speech

def convert_text_to_speech(message):
    #define the data(Body)
    body={

        "text":message,
        "voice_settings":{
            "stability": 0,
            "similarity_boost": 0,
        }

    }
    voice_EchoTalk="21m00Tcm4TlvDq8ikWAM"

    #header
    headers={"xi-api-key":ELEVEN_LABS_API_KEY,"Content-Type":"application/json", "accept":"audio/mpeg"}
    #api end point
    endpoint=f"https://api.elevenlabs.io/v1/text-to-speech/{voice_EchoTalk}"

    #send request

    try:
        response=requests.post(endpoint,json=body,headers=headers)

    except Exception as e:
        print(e)
        return
    #handle response
    if response.status_code == 200:
        return response.content
    else:
        return


and in main.py

  audio_output=convert_text_to_speech(chat_response)

    #gurd: Ensure message decoded
    
    if not audio_output:
        return HTTPException(status_code=400 ,detail="Failed to get Eleven labs audio response")
    
    #create a generater that yields chunk of data
    def iterfile():
        yield audio_output
    #return the audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream")
 
#sending audiofile with frontend and returning audio as stream-octent

@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

    #get saved audio
    #audio_input=open("TanmayVoice.mp3","rb")

    #save file from frontend
    with open(file.filename,"wb") as buffer:
        buffer.write(file.file.read())

    audio_input=open(file.filename,"rb")

     #return the audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream")
 
#FRONTEND


![frontend](https://github.com/TANMAY980/EchoTalk/assets/65010491/a3901b0f-5624-4adf-83ce-73390684d63c)

now switch to frontend folder and create components folder inside src and create controller.tsx and import conroller in App.tsx to check the controller running fine run command yarn dev.

in controller importing usestate from react  

function Controller(){
const[loading,isLoading]=useState(false);
const[message,setMessages]=useState<any[]>([]);

const CreateBlobUrl=(data:any)=>{};

handlestop is going to do when user stop recording thats going to trigger off the event to go and  send that recording to stop recordng 
and send it to our backend
const handlestop =async()=>{
}

#Title component-
here we are going to use props for the reset messages to use in title section

PROPS-
In React, props (short for properties) are a way to pass data from a parent component to a child component. They are one of the fundamental concepts of React and play a crucial role in building modular and reusable components. Here are some reasons why props are used in React:

Component Communication:

Parent to Child Communication: Props allow you to pass data from a parent component to a child component. This enables the parent to communicate with its children and share information.
Reusability:

By passing props, you can create reusable components that can be used in different parts of your application. These components can accept different data through props, making them versatile.
Dynamic Content:

Props enable the dynamic rendering of content. You can pass different values to the same component and have it render different content based on the provided props.
Configuration:

Props can be used to configure a component's behavior. For example, you might pass a boolean prop to determine whether a component should display a certain feature.
Maintainability:

Props make it easier to understand and maintain your code. When a component relies on props for its data, it becomes more self-contained and easier to reason about.
Consistent Interface:

Props define the interface of a component. By looking at a component's props, you can understand what data it expects and how it can be customized.
Here's a simple example to illustrate how props work:

jsx
Copy code
// ParentComponent.jsx
import ChildComponent from './ChildComponent';

function ParentComponent() {
  const dataForChild = "Hello from parent!";

  return (
    <div>
      <ChildComponent message={dataForChild} />
    </div>
  );
}

// ChildComponent.jsx
function ChildComponent(props) {
  return <p>{props.message}</p>;
}

In this example, ParentComponent passes a prop called message to ChildComponent, and the child component displays that message using props.message. This is a basic illustration of how props facilitate communication between components.

















