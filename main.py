import argparse
import sys

from util.grammar import GrammarChecker


def main(config):
    grammar_checker = GrammarChecker(config.grammar_file, config.dictionary)

    if not config.web_mode:
        with open(config.input_file, 'r', encoding='UTF-8') as f:
            text = f.read().split('.')
            print(text)
            for sentence in text:
                grammar_checker.print_tree(sentence)


def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('--grammar_file', type=str, default='./grammar.cfg')
    parser.add_argument('--dictionary', type=str, default='dictionary')
    parser.add_argument('--input_file', type=str, default='sentences')
    parser.add_argument('--web_mode', type=str, default=False)

    return parser.parse_args()


if __name__ == '__main__':
    conf = get_config()
    main(conf)
