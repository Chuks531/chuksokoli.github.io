import { useState } from "react";

const SpeechToText = ({ onTranscript }) => {
    const [isListening, setIsListening] = useState(false);
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US"; // Default language

    recognition.onstart = () => setIsListening(true);
    recognition.onend = () => setIsListening(false);
    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        onTranscript(transcript);
    };

    const startListening = () => recognition.start();

    return (
        <div className="p-4">
            <button onClick={startListening} className="px-4 py-2 bg-blue-500 text-white rounded">
                {isListening ? "Listening..." : "Start Speaking"}
            </button>
        </div>
    );
};

export default SpeechToText;





