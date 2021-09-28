from translate import Translator

# My solution
#  sentence = input('Type the sentence you want to translate into Japanese: ')

#  translator = Translator(to_lang='jp')
#  JP_sentence = translator.translate(sentence)

translator = Translator(to_lang="ja")
# ISO639-1
try:
  with open('test.txt',mode='r') as my_file:
      text = my_file.read()
      translation = translator.translate(text)
      with open('test-ja.txt',mode='w')as my_file2:
        my_file2.write(translation)
except FileNotFoundError as e:
    print('check your file path,please.')
