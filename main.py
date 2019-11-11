import argparse

from flask import Flask, request, render_template
from wtforms import Form

from util.grammar import GrammarChecker
app = Flask(__name__)


def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('--grammar_file', type=str, default='./grammar.cfg')
    parser.add_argument('--dictionary', type=str, default='dictionary')
    parser.add_argument('--input_file', type=str, default='sentences')
    parser.add_argument('--web_mode', type=str, default=True)

    return parser.parse_args()


conf = get_config()
grammar_checker = GrammarChecker(conf.grammar_file, conf.dictionary)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/checkSentence', methods=['POST'])
def check_sentence():
    form = Form(request.form)
    sentence = request.form['sentence']
    result = grammar_checker.check_grammar(sentence)
    if result >= 1:
        return "[+] The sentence is a complete Yourba sentence."
    elif result == 0:
        return "[-] The sentence is not a complete Yoruba sentence."
    else:
        return "[-] Grammar does not cover some of the input words:" \
               "Update your dictionary to include the missing words"


def main(config):
    with open(config.input_file, 'r', encoding='UTF-8') as f:
        text = f.read().split('.')
        print(text)
        for sentence in text:
            grammar_checker.check_grammar(sentence)


if __name__ == '__main__':
    if not conf.web_mode:
        main(conf)
    else:
        app.run()
