import contextlib
import json

from asyncio import sleep

from pagermaid.dependence import sqlite
from pagermaid.hook import Hook
from pagermaid.listener import listener
from pagermaid.enums import Message
from pagermaid.services import bot
from pagermaid.utils import pip_install
from pagermaid.utils.bot_utils import log
from pagermaid.dependence import scheduler

pip_install("aiohttp")

import aiohttp


class WebSocket:
    def __init__(self):
        self.uri = sqlite.get("websocket_uri", "")
        self.loop = bot.loop
        self.client = aiohttp.ClientSession(loop=self.loop)
        self.need_stop = False
        self.ws = None
        self.connection = None

    @staticmethod
    def database_have_uri():
        return sqlite.get("websocket_uri", "") != ""

    def restore_uri(self):
        self.uri = sqlite.get("websocket_uri", "")

    async def set_uri(self, uri):
        await self.disconnect()
        self.uri = uri
        sqlite["websocket_uri"] = uri

    def is_connected(self):
        return self.connection is not None

    async def connect(self):
        if self.is_connected():
            await self.disconnect()
        if self.uri:
            self.ws = self.client.ws_connect(
                self.uri, autoclose=False, autoping=False, timeout=5
            )
            self.connection = await self.ws._coro

    async def disconnect(self):
        if self.connection:
            with contextlib.suppress(Exception):
                await self.connection.close()
            self.ws = None
            self.connection = None

    async def keep_alive(self):
        if not self.uri:
            return
        i = 0
        while i < 3:
            try:
                await self.connect()
            except Exception:
                i += 1
                if i == 3:
                    await log("[autMan] Connection lost, reconnect 3 times failed...")
                await sleep(5)
                continue
            await self.get()
            i = 0
            if self.need_stop:
                await self.disconnect()
                self.need_stop = False
                break

    async def get(self):
        ws_ = self.connection
        if not ws_:
            return
        while True:
            msg = await ws_.receive()
            if msg.type == aiohttp.WSMsgType.TEXT:
                bot.loop.create_task(self.process_message(msg.data))
            elif msg.type == aiohttp.WSMsgType.PING:
                await ws_.pong()
            elif msg.type == aiohttp.WSMsgType.BINARY:
                pass
            elif msg.type != aiohttp.WSMsgType.PONG:
                if msg.type == aiohttp.WSMsgType.CLOSE:
                    await ws_.close()
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    print(f"Error during receive {ws_.exception()}")
                break
        self.ws = None
        self.connection = None

    async def push(self, msg):
        if self.is_connected():
            await self.connection.send_str(msg)

    @staticmethod
    async def process_message(text: str):
        try:
            data = json.loads(text)
        except Exception:
            return
        action = data.get("action", None)
        action_data = data.get("data", None)

        bot_action = getattr(bot, action)
        if bot_action and action_data:
            await bot_action(**action_data)


ws = WebSocket()

#定时检查ws连接，断线重连
@scheduler.scheduled_job("interval", seconds=60)
async def check_ws():
    if not ws.is_connected():
        await connect_ws()

#启动时连接ws
@Hook.on_startup()
async def connect_ws():
    try:
        await ws.connect()
        bot.loop.create_task(ws.keep_alive())
    except Exception as e:
        await log(f"[autMan] Connection failed: {e}")

#监听消息，转发到ws
@listener(incoming=True, outgoing=True)
async def websocket_push(message: Message):
    with contextlib.suppress(Exception):
        await ws.push(message.__str__())

# ws命令
@listener(command="autman", description="autMan Connect", parameters="[uri]")
async def websocket_to_connect(message: Message):
    if message.arguments:
        uri = message.arguments
        if not uri.startswith("ws://"):
            return await message.edit(
                "[autMan] 请输入正确的 uri ，例如：ws://127.0.0.1:8080/pp/receive\n\n"
                "**格式：ws://autMan地址:端口/pp/receive**"
            )
        msg: Message = await message.edit("[autMan] 尝试连接中...")
        try:
            if ws.is_connected():
                ws.need_stop = True
            await ws.disconnect()
            await ws.set_uri(uri)
            await ws.connect()
        except Exception as e:
            return await msg.edit(f"[autMan] 连接失败：{e}")
        await msg.edit("[autMan] 连接成功")
        bot.loop.create_task(ws.keep_alive())
    elif not ws.is_connected():
        if not ws.database_have_uri():
            return await message.edit(
                "[autMan] 未链接，请检查url是否正确，autMan是否运行中\n\n"
                "**请确保autMan处于运行当中，uri格式：ws://autMan地址:端口/pp/receive**"
            )
        ws.restore_uri()
        msg: Message = await message.edit("[autMan] 尝试连接中...")
        try:
            await ws.connect()
        except Exception:
            return await msg.edit("[autMan] 连接失败")
        await msg.edit("[autMan] 连接成功")
        bot.loop.create_task(ws.keep_alive())
    else:
        return await message.edit("[autMan] 已连接")
