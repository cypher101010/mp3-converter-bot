# TODO: implement title song seacrh by using the youtubesearch library 

import discord, youtube_dl, re, os, glob, mp3
from os.path import getsize


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user} \n'.format(client))





@client.event
async def on_message(message):


    if message.author == client.user:
        return

    if message.content.startwith('!'):
        embedVar = discord.Embed(title="Sorry, we changed our call sign from ! to - .\\You also don't need to write -mp3 [youtube link] just - [youtube link]\\For example:\\ - https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=0x0066ff)

        await message.channel.send(embed=embedVar)


    # main command
    if message.content.startswith('-'):

        #get the message content
        msg = message.content        
        print(f'Mesagge content: {msg} \n')


        # regex to find url in the sent message
        url = re.findall(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', msg)
        print(url)

        if url:

            # check if there are more than one links being sent
            if (len(url) == 1):

                validated_yt_url_1 = 'https://www.youtube.com/watch?v='
                validated_yt_url_2 = 'https://youtu.be/'

                if(validated_yt_url_1 in url[0] or validated_yt_url_2 in url[0]):


                    print('Youtube link is valid...')

                    mp3.song(url)

                    os.listdir()

                    # get all of the .mp3 file in this directory
                    for files in glob.glob('*.mp3'):

                        # for each .mp3 file get the file size
                        file_size = getsize(files)
                        # convert the file size into an integer
                        file_size = int(file_size)
        
                        # check if the file size is over 8000000 bytes (discord limit for non bosted server's)
                        if file_size > 8000000:
                            print('The file size is over 8MB...\n')

                            embedVar = discord.Embed(title="Something went wrong :confused:\n\nTry sending a song that is under 7 minutes long, \nbecause of Discord's file size limit.\\Check out -help and -info commands.", color=0x0066ff)
                            await message.channel.send(embed=embedVar)

                            os.remove(files)
                            print('File was removed')
                        else:                
                            await message.channel.send(file=discord.File(files))
                            print('File was sent...\n')

                            os.remove(files)
                            print('File was deleted...\n')  
                else:

                   
                    await message.channel.send(embed=embedVar)

                    print('The link was not valid')

            else: 

                embedVar = discord.Embed(title="Something went wrong :confused: \n\nIt looks like you sent more than one url's, please send one url at time.\\Check out -help and -info commands.", color=0x0066ff)
                await message.channel.send(embed=embedVar)
        else:

            embedVar = discord.Embed(title="It seems like didn't send a proper youtube video link.\\Check out -help and -info commands. \\Note: We are working on adding search by title support and we hope to implement it soon, Zae.", color=0x0066ff)
            await message.channel.send(embed=embedVar)




    # help command
    if message.content.startswith('-help'):
        embedVar = discord.Embed(title="List of commands with examples: \n\n - [youtube video link]\n -help\n\n -info \n\n ** Important: The video length must be under 7 minutes long. **", color=0x0066ff)
        await message.channel.send(embed=embedVar)

    
    #info command
    if message.content.startswith('-info'):
        embedVar = discord.Embed(title="Bot information: \n\nGithub: [not public yet]\n\nCreated by Zae", color=0x0066ff)
        await message.channel.send(embed=embedVar)







client.run(os.environ['DISCORD_TOKEN'])


