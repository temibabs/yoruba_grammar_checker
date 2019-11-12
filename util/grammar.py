import nltk


class GrammarChecker(object):
    def __init__(self, grammar_file, dictionary):
        self.grammar = None
        self.new_grammar_file = self.update_grammar(grammar_file, dictionary)
        self.define_grammar(self.new_grammar_file)

    def define_grammar(self, grammar_file):
        self.grammar = nltk.data.load(grammar_file)

    def check_grammar(self, sentence):
        sent = sentence.lower().split()
        print(sent)
        rd_parser = nltk.IncrementalChartParser(self.grammar)

        trees = 0
        try:
            for tree in rd_parser.parse(sent):
                trees += 1
        except ValueError:
            print('[-] Grammar does not cover some of the input words: '
                  'Update your dictionary to include the missing words')
            raise Exception('[-] Grammar does not cover some of the input '
                            'words:Update your dictionary to include '
                            'the missing words')

        return trees

    def update_grammar(self, grammar_file, dictionary):
        grammar = open(grammar_file, 'r', encoding='UTF-8').read()
        with open(dictionary + '/pre-verbal-modifiers', encoding='UTF-8') as f:
            grammar += 'Pre-Verbal ->'
            lines = f.read().splitlines()
            grammar += ' \'{}\' '.format(lines[0])
            for i in lines[1:]:
                grammar += '| \'{}\' '.format(i)
            grammar += '\n'

        with open(dictionary + '/post-verbal-modifiers', encoding='UTF-8') as f:
            grammar += 'Post-Verbal ->'
            lines = f.read().splitlines()
            grammar += ' \'{}\' '.format(lines[0])
            for i in lines[1:]:
                grammar += '| \'{}\' '.format(i)
            grammar += '\n'

        with open(dictionary + '/conjunctions', encoding='UTF-8') as f:
            grammar += 'Conjunction ->'
            lines = f.read().splitlines()
            grammar += ' \'{}\' '.format(lines[0])
            for i in lines[1:]:
                grammar += ' | \'{}\''.format(i)
            grammar += '\n'

        with open(dictionary + '/disjunctions', encoding='UTF-8') as f:
            grammar += 'Disjunction ->'
            lines = f.read().splitlines()
            grammar += ' \'{}\' '.format(lines[0])
            for i in lines[1:]:
                grammar += '| \'{}\' '.format(i)
            grammar += '\n'

        with open(dictionary + '/nouns', encoding='UTF-8') as f:
            grammar += 'Noun ->'
            lines = f.read().splitlines()
            grammar += ' \'{}\' '.format(lines[0])
            for i in lines[1:]:
                grammar += '| \'{}\' '.format(i)
            grammar += '\n'

        with open(dictionary + '/qualifiers', encoding='UTF-8') as f:
            grammar += 'Qualifier ->'
            lines = f.read().splitlines()
            grammar += ' \'{}\' '.format(lines[0])
            for i in lines[1:]:
                grammar += '| \'{}\' '.format(i)
            grammar += '\n'

        with open(dictionary + '/sf-sententials', encoding='UTF-8') as f:
            grammar += 'SF-sentential ->'
            lines = f.read().splitlines()
            grammar += ' \'{}\' '.format(lines[0])
            for i in lines[1:]:
                grammar += '| \'{}\' '.format(i)
            grammar += '\n'

        with open(dictionary + '/si-sententials', encoding='UTF-8') as f:
            grammar += 'SI-sentential ->'
            lines = f.read().splitlines()
            grammar += ' \'{}\' '.format(lines[0])
            for i in lines[1:]:
                grammar += '| \'{}\' '.format(i)
            grammar += '\n'

        with open(dictionary + '/verbs', encoding='UTF-8') as f:
            grammar += 'Verb ->'
            lines = f.read().splitlines()
            grammar += ' \'{}\' '.format(lines[0])
            for i in lines[1:]:
                grammar += '| \'{}\' '.format(i)
            grammar += '\n'

        new_file_name = 'custom_grammar.cfg'
        with open(new_file_name, 'w', encoding='UTF-8') as f:
            f.write(grammar)

        return new_file_name

    @staticmethod
    def update_dictionary(word, file):
        with open('dictionary/'+file, 'a') as f:
            f.write(word)
