const dotenv = require('dotenv')
const Telegraf = require('telegraf')
const HttpsProxyAgent = require('https-proxy-agent')

dotenv.config()

const bot = new Telegraf(process.env.BOT_TOKEN)

bot.start(ctx => ctx.reply('Hello friend'))
bot.on('message', ctx => console.log(ctx.message))

bot.startPolling()
