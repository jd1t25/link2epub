import requests
from bs4 import BeautifulSoup as bs
from ebooklib import epub

# URL of the chapter
url = "https://novelbin.me/novel-book/shadow-slave/chapter-1-nightmare-begins"

# Send a GET request to fetch the webpage content
urlpage = requests.get(url)
urldoc = bs(urlpage.text, "html.parser")

# Find the content of the chapter (assuming it's in a div with class 'chr-c')
content_div = urldoc.find("div", class_="chr-c")

# Extract the title (assuming it's inside an <h4> tag inside the content)
title_tag = content_div.find("h4")
chapter_title = title_tag.get_text() if title_tag else "Untitled Chapter"

# Extract the chapter content (assuming it's the rest of the div)
chapter_content = content_div.prettify()


# Create an EPUB file
def create_ebook(content, title):
    book = epub.EpubBook()
    book.set_identifier("id123456")
    book.set_title("Shadow Slave")  # You can change the main book title here
    book.set_language("en")

    # Create a list to store the TOC (Table of Contents)
    toc_items = []

    # Add the chapter content
    chapter_item = epub.EpubHtml(
        title=title, file_name="Chapter1.xhtml", content=chapter_content
    )

    # Add the chapter to the book and TOC
    book.add_item(chapter_item)
    toc_items.append(chapter_item)
    book.spine.append(chapter_item)

    # Set the TOC for the EPUB
    book.toc = toc_items

    # Add the navigation (NCX and Nav) files
    book.add_item(epub.EpubNav())  # Navigation file for modern readers
    book.add_item(epub.EpubNcx())  # NCX file for older EPUB readers

    # Write the EPUB file to disk
    epub.write_epub("shadow_slave_ebook.epub", book)
    print("Ebook created successfully with TOC and Navigation!")


# Create the ebook with the extracted chapter content and title
create_ebook(chapter_content, chapter_title)

