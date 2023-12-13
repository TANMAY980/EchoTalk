# Echo
Echo ChatGpt AI voice chatbot using OpenAi Chat model-gpt-3.5-turbo  Audio model-whisper-1  text-to-speech-Elevenlabs Rachel AI voice 

Backend
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




