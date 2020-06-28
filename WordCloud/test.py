from WordCloudAssistant import *


def main():
    wcAssistant = WordCloudAssistant()

    with open('C:\\WorkSpace\\WordCloud\\minister.txt', 'r', encoding='utf8') as fp:
        text = fp.read()
        wcAssistant.Generate(text = text, backgroundFile = 'C:\\WorkSpace\\WordCloud\\test1.jpg', isChines = True)

if __name__ == '__main__':
    main()
        