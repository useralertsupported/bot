from collections.abc import Iterable

from discord import Member, Message


async def apply(
    last_message: Message, recent_messages: list[Message], config: dict[str, int]
) -> tuple[str, Iterable[Member], Iterable[Message]] | None:
    """Detects total message char count exceeding the limit sent by a single user."""
    relevant_messages = tuple(
        msg
        for msg in recent_messages
        if msg.author == last_message.author
    )

    total_recent_chars = sum(len(msg.content) for msg in relevant_messages)

    if total_recent_chars > config['max']:
        return (
            f"sent {total_recent_chars} characters in {config['interval']}s",
            (last_message.author,),
            relevant_messages
        )
    return None
