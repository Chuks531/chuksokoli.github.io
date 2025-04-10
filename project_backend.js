require("dotenv").config();
const express = require("express");
const cors = require("cors");
const axios = require("axios");

const app = express();
app.use(express.json());
app.use(cors());

app.post("/translate", async (req, res) => {
  const { text } = req.body;

  try {
    const response = await axios.post(
      "https://api.openai.com/v1/chat/completions",
      {
        model: "gpt-4-turbo",
        messages: [{ role: "system", content: `Translate this to Spanish: ${text}` }],
      },
      {
        headers: { Authorization: `Bearer ${process.env.OPENAI_API_KEY}` },
      }
    );

    res.json({ translation: response.data.choices[0].message.content });
  } catch (error) {
    console.error("Translation API Error:", error);
    res.status(500).json({ error: "Translation failed" });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
