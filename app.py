import asyncio
from contextlib import suppress
import flet as ft


async def main(page: ft.Page) -> None:
    page.title ="Coin Clicker"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#141221"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"Style_text": "fonts/beer money.ttf"}
    page.theme = ft.Theme(font_family="Style_text")


    async def score_up(event: ft.ContainerTapEvent) -> None:
        print(f"event.control: {event.control}")  # Print the control attribute for inspection
        print(f"event.data: {event.data}")  # Print the data attribute for inspection
        print(f"event.target: {event.target}")  # Print the target attribute for inspection

        print(dir(event))
        print(event)

        score.data += 1
        score.value = str(score.data)
        # score.text = f"{score.data}"
        # score_counter.text = f"Score: {score.data}"
        #
        # if score.data % 5 == 0:
        #     progress_bar.value = min(score.data / 100, 1)

        image.scale = 0.95

        score_counter.opacity = 1
        score_counter.value = "+1"
        # score_counter.right = 0

        # score_counter.left = event.local_x
        # score_counter.top = event.local_y

        # score_counter.left = page.width // 2
        # score_counter.top = page.height // 2


        score_counter.bottom = 0

        progress_bar.value += (1 / 100)

        audio = ft.Audio(src="audio/click.mp3", autoplay=True)
        page.overlay.append(audio)

        if score.data % 100 == 0:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="Coin +100",
                    size=20,
                    color="#ff8b1f",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor="#25223a"
            )
            page.snack_bar.open = True
            progress_bar.value = 0

        await page.update_async()

        # Звук
        with suppress(AttributeError):
            await audio.play_async()

        await asyncio.sleep(0.1)
        image.scale = 1

        score_counter.opacity = 0

        await page.update_async()



    score = ft.Text(value="0", size=100, data=0)
    score_counter = ft.Text(
        size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )
    image = ft.Image(
        src="coin.png",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )
    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width - 100,
        bar_height=20,
        color="#ff8b1f",
        bgcolor="#bf6524"
    )

    await page.add_async(
        score,
        ft.Container(
            content=ft.Stack(controls=[image,score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=None, port=8000)