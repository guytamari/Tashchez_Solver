from urllib.parse import quote
import sys
import requests
from bs4 import BeautifulSoup
import pprint
import re

# url = solution == '-' between words
# second_url= solutions == '_' between words


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36'}
url = 'https://www.note.co.il/solution/'
second_url = 'https://www.note.co.il/solutions/'
number_pattern = re.compile(r'\d+(\.\d+)?')
user_hint = sys.argv[1:]
# num_of_letters = sys.argv[1]
combined_hint = ' '.join(user_hint)
final_hint = combined_hint.replace(' ', '-')
final_hint2 = combined_hint.replace(' ', '_')


# first url req
def req(hint):
    full_url = url + quote(hint)
    res = requests.get(full_url, headers=headers)
    return res


# second url req
def req2(hint):
    full_url = second_url + quote(hint)
    res = requests.get(full_url, headers=headers)
    return res


# modifying answers
def answers(soup):
    div = soup.find(class_='dictionary origin_content').text
    if div:
        div = div.split('\n')
        # reversing the strings
        for sentence in div:
            corrected_sentences_list = sentence[::-1]
            # search for number in the strings
            match = number_pattern.search(corrected_sentences_list)
            if match:
                print(match.group())
            elif match is None:
                print('שתי מילים או יותר'[::-1])
            else:
                return []
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


def find_how_many_letter(letter):
    pass
    # given the number of letters filer specific answer


if __name__ == '__main__':
    main()
