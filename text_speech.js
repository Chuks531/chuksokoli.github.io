const TextToSpeech = ({ text }) => {
    const speak = () => {
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = "en-US"; // Change based on translation
        speechSynthesis.speak(utterance);
    };

    return (
        <button onClick={speak} className="px-4 py-2 bg-green-500 text-white rounded">
            Speak Translation
        </button>
    );
};

export default TextToSpeech;
