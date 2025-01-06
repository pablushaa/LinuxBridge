from aiogram import types
import datetime, psutil, requests

def getPublicIP() -> str:
    return requests.get("https://ifconfig.me").text.replace(".", "\\.")


def roundMD(n: float) -> str:
    return str(round(n, 1)).replace(".", "\\.")


def getGreet(msg: types.Message) -> str:
    now = datetime.datetime.now()
    disk = psutil.disk_usage("/")

    return f"""
👋 Привет, *{ msg.from_user.mention_markdown(msg.from_user.full_name) }* 
🖥 Статистика хоста *{ open("/etc/hostname").read().replace("\n", "") }:*

> Процессор: *{ roundMD(psutil.cpu_percent()) }%*
> ОЗУ: *{ roundMD(psutil.virtual_memory().percent) }%*
> Диск: *{ roundMD(disk.percent) }%* \\| *{ roundMD(float(disk.used / 1024 ** 3)) } из { roundMD(disk.total / 1024 ** 3) } ГБ*
> Аптайм: *{ roundMD(float(open("/proc/uptime").read().split()[0]) / 3600) }* часа \\(ов\\)
> IP: ||*{ getPublicIP() }*||
    """