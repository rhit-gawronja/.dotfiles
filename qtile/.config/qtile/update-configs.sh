#! /bin/sh

title="Qtile Rice Update"
updating="Updating..."

notify-send "$title" "$updating Qtile."
cd ~/.config/qtile/
git pull origin main

notify-send "$title" "$updating Picom."
cd ~/.config/picom/
git pull origin main

notify-send "$title" "$updating Dunst."
cd ~/.config/dunst/
git pull origin main

notify-send "$title" "$updating Rofi."
cd ~/.config/rofi/
git pull origin main

notify-send "$title" "$updating Alacritty."
cd ~/.config/alacritty/
git pull origin main

notify-send "$title" "$updating Polybar."
cd ~/.config/polybar/
git pull origin main

notify-send "$title" "$updating Conky."
cd ~/.config/conky/
git pull origin main

notify-send "$title" "$updating CLI Visualizer."
cd ~/.config/vis/
git pull origin main

cd ~

notify-send "$title" "Done! :-D"