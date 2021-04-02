import discord
import asyncio
import random
import string
import requests
from bs4 import BeautifulSoup
import urllib.request
import datetime
import os
import sys




client = discord.Client()

token = "ODEyNTc0OTY1NzY4NjUwODIz.YDCvaA.eg3ycIIghX3AsgBFZ6KSpeTipEo"

@client.event
async def on_ready():

    print(client.user.name)
    print('봇 실행 완료!!!')
    game = discord.Game('일')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content == "독도는":
        await message.channel.send("우리땅")
    if message.content == "박순민":
        await message.channel.send("바보")
    if message.content == "!":
        await message.channel.send("https://discord.gg/qZbquHxmmj")

    
    if message.content.startswith('!소라고동'):
        ran = random.randint(0,5)
        if ran == 0:
            d = "YES"
        if ran == 1:
            d = "YES"
        if ran == 2:
            d = "YES"
        if ran == 3:
            d = "NO"
        if ran == 4:
            d = "NO"
        if ran == 5:
            d = "NO"
        await message.channel.send(d)


    if message.content.startswith('!니트로'):
        ranNitro = ""
        for i in range(0, 16):
            ranNitro += str(random.choice(string.ascii_letters))
            NitroEmbed = discord.Embed(title='니트로 생성기', description='https://discord.gift/' + ranNitro)
        await message.channel.send(embed=NitroEmbed)

    
    if message.content.startswith('!한강온도'):
        json = requests.get('http://hangang.dkserver.wo.tc/').json()
        temp = json.get("temp") # 한강온도
        time = json.get("time") # 측정시간
        embed = discord.Embed(title='💧 한강온도', description=f'{temp}°C', colour=discord.Colour.blue())
        embed.set_footer(text=f'{time}에 측정됨')
        await message.channel.send(embed=embed)


    if message.content.startswith('!주사위'):
        randomNum = random.randrange(1, 7)
        if randomNum == 1:
            await message.channel.send(embed=discord.Embed(description=':one:', color=0x7C40E5))
        if randomNum == 2:
            await message.channel.send(embed=discord.Embed(description=':two:', color=0x7C40E5))
        if randomNum == 3:
            await message.channel.send(embed=discord.Embed(description=':three:', color=0x7C40E5))
        if randomNum == 4:
            await message.channel.send(embed=discord.Embed(description=':four:', color=0x7C40E5))
        if randomNum == 5:
            await message.channel.send(embed=discord.Embed(description=':five:', color=0x7C40E5))
        if randomNum == 6:
            await message.channel.send(embed=discord.Embed(description=':six: ', color=0x7C40E5))

    
    if message.content.startswith('!위성'):
        url = 'https://www.weather.go.kr/weather/images/satellite_service.jsp'
        res = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(res, 'html.parser')
        soup = soup.find("div", class_="image-player-slide")
        imgUrl = 'https://www.weather.go.kr' + soup.find("img")["src"]

        typoonEmbed = discord.Embed(title='천리안 2A호 위성사진', description='제공: 기상청', colour=discord.Colour.dark_grey())
        typoonEmbed.set_image(url=imgUrl)
        await message.channel.send(embed=typoonEmbed)


    if message.content.startswith('!dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    #메시지 관리권한이 있을시 사용가능
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(color=0x1DDB16, timestamp=message.created_at)
                        embed.add_field(name="★★제목★★", value=msg, inline=True)
                        embed.set_footer(text="★맨 밑에 들어갈 내용★")
                        await i.send(embed=embed)
                except:
                    pass


    if message.content.startswith('!코로나'):
        url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        datecr = soup.find('span', {'class': 't_date'}) #기준날짜
        #print(f'기준일: {datecr.string}')
        totalcovid = soup.select('dd.ca_value')[0].text #누적 확진자수
        #print(f'누적 확진자: {totalcovid} 명')
        todaytotalcovid = soup.select('p.inner_value')[0].text #당일 확진자수 소계
        #print(f'확진자 소계: {todaytotalcovid} 명')
        todaydomecovid = soup.select('p.inner_value')[1].text #당일 국내발생 확진자수
        #print(f'국내발생: {todaydomecovid} 명')
        todayforecovid = soup.select('p.inner_value')[2].text #당일 해외유입 확진자수
        #print(f'해외유입: {todayforecovid} 명')
        totalca = soup.select('dd.ca_value')[2].text #누적 격리해제
        #print(f'누적 격리해제: {totalca} 명')
        todayca = soup.select('span.txt_ntc')[0].text #당일 격리해제
        #print(f'격리해제: {todayca} 명')
        totalcaing = soup.select('dd.ca_value')[4].text #누적 격리중
        #print(f'누적 격리중: {totalcaing}')
        todaycaing = soup.select('span.txt_ntc')[1].text #당일 격리중
        #print(f'격리중: {todaycaing} 명')
        totaldead = soup.select('dd.ca_value')[6].text #누적 사망자
        #print(f'누적 사망자: {totaldead} 명')
        todaydead = soup.select('span.txt_ntc')[2].text #당일 사망자
        #print(f'사망자: {todaydead} 명')
        covidembed = discord.Embed(title='코로나19 국내 발생현황', description="", color=0xFF0F13, url='http://ncov.mohw.go.kr/')
        covidembed.add_field(name='🦠 확진환자', value=f'{totalcovid}({todaytotalcovid}) 명'
                                                f'\n\n국내발생: {todaydomecovid} 명\n해외유입: {todayforecovid} 명', inline=False)
        covidembed.add_field(name='😷 격리중', value=f'{totalcaing}({todaycaing}) 명', inline=False)
        covidembed.add_field(name='🆓 격리해제', value=f'{totalca}({todayca}) 명', inline=False)
        covidembed.add_field(name='💀 사망자', value=f'{totaldead}({todaydead}) 명', inline=False)
        covidembed.set_footer(text=datecr.string)
        await message.channel.send(embed=covidembed)


    if message.content.startswith("!문재인"):
        time1= datetime.datetime(2022, 5, 9, 0, 0, 0)
        time2 = datetime.datetime.now()

        await message.channel.send("문재인년의 임기기간은 {0}일 남았습니다.".format((time1-time2).days+1))


    if message.content == '!핑':
        ping= round(client.latency * 1000)
        if ping >= 0 and ping <= 100:
            pings = "매우좋음"
        elif ping >= 101 and ping <= 200:
            pings = "좋음" 
        elif ping >= 201 and ping <= 500:
            pings = "보통"
        elif ping >= 501 and ping <= 1000:
            pings = "나쁨"
        elif ping >= 1000:
            pings = "매우나쁨"
        embed = discord.Embed(title=':ping_pong:퐁!', colour = message.author.colour)
        embed.add_field(name = '핑', value=f'{ping}ms')
        embed.add_field(name = '상태:', value=f"{pings}")
        await message.channel.send(embed=embed)







client.run(token)