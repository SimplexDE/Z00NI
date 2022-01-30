from nextcord.ext.commands import Context, check

STAFF = int(876893416989024266)
DEV = int(579111799794958377)
BOT = int(881186799538540565)


def is_staff():
    async def predicate(ctx: Context) -> bool:
        if not ctx.guild: return False

        return STAFF in ctx.author._roles  # type: ignore

    #print("DEBUG: is_staff check was called.")
    return check(predicate)


def is_dev():
    async def predicate(ctx: Context) -> bool:
        if not ctx.guild: return False

        return DEV == ctx.author.id  # type: ignore

    #print("DEBUG: is_staff check was called.")
    return check(predicate)

def is_bot():
    async def predicate(ctx: Context) -> bool:
        if not ctx.guild: return False

        return BOT == ctx.author.id  # type: ignore

    #print("DEBUG: is_staff check was called.")
    return check(predicate)
