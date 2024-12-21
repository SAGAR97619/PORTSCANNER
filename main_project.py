import socket,sys,threading,time
import urllib.request
import webbrowser
from tkinter import *

# ==== Scan Vars ====
ip_s = 1
ip_f = 1024
log = []
ports = []
target = 'localhost'
 
# ==== Scanning Functions ====
def scanPort(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        c = s.connect_ex((target, port))
        if c == 0:
            m = ' Port %d \t[open]' % (port,)
            log.append(m)
            ports.append(port)
            listbox.insert("end", str(m))
            updateResult()
        s.close()
    except OSError: print('> Too many open sockets. Port ' + str(port))
    except:
        c.close()
        s.close()
        sys.exit()
    sys.exit()
     
def updateResult():
    rtext = " [ " + str(len(ports)) + " / " + str(ip_f) + " ] ~ " + str(target)
    L27.configure(text = rtext)
 
def startScan():
    global ports, log, target, ip_f
    clearScan()
    log = []
    ports = []
    # Get ports ranges from GUI
    ip_s = int(L24.get())
    ip_f = int(L25.get())
    # Start writing the log file
    log.append('> Port Scanner')
    log.append('='*14 + '\n')
    log.append(' Target:\t' + str(target))
     
    try:
        target = socket.gethostbyname(str(L22.get()))
        log.append(' IP Adr.:\t' + str(target))
        log.append(' Ports: \t[ ' + str(ip_s) + ' / ' + str(ip_f) + ' ]')
        log.append('\n')
        # Lets start scanning ports!
        while ip_s <= ip_f:
            try:
                scan = threading.Thread(target=scanPort, args=(target, ip_s))
                scan.setDaemon(True)
                scan.start()
            except: time.sleep(0.01)
            ip_s += 1
    except:
        m = '> Target ' + str(L22.get()) + ' not found.'
        log.append(m)
        listbox.insert(0, str(m))
         
def url():
    weburl=urllib.request.urlopen("https://packetlife.net/media/library/23/common_ports.pdf")
    webbrowser.open_new("https://packetlife.net/media/library/23/common_ports.pdf")

def clearScan():
    listbox.delete(0, 'end')
 
# ==== GUI ====
gui = Tk()
gui.title('Port Scanner')
gui.geometry("1350x700+0+0")

# ==== Colors ====
m1c = '#00ee00'
bgc = "azure3"#'#222222'
dbg = '#000000'
fgc = "green"#'#111111'
bg_color="#074463"
gui.tk_setPalette(background=bgc, foreground=m1c, activeBackground=fgc,activeForeground=bgc, highlightColor=m1c, highlightBackground=m1c)


# ==== Labels ====

L10=Label(gui,text="PORT SCANNER",bd=12,font=("times new roman",20,"bold"),fg="white",relief=GROOVE,bg="blue")
L10.place(x=0,y=0,width=1370,height=75)

L11=LabelFrame(gui,text="PORT SCANNER",bd=12,font=("times new roman",20,"bold"),fg="gold",bg=bg_color)
L11.place(x=55,y=100,width=600,height=500)

L21 = Label(gui,text="Target: ",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=120,pady=200,sticky="w")

L22 = Entry(gui, text = "localhost",bg="black")
L22.place(x = 250, y = 210, width=250)
L22.insert(0, "localhost")
 
L23 = Label(gui, text = "Ports: ",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
L23.place(x = 120, y = 260)
 
L24 = Entry(gui, text = "1",bg="black")
L24.place(x = 250, y = 265, width = 100)
L24.insert(0, "1")
 
L25 = Entry(gui, text = "1024",bg="black")
L25.place(x = 400, y = 265, width = 100)
L25.insert(0, "1024")
 
L26 = Label(gui, text = "Results: ",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
L26.place(x = 120, y = 310)
L27 = Label(gui, text = "[ ... ]",bg="black")
L27.place(x = 250, y = 315)
 
L28 = Label(gui, text = "Port Info. Link",font=("times new roman",14,"bold"),bg=bg_color,fg="lightgreen")
L28.place(x = 120, y = 500)
# =====Result====

res=Frame(gui)
res=Label(gui,text="RESULT",bd=12,font=("times new roman",20,"bold"),fg="gold",relief=GROOVE,bg=bg_color)
res.place(x=700,y=100,width=600,height=50)

#==extra editing====
gol=Frame(gui)
gol=Label(gui,text="☠",bd=12,font=("times new roman",20,"bold"),fg="gold",relief=GROOVE,bg=bg_color)
gol.place(x=0,y=605,width=1370,height=75)
# ==== Ports list ====
frame = Frame(gui)

frame=Frame(gui,bd=12,relief=GROOVE,bg="black")
frame.place(x=700,y=150,width=600,height=450)

listbox = Listbox(frame,bg="black",width = 600, height =450)
listbox.place(x = 0, y = 0)
listbox.bind('<<ListboxSelect>>')
scrollbar = Scrollbar(frame,orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

 
# ==== Buttons / Scans ====

B11 = Button(gui, text = "Start Scan",bg=bg_color,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,fg="black", command=startScan)
B11.place(x = 255, y = 350, width = 170)

B20 = Button(gui, text = "Link",bg=bg_color,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN,fg="black", command=url)
B20.place(x = 255, y = 490, width = 170)


# ==== Start GUI ====
gui.mainloop()