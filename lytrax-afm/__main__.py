import re
from utils import get_random_int
from _validation import validate_afm

def main():
    """Read the Real Python article feed"""
    print("Testing!!!")

    afm = '130558790'
    if not re.match(r"^\d+$", afm):
        print("invalid")
    else:
        print("valid")

    print(validate_afm(afm))

    # print("00000000" == "0" * 9)

    print("1234567"[:5])

    for index in range(len(afm)):
        print("idx %i, c %c" % (index, afm[index]))

    #print(get_random_int(0, 9, 5))
    # Read URL of the Real Python feed from config file
    # cfg = ConfigParser()
    # cfg.read_string(resources.read_text("reader", "config.txt"))
    # url = cfg.get("feed", "url")

    # # If an article ID is given, show the article
    # if len(sys.argv) > 1:
    #     article = feed.get_article(url, sys.argv[1])
    #     viewer.show(article)

    # # If no ID is given, show a list of all articles
    # else:
    #     site = feed.get_site(url)
    #     titles = feed.get_titles(url)
    #     viewer.show_list(site, titles)

if __name__ == "__main__":
    main()
