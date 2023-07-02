from playwright.sync_api import sync_playwright

# New Client xpath
FILTERMENU_OPERACIONES = '//a[@href="#c1"]'
FILTERMENU_OPERACIONES_CLIENTE = '//a[@href="#c1043123"]'
FILTERMENU_OPERACIONES_CLIENTE_CLIENTE = '//a[@href="#c6"]'
FILTERMENU_OPERACIONES_CLIENTE_CLIENTE_ADMINISTRADOR = '//a[@href="ClienteAdministrador.aspx"]'
BTNALTA = '//*[contains(@id, "btnAlta")]//a'



def create_new_client(page):
    # Operaciones
    page.query_selector(FILTERMENU_OPERACIONES).click()
    # Cliente
    page.query_selector(FILTERMENU_OPERACIONES_CLIENTE).click()
    # Cliente
    page.query_selector(FILTERMENU_OPERACIONES_CLIENTE_CLIENTE).click()
    # Administrador
    page.query_selector(FILTERMENU_OPERACIONES_CLIENTE_CLIENTE_ADMINISTRADOR).click()
    # Alta

    # iframeButton = page.frame_locator('iFrame').locator(BTNALTA);
    # iframeButton.click();

    # iframe_selector = '//iframe[@src="ClienteBusqueda.aspx"]'
    # frame = page.query_selector(iframe_selector)
    # page.switch_to_frame(frame)

    # element = page.wait_for_selector(BTNALTA)
    # element.query_selector(BTNALTA).click(force=True)

    # TODO
    # No encuentra el elemento para hacer click, revisar el iframe