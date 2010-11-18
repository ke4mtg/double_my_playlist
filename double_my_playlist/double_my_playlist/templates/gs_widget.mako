<%def name="show_widget(songs)">
<object width="250" height="400">
<param name="movie" value="http://listen.grooveshark.com/widget.swf" />
<param name="wmode" value="window" />
<param name="allowScriptAccess" value="always" />
<param name="flashvars" value="hostname=cowbell.grooveshark.com&songIDs=${','.join(songs)}&style=metal&bbg=000000&bfg=666666&bt=FFFFFF&bth=000000&pbg=FFFFFF&pbgh=666666&pfg=000000&pfgh=FFFFFF&si=FFFFFF&lbg=FFFFFF&lbgh=666666&lfg=000000&lfgh=FFFFFF&sb=FFFFFF&sbh=666666&p=0" />
<embed src="http://listen.grooveshark.com/widget.swf" type="application/x-shockwave-flash" width="250" height="400" flashvars="hostname=cowbell.grooveshark.com&songIDs=${','.join(songs)}&style=metal&bbg=000000&bfg=666666&bt=FFFFFF&bth=000000&pbg=FFFFFF&pbgh=666666&pfg=000000&pfgh=FFFFFF&si=FFFFFF&lbg=FFFFFF&lbgh=666666&lfg=000000&lfgh=FFFFFF&sb=FFFFFF&sbh=666666&p=0" allowScriptAccess="always" wmode="window" />
</object>
</%def>


