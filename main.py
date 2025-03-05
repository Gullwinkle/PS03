from bs4 import BeautifulSoup
from googletrans import Translator
import requests


def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()
        return {
            'english_word': english_word,
            'word_definition': word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def translate_word(word):
    translator = Translator()
    word_translation = translator.translate(word['english_word'], dest='ru')
    definition_translation = translator.translate(word['word_definition'], dest='ru')
    translation = {
        'russian_word': word_translation.text,
        'rus_word_definition': definition_translation.text
    }
    return translation

def word_game():
    print("Добро пожаловать в игру \"Угадай слово\"!")
    while True:
        eng_dict = get_english_words()
        rus_dict = translate_word(eng_dict)
        word = rus_dict.get('russian_word')
        definition = rus_dict.get('rus_word_definition')
        print(f"Значение слова - {definition}")
        user = input("Что это за слово? Введите свое предположение:\n")
        if user.lower() == word.lower():
            print("Поздравляем! Вы угадали слово!")
        else:
            print(f"К сожалению, вы не угадали слово. Было загадано слово - {word}")

        play_again = input("Хотите сыграть еще? (д/н): ")
        if play_again.lower() != 'д':
            print("Спасибо за игру!")
            break

word_game()