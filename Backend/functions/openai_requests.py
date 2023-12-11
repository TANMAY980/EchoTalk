import openai
from decouple import config

#import custom function

from functions.Database import get_recent_messages


#Retrieve ENV variables

openai.organization=config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

#open_ai -whisper
#convert audio to text

def convert_audio_to_text(audio_file):
    try:
        transcript=openai.Audio.transcribe("whisper-1",audio_file)
        message_text=transcript["text"]
        return message_text
    except Exception as e:
        print(e)
        return


#open-ai chatGpt response
#get response to our mesage

def get_chat_response(message_input):

    # this get_recent_messages coming from database.get the recent messages
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

