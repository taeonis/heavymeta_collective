from nicegui import ui, app
import os

static_files_dir = os.path.join(os.path.dirname(__file__), 'static')
app.add_static_files('/static', static_files_dir)


@ui.page('/')
def landing():
    ui.page_title('HEAVYMETA COLLECTIVE')
    with ui.header():
        ui.label('HEAVYMETA COLLECTIVE').classes('text-lg font-semibold')
    with ui.column(
    ).classes('w-full items-center gap-16 mt-12'
    ).style(
        'padding-inline: clamp(1rem, 20vw, 50rem);'
    ):
        ui.image('/static/placeholder.png'
            ).classes('w-full max-w-5l'
            ).props('fit=cover')

        with ui.row().classes('w-full max-w-5l items-start gap-8'):
            ui.image('static/placeholder.png').classes('w-1/2').props('fit=cover')
            ui.label('lorem ipsum').classes('text-base leading-relaxed')

        with ui.row().classes('w-full max-w-5l items-start gap-8'):
            ui.image('static/placeholder.png').classes('w-1/2').props('fit=cover')
            ui.label('lorem ipsum').classes('text-base leading-relaxed')

        ui.button(
            'JOIN',
            on_click=lambda: ui.navigate.to('/join')
        ).classes('mt-8 px-8 py-3 text-lg w-full md:w-1/2 max-w-lg')


@ui.page('/join')
def join():
    ui.page_title('Join HEAVYMETA') 

    with ui.header():
        ui.button('← Back', on_click=lambda: ui.navigate.to('/'))

    with ui.column(
    ).classes(
        'w-full items-center gap-16 mt-12'
    ).style(
        'padding-inline: clamp(1rem, 20vw, 50rem);'
    ):
        ui.label('JOIN').classes('text-2xl mt-12')
        with ui.row():
            ui.label(
                'Already Registered?'
            ).classes('mt-4 text-base leading-relaxed')
            ui.link('LOGIN', '/login')
        
        with ui.column().classes('item-left w-full'):
            ui.label("MONIKER")
            entry = ui.input('Enter your email').classes('w-full md:w-1/2 mt-4').props('placeholder=you@example.com')
        with ui.column().classes('item-left w-full'):
            ui.label("EMAIL")
            entry = ui.input('Enter your email').classes('w-full md:w-1/2 mt-4').props('placeholder=you@example.com')
        with ui.column().classes('item-left w-full'):
            ui.label("PASSWORD")
            entry = ui.input('Enter your email').classes('w-full md:w-1/2 mt-4').props('placeholder=you@example.com')
        with ui.column().classes('item-left w-full'):
            ui.label("MEMBER TYPE")
            entry = ui.input('Enter your email').classes('w-full md:w-1/2 mt-4').props('placeholder=you@example.com')

@ui.page('/login')
def join():
    ui.page_title('Login to HEAVYMETA') 

    with ui.header():
        ui.button('← Back', on_click=lambda: ui.navigate.to('/'))

ui.run()