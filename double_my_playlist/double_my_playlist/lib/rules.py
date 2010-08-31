from double_my_playlist.lib import lastfm

def everything_gets_five(originals, fetched):
    """This is a debugging rule that sets the score for all songs to 5."""
    results = []
    for f in fetched:
        results.append(lastfm.TrackSearchResult(f.track, 5))
    return results
