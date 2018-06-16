import xbmc
import os

# xbmc.executebuiltin( "PlayMedia(/Users/krsna/Desktop/media/), isdir" ) # playing videos by themselves, pictures are skipped
# xbmc.executebuiltin("RecursiveSlideShow(/Users/krsna/Desktop/media/)") # playing pictures by themselves, video blacks out and plays in background
# xbmc.executebuiltin( "PlayerControl(RepeatAll)" )
# .m4v|.3g2|.3gp|.nsv|.tp|.ts|.ty|.strm|.pls|.rm|.rmvb|.mpd|.m3u|.m3u8|.ifo|.mov|.qt|.divx|.xvid|.bivx|.vob|.nrg|.img|.iso|.pva|.wmv|.asf|.asx|.ogm|.m2v|.avi|.bin|.dat|.mpg|.mpeg|.mp4|.mkv|.mk3d|.avc|.vp3|.svq3|.nuv|.viv|.dv|.fli|.flv|.rar|.001|.wpl|.zip|.vdr|.dvr-ms|.xsp|.mts|.m2t|.m2ts|.evo|.ogv|.sdp|.avs|.rec|.url|.pxml|.vc1|.h264|.rcv|.rss|.mpls|.webm|.bdmv|.wtv|.pvr|.disc
# .png|.jpg|.jpeg|.bmp|.gif|.ico|.tif|.tiff|.tga|.pcx|.cbz|.zip|.cbr|.rar|.rss|.webp|.jp2|.apng

supported_images = ["jpg", "jpeg"]
supported_videos = ["mp4", "m4v", "3gp", "mov", "wmv", "avi", "flv", "h264", "ogv"]
supported_medias = ["jpg", "jpeg", "mp4"]

media_directory = "/Users/krsna/Desktop/media"
media_directory_content = os.listdir(media_directory)

medias = [media_directory + "/" + files for files in media_directory_content if files.split(".")[1] in supported_medias]
images = [media_directory + "/" + files for files in media_directory_content if files.split(".")[1] in supported_images]
videos = [media_directory + "/" + files for files in media_directory_content if files.split(".")[1] in supported_videos]

xbmc.log(str(medias), 2)
xbmc.log(str(images), 2)
xbmc.log(str(videos), 2)

video_playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

for video in videos:
    video_playlist.add(url=video)

xbmc.Player().play(video_playlist)
