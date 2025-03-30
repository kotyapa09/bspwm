
# Create aliases
alias la='ls -la'


alias fetch='/home/user/bin/fetchs/fetch'
alias sysfetch='/home/user/bin/fetchs/sysfetch'


alias weather='/home/user/bin/weather'
alias prognose='/home/user/bin/weather2'
# TODO: Replace journal aliases after switching to OpenRC

# Display critical errors
alias syslog_emerg="sudo dmesg --level=emerg,alert,crit"

# Output common errors
alias syslog="sudo dmesg --level=err,warn"

# Print logs from x server
alias xlog='grep "(EE)\|(WW)\|error\|failed" ~/.local/share/xorg/Xorg.0.log'

# Remove archived journal files until the disk space they use falls below 100M
alias vacuum="journalctl --vacuum-size=100M"

# Make all journal files contain no data older than 2 weeks
alias vacuum_time="journalctl --vacuum-time=2weeks"

set -U fish_greeting
set fish_color_command green
set -gx EDITOR micro
set -gx VISUAL micro
set -gx BROWSER /usr/bin/firefox


if status is-interactive
    # Commands to run in interactive sessions can go here
end

sh /home/user/.config/fish/script.sh

zoxide init fish
