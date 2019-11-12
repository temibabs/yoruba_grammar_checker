import argparse

from flask import Flask, request, render_template
from wtforms import Form

from util.grammar import GrammarChecker
app = Flask(__name__)
grammar_checker = GrammarChecker('./grammar.cfg', 'dictionary')


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/checkSentence', methods=['POST'])
def check_sentence():
    sentence = request.form['sentence']
    try:
        result = grammar_checker.check_grammar(sentence)
        if result >= 1:
            return "[+] The sentence is a complete Yourba sentence."
        elif result == 0:
            return "[-] The sentence is not a complete Yoruba sentence."
    except Exception:
        return "[-] Grammar does not cover some of the input words:" \
               "Update your dictionary to include the missing words"


@app.route('/updateDictionary', methods=['POST'])
def update_dictionary():
    word = request.form['word']
    file = request.form['pos']
    grammar_checker.update_dictionary(word, file)
    grammar_checker.update_grammar('grammar.cfg', 'dictionary')
    grammar_checker.define_grammar('custom_grammar.cfg')
    return 'The dictionary has been updated with your word. ' \
           'Thank you for your input.'

def main(config):
    with open(config.input_file, 'r', encoding='UTF-8') as f:
        text = f.read().split('.')
        print(text)
        for sentence in text:
            grammar_checker.check_grammar(sentence)


if __name__ == '__main__':
    app.run()
