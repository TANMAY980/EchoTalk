import {useState} from 'react';
import Title from './Title';
import RecordMessage from './RecordMessage';
import axios from 'axios';
function controller() {
    const[isloading,setIsloading]=useState(false);
    const[messages,setMessages]=useState<any[]>([]);

    const[blob,setBlob]=useState("");

    const createBlobURL= (data:any) =>{

      const blob=new Blob([data],{type:"audio/mpeg"});
      //this is what going to convert that into somehing that we can actually play as an audio file from backend
      const url=window.URL.createObjectURL(blob);
      return url;
    };
    const handleStop= async(blobUrl:string) =>{
      setIsloading(true)
      //appending my recorded message to messages we can see what we sent to EchoTalk
      const myMessage={sender:"me",blobUrl};
      const messagesArr=[...messages,myMessage];

      //convert bloburl to blob object sending over the backend

      fetch(blobUrl)
        .then((res)=> res.blob())
        .then(async (blob) => {
        //construct audio to send file to send in the backend
        const formData= new FormData();
        //getting the file which i need to send it to the backend
        formData.append("file",blob,"myFile.wav")

        //send from data to api endpoint

        await axios.post("http://localhost:8000/post-audio",formData,{
        headers:{"Content-Type":"audio/mpeg"},
        responseType:"arraybuffer",
      }).then((res:any) => {
        const blob = res.data
        const audio = new Audio()
        audio.src= createBlobURL(blob);

        //append to audio
        const EchoTalkMessage ={sender:"Echo",blobUrl:audio.src}
        messagesArr.push(EchoTalkMessage)
        //setmessages to new messages latest conversation
        setMessages(messagesArr)

        //play audio automatically
        setIsloading(false)
        audio.play()

      })
      .catch((err:any)=>{
        console.error(err.message)
        setIsloading(false)

      })

      })


      //console.log(blobUrl)
      //setBlob(blobUrl)
    };
  return (
    <div className='h-screen overflow-y-hidden'>
        <Title setMessages={setMessages}/>
      <div className='flex flex-col  justify-between h-full overflow-y-scroll pb-96 bg-gradient-to-r from-white to-sky-200'>
        {/*<audio src={blob} controls/>*/}

        {/*conversation recorder*/}
        <div className="mt-5 px-5">
          {messages.map((audio, index) => {
            return ( 
            <div 
              key={index + audio.sender} 
              className={
              "flex flex-col " +
              (audio.sender == "Echo" && "flex items-end")
            }
            >
              {/*sender*/}
              <div className="mt-4">
                <p 
                  className={
                  audio.sender == "Echo"
                  ? "text-right mr-2  rounded-full font-bold italic  bg-gradient-to-r from-white to-green-500"
                  : "ml-2 italic  rounded-full font-bold bg-gradient-to-l from-white to-sky-300"
                }>
                  {audio.sender}
                </p>
                {/*audio message*/}
                <audio
                  src={audio.blobUrl}
                  className="appearance-none"
                  controls
                
                />

              </div>

            </div>
            );
          })}
        </div>
        {messages.length == 0 && !isloading &&(
          <div className="text-center  rounded-full font-bold italic mt-10 mx-auto max-w-sm animate-bounce bg-gradient-to-r from-white to-sky-300">ask Echo with your voice....</div>
        )}
        {isloading &&(
          <div className="text-center rounded-full font-bold italic mt-10 mx-auto max-w-sm animate-pulse bg-gradient-to-r from-sky-500 to-green-500"> ummm let me answer your question.....</div>
        )}

        {/*recoder*/}
        <div className="fixed bottom-0 rounded-full w-full py-6 border-t text-center bg-gradient-to-r from-sky-500 to-green-500">
          <div className="flex justify-center items-center w-full">
            <div>
              <RecordMessage handleStop={handleStop}/>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default controller;
