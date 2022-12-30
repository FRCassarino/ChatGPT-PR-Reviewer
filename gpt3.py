import os
import openai

import json
import requests

class GPT3API:
    def __init__(self, token):
        self.token = token
        openai.api_key = token

    def generate_response(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            best_of=2
        )

        return response.choices[0].text

