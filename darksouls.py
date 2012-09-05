from util import hook, http

# constants
result_xpath = "//div[@id='page-content']/div[@class='search-box']/div[@class='search-results']/div[@class='item'][1]/div[@class='title']/a"
search_url = "http://darksouls.wikidot.com/search:site/q/%s"

def get_wiki_article(inp):
    # using scraping instead of the wikidot api because it sucks
    # it doesn't have a text search, though the site might just be using the api method to select tags anyway
    
    results = http.get_html(search_url % http.quote_plus(inp))
    
    try:
        result = results.xpath(result_xpath)[0]
        page_url = result.values()[0]
    except IndexError:
        return "No Results"

    title = result.text_content()
    return "%s -- %s" % (title, page_url)

@hook.command
def darksouls(inp):
    """ darksouls <query> -- Searches DarkSouls Wiki for <query> """
    return get_wiki_article(inp)

if __name__ == "__main__":
    print get_wiki_article("Solaire") # Praise the Sun!