from bs4 import BeautifulSoup
import requests
# import chardet

response = requests.get("https://news.ycombinator.com/news")    # removed: , verify=False)
webpage_html_document = response.text

# PRINT THE WHOLE HTML DOC ONLY IF YOU NEED IT (will take up a lot of space in the console)
# print(webpage_html_document)

score_id = 'score_39530203'


soup = BeautifulSoup(webpage_html_document, "html.parser")  # we want to pass the html document that we want to parse (yc_webpage), then we provide the Method of which we are going to parse it with.
# NOW: dig in, and find the parts that we want out of the html doc.

# print(soup.title)  # For example, if we want the tab Title name, use print(soup.title)

  # what if we wanted to get a hold of the text that is the title of the first story link?

article_tag_first_yc_story_link = soup.find(name="a", href="https://overkill.wtf/nintendo-sue-yuzu-emulator/")
article_upvote_tag = soup.find('span', id=score_id)
article_upvote = article_upvote_tag.getText()


# print(f"The <a> tag line is: {article_tag_first_yc_story_link}")    # the <a> tag line:  <a href="https://overkill.wtf/nintendo-sue-yuzu-emulator/">Nintendo is suing the creators of Switch emulator Yuzu</a>
# print(f"The .getText Method of article_tag_first_yc_story_link is: {article_tag_first_yc_story_link.getText()}\n")  # to GET the Text INSIDE/WITHIN the anchor tag:

# print(f"The Title of the article is: {article_tag_first_yc_story_link.text}")   # text of the article title itself: Nintendo is suing the creators of Switch emulator Yuzu

article_text = article_tag_first_yc_story_link.getText()
article_link = article_tag_first_yc_story_link.get("href")  #looking for the Value: href
# article_upvote = soup.find(name="span", class_="score")  # <span class="score" id="score_39530203">480 points</span>

print(f"The Title of the article is: {article_text}")
print(f"The article URL Link itself is: {article_link}")
print(f"The article Upvote Score is: {article_upvote}")

# print(article_text)

# print(f"The Upvote point score.text is currently: {article_upvote.text}")
# print(f"The Upvote point score.getText() is currently: {article_upvote.getText()}")

# OR:

# article_upvote = soup.find(name="span", class_="score").getText()  # <span class="score" id="score_39530203">480 points</span>
# print(f"Using a different Method of .getText(), the article_upvote is: {article_upvote}")


