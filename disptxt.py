import tkinter as tk
import pygame

def create_skeleton_window():
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # フルスクリーンで表示
    root.attributes('-topmost', True)  # 常に最前面に表示
    root.overrideredirect(True)  # ウィンドウ枠を削除
    root.configure(bg="black")
    root.wm_attributes('-transparentcolor', 'black')  # 背景色（ここでは黒）を透明に設定

    return root

def show_text():
    # サウンドエフェクトをロード
    pygame.mixer.init()
    sound_effect = pygame.mixer.Sound('data/lgd.mp3')
    
    # サウンドエフェクトを再生
    sound_effect.play()

    # ウィンドウの作成
    root = create_skeleton_window()
    root2 = create_skeleton_window()

    # テキストラベルの作成
    label = tk.Label(root, text="LOST  GRACE  DISCOVERED", font=("Sylfaen", 65), fg="#e6bf00", bg="black")
    label.pack(expand=True, anchor='center')

    # テキストラベルの作成
    label2 = tk.Label(root2, text="LOST   GRACE    DISCOVERED", font=("Sylfaen", 65), fg="#e6bf00", bg="black")
    label2.pack(expand=True, anchor='center')

    opacity = 0
    decrease_opacity = 0.025

    opacity2 = 0
    decrease_opacity2 = 0.025

    root2.attributes('-alpha', opacity2)

    def fade_out_end():
        root.destroy()
        root2.destroy()

    def destroy_windows_after_sound():
        sound_length_ms = sound_effect.get_length() * 1000

        root.after(int(sound_length_ms), fade_out_end)

    def fade_out_text():
        nonlocal opacity
        opacity -= decrease_opacity
        root.attributes('-alpha', opacity)

        if opacity > 0:
            root.after(40, fade_out_text)

    def fade_out_text2():
        nonlocal opacity2
        opacity2 -= decrease_opacity2
        root2.attributes('-alpha', opacity2)

        if opacity2 > 0:
            root.after(100, fade_out_text2)

    def fade_in_end():
        fade_out_text()
        fade_out_text2()

    def fade_in_text():
        nonlocal opacity
        opacity += decrease_opacity
        root.attributes('-alpha', opacity)

        nonlocal opacity2
        if opacity2 < 0.25:
            opacity2 += decrease_opacity2
            root2.attributes('-alpha', opacity2)

        if opacity < 1:
            root.after(10, fade_in_text)
        else:
            root.after(1000, fade_in_end)
    
    fade_in_text()
    destroy_windows_after_sound()

    root.mainloop()
    root2.mainloop()

show_text()
