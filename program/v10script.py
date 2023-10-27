
INIT_URL = 'https://sistema.spc.org.br/spc/controleacesso/autenticacao/entry.action'

SCRIPT = [
    ["execute_script", ["document.getElementsByTagName('textarea')[0].value='v10!'"]],
    ["save_screenshot", ["image.png"]]
]