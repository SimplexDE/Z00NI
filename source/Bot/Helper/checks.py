from nextcord.ext.commands import Context, check

STAFF_IDS = [int(579111799794958377)]
BOT_IDS = [int(924832290616508476), int(937481737750057011)]

def is_staff():
    async def predicate(ctx: Context) -> bool:
        if not ctx.guild: return False

        return ctx.author.id in STAFF_IDS

    return check(predicate)

def is_bot():
    async def predicate(ctx: Context) -> bool:
        if not ctx.guild: return False

        return ctx.author.id in BOT_IDS

    return check(predicate)
