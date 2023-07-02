"""Make the banner for my GitHub profile."""

import asyncio

from textual.app import App, ComposeResult
from textual.widgets import Label

NAME = """
████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀░░▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░█████████
█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░░░▄▀▄▀▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████
█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀░░██░░▄▀░░███░░░░▄▀░░░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████
█░░░░░░░░░░░░███░░░░░░██░░░░░░█████░░░░░░█████░░░░░░░░░░░░░░█░░░░░░█████████
████████████████████████████████████████████████████████████████████████████
"""

PRATTLE = """\
The programs included with the davep system are Free Software, the exact distribution terms for each program are described in the individual repositories.
"""

class GitHubBannerApp(App[None]):

    TITLE = "github.com/davep"

    CSS = """
    Screen {
        background: #282828;
    }

    Label {
        color: #ffb000;
        background: #282828;
        height: auto;
        width: 1fr;
    }

    .banner {
        text-align: center;
    }
    """

    BINDINGS = [
        ("space", "screenshot"),
    ]

    def compose(self) -> ComposeResult:
        yield Label(NAME, classes="banner")
        yield Label(PRATTLE)
        yield Label("github.com/davep login: _")

    def action_screenshot(self) -> None:
        self.save_screenshot("davep.svg")

async def make_banner() -> None:
    async with GitHubBannerApp().run_test() as pilot:
        await pilot.press("space")

if __name__ == "__main__":
    asyncio.run(make_banner())

### make_banner.py ends here
