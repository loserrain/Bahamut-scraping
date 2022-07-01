import scrapy 




class BHItem(scrapy.Item):

    artcle_title = scrapy.Field()
    text = scrapy.Field()

    def __repr__(self):
        return 'artcle_title: {}, text: {}'.format(self['artcle_title'], self['text'])

    
