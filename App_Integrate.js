import { useState } from "react";
import SpeechToText from "../components/SpeechToText";
import TextToSpeech from "../components/TextToSpeech";

export default function Home() {
    const [transcript, setTranscript] = useState("");
    const [translation, setTranslation] = useState("");

    const handleTranslate = async () => {
        const response = await fetch("/api/translate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: transcript, targetLanguage: "es" }) // Spanish example
        });

        const data = await response.json();
        setTranslation(data.translation);
    };

    return (
        <div className="min-h-screen flex flex-col items-center justify-center p-6 bg-gray-100">
            <h1 className="text-2xl font-bold">Healthcare Translation App</h1>

            <SpeechToText onTranscript={setTranscript} />

            <p className="mt-4 p-2 border">{transcript}</p>

            <button onClick={handleTranslate} className="px-4 py-2 bg-purple-500 text-white rounded mt-4">
                Translate
            </button>

            <p className="mt-4 p-2 border">{translation}</p>

            {translation && <TextToSpeech text={translation} />}
        </div>
    );
}
