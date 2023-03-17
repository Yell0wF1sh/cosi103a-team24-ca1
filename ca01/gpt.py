'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai


class GPT():
    ''' make queries to gpt from a given API '''

    def __init__(self, apikey):
        ''' store the apikey in an instance variable '''
        self.apikey = apikey
        # Set up the OpenAI API client
        openai.api_key = apikey  # os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self, prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completion.choices[0].text
        return response

    def poetry_generator(self, theme, keywords):
        ''' Generate a poetry 

        @Author: Qiuyang Wang
        '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt='Please generate a romentic poem for me. Style: Ideal and Romanticism. Theme: ' +
            theme + '. Keywords: ' + keywords + '.',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=1.0,
        )

        response = completion.choices[0].text
        return response

    def poetry_translator(self, text, lang):
        '''Generate a translation for a poem
            @Author: Steve Wang
        '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt='Please translate the following poem into ' +
            lang + '. Here is the poem: ' + text + '.',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=1.0,
        )

        response = completion.choices[0].text
        return response


if __name__ == '__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.getResponse("what does openai's GPT stand for?"))
