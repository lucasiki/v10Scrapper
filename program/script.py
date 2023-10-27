
INIT_URL = 'https://google.com'

SCRIPT = [
    ["execute_script", ["document.getElementsByTagName('textarea')[0].value='eliote'"]],
    ["save_screenshot", ["image.png"]],
    ["execute_script", ["return document.getElementsByTagName('body')[0].outerHTML"]]
]
