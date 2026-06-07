from rich import print

from rich.text import Text
from strands.hooks import HookProvider, HookRegistry
from strands.hooks.events import BeforeToolCallEvent

# ツール呼び出し時にログを出力するフック
class ToolLoggingHook(HookProvider):
    # フックを登録するメソッド
    def register_hooks(self, registry: HookRegistry) -> None:
        # BeforeToolCallEvent 発生時のコールバックを登録
        registry.add_callback(BeforeToolCallEvent, self.on_tool_start)

    # ツール開始時に呼ばれるフック
    def on_tool_start(self, event: BeforeToolCallEvent) -> None:
        agent_name = event.agent.name
        tool_name = event.tool_use["name"]
        tool_input = event.tool_use["input"]

        if tool_name == "handoff_to_agent":
            # ストリーミング処理で出力するためスキップ
            pass

        else:
            # コンソールにツール呼び出しログを出力
            print(Text(
                f"{agent_name} : {tool_name} : {tool_input}"
            ))
