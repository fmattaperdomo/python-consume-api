from aylienapiclient import textapi
import sys
import os

url = ''

#initialization
LANGUAGE = 'en'
MODE = 'document'
APP_ID = os.environ['TEXTAPI_APP_ID']
APP_KEY = os.environ['TEXTAPI_APP_KEY']
client = textapi.Client(APP_ID, APP_KEY)

#Request that you enter the url


def writeURL():
    return str(input("Write the URL: "))

#Request if you want to continue


def continueProgram():
    continueP = ""
    while continueP != "y":
        continueP = str(input("Do you wish to continue? (y/n):  ")).lower()
        if continueP == 'n':
            sys.exit()
    menu()

#Procedure to perform sentiment analysys


def sentiment_analysis():
    url = writeURL()

    sentiment = client.Sentiment({'url' : url, 'language' : LANGUAGE,
                                  'mode' : MODE})
    print("-----------------------------------------")
    print("----         R e s u l t             ----")
    print('-----------------------------------------')
    print('   polarity : ' + sentiment['polarity'])
    print('   confidence : ' + str(round(sentiment['polarity_confidence'], 4)))
    print('   text : ' + sentiment['text'])
    continueProgram()

#Procedure to perform classify analysys


def classify_analysis():
    url = writeURL()
    classifications = client.Classify({'url' : url, 'language' : LANGUAGE})
    print('-----------------------------------------------------------------')
    print("----                           R e s u l t                   ----")
    print('-----------------------------------------------------------------')
    print('CODE                 LABEL                       CONFIDENCE------')
    for category in classifications['categories']:
        print(category['code'] + " - " + category['label'] +
                                 " - " + str(category['confidence']))
    continueProgram()

#Procedure to perform entity analysys


def entity_analysis():
    url = writeURL()
    entities = client.Entities({'url' : url, 'language' : LANGUAGE})
    print('-----------------------------------------------------------------')
    print("----                           R e s u l t                   ----")
    print('-----------------------------------------------------------------')
    print('TYPE                 ENTITY                                ------')
    for type, values in entities['entities'].items():
        print(type + " ==> ", " - ".join(values))
    continueProgram()

#Procedure to perform concept analysys


def concept_analysis():
    url = writeURL()
    concepts = client.Concepts({'url' : url, 'language' : LANGUAGE})
    print('-----------------------------------------------------------------')
    print("----                           R e s u l t                   ----")
    print('-----------------------------------------------------------------')
    print('URL                             WORDS                       -----')
    for uri, value in concepts['concepts'].items():
        sfs = map(lambda c: c['string'] + " :" +
                            str(round(c['score'], 4)), value['surfaceForms'])
        print(uri + " ==> ", " - ".join(sfs))
    continueProgram()

#Procedure to perform summarization analysys


def summarization_analysis():
    url = writeURL()
    summary = client.Summarize({'url' : url, 'language' : LANGUAGE})
    print('-----------------------------------------------------------------')
    print("----                           R e s u l t                   ----")
    print('-----------------------------------------------------------------')
    print('#                 SENTENCE                                 ------')
    i = 0
    for sentence in summary['sentences']:
        i += 1
        print(str(i) + " ==> ", sentence)
    continueProgram()


def menu():
    url = ''
    print('***********************************************')
    print('*****     T E S T   A P I  A Y L I E N    *****')
    print('***********************************************')
    print('*** <1> Sentiment Analysis                  ***')
    print('*** <2> Classify Analysis                   ***')
    print('*** <3> Entity Analysis                     ***')
    print('*** <4> Concept Analysis                    ***')
    print('*** <5> Summarization Analysis              ***')
    print('*** <6> exit                                ***')
    print('***********************************************')
    option = 6
    while option > 0 or option < 7:
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Inavlid option.  Please select from 1 to 6")
            option = 6
            continue
        if option == 1:
            sentiment_analysis()
        elif option == 2:
            classify_analysis()
        elif option == 3:
            entity_analysis()
        elif option == 4:
            concept_analysis()
        elif option == 5:
            summarization_analysis()
        else:
            sys.exit()


def run():
    # llamado al menu
    menu()

if __name__ == '__main__':
    run()
