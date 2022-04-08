import webbrowser as wb

def web_automation ():
    explorer_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    URLS = ('apple.com', 'google.com', 'github.com')

    for url in URLS:
        print ('Opening' + url)
        wb.get(explorer_path).open(url)

web_automation()