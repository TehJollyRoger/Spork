import socketserver, http.server, os, webbrowser
from time import sleep
from colorama import Fore

y = os.environ["COMPUTERNAME"]
url = "127.0.0.1:1337/index.html"
print(Fore.RED + "Thing by " + Fore.GREEN + "The Jolly Roger")
print("Henlo" + " " +  y)
sleep(2)
print("Starting Server")
print("3...")
print("2...")
print("1...")
# Starting Server
port = 1337
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json'
})
httpx = socketserver.TCPServer(("", port), Handler)
print("server started on port " + str(port))
httpx.serve_forever()
webbrowser.open_new_tab(url)
