from collections.abc import Iterable

from discord import Member, Message


async def apply(
    last_message: Message, recent_messages: list[Message], config: dict[str, int]
) -> tuple[str, Iterable[Member], Iterable[Message]] | None:
    """Detects repeated messages sent by multiple users."""
    total_recent = len(recent_messages)

    if total_recent > config['max']:
        return (
            f"sent {total_recent} messages in {config['interval']}s",
            set(msg.author for msg in recent_messages),
            recent_messages
        )
    return None
