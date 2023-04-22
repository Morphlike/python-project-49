#!/usr/bin/env python3
import sys
from brain_games import even_game
sys.path.append('../')


def main():
    print('Welcome to the Brain Games!')
    even_game.game_logic()


if __name__ == '__main__':
    main()
