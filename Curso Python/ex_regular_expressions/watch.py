
#Implement a function called parse that expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element therein,
#and returns its shorter, shareable youtu.be equivalent as a str. Expect that any such URL will be in one of the formats below. Assume that the value of src will be surrounded by double quotes.
#And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return None.


import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"(<iframe(.)*><iframe(.)*>\</iframe>"),s):                                                  # The expression that needs to be verified each time is <iframe  at the beginning and </iframe> at the end.
                                                                                                            # (.) anything afer frame, * 0 or more repetitions
                                                                                                            #\to express that what comes after is literally something



        url_pattern=re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)",s)                #() different groups, * to express it's optional
        if url_pattern:                                                                                         #[a-z_A-Z_0-9] all the possible strings or numbers, +: 1 or more repetitions of them
            split_url=url_pattern.groups() #It divides it into the four groups                                  # first group, the big one: (http(s)*:\/\/(www\.)*youtube\.com\/embed\/)
            return "https://youtu.be/" + split_url[3]    #We want what's in position 3, which is group 4        #second group: (s), third group:(www\.), fourth group:([a-z_A-Z_0-9]+)




if __name__ == "__main__":
    main()

