# MP3 CONVERTER BOT

[![iconfinder-file-type-document-format-computer-mp3-music-3280449.png](https://i.postimg.cc/02fN6DTK/iconfinder-file-type-document-format-computer-mp3-music-3280449.png)](https://postimg.cc/Yhv7ZGqt)

__MP3 Converter is a discord bot for convreting youtube video links in .mp3 files wich it then sent to users.__


## Example command:
 * -a [example youtube video link]
 
 
## How it works:
 * Bot receives a message from a user
 * Bot checks if the message you sent contains a link
 * Bot check if the message contains more than one links
 * Bot check if you sent a valid youtube video link - security check
 * The valid yt link is passed to the youtube_dl library
 * Youtube_dl library downloads the youtube video within seconds
 * Bot checks if the file size of the downloaded mp3 file is over 8MB
 * Bot sends a message with the file embeeded

!Note: Unless you're discord server is boosted then you wont be able to convert videos longer that 7 minutes.
 
 
