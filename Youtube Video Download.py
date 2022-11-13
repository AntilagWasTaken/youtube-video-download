from pytube import YouTube
from pystyle import Colors, Colorate
link = str(input(Colorate.Horizontal(Colors.blue_to_cyan,"Your YouTube Link: ",1)))
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
print("Download Successful!!")