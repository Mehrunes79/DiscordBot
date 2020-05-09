
#Discord Bot

import argparse
import discord
import requests
import os
import random
from discord.ext import commands
from datetime import datetime
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.command(name='trekky', help='Responds with quote form Star Trek')
async def trekky(ctx):
	trek_quotes = [
		'KHAAANNN!', 'Computers make excellent and efficient servants, but I have no wish to serve under them.',
       		(
        	'Live long, and prosper.'
        	'Highly illogical.'
        	),
	]
	response = random.choice(trek_quotes)
	await ctx.send(response)

@bot.command(name='date', help='Responds with current date and time')
async def date(ctx):
	now = datetime.now()
	date = now.strftime("%m/%d/%Y, %H:%M:%S")
	response = date
	await ctx.send(response)

@bot.command(name='JobSearch', help= 'Responds with result of job search')
async def JobSearch(ctx,args1,args2):
	q = args1
	where = args2
	URL = ("https://www.monster.com/jobs/search/?q=%s&where=%s"%(q, where))
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, "html.parser")
	results = soup.find(id="ResultsContainer")

	i=0
	job_elems = results.find_all("section", class_="card-content")

	while i < 1:
		for job_elem in job_elems:
			title_elem = job_elem.find("h2", class_="title")
			company_elem = job_elem.find("div", class_="company")
			location_elem = job_elem.find("div", class_="location")
			if None in(title_elem, company_elem, location_elem):
				continue

		title = title_elem.text.strip()
		company = company_elem.text.strip()
		location = location_elem.text.strip()
		await ctx.send(title)
		await ctx.send(company)
		await ctx.send(location)
		i = i+1

bot.run(TOKEN)
