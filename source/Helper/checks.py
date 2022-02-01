from nextcord.ext.commands import Context, check

STAFF = int['579111799794958377']
BOT = int['924832290616508476', '937481737750057011']

def is_staff():
    async def predicate(ctx: Context) -> bool:
        if not ctx.guild: return False

        return STAFF in ctx.author.id

    return check(predicate)

def is_bot():
    async def predicate(ctx: Context) -> bool:
        if not ctx.guild: return False

        return BOT in ctx.author.id

    return check(predicate)
