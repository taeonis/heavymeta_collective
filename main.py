from nicegui import ui, app
import os
from components import *

static_files_dir = os.path.join(os.path.dirname(__file__), 'static')
app.add_static_files('/static', static_files_dir)


@ui.page('/')
def landing():
    style_page('HEAVYMETA COLLECTIVE')

    with ui.column(
    ).classes('w-full items-center gap-16 mt-12'
    ).style('padding-inline: clamp(1rem, 20vw, 50rem);'):
        ui.image('/static/placeholder.png'
            ).classes('w-full max-w-5l'
            ).props('fit=cover')

        image_with_text('static/placeholder.png', 'lorem ipsum')
        image_with_text('static/placeholder.png', 'lorem ipsum')

        ui.button(
            'JOIN',
            on_click=lambda: ui.navigate.to('/join'),
        ).classes('mt-8 px-8 py-3 text-lg w-1/2')


@ui.page('/join')
def join():
    style_page('Join HEAVYMETA')

    with ui.column(
    ).classes(
        'w-full items-center gap-8 mt-12'
    ).style(
        'padding-inline: clamp(1rem, 35vw, 50rem);'
    ):
        ui.label('JOIN').classes('text-5xl font-semibold tracking-wide')
        with ui.row().classes('items-center gap-2'):
            ui.label(
                'Already Registered?'
            ).classes('text-xl tracking-wide')
            ui.link('Login', '/login').classes('text-primary text-xl font-bold tracking-wide no-underline')
        
        moniker = form_field('MONIKER', 'Create a moniker')
        email = form_field('EMAIL', 'Enter your email')
        password = form_field('PASSWORD', 'Create a password', True)
        with ui.column().classes('w-full gap-1'):
            ui.label("MEMBER TYPE").classes('text-base tracking-widest opacity-70')
            ui.select(
                ['Member Type 1', 'Member Type 2']
            ).classes('w-full').props('outlined')
        
        ui.button(
            'SIGN UP',
            on_click=lambda: ui.navigate.to('/'),
        ).classes('mt-8 px-8 py-3 text-lg w-1/2')

@ui.page('/login')
def login():
    style_page('HEAVYMETA Login')

    with ui.column(
    ).classes(
        'w-full items-center gap-8 mt-12'
    ).style(
        'padding-inline: clamp(1rem, 35vw, 50rem);'
    ):
        ui.label('LOGIN').classes('text-5xl font-semibold tracking-wide')
        
        email = form_field('EMAIL', 'Enter your email')
        password = form_field('PASSWORD', 'Enter your password', True)
        with ui.column().classes('w-full gap-1'):
            ui.label("MEMBER TYPE").classes('text-base tracking-widest opacity-70')
            ui.select(
                ['Member Type 1', 'Member Type 2']
            ).classes('w-full').props('outlined')
        
        ui.button(
            'LOGIN',
            on_click=lambda: ui.navigate.to('/profile/edit'),
        ).classes('mt-8 px-8 py-3 text-lg w-1/2')

@ui.page('/profile/edit')
def profile():
    with ui.header(
    ).classes(
        'text-black justify-center items-center bg-gradient-to-r from-[#f2d894] to-[#d6a5e2]'
    ):
        ui.image('/static/placeholder.png').classes('w-[20vw] h-[20vw] rounded-full m-8 shadow-md')
        with ui.column().classes('h-50 flex justify-between w-[50vw]'):
            with ui.column():
                ui.label('SAMPLE NAME').classes('text-5xl font-medium font-bold')
                ui.element('div').classes('bg-[#ffde59] w-48 h-12 rounded-t-lg rounded-b-lg shadow-md')
            with ui.row().classes('items-center gap-1'):
                ui.icon('chevron_right').classes('text-lg')
                ui.link('https://sample-link.com', '/').classes('text-[#8c52ff] font-semibold text-lg')
    
    with ui.column().classes('w-full items-center gap-16 mt-12'):
        with ui.column().classes('w-[45vw] gap-1 border p-4 rounded-lg'):
            ui.label('LINKS').classes('text-2xl font-bold')
            user_link('/static/placeholder.png', 'google.com')
        with ui.column().classes('w-[45vw] gap-1 border p-4 rounded-lg'):
            ui.label('WALLETS').classes('text-2xl font-bold')

ui.run()