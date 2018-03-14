import discord
from discord.ext import commands

bot = commands.Bot(description="elliot alderson", command_prefix=":)")

@bot.command()
async def hi():
    await bot.say("hello friend")

@bot.command()
async def ily():
    await bot.say("love you too")

@bot.command()
async def quote():
    await bot.say("How do we know if we’re in control? That we’re not just making the best of what comes at us, and that’s it. Trying to constantly pick between two options. Like your two paintings in the waiting room. Or Coke and Pepsi. McDonald’s or Burger King? Hyundai or Honda? It’s all part of the same blur, right? Just out of focus enough. It’s the illusion of choice. Half of us can’t even pick our own our cable, gas, electric. The water we drink, our health insurance. Even if we did, would it matter? You know, if our only option is Blue Cross or Blue Shield, what the f*** is the difference? In fact, aren’t they the same? No, man, our choices are prepaid for us, long time ago.")

@bot.command(pass_context=True)
async def say(ctx, *, something=None):
    if something is None:
        await bot.say("Hm? Sorry, I thought you were gonna ask something.")
    else:
        await bot.say(something)

@bot.command()
async def peepee():
    await bot.say("**PEEPEE**")

@bot.command()
async def pickle():
    await bot.say("my pickle is the same size as izzy's")


@bot.event
async def on_message(message):
    if message.content.startswith('elliot we love you'):
        await bot.send_message(message.channel, '<3')
    if message.content.startswith(':)hello'):
        await bot.send_message(message.channel, 'I\'m afraid I don\'t understand.')
    if message.content.startswith('he\'s cool'):
        await bot.send_message(message.channel, 'thanks, qwerty')

    await bot.process_commands(message)


    
bot.run("NDE2MDA2OTIzMzE4NDYwNDI3.DW-lTw.soaBuSHipnar3ff7G6Buz927UYo")
