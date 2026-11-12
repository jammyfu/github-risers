"""Prevent localized landing pages drifting away from visible content and navigation."""
import json
import re
import sys
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import render_site

class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.links=[];self.lang=None;self.h1=0;self.details=0;self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.lang=a.get('lang')
        if tag=='h1':self.h1+=1
        if tag=='details':self.details+=1
        if tag=='link':self.links.append(a)

class SiteTests(unittest.TestCase):
    def test_generated_site_is_current(self):
        self.assertEqual(render_site.main(['--check']),0)
    def test_all_locales_are_complete_and_reciprocal(self):
        locales=json.loads((ROOT/'tools/site_locales.json').read_text())
        self.assertEqual(set(locales),set(render_site.LANGS))
        for code,s in locales.items():
            self.assertEqual(len(s['faq']),8);self.assertEqual(len(s['facts']),6)
            self.assertEqual(len(s['docs']),8);self.assertEqual(len(s['headings']),4)
            text=render_site.render(code,s);page=Page(text)
            self.assertEqual(page.lang,code);self.assertEqual(page.h1,1);self.assertEqual(page.details,8)
            links={a.get('hreflang'):a['href'] for a in page.links if a.get('rel')=='alternate'}
            self.assertEqual(links,{**{c:render_site.page_url(c) for c in locales},'x-default':render_site.BASE})
            self.assertIn({'rel':'canonical','href':render_site.page_url(code)},page.links)
            schema=[json.loads(x) for x in re.findall(r'<[s]cript type="application/ld\+json">(.*?)</script>',text,re.S)]
            faq=next(x for x in schema if x['@type']=='FAQPage')
            self.assertEqual(faq['inLanguage'],code)
            self.assertEqual([(q['name'],q['acceptedAnswer']['text']) for q in faq['mainEntity']],[tuple(x) for x in s['faq']])
            self.assertNotRegex(text, r'<[s]cript\s+src=')
    def test_sitemap_has_all_five_destinations(self):
        doc=ET.fromstring(render_site.outputs()[Path('docs/sitemap.xml')])
        ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9','x':'http://www.w3.org/1999/xhtml'}
        self.assertEqual({x.text for x in doc.findall('s:url/s:loc',ns)},{render_site.page_url(c) for c in render_site.LANGS})
        for url in doc.findall('s:url',ns):self.assertEqual(len(url.findall('x:link',ns)),6)
    def test_machine_navigation_matches_site(self):
        self.assertEqual((ROOT/'llms.txt').read_bytes(),(ROOT/'docs/llms.txt').read_bytes())
        for code in render_site.LANGS:
            self.assertIn(render_site.page_url(code),(ROOT/'llms.txt').read_text())

if __name__=='__main__':unittest.main()
