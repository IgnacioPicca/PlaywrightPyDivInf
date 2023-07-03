from playwright.async_api import async_playwright
import asyncio

# New Client xpath
FILTERMENU_OPERACIONES = '//a[@href="#c1"]'
FILTERMENU_OPERACIONES_CLIENTE = '//a[@href="#c1043123"]'
FILTERMENU_OPERACIONES_CLIENTE_CLIENTE = '//a[@href="#c6"]'
FILTERMENU_OPERACIONES_CLIENTE_CLIENTE_ADMINISTRADOR = (
    '//a[@href="ClienteAdministrador.aspx"]'
)


async def create_new_client(page):
    # Operaciones
    await page.click(FILTERMENU_OPERACIONES)
    # Cliente
    await page.click(FILTERMENU_OPERACIONES_CLIENTE)
    # Cliente
    await page.click(FILTERMENU_OPERACIONES_CLIENTE_CLIENTE)
    # Administrador
    await page.click(FILTERMENU_OPERACIONES_CLIENTE_CLIENTE_ADMINISTRADOR)
    # Alta

    iframe = page.frame(name="basefrm")
    await iframe.wait_for_load_state()

    btn = await iframe.query_selector('[id="btnAlta"] a')
    if btn:
        await btn.click()
    else:
        print("No se encontró el botón en el iframe.")

    # iframe_context = await iframe.frame_context()
    # await iframe_context.click(BTNALTA)

    # iframe_selector = '//iframe[@src="ClienteBusqueda.aspx"]'
    # frame = page.query_selector(iframe_selector)
    # page.switch_to_frame(frame)

    # element = page.wait_for_selector(BTNALTA)
    # element.query_selector(BTNALTA).click(force=True)

    # TODO
    # No encuentra el elemento para hacer click, revisar el iframe
