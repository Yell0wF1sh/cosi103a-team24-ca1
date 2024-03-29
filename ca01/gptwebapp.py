'''
gptwebapp will ask the user for some needs related to poetry and 
then sends it to openai's GPT API to generate the output.

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
@Modifier: Steve Wang
@Modifier: Shentong Rao
@Date: 2023-3-19
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
        <!DOCTYPE html>
        <head>
        </head>
        <body>
            <div style="width: 80vw;height: 80vh;text-align: center;margin: auto;box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);padding:10px;">
                <h1>cosi103a-team24-ca1</h1>
                <table style="width: 100%;height:100%">
                    <tr style="align-item=center;">
                        <td><a href="{url_for('about')}" style="background-color: rgb(56, 245, 191); padding: 50px 70px;text-decoration:none;text-align:center;border-radius:5px;font-size: 30px;font-weight:bold">About</a></td>
                        <td><a href="{url_for('team')}" style="background-color: rgba(85, 224, 54); padding: 50px 70px;text-decoration:none;text-align:center;border-radius:5px;font-size: 30px;font-weight:bold">Member</a></td>
                    </tr>
                    <tr>
                        <td><a href="{url_for('qiuyangwang')}" style="background-color: rgb(80, 159, 250); padding: 50px 70px;text-decoration:none;text-align:center;border-radius:5px;font-size: 30px;font-weight:bold">Generator</a></td>
                        <td><a href="{url_for('ShentongRao')}" style="background-color: rgb(111, 151, 252); padding: 50px 70px;text-decoration:none;text-align:center;border-radius:5px;font-size: 30px;font-weight:bold">poem_namer</a></td>
                        <td><a href="{url_for('translate')}" style="background-color: rgb(139, 147, 247); padding: 50px 70px;text-decoration:none;text-align:center;border-radius:5px;font-size: 30px;font-weight:bold">Translator</a></td>
                    </tr>
                </table>
            </div>
        </body>

    '''

#         <h1>cosi103a-team24-ca1</h1>
#         <a href="{url_for('about')}">About</a>
#         <br>
#         <a href="{url_for('qiuyangwang')}">Generator</a>
#         <br>
#         <a href="{url_for('translate')}">Translator</a>
#         <br>
#         <a href="{url_for('ShentongRao')}">poem_namer</a>
#         <br>

#         <a href="{url_for('team')}">Member</a>


@app.route('/team')
def team():
    """Display the team page."""
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                #header {
                    margin: auto;
                    padding: 20px;
                    width: 60%;
                    background-color: rgb(85, 224, 54);
                    text-align: center;
                }
                #body {
                    margin: auto;
                    width: 60%;
                    padding: 10px;
                    text-align: center;
                }
                #sr, #qw, #sw {
                    border: 3px solid rgb(85, 224, 54);
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
                    <div>github: <a href="https://github.com/Shentongr">https://github.com/Shentongr</a></div>
                </div>
            </div>
        </body>
    </html>
    '''


@app.route('/about')
def about():
    """Display the about page."""
    return """
    <!DOCTYPE html>
    <html>
	<title>About</title>
	<style>
		body {
			font-family: Arial, sans-serif;
			background-color: #f7f7f7;
		}
		h1 {
			text-align: center;
			color: #333;
		}
		p {
			font-size: 18px;
			line-height: 1.5;
			margin-bottom: 20px;
			text-align: justify;
			padding: 0 20px;
		}
		.container {
			max-width: 800px;
			margin: 0 auto;
			padding: 50px 20px;
			background-color: #fff;
			box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
		}
	</style>
    <body>
	    <div class="container">
		    <h1>About</h1>
		    <p>
                This is a web application that can implement several functionalities related to poetry based on the user's input. It is built on Flask and GPT-3.
            </p>
            <p>
                Genarator can generate poems based on the user's setting. Translator can translate the user's poetry into any language. the namer is used for naming
                a poem after the poem is generated or translated which make the web application more complete with generator, translator of poem and namer of the poem
            </p>
            <p>
                Have fun!
            </p>
            <p>
                Built by Qiuyang Wang, Steve Wang, and Shentong Rao.
            </p>

	    </div>
    </body>


    <script type="text/javascript">
        console.log("Hi there!");
        alert("Hi there!")
        let flag = confirm("Are you happy today?")
        while(!flag){
            flag = confirm("Are you happy today?")
        }
    </script>
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

            <!DOCTYPE html>

            <head>
                <style>
                    #page {
                        width: 80vw;
                        height: 80vh;
                        border: 3px solid rgba(66, 245, 144, 0.837);
                        text-align: center;
                        margin: auto;
                        text-shadow: 2px 2px 5px rgba(75, 176, 47, 0.866);
                    }

                    #submit {
                        font-size: 24;
                    }
                </style>
            </head>

            <body>
                <div id="page">
                    <div id="header">
                        <h1>GPT Demo App</h1>
                    </div>
                    <div id="form">
                        <form method="post">
                            <textarea name="prompt" placeholder="Enter your query here"></textarea>
                        </form>
                    </div>
                    <div id="submit">
                        <input type=submit value="get response">
                    </div>
                </div>
            </body>
        '''


"""
@Author: Qiuyang Wang
"""


