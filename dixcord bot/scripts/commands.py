import discord
import random
from discord import guild
from discord import member
from discord import file
from discord import message
from discord.ext import commands
from discord.ext.commands.core import has_permissions, has_role
from main import client

class Handler(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def back_me_up(self, ctx):
        if str(ctx.message.author) == 'Senpairo#2528':
            await ctx.send('wow senpai, your like soooo right and everyone who says otherwise is like sooo wrong')
        else:
            await ctx.send('no')

    @commands.command()
    async def when_is_p5s_getting_a_western_release(self, ctx):
        await ctx.send('...')
        await ctx.send('...')
        await ctx.send('...')
        await ctx.send('...')
        await ctx.send('...')
        await ctx.send('...')
        await ctx.send('good question')

    @commands.command()
    async def explain(self, ctx):
        await ctx.send('hi my name is sexy toaster, i am a bot created by this super awesome really cool guy called senpairo, i was created to do (insert something usefull here) anyways, leave suggestions for what i should do')

    @commands.command()
    async def rnd_smash(self, ctx, ):
        characters = ["mario", "donkey kong", "link", "samus", "yoshi", "kirby", "fox", "pikachu", "luigi", "ness", "captain falcon", "jigglypuff", "peach", "bowser", "ice climbers", "sheik", "zelda", "dr. mario", "pichu", "falco", "marth", "young link", "ganondorf", "mewtwo", "roy", "mr. game and watch", "metaknight", "pit", "zero suit samus", "wario", "snake","ike", "pokemon trainer", "diddy kong", "lucas", "sonic", "king dedede", "olimar", "lucario", "R.O.B", "toon link", "wolf", "villager", "MEGAMAN", "wii fit trainer", "rosalina & luma", "little mac", "greninja", "mii gunner", "mii fighter", "mii swordsman", "palutena", "pacman", "robin", "shulk", "bowser jr", "duck hunt duo", "lucina", "dark pit", "ryu", "cloud", "corrin", "bayonetta", "inkling", "daisy", "dark samus", "chrom", "ridley", "simon belmont", "richter", "king k.rool", "isabelle", "ken", "incineroar", "piranha plant", "JOKER FROM PERSONA 5", "hero", "banjo & kazooie", "terry bogard", "byleth", "min min", "STEEEEEEVE"]
        await ctx.send(random.choice(characters))
    
    @commands.command()
    async def kill(self, ctx, member, *, after=""):
        await ctx.send(f"killing {member} {after} in process")
        await ctx.send('...')
        await ctx.send('...')
        await ctx.send('...')
        await ctx.send('...')
        await ctx.send('...')
        await ctx.send('...')
        await ctx.send('...')
        await ctx.send(f"succesfully killed {member} {after}")
    
    @commands.command()
    async def send_nudes(self, ctx):
        pics_array = ['https://cdn.discordapp.com/attachments/653960437112635406/774256227369877514/20201106_145732.jpg', 'https://cdn.discordapp.com/attachments/773997385717252129/775348868446552064/Z.png', 'https://cdn.discordapp.com/attachments/663798504682029096/775349600785530891/Screenshot_20200211-192727_TikTok.jpg', 'https://cdn.discordapp.com/attachments/663798504682029096/775349845778366474/Screenshot_20201101-085510_Instagram.jpg', 'https://cdn.discordapp.com/attachments/663798504682029096/775349916515565578/Screenshot_20201011-215015_Instagram.jpg', 'https://cdn.discordapp.com/attachments/663798504682029096/775349997146472448/Screenshot_20201019-171217_Instagram.jpg', 'https://cdn.discordapp.com/attachments/773538182683557889/774388789098577940/20201106_234408.jpg', 'https://cdn.discordapp.com/attachments/773538182683557889/773937924403888168/sketch-1604327984843.jpg', 'https://cdn.discordapp.com/attachments/653933938427035650/756979780347232286/luigi.jpg', 'https://cdn.discordapp.com/attachments/707163826369331253/774943954675826738/MORGANA_TRANSFORM.gif', 'https://cdn.discordapp.com/attachments/653960437112635406/775352768008945684/DA_G-MAN.jpg', 'https://cdn.discordapp.com/attachments/653960437112635406/775352774665568256/donkey_kong_cosplay.jpg', 'https://cdn.discordapp.com/attachments/653960437112635406/775352775831715860/donkey_kong_2.jpg',  'https://cdn.discordapp.com/attachments/653960437112635406/775352776145502208/donkey_kong.jpg', 'https://cdn.discordapp.com/attachments/653960437112635406/775352781053231124/donkey_kong.png', 'https://cdn.discordapp.com/attachments/653960437112635406/775352816390373376/elmo_on_fire.gif', 'https://cdn.discordapp.com/attachments/653960437112635406/775352843414536232/dancing_spider-man.gif', 'https://media.tenor.com/images/8566d06f18ee38247a28719d9aa55355/tenor.gif','https://media.tenor.com/images/d0f644525d3be9eb3b287edca97d20f4/tenor.gif','https://media.tenor.com/images/01eb0b47e0919f8b02407010a08960dd/tenor.gif']
        await ctx.send(random.choice(pics_array))

    @commands.command()
    async def send_zoom(self, ctx, the_class=""):
        if the_class == "ערבית":
            await ctx.send('https://edu-il.zoom.us/j/7328072750')
        elif the_class == "כישורי חיים":
            await ctx.send('https://edu-il.zoom.us/j/96050052341?pwd=RndxY0M4RElXQzRpV2dXeGpXdVdaQT09')
        elif the_class == "ספורט":
            await ctx.send('https://us04web.zoom.us/j/75667411544?pwd=bm1jZ1F0b0syVnZJSjduYUtOc1h0dz09')
        elif the_class == "חינוך":
            await ctx.send('https://edu-il.zoom.us/j/92207525681?pwd=czJqblZpSzZkaGREZVVmVFV6UHlYdz09')
        elif the_class == "מדעים":
            await ctx.send('https://edu-il.zoom.us/j/92439764649?pwd=Q2NkNWVKdmtiVVB2VllPNG5vdVdlZz09')
        elif the_class == "מתמטיכיף":
            await ctx.send('https://edu-il.zoom.us/j/94422187142?pwd=MUJmRG8xR0w4WitiWVVHYmNZaWlBdz09')
        elif the_class == "מתמטיקה":
            await ctx.send('https://edu-il.zoom.us/j/6029618489?pwd=VlZidW84Z3E2L3RCK2hKWWg1ZzRUQT09')
        elif the_class == "ספרות":
            await ctx.send('https://edu-il.zoom.us/j/3557883542')
        elif the_class == "שלח":
            await ctx.send('https://edu-il.zoom.us/j/6044478281')
        elif the_class == "אזרחות":
            await ctx.send('https://edu-il.zoom.us/j/93395805154?pwd=dm0vY2ozc3pOUWV0MGdlazlaTHJSUT09')
        elif the_class == "אנגלית":
            await ctx.send('https://us04web.zoom.us/j/72069513802?pwd=NEs1Ym1xbnRBS0U4ZWNsaXFzbm1Ndz09')
        elif the_class == "עברית":
            await ctx.send('https://edu-il.zoom.us/j/93926817554?pwd=YldIRWUwbmhOTlFNdTdsZkZzUmRZQT09')
        elif the_class == "תקשורת":
            await ctx.send('https://edu-il.zoom.us/j/92207525681?pwd=czJqblZpSzZkaGREZVVmVFV6UHlYdz09')
        elif the_class == "היסטוריה":
            await ctx.send('https://edu-il.zoom.us/j/96656013660?pwd=Um5BeE9CRktySm9UbWNPUDErcitKQT09')
        else:
            await ctx.send('class not found, the avalibe classes are: ערבית, כישורי חיים, ספורט, חינוך, מדעים, מתמטיכיף, מתמטיקה, ספרות, שלח, אזרחות, אנגלית, עברית, תקשורת, היסטוריה')
    # @client.command()
    # @commands.has_role(role_check_test=True)
    # async def role_checker(self, ctx):
    #      await ctx.send("working")
            

def setup(client):
    client.add_cog(Handler(client))
