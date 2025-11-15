// This file contains the JavaScript code for interacting with OpenAI's API.

const axios = require('axios');
require('dotenv').config();

const OPENAI_API_KEY = process.env.OPENAI_API_KEY;
const OPENAI_API_URL = 'https://api.openai.com/v1/chat/completions';

async function getOpenAIResponse(prompt) {
    try {
        const response = await axios.post(OPENAI_API_URL, {
            model: 'gpt-3.5-turbo',
            messages: [{ role: 'user', content: prompt }],
        }, {
            headers: {
                'Authorization': `Bearer ${OPENAI_API_KEY}`,
                'Content-Type': 'application/json',
            },
        });

        return response.data.choices[0].message.content;
    } catch (error) {
        console.error('Error fetching response from OpenAI:', error);
        throw error;
    }
}

module.exports = { getOpenAIResponse };