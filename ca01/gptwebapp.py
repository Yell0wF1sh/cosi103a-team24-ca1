'''
gptwebapp will ask the user for a prompt and 
then sends it to openai's GPT API to get a response.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py

@Modifier: Qiuyang Wang
@Modifier: Shihao Wang
@Date: 2023-3-15
'''
from flask import request, redirect, url_for, Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'


@app.route('/')
def index():
    ''' display links to each of the team-members pages '''
    print('processing / route')
    return f'''
        <h1>cosi103a-team24-ca1</h1>
        <a href="{url_for('about')}">About</a>
        <br>
        <a href="{url_for('qiuyangwang')}">Qiuyang Wang's Page</a>
        <br>
        <a href="{url_for('team')}">Member</a>

    '''


@app.route('/team')
def team():
    """Display the team page."""
    return '''
    <html>
        <head>
            <style>
                #header {
                    margin: auto;
                    padding: 20px;
                    width: 60%;
                    background-color: lightblue;
                    text-align: center;
                }
                #body {
                    margin: auto;
                    width: 60%;
                    padding: 10px;
                    text-align: center;
                }
                #sr, #qw, #sw {
                    border: 3px solid blue;
                    padding: 5px;
                    margin: 5px;
                }
            </style>
        </head>
        <body>
            <h1 id="header">Members:</h1>
            <div id="body">
                <div id="qw">
                    <h2>Qiuyang Wang</h2>
                    <div>github: <a href="https://github.com/Billy-FIN">https://github.com/Billy-FIN</a></div>
                </div>
                <div id="sw">
                    <h2>Steve Wang</h2>
                    <div>github: <a href="https://github.com/Yell0wF1sh">https://github.com/Yell0wF1sh</a></div>
                </div>
                <div id="sr">
                    <h2>Shentong Rao</h2>
                    <p>github:</p>
                </div>
            </div>
        </body>
    </html>
    '''


@app.route('/about')
def about():
    """Display the about page."""
    return """
    <html>

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

        <style type="text/css">
            .class1 {
                font-size: 50
            }

            .class2 {
                font-size: 25
            }

            .class3 {
                font-size: 20
            }
        </style>

    </head>


<body>
    <b class="class1">About</b>
    <br>
    <br>
    <b class="class2">Qiuyang Wang's Page</b>
   
    

    <br>
    <b class="class2">Steve Wang's Page</b>
    <br>

    
    <br>
    <b class="class2">Shentong Rao's Page</b>
    <br>
    
</body>

</html>
    
    
    
    
    
    """


@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

"""
@Author: Qiuyang Wang
"""
@app.route('/qiuyang-wang', methods=['GET', 'POST'])
def qiuyangwang():
    """Display the qiuyang-wang page."""
    if request.method == 'POST':
        theme = request.form['theme']
        keywords = request.form['keywords']
        answer = gptAPI.poetry_generator(theme, keywords)
        return f'''
        <h1>Poetry Generator</h1>
        <pre style="bgcolor:yellow">Theme: {theme}. Keywords: {keywords}</pre>
        <hr>
        Here is the poem:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('qiuyangwang')}> Make Another Poem</a>
        <br>
        <a href={url_for('index')}> Back to Home Page</a>
        '''
    elif request.method == 'GET':
        return f'''
        <h1>Poetry Generator</h1>
        <form method="post">
            Enter your the theme of your poem below (seperate with space if there are multiple keywords): <input type="text" name="theme"><br>
            Enter your the keywords of your poem below (seperate with space if there are multiple keywords): <input type="text" name="keywords"><br>
            <p><input type=submit value="generate">
        </form>
        <br>
        <a href={url_for('index')}> Back to Home Page</a>
        '''


if __name__ == '__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True, port=5001)
