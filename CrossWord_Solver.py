from urllib.parse import quote
import sys
import requests
from bs4 import BeautifulSoup
import re
import pdb

# url = solution == '-' between words
# second_url= solutions == '_' between words


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36'}
url = 'https://www.note.co.il/solution/'
second_url = 'https://www.note.co.il/solutions/'
number_pattern = re.compile(r'\d+(\.\d+)?')
word = re.compile("םילימ")


# first url req
def req(hint):
    full_url = url + quote(hint)
    res = requests.get(full_url, headers=headers)
    # print(full_url)
    return res


# second url req
def req2(hint):
    full_url = second_url + quote(hint)
    res = requests.get(full_url, headers=headers)
    return res


# modifying answers
def answers(soup):
    div = soup.find(class_='dictionary origin_content').text.split('\n')
    if div:
        corrected_sentences_list = []
        for sentence in div:

            corrected_sentences_list.append(sentence)
            # search for number in the strings
            match = number_pattern.search(sentence)
            words = word.search(sentence)
            if match and words and letter_or_word == '+':
                print(sentence)
            elif match.group() == letter_or_word:
                print(sentence)
            else:
                pass
    else:
        return "Element not found."


def main():
    # creating soup var
    soup = BeautifulSoup(req(final_hint).text, 'html.parser')
    # filtering between both url's
    not_found = soup.find('meta', attrs={"content": "הדף לא נמצא - עזרה בפתרון תשחצים ותשבצים"})
    if not_found:
        # using second url
        soup = BeautifulSoup(req2(final_hint2).text, 'html.parser')
        answers(soup)
    else:
        answers(soup)


if __name__ == '__main__':
    print('-------------Hello, Welcome to my CrossWord Solver-------------\n'
          '---------------------------------------------------------------\n')
    user_hint = input('-------------Enter Your Given Hint------------- ')[::-1]
    letter_or_word = input('-------------Enter The Number of Letters Given (for 2 + words enter W)------------- ')

    final_hint = user_hint.replace(' ', '-')[::-1]
    final_hint2 = user_hint.replace(' ', '_')[::-1]
    main()
