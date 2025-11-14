import asyncio
from kimi_cli.soul import Soul, StatusSnapshot, wire_send
from kimi_cli.llm import ModelCapability, ALL_MODEL_CAPABILITIES
from kimi_cli.wire.message import StepBegin
from kimi_cli.ui.shell import ShellApp
from kosong.message import ContentPart, TextPart


class EchoSoul(Soul):
    def __init__(self) -> None:
        pass

    @property
    def name(self) -> str:
        return "EchoSoul"

    @property
    def model_name(self) -> str:
        return "mock"

    @property
    def model_capabilities(self) -> set[ModelCapability]:
        return ALL_MODEL_CAPABILITIES

    @property
    def status(self) -> StatusSnapshot:
        return StatusSnapshot(context_usage=0.0)

    async def run(self, user_input: str | list[ContentPart]) -> None:
        wire_send(StepBegin(n=1))
        if isinstance(user_input, str):
            wire_send(TextPart(text=user_input))
        else:
            for part in user_input:
                wire_send(part)


if __name__ == "__main__":
    soul = EchoSoul()
    app = ShellApp(soul)
    asyncio.run(app.run())
