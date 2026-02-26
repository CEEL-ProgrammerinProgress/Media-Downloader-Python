import yt_dlp
import os
#  función se encarga de mostrar el progreso en la consola
def mi_hook(d):
    if d["status"] == "downloading":
        porcentaje = d.get("_percent_str", "0%")
        velocidad = d.get("_speed_str", "N/A")
        eta = d.get("_eta_str", "N/A")
        print(
            f"   Descargando: {porcentaje} | Velocidad: {velocidad} | Tiempo restante: {eta}",
            end="\r",
        )
    elif d["status"] == "finished":
        print("\n   Descarga finalizada, procesando archivo...")



def mi_descargador():
    while True:
        print("\n" + "=" * 30)
        print("---- Videos DOWNLOADER ----\n")
        print("     === By CEEL === ")
        print("=" * 30)

        
        print("\n¿Qué deseas descargar?.")
        print("1. Video MP4 (Máxima calidad + Audio).")
        print("2. Video MP4 (SIN AUDIO).")
        print("3. Audio MP3.")
        print("4. Sitios compatibles.")
        print("5. Problemas al descargar?")
        print("6. Salir del programa.")
        opcion = input("\nSelecciona una opción (1, 2, 3, 4, 5, o 6): ").strip()
        
        if opcion == '6':
            print("Saliendo del programa... Hasta pronto!")
            break
        
        if opcion == '5':
            print("\n Si el Archivo presenta problemas se le recomienda hacer lo siguiente")
            print("\n 1. Cambiar de reprodutor multimedia:\n  - Presione click derecho en el archivo > Abrir con > (Selecione otra opcion.)")
            print("\n 2. Busque el mismo contenido en otro sitio diferente.\n   - Ejemplo un video de tiktok busquelo en yt.")
            print("\n 3. Descarge el Audio y video e mezclelo en un Editor de video.\n  - Puede ser Filmora, chimchap, etc.")
            continue
        
        if opcion == "4":
                # Lista de 50 sitios organizada para que se vea bien en consola | Hay muchos mas
                sitios_50 = (
                    "1. YouTube      2. TikTok       3. Instagram    4. Facebook     5. X (Twitter)\n"
                    "6. Twitch       7. Vimeo        8. SoundCloud   9. Reddit       10. Pinterest\n"
                    "11. LinkedIn    12. DailyMotion 13. Rumble      14. BitChute    15. BiliBili\n"
                    "16. Steam       17. Flickr      18. Bandcamp    19. Mixcloud    20. Audiomack\n"
                    "21. Apple Pod.  22. Google Pod. 23. TED         24. Khan Acad.  25. Udemy\n"
                    "26. Coursera    27. BBC news    28. CNN         29. Bloomberg   30. Reuters\n"
                    "31. ABC News    32. Fox News    33. Al Jazeera  34. RT News     35. ESPN\n"
                    "36. NBA         37. MLB         38. RedBull TV  39. Arte.tv     40. NASA\n"
                    "41. Archive.org 42. Imgur       43. 9GAG        44. Giphy       45. Coub\n"
                    "46. Patreon     47. Substack    48. Medium      49. Blogger     50. Tumblr"
                )
                print("\n" + "=" * 70)
                print(" " * 15 + "TOP 50 SITIOS COMPATIBLES (CEEL DOWNLOADER)")
                print("=" * 70)
                print(sitios_50)
                print("=" * 70 + "\n")
                input("\nPresiona Enter para volver al menú...")
                continue 
        
        if opcion in ["1","2","3"]:
                url = input("Pega el link(URL) aquí: ")
            # Detecta la carpeta Descarga del Usuario (usando os)
                ruta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
            
            # Configuración base con el HOOK de progreso
                ydl_opts = {
                "outtmpl": os.path.join(
                    ruta_descargas, "%(title)s.%(ext)s"
                ),  # Une la ruta de descargas y le coloca  el titulo y el nombre del formato al alchivo
                "noplaylist": True,  # evita descaragar playlist
                "progress_hooks": [mi_hook],  # <-- Aquí conectamos la barra de progreso
                "quiet": True,  # Esto limpia la basura de texto innecesaria de la consola
                "no_warnings": True,
            }

        if opcion == "1":  # Video con audio compatible
                ydl_opts.update(
                    {
                        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                        "merge_output_format": "mp4",
                        "postprocessors": [
                            {
                                "key": "FFmpegVideoConvertor",
                                "preferedformat": "mp4",
                            }
                        ],
                    }
                )
        elif opcion == "2":  # Video sin audio
                ydl_opts.update(
                    {
                        "format": "bestvideo",
                        "postprocessors": [
                            {
                                "key": "FFmpegVideoConvertor",
                                "preferedformat": "mp4",
                            }
                        ],
                    }
                )
        elif opcion == "3":  # Audio
                ydl_opts.update(
                    {
                        "format": "bestaudio/best",
                        "postprocessors": [
                            {
                                "key": "FFmpegExtractAudio",
                                "preferredcodec": "mp3",
                                "preferredquality": "192",
                            }
                        ],
                    }
                )
                
        else:
            print(" Opción no válida.")
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("\n * Archivo descargado con Exito. * ")
        except Exception as e:
            print(f"\n Se a producido un Error por: {e}")
            
if __name__ == "__main__":
    mi_descargador()
