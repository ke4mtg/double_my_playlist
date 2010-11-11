import lastfm

def split_duration(duration):
    seconds = (duration / 1000) % 60
    minutes = (duration / 1000) / 60
    hours = (duration / 1000) / 3600

    return hours, minutes, seconds

def format_duration(duration):
    hours, minutes, seconds = split_duration(duration)

    if hours: 
        return '%d:%02d:%02d' % (hours, minutes, seconds)
    else:
        return '%d:%02d' % (minutes, seconds)


if __name__ == '__main__':
    api = lastfm.Api('578ff28eb42a625b4beb7cd1ec8c1dae')
    track = api.get_track('Sweet Disposition', artist='The Temper Trap')
    
    for similar in track.similar:
        try:            
            print '"%s" by %s' % (similar.name, similar.artist.name)
        except AttributeError, e:
            # there's no artist, album, position, etc for this track, so just exit out for now
            pass
