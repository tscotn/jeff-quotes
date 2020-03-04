from random import randint
from twython import Twython

# "I'll go tally the votes."
# "Come on in, guys."
# "Fire in the form of flint."
# "Fire represents your life, when your fire's gone, so are you."
# "___ wins immunity."
# "It is time to vote. ___, you're up."
# "Any votes cast against ___ will not count."
# "Got nothing for you."
# "Thirty-nine days, twenty people, one survivor."
# "Wanna know what you're playing for?"
# "Worth playing for?"
# "Stay tuned for some scenes from our next episode."
# "The tribe has spoken."

def print0(str1, str2):
    return "The " + str1 + " has spoken."


def print1(str1, str2):
    return "I'll go " + str1 + " the " + str2 + "."


def print2(str1, str2):
    return "Come on in, " + str1 + "."


def print3(str1, str2):
    return str1.capitalize() + " in the form of " + str2 + "."


def print4(str1, str2):
    return str1.capitalize() + " represents your " + str2 + ", when your " + str1 + "'s gone, so are you."


def print5(str1, str2):
    return str1.capitalize() + " wins immunity."


def print6(str1, str2):
    return "It's time to vote. " + str1.capitalize() + ", you're up."


def print7(str1, str2):
    return "Any votes cast against " + str1 + " will not count."


def print8(str1, str2):
    return str1.capitalize() + ", got nothing for you."


def print9(str1, str2):
    return str1.capitalize() + ", " + str2 + ", one survivor."


def print10(str1, str2):
    return "Wanna know what you're " + str1 + " for?"


# def print11(str1, str2):
#    return "Worth playing for?"

def print12(str1, str2):
    return "Worth " + str1 + " for?"


def print13(str1, str2):
    return "Stay tuned for some " + str1 + " from our next " + str2 + "."


quoteList = ["tally", "votes", "come on in", "guys", "fire", "flint", "life", "gone, so are you", "wins immunity",
             "vote", "you're up", "thirty-nine days", "twenty people", "one survivor", "playing", "worth",
             "stay tuned", "episode", "spoken"]

printList = [print0, print1, print2, print3, print4, print5, print6, print7, print8, print9, print10,
             print12, print13]  # print11


def generateTweet():
    return printList[randint(0, len(printList) - 1)](quoteList[randint(0, len(quoteList) - 1)],
                                                 quoteList[randint(0, len(quoteList) - 1)])


APP_KEY = ''
APP_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

def main():
    tweet = generateTweet()

    while (len(tweet) > 140):
        tweet = generateTweet()

    print(tweet)
    twitter.update_status(status=tweet)

if __name__ == "__main__":
    main()
