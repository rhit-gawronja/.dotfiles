#!/bin/bash

picom -b --experimental-backends
bash ~/.config/conky/startup &
nm-applet &
blueman-applet &
flameshot &
dunst &
lxsession &
nitrogen --restore &
