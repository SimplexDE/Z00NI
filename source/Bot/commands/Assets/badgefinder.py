from loguru import logger

from ...Helper.checks import ids
from .emotes import Emotes


def badgefinder(member):
    badges = ""
    if member.id in ids.DEVs:
        badges += Emotes.dev

    if member.id in ids.STAFFs:
         badges += Emotes.staff

    if member.id in ids.VIPs:
        badges += Emotes.vip

    if member.id in ids.BOTs:
        badges += Emotes.bot

    return badges
