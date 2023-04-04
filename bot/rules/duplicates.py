from collections.abc import Iterable

from discord import Member, Message


async def apply(
    last_message: Message, recent_messages: list[Message], config: dict[str, int]
) -> tuple[str, Iterable[Member], Iterable[Message]] | None:
    """Detects duplicated messages sent by a single user."""
    relevant_messages = tuple(
        msg
        for msg in recent_messages
        if (
            msg.author == last_message.author
            and msg.content == last_message.content
            and msg.content
        )
    )

    total_duplicated = len(relevant_messages)

    if total_duplicated > config["max"]:
        return (
            f"sent {total_duplicated} duplicated messages in {config['interval']}s",
            (last_message.author,),
            relevant_messages
        )
    return None
