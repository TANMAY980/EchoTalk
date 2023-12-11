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




