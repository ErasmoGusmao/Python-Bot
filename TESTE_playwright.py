from playwright.sync_api import sync_playwright

URL ="https://pegalookup.netlify.app/lookup"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(URL)
    # Preencher com a pesquisa
    page.fill("#root > div.align-items-center.shadow-lg.card > div > div > div.col > div:nth-child(1) > div > div.mt-4.row > div > div > input", "73930")
    # Clicar
    #page.click("input[name ='btnK']")
    page.click('#root > div.align-items-center.shadow-lg.card > div > div > div.col > div:nth-child(1) > div > div.mt-4.row > div > div > button')
    page.wait_for_timeout(500)

    #page.fill("")

    page.wait_for_timeout(5000)
    # Imprime Título
    print(page.title())
    browser.close()