@app.route('/qiuyang-wang', methods=['GET', 'POST'])
def qiuyangwang():
    """Display the qiuyang-wang page."""
    if request.method == 'POST':
        theme = request.form['theme']
        style = request.form['style']
        answer = gptAPI.poetry_generator(theme, style)
        return f'''
        <h1>Poetry Generator</h1>
        <pre style="bgcolor:yellow">Theme: {theme}</pre>
        <pre style="bgcolor:yellow">Style: {style}</pre>
        <hr>
        Here is the poem:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('qiuyangwang')}> Make Another Poem</a>
        <br>
        <a href={url_for('index')}> Back to Home Page</a>
        '''
    elif request.method == 'GET':
        return f'''
        <div style="width: 80vw;height: 80vh;border: 3px solid rgb(80, 159, 250);text-align: center;margin: auto;box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);">
            <h1>Poetry Generator</h1>
            <form method="post">
                <h3>Enter your the theme of your poem below (seperate with space if there are multiple themes):</h3>
                <input type="text" name="theme" style="width: 90%;border-radius: 5px;padding: 20px 10px; line-height: 28px;">
                <h3>Enter your the style of your poem below:</h3>
                <input type="text" name="style" style="width: 90%;border-radius: 5px;padding: 20px 10px; line-height: 28px;"><br>
                <input type=submit value="generate" style="padding: 15px 32px;background-color: rgb(80, 159, 250);text-align: center;font-size: 16px;border:none;font-weight:bold;margin-top:20px;border-radius:5px">
            </form>
            <br>
            <a href={url_for('index')} style="background-color: rgb(80, 159, 250); padding: 15px 32px;text-decoration:none;text-align:center;border-radius:5px;font-size: 16px;font-weight:bold"> Back to Home Page</a>
        </div>
        '''


"""
@Author: Shentong Rao
"""


@app.route('/ShentongRao', methods=['GET', 'POST'])
def ShentongRao():
    """Display shentongrao's page which is a poem name generator"""
    if request.method == 'POST':
        text = request.form['text']
        answer = gptAPI.poetry_namer(text)
        return f'''
        <h1>Poetry Generator</h1>
        <pre style="bgcolor:blue">the poem is: {text}</pre>
        <br>
        the poem name is :
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('ShentongRao')}> Name another poem</a>
        <br>
        <a href={url_for('index')}> Back to Home Page</a>
        '''
    elif request.method == 'GET':
        return f'''
        <div style="width: 80vw;height: 80vh;border: 3px solid rgb(111, 151, 252);text-align: center;margin: auto;box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);">
            <h1>Poetry Generator</h1>
            <form method="post">
                <h3>Enter the poem you want to generate name below (note: the name of the poem would be in English):</h3>
                <input type="text" name="text" style="width: 90%;border-radius: 5px;padding: 20px 10px; line-height: 28px;"><br>
                <input type=submit value="generate" style="padding: 15px 32px;background-color: rgb(111, 151, 252);text-align: center;font-size: 16px;border:none;font-weight:bold;margin-top:20px;border-radius:5px">
            </form>
            <br>
            <a href={url_for('index')} style="background-color: rgb(111, 151, 252); padding: 15px 32px;text-decoration:none;text-align:center;border-radius:5px;font-size: 16px;font-weight:bold"> Back to Home Page</a>
        </div>
        '''


"""
@Author: Steve Wang
"""


@app.route('/translate', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        text = request.form['text']
        lang = request.form['lang']
        answer = gptAPI.poetry_translator(text, lang)
        print(answer)
        return f'''
         <!DOCTYPE html>

            <head>
            </head>

            <body>
                <div style="width: 80vw;border: 3px solid rgb(139, 147, 247);text-align: center;margin: auto;box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);">
                    <h1 style="text-shadow: 2px 2px 5px rgb(139, 147, 247);">Poetry Generator</h1>
                    <table style="margin-bottom: 10px">
                        <tr style="margin: 10px">
                            <th style="text-shadow: 2px 2px 5px rgb(139, 147, 247);">Original Text</th>
                            <th style="text-shadow: 2px 2px 5px rgb(139, 147, 247);">Translated Text</th>
                        </tr>
                        <tr>
                            <td style="text-align: center; padding: 10px 10px;border:1.5px solid rgb(139, 147, 247);">{text}</td>
                            <td style="text-align: center; padding: 10px 10px;border:1.5px solid rgb(139, 147, 247);">{answer}</td>
                        </tr>
                    <table>
                    <a href={url_for('translate')} style="background-color: rgb(139, 147, 247); padding: 15px 32px;text-decoration:none;text-align:center;border-radius:5px;font-size: 16px;font-weight:bold"> Translate Another Poem</a>
                    <br>
                    <a href={url_for('index')} style="background-color: rgb(139, 147, 247); padding: 15px 32px;text-decoration:none;text-align:center;border-radius:5px;font-size: 16px;font-weight:bold"> Back to Home Page</a>
                </div>
            </body>
        '''
    elif request.method == 'GET':
        return f'''
        <!DOCTYPE html>

            <head>
            </head>
            <body>
                <div style="width: 80vw;height: 80vh;border: 3px solid rgb(139, 147, 247);text-align: center;margin: auto;box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);">
                    <h1>Poetry Translator</h1>
                    <form method="post">
                        <h3>Enter your the text of the original poem below:</h3>
                        <input type="text" name="text" style="width: 90%;border-radius: 5px;padding: 20px 10px; line-height: 28px;"><br>
                        <h3>Enter the language that you want the poem to be:</h3>
                        <input type="text" name="lang" style="width: 90%;border-radius: 5px;padding: 20px 10px; line-height: 28px;"><br>
                        <input type=submit value="Generate" style="padding: 15px 32px;background-color: rgb(139, 147, 247);text-align: center;font-size: 16px;border:none;font-weight:bold;margin-top:20px;border-radius:5px">
                    </form>
                    <br>
                    <a href={url_for('index')} style="background-color: rgb(139, 147, 247); padding: 15px 32px;text-decoration:none;text-align:center;border-radius:5px;font-size: 16px;font-weight:bold"> Back to Home Page</a>
                </div>
            </body>
        '''


if __name__ == '__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True, port=5001)
