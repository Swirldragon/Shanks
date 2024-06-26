from random import choice
from plugins.start import photos
from plugins.database.db import DB
from plugins.helper.button_build import ButtonMaker
from aiofiles import open as aiopen
from aiofiles.os import remove as aioremove, path as aiopath, mkdir

handler_dict = {}
default_values = {}
bool_vars = 'AS_DOCUMENT'
STATE = 'view'
user_data = {}

@Bot.on_message(filters.command("settings") & filters.private) 
async def get_settings(client: Client, message: Message):
  user_id = message.from_user.id
  buttons = ButtonMaker()
  thumbpath = f"Thumbnails/{user_id}.jpg"
  user_dict = user_data.get(user_id, {})
  if key is None:
    if user_dict.get('as_doc', False) or 'as_doc' not in user_dict and config_dict['AS_DOCUMENT']:
      ltype = "DOCUMENT"
            buttons.ibutton("Send As Media", f"userset {user_id} doc")
        else:
            ltype = "MEDIA"
            buttons.ibutton("Send As Document", f"userset {user_id} doc")
          
    thumbmsg = "Exists" if await aiopath.exists(thumbpath) else "Not Exists"
    buttons.ibutton(f"{'✅️' if thumbmsg == 'Exists' else ''} Thumbnail", f"userset {user_id} thumb")
  
    lcaption = 'Not Exists' if (val:=user_dict.get('lcaption', config_dict.get('CAPTION', ''))) == '' else val
    buttons.ibutton(f"{'✅️' if lcaption != 'Not Exists' else ''} Caption", f"userset {user_id} lcaption")
  
    lprefix = 'Not Exists' if (val:=user_dict.get('lprefix', config_dict.get('PREFIX', ''))) == '' else val
    buttons.ibutton(f"{'✅️' if lprefix != 'Not Exists' else ''} Prefix", f"userset {user_id} lprefix")

    lsuffix = 'Not Exists' if (val:=user_dict.get('lsuffix', config_dict.get('SUFFIX', ''))) == '' else val
    buttons.ibutton(f"{'✅️' if lsuffix != 'Not Exists' else ''} Leech Suffix", f"userset {user_id} lsuffix")
  
    mega_email = = 'Not Exists' if (val:=user_dict.get('megaemail', config_dict.get('MEGA EMAIL', ''))) == '' else val
    buttons.ibutton(f"{'✅️' if megaemail != 'Not Exists' else ''} Mega Email", f"userset {user_id} megaemail")
  
    mega_password = 'Not Exists' if (val:=user_dict.get('megapass', config_dict.get('MEGA PASSWORD', ''))) == '' else val
    buttons.ibutton(f"{'✅️' if megapass != 'Not Exists' else ''} MEGA PASSWORD", f"userset {user_id} megapass")
  
    text = BotTheme('Setting', NAME=name, THUMB=thumbmsg,
                LCAPTION=escape(lcaption), LPREFIX=escape(lprefix),
                LSUFFIX=escape(lsuffix), MEGA_PASSWORD=escape(mega_email), MEGA_PASSWORD=escape(mega_password))
    buttons.ibutton("Back", f"userset {user_id} back", "footer")
    buttons.ibutton("Close", f"userset {user_id} close", "footer")
    button = buttons.build_menu(2)


