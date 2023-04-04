from collections.abc import Iterable

from discord import Member, Message


async def apply(
    last_message: Message, recent_messages: list[Message], config: dict[str, int]
) -> tuple[str, Iterable[Member], Iterable[Message]] | None:
    """Detects repeated messages sent by a single user."""
    relevant_messages = tuple(
        msg
        for msg in recent_messages
        if msg.author == last_message.author
    )
    total_relevant = len(relevant_messages)

    if total_relevant > config["max"]:
        return (
            f"sent {total_relevant} messages in {config['interval']}s",
            (last_message.author,),
            relevant_messages
        )
    return None
