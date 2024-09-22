import test
import Browser

def run():
    browser = Browser.BrowserCommand("example.json")
    browser.get_command()
    #print("Hello James!")

run()