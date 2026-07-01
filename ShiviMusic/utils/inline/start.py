from pyrogram.types import InlineKeyboardButton

import config
from ShiviMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="👤 Owner",
                url=f"https://t.me/{config.OWNER_USERNAME}",
            ),
            InlineKeyboardButton(
                text="• BACK •",
                callback_data="settings_back_helper"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="👤 Owner",
                url=f"https://t.me/{config.OWNER_USERNAME}",
            ),
            InlineKeyboardButton(
                text="• BACK •",
                callback_data="settings_back_helper"
            ),
        ],
    ]
    return buttons
