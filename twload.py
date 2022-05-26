from datetime import datetime

def tload(tw):
    ruid = ''
    rcreate = ''
    rfulltext = ''
    rretweet = ''
    rfavorite = ''
    rsource = ''

    try:
        uid = tw.retweeted_status.id
        create  = datetime.strptime(tw.retweeted_status.created_at, '%a %b %d %H:%M:%S +0000 %Y').strftime("%A %d %b %Y %H:%M") 
        fulltext = tw.retweeted_status.full_text
        retweet = tw.retweeted_status.retweet_count
        favorite = tw.retweeted_status.favorite_count
        source = tw.retweeted_status.source

        ruid = tw.id
        rcreate  = datetime.strptime(tw.created_at, '%a %b %d %H:%M:%S +0000 %Y').strftime("%A %d %b %Y %H:%M")
        rfulltext = tw.full_text
        rretweet = tw.retweet_count
        rfavorite = tw.favorite_count
        rsource = tw.source

    except AttributeError:
        uid = tw.id
        create  = datetime.strptime(tw.created_at, '%a %b %d %H:%M:%S +0000 %Y').strftime("%A %d %b %Y %H:%M")
        fulltext = tw.full_text
        retweet = tw.retweet_count
        favorite = tw.favorite_count
        source = tw.source
    
    tw = {'id': uid, 'create': create, 'fulltext': fulltext, 'retweet': retweet, 'favorite': favorite, 'source': source}
    rtw = {'id': ruid, 'create': rcreate, 'fulltext': rfulltext, 'retweet': rretweet, 'favorite': rfavorite, 'source': rsource}
    
    return tw, rtw