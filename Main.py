try:emoji = str(msg.text).split(' ')[2]
    except IndexError:emoji = '🤓' 

    try:chat = str(msg.text).split(' ')[3]
    except IndexError:chat = None

    chat_id = msg.chat.id
    await msg.delete()
    async for m in app.get_chat_history(chat_id,int(limit)):
        try:
            await app.send_reaction(chat_id,m.id,emoji)
        except errors.exceptions.bad_request_400.MessageNotModified:
            pass
