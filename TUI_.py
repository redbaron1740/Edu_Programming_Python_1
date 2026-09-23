from datetime import datetime
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Header, Footer, Digits, Static, Button


class DigitalClockApp(App):
    """Textual 기반 Modern 디지털 시계 애플리케이션 (수정본)"""

    CSS = """
    Screen {
        align: center middle;
        background: $surface;
    }

    #clock-container {
        width: 70;
        height: auto;
        border: heavy $primary;
        padding: 1 2;
        background: $panel;
    }

    #title-zone {
        content-align: center middle;
        text-style: bold;
        color: $accent;
        margin-bottom: 1;
    }

    #time-display {
        content-align: center middle;
        color: $success;
        margin: 1 0;
    }

    #date-display {
        content-align: center middle;
        text-style: italic;
        color: $text-muted;
        margin-bottom: 1;
    }

    #control-panel {
        align: center middle;
        height: 3;
        margin-top: 1;
    }

    Button {
        margin: 0 1;
    }
    """

    BINDINGS = [
        ("d", "toggle_dark", "다크/라이트 모드 전환"),
        ("q", "quit", "종료"),
    ]

    def compose(self) -> ComposeResult:
        """UI 레이아웃 구성"""
        yield Header(show_clock=False)
        
        with Container(id="clock-container"):
            yield Static("⏱️ DIGITAL CLOCK SYSTEM", id="title-zone")
            # 초깃값을 지정하여 Digits 및 Static 위젯 생성
            yield Digits("00:00:00", id="time-display")
            yield Static("2026-00-00", id="date-display")
            
            with Horizontal(id="control-panel"):
                yield Button("다크모드 토글 (D)", id="btn-toggle", variant="primary")
                yield Button("종료 (Q)", id="btn-quit", variant="error")

        yield Footer()

    def on_mount(self) -> None:
        """마운트 완료 후 1초 간격 타이머 동작 시작"""
        self.update_time()
        self.set_interval(1.0, self.update_time)

    def update_time(self) -> None:
        """마운트가 확실히 끝난 상태에서 안전하게 query_one 호출"""
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        date_str = now.strftime("%Y년 %m월 %d일 (%A)")

        # UI 위젯에 직접 업데이트
        self.query_one("#time-display", Digits).update(time_str)
        self.query_one("#date-display", Static).update(date_str)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """버튼 이벤트 처리"""
        if event.button.id == "btn-toggle":
            self.action_toggle_dark()
        elif event.button.id == "btn-quit":
            self.exit()


if __name__ == "__main__":
    app = DigitalClockApp()
    app.run()