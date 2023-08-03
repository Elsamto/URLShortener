#  pip install googletrans==4.0.0-rc1
from googletrans import Translator

translator = Translator()

language = {"bn": "Bangla",
            "en": "English",
            "ko": "Koren",
            "fr": "French",
            "de": "German",
            "he": "Hebrew",
            "hi": "Hindi",
            "it": "Italian",
            "ja": "Japanese",
            'la': "Latin",
            "ms": "Malay",
            "ne": "Nepali",
            "ru": "Russian",
            "ar": "Arabic",
            "zh": "Chinese",
            "es": "Spanish"
            }

allow = True
while allow:
  user_code = input(f"Please input desired language code. To see the language code list enter 'options' \n")
  if user_code == "options":
    print("Code: Languaje")
    for i in language.items():
      print(f"{i[0]} => {i[1]}")
    print()
  else:
    for lan_code in language.keys():
      if lan_code == user_code:
        print(f"You have selected {language[lan_code]}")
        allow =False
    if allow:
      print("It is not avalid language code!")

while True:
    string = input("\nWrite the text you want to translate: \nTo exit the program write 'close'\n")
    if string == "close":
      print(f"\nHave a nice Day!")
      break
   
    translated = translator.translate(string, dest=user_code)

    print(f"\n{language[user_code]} translation: {translated.text}")

    print(f"Pronunciation : {translated.pronunciation}")

for i in language.items():
   if translated.src == i [0]:
      print(f"translated from {i[1]}")