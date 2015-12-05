# -*- coding: utf-8 -*-
__author__ = 'Nicolas'

import random
import argparse

class Game(object):

    def __init__(self):
        self.current_words = []
        self.filenames = ["lecon5.txt"]
        self.parse_arguments()
        lines = self.open_file()
        self.dictionnary = self.make_dict(lines)
        self.init_current_words(self.dictionnary)

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Learn some japanese using text files. Just enter "q" to leave the app.')
        parser.add_argument('files', metavar='filename', type=str, nargs='+',
                            help='Filename to learn from (lecon5.txt or lecon6.txt, etc)')
        args = parser.parse_args()
        self.filenames = args.files

    def play(self):
        while(len(self.current_words) > 0):
            word = random.choice(self.current_words)
            guess = input(word + ": ")
            if guess == "q":
                print("Good bye!")
                break
            if(self.dictionnary.get(word) == guess):
                print("Good!\n")
                self.current_words.remove(word)
            else:
                print("Wrong! It's "+ self.dictionnary.get(word) +"\n")
        if(len(self.current_words) == 0):
            print("Well done!")

    def open_file(self):
        lines = []
        for filename in self.filenames:
            with open(filename, encoding='UTF-8') as f:
                lines += f.readlines()
            f.close()
        return lines

    def make_dict(self, lines):
        splitted = [line[:-1].split(':') for line in lines]
        return {item[0]: item[1] for item in splitted}

    def init_current_words(self, dictionnary):
        for key, value in dictionnary.items():
            self.current_words.append(key)
        print("Loaded " + str(len(self.current_words)) + " words.\n")


if __name__ == "__main__":
    game = Game()
    game.play()
