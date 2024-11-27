from prisma import Prisma

prisma = Prisma()

async def connect_db():
    if not prisma.is_connected():
        await prisma.connect()
    print("❤️❤️❤️❤️ Connected to database ❤️❤️❤️❤️ ")

async def disconnect_db():
    if prisma.is_connected():
        await prisma.disconnect()
    print("💔💔💔💔 Disconnected from database 💔💔💔💔💔 ")