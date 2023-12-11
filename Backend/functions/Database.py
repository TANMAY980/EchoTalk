import json
import random

#get recent messages

def get_recent_messages():

    #Define the file name and learn instruction
    
    file_name="stored_data.json"
    #confining the ai trying to tell ai what exactly you expect this is called promt engineering
    learn_instruction={
        "role":"system",
        "content":"you are interviewing the user for a job as a software Engineer .Ask short questions that are relevant to the junior position.Your name is Echo.The user name is Tanmay keep your answer under 30 words ."
    }

    #initialize messages
    messages = []

    #adding random element for making interesting prompt engineering

    x=random.uniform(0,1)

    #making 50% chance of chatgpt humour 

    if x<0.5:
        learn_instruction["content"] = learn_instruction["content"] + "your response will include some dry humour."
    else:
        learn_instruction["content"] = learn_instruction["content"] + "your respose will include a rather challenging question."
    #append the instruction to messages
    
    messages.append(learn_instruction)
    #over time untill we reset the chat message gonna stored in the json file
    #so what we need to do write the function that will actually go and get those messages and add them to the history here

    #get the messages

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


#store messages

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


    #save the updated file
    with open(file_name,"w")as f:
        json.dump(messages,f)
    
def reset_messages():
    #overwrite current file
    open("stored_data.json","w")

    