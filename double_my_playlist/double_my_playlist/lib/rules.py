from double_my_playlist.lib import lastfm

def everything_gets_five(originals, fetched):
    """This is a debugging rule that sets the score for all songs to 5."""
    results = []
    for f in fetched:
        results.append(lastfm.TrackSearchResult(f.track, 5))
    return results

def identity(originals, fetched):
    """Returns all tracks with their scores unmodified."""
    return fetched

def remove_repeat_artists(originals, fetched):
    """Sets the score to 0 for any artists that are in the original list.

    Also sets the score to 0 for all fetched songs that are repeats in the fetched list if they're not the highest.
    """
    artists = [x.artist for x in originals]
    results = []
    for result in fetched:
        if result.track.artist in artists:
            results.append(lastfm.TrackSearchResult(result.track, 0))
        else:
            results.append(lastfm.TrackSearchResult(result.track, 100))
            artists.append(result.track.artist)
    return results
