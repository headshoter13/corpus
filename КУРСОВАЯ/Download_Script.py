import mechanize
import urllib
import urllib2
import re
import os
import time

def subtitle(link):
    #browser = openBrow('http://www.opensubtitles.org/ru/login/redirect-%7Cru')
    for film in range(90,100):
        #browser.open('http://www.opensubtitles.org/addons/clear_cookie.html')
        time.sleep(4)
        films_id = links_to_others('" href="/ru/subtitles/([0-9]+)/.*?">', 'http://www.opensubtitles.org/ru/search/sublanguageid-all/idmovie-', film)
        for number in films_id:
            try:
                name = folders_names('http://www.opensubtitles.org/ru/subtitles/', 'hreflang="ar" href="http://www.opensubtitles.org/ar/subtitles/' + str(number) + '(.*?)"', number)
                browser = openBrow('http://www.opensubtitles.org/ru/login/redirect-%7Cru')
                browser.retrieve(link + str(number), './/subs//' + name[:-3] + '//' + name + '.zip')
                time.sleep(2)
                browser.close()
            except:
                continue
    #browser.close()


def links_to_others(reg_exp, link, film):
    reg_srt = '(</a><br/><span class="p">srt</span></td>.*href="/ru/subtitles/[0-9]+/.+?)">'
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open(link + str(film)).read().decode('utf-8')
    srt_text = re.findall(reg_srt, page)
    films_id = re.findall(reg_exp, str(srt_text))
    return films_id


def folders_names(link1, reg_exp, number):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open(link1 + str(number)).read().decode('utf-8')
    name = re.findall(reg_exp, page)
    if not os.path.exists('.//subs//' + name[0][:-3]):
        os.makedirs('.//subs//' + name[0][:-3])
    return name[0]


def openBrow(auth,USERNAME = 'headshoter13', PASSWORD = 'qwerty143'):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko')]
    browser.open(auth)
    browser.select_form(nr = 0)
    browser.form['user'] = USERNAME
    browser.form['password'] = PASSWORD
    browser.submit()
    return browser

subtitle('http://dl.opensubtitles.org/en/download/sub/vrf-108d030f/')


