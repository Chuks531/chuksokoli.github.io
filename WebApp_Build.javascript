import { useState } from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';
import { Button } from "@/components/ui/button";

export default function TranslatorApp() {
  const [translatedText, setTranslatedText] = useState('');
  const { transcript, listening, resetTranscript } = useSpeechRecognition();

  const translateText = async () => {
    const response = await fetch('/api/translate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: transcript, targetLang: 'es' })
    });
    const data = await response.json();
    setTranslatedText(data.translated);
  };

  return (
    <div className="p-6 max-w-2xl mx-auto text-center">
      <h1 className="text-2xl font-bold">Healthcare Translation AI</h1>
      <Button onClick={SpeechRecognition.startListening} disabled={listening}>
        {listening ? "Listening..." : "Start Speaking"}
      </Button>
      <Button onClick={resetTranscript}>Reset</Button>
      <p className="mt-4">Original: {transcript}</p>
      <Button onClick={translateText}>Translate</Button>
      <p className="mt-4">Translated: {translatedText}</p>
    </div>
  );
}