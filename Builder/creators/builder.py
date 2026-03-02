import os
import packages

from logger import Logger, LoggerStatus
from creators.software import AurBuilder, FirefoxCustomize
from creators.patches import PatchSystemBugs
from creators.daemons import Daemons

# TODO: Implement error handling for package installation

class SystemConfiguration:
    def start(*args):
        start_text = f"[+] Starting assembly. Options {args}"
        Logger.add_record(start_text, status=LoggerStatus.SUCCESS)

        SystemConfiguration.__install_dotfiles()
        SystemConfiguration.__pacman_update()
        SystemConfiguration.__default_packages()

        if args[0]: SystemConfiguration.__base_packages()
        if args[1]: SystemConfiguration.__pentest_packages()
        if args[2]: SystemConfiguration.__extra_packages()

        # TODO: The process should not be repeated when reassembling, important components should only be updated with new ones
        Daemons.enable_all_daemons()
        PatchSystemBugs.enable_all_patches()

    @staticmethod
    def __install_dotfiles():
        SystemConfiguration.__create_default_folders()
        SystemConfiguration.__copy_bspwm_dotfiles()

    @staticmethod
    def __pacman_update():
        Logger.add_record("[+] Updates Enabled", status=LoggerStatus.SUCCESS)
        os.system("sudo pacman -Sy")

    @staticmethod
    def __default_packages():
        Logger.add_record("[+] Installed Default Dependencies", status=LoggerStatus.SUCCESS)
        AurBuilder.build()
        SystemConfiguration.__install_pacman_package(packages.DEFAULT_PACKAGES)
        SystemConfiguration.__install_aur_package(packages.DEFAULT_AUR_PACKAGES)
        FirefoxCustomize.build()

    @staticmethod
    def __base_packages():
        Logger.add_record("[+] Installed BSPWM Dependencies", status=LoggerStatus.SUCCESS)
        AurBuilder.build()
        SystemConfiguration.__install_pacman_package(packages.BASE_PACKAGES)
        SystemConfiguration.__install_aur_package(packages.BASE_AUR_PACKAGES)

    @staticmethod
    def __pentest_packages():
        Logger.add_record("[+] Installed Dev Dependencies", status=LoggerStatus.SUCCESS)
        SystemConfiguration.__install_pacman_package(packages.PENTEST_PACKAGES)
        SystemConfiguration.__install_pacman_package(packages.PENTEST_AUR_PACKAGES)

    @staticmethod
    def __extra_packages():
        Logger.add_record("[+] Install Extra Packages", status=LoggerStatus.SUCCESS)
        SystemConfiguration.__install_pacman_package(packages.GNOME_OFFICIAL_TOOLS)

    @staticmethod
    # TODO: Make a universal function for installing packages
    # TODO: Catch errors if the software is not detected
    def __install_pacman_package(package_names: list):
        for package in package_names:
            os.system(f"sudo pacman -S --noconfirm {package}")
            Logger.add_record(f"Installed: {package}", status=LoggerStatus.SUCCESS)

    @staticmethod
    # TODO: Make a universal function for installing packages
    # TODO: Catch errors if the software is not detected
    def __install_aur_package(package_names: list):
        for package in package_names:
            os.system(f"yay -S --noconfirm {package}")
            Logger.add_record(f"Installed: {package}", status=LoggerStatus.SUCCESS)

    @staticmethod
    def __create_default_folders():
        Logger.add_record("[+] Create default directories", status=LoggerStatus.SUCCESS)
        default_folders = "~/Downloads ~/Desktop"
        os.system("mkdir -p ~/.config")
        os.system(f"mkdir -p {default_folders}")
        os.system("cp -r Images/ ~/")

    @staticmethod
    def __copy_bspwm_dotfiles():
        Logger.add_record("[+] Copy Dotfiles & GTK", status=LoggerStatus.SUCCESS)
        os.system("cp -r config/* ~/.config/")
        os.system("cp Xresources ~/.Xresources")
        os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
        os.system("cp -r local ~/.local")
        os.system("cp -r themes ~/.themes")
        os.system("cp xinitrc ~/.xinitrc")
        os.system("cp -r bin/ ~/")
