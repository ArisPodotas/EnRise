import os
import re
import argparse

def main():
    # News.html section
    def makeEntry():
        query = open("./news.html", "r")
        file = query.readlines()
        query.close()
        for line in file:
            if re.search():
                pass
    # Article section
    def makeArticle():
        articel = f'''
            <main>
                <div class="bounder" id="bounding">
                    <div class="topdown" id = 'bisection'>
                       <img src="{}" id = 'gbox' class="head">
                       <div>{}
                       </div>
                    </div>
                </div>
            </main>
            '''

if __name__ == "__main__":
    main()

