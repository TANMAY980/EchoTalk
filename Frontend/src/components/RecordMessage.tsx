import { ReactMediaRecorder } from "react-media-recorder";
import Recordicon from "./Recordicon";

type Props={
    handleStop:any;

}
function RecordMessage({handleStop}:Props) {
  return (
    <div>
      <ReactMediaRecorder
      audio
      onStop={handleStop} render ={({status,startRecording,stopRecording})=>
      <div className="mt-2 ">
        <button onMouseDown={startRecording} onMouseUp={stopRecording}
        className="bg-white p-4 rounded-full transition-all duration-300 text-blue-300  hover:text-green-500"
        
        >
        <Recordicon 
        classText={
            status =="recording" 
            ? "animate-pulse text-red-500"
            : "text-sky-500" }/>
        </button>
        <p className="mt-2 rounded-full animate-pulse bg-gradient-to-r from-white to-red-500">{status}</p>
        </div>}
      
      />
    </div>
  )
}

export default RecordMessage
