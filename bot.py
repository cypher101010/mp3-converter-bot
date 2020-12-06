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


    # main command
    if message.content.startswith('!mp3'):

        #get the message content
        msg = message.content        
        print(f'Mesagge content: {msg} \n')


        # regex to find url in the sent message
        url = re.findall(r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', msg)
        print(url)

        if url:

            # check if there are more than one links being sent
            if (len(url) == 1):

                validated_string = 'www.youtube.com/watch?v='

                if(validated_string in url[0]):


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

                            embedVar = discord.Embed(title="Something went wrong :confused:\n\nTry sending a song that is under 7 minutes long, \nbecause of Discord's file size limit.", color=0x0066ff)
                            await message.channel.send(embed=embedVar)

                            os.remove(files)
                            print('File was removed')
                        else:                
                            await message.channel.send(file=discord.File(files))
                            print('File was sent...\n')

                            os.remove(files)
                            print('File was deleted...\n')  
                else:

                    embedVar = discord.Embed(title="Something went wrong :confused:\n\nIt seems like you didn't send a valid Youtube video link.", color=0x0066ff)
                    await message.channel.send(embed=embedVar)

                    print('The link was not valid')

            else: 

                embedVar = discord.Embed(title="Something went wrong :confused: \n\nIt looks like you sent more than one url's, please send one url at time.", color=0x0066ff)
                await message.channel.send(embed=embedVar)
        else:

            embedVar = discord.Embed(title="List of commands with examples: \n\n- !mp3 [youtube video link]\n - !help \n\n ** Important: The video length must be under 7 minutes long. **", color=0x0066ff)
            await message.channel.send(embed=embedVar)




    # help command
    if message.content.startswith('!help'):
        embedVar = discord.Embed(title="List of commands with examples: \n\n- !mp3 [youtube video link]\n - !help \n\n ** Important: The video length must be under 7 minutes long. **", color=0x0066ff)
        await message.channel.send(embed=embedVar)





client.run(os.environ['DISCORD_TOKEN'])


