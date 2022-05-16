import PySimpleGUI as sg
import requests

from images import bytes_icon


def load_words():
    response = requests.get(f'https://raw.githubusercontent.com/crenod/wordle_pub/main/all_words.txt')
    response.encoding = 'utf-8'
    words = response.text.split(sep='\n')[:-1]
    # print(words)
    return words


def go_wordle(words_list, eps_symbols='', have_symbols='', symb_1='', symb_2='', symb_3='', symb_4='', symb_5='',
              not_symb_1='', not_symb_2='', not_symb_3='', not_symb_4='', not_symb_5=''):
    have_symbols += not_symb_1 + not_symb_2 + not_symb_3 + not_symb_4 + not_symb_5
    good_words = set(words_list)
    # with open('singular_and_plural_5.txt', 'r', encoding="utf8") as ru_5:
    #     for word in ru_5:
    #         word = word.strip()
    #         good_words.add(word)
    for one_word in list(good_words):
        for eps_symbol in eps_symbols:
            if one_word.find(eps_symbol) != -1:
                good_words.discard(one_word)
        for have_symbol in have_symbols:
            if one_word.find(have_symbol) == -1:
                good_words.discard(one_word)
        if symb_1 and symb_1 != one_word[0]:
            good_words.discard(one_word)
        if symb_2 and symb_2 != one_word[1]:
            good_words.discard(one_word)
        if symb_3 and symb_3 != one_word[2]:
            good_words.discard(one_word)
        if symb_4 and symb_4 != one_word[3]:
            good_words.discard(one_word)
        if symb_5 and symb_5 != one_word[4]:
            good_words.discard(one_word)
        for not_symb_1_1 in not_symb_1:
            if not_symb_1_1 == one_word[0]:
                good_words.discard(one_word)
        for not_symb_2_1 in not_symb_2:
            if not_symb_2_1 == one_word[1]:
                good_words.discard(one_word)
        for not_symb_3_1 in not_symb_3:
            if not_symb_3_1 == one_word[2]:
                good_words.discard(one_word)
        for not_symb_4_1 in not_symb_4:
            if not_symb_4_1 == one_word[3]:
                good_words.discard(one_word)
        for not_symb_5_1 in not_symb_5:
            if not_symb_5_1 == one_word[4]:
                good_words.discard(one_word)

    return good_words


known_words = load_words()
sg.theme('BluePurple')
layout = [
    [sg.T('Отсутствуют:'), sg.Input(key='-IN-EPS-')],
    [sg.T('Буквы на своих местах:')],
    [sg.T('1:'), sg.Input(key='-IN-G1-', size=(2, 1)), sg.T('2:'), sg.Input(key='-IN-G2-', size=(2, 1)),
     sg.T('3:'), sg.Input(key='-IN-G3-', size=(2, 1)), sg.T('4:'), sg.Input(key='-IN-G4-', size=(2, 1)),
     sg.T('5:'), sg.Input(key='-IN-G5-', size=(2, 1))],
    [sg.T('Буквы не на своих местах:')],
    [sg.T('1:'), sg.Input(key='-IN-Y1-', size=(4, 1)), sg.T('2:'), sg.Input(key='-IN-Y2-', size=(4, 1)),
     sg.T('3:'), sg.Input(key='-IN-Y3-', size=(4, 1)), sg.T('4:'), sg.Input(key='-IN-Y4-', size=(4, 1)),
     sg.T('5:'), sg.Input(key='-IN-Y5-', size=(4, 1))],
    [sg.Text(f'Найдено слов: '), sg.Text(len(known_words), size=(15, 1), key='-OUTPUT-LEN-')],
    [sg.Text(size=(60, 10), key='-OUTPUT-')],
    [sg.Button('Show'), sg.Button('Clear'), sg.T(size=(3, 1)), sg.Button('Exit')]
]

window = sg.Window('Wordle Helper v2', layout, icon=bytes_icon)

while True:  # Event Loop
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        window['-IN-EPS-'].update('')
        window['-IN-G1-'].update('')
        window['-IN-G2-'].update('')
        window['-IN-G3-'].update('')
        window['-IN-G4-'].update('')
        window['-IN-G5-'].update('')
        window['-IN-Y1-'].update('')
        window['-IN-Y2-'].update('')
        window['-IN-Y3-'].update('')
        window['-IN-Y4-'].update('')
        window['-IN-Y5-'].update('')
    if event == 'Show':
        all_words = go_wordle(words_list=known_words,
                              eps_symbols=values['-IN-EPS-'],
                              symb_1=values['-IN-G1-'],
                              symb_2=values['-IN-G2-'],
                              symb_3=values['-IN-G3-'],
                              symb_4=values['-IN-G4-'],
                              symb_5=values['-IN-G5-'],
                              not_symb_1=values['-IN-Y1-'],
                              not_symb_2=values['-IN-Y2-'],
                              not_symb_3=values['-IN-Y3-'],
                              not_symb_4=values['-IN-Y4-'],
                              not_symb_5=values['-IN-Y5-'])
        window['-OUTPUT-LEN-'].update(len(all_words))
        window['-OUTPUT-'].update(', '.join(all_words))

window.close()
