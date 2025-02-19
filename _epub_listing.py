import os
import pandas as pd

## Setting main path
main_pth = os.getcwd()
print("Folders in current path:")
print(os.listdir(main_pth))


## Folders navigator function
def root_folder_navigator():
    ## Root folder level
    folder_selector = input("\nSelect an option:\n"
                            "   [f]  _FILOSOFIA\n"
                            "   [l]  _LETTERATURA\n"
                            "   [s]  _SAGGISTICA\n"
                            "   [h]  _STORIA\n"
                            "   [c]  _CLASSICI_LATINI_GRECI\n"
                            "   [p]  _POESIA\n"
                            "   [w]  _SCRITTURA\n"
                            "   [a]  _ARTE\n"
                            "   [m]  _MANUALI\n"
                            "   [t]  _TEATRO\n"
                            "   [x]  exit program\n"
                            "    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     ")

    ## Folders options
    if folder_selector == "f":
        ch_folder_path = main_pth + "/" "_FILOSOFIA"
    if folder_selector == "l":
        ch_folder_path = main_pth + "/" "_LETTERATURA"
    if folder_selector == "s":
        ch_folder_path = main_pth + "/" "_SAGGISTICA"
    if folder_selector == "h":
        ch_folder_path = main_pth + "/" "_STORIA"
    if folder_selector == "c":
        ch_folder_path = main_pth + "/" "_CLASSICI_LATINI_GRECI"
    if folder_selector == "p":
        ch_folder_path = main_pth + "/" "_POESIA"
    if folder_selector == "w":
        ch_folder_path = main_pth + "/" "_SCRITTURA"
    if folder_selector == "a":
        ch_folder_path = main_pth + "/" "_ARTE"
    if folder_selector == "m":
        ch_folder_path = main_pth + "/" "_MANUALI"
    if folder_selector == "t":
        ch_folder_path = main_pth + "/" "_TEATRO"
    if folder_selector not in ["f", "l", "s", "h", "c", "p", "w", "a", "m", "t", "x"]:
        print("Sorry, no such option,\nplease select a valid option:")
        root_folder_navigator()
    if folder_selector == "x":
        print("\nGoodbye!")
        exit()

    ## Folder path composer
    os.chdir(ch_folder_path)
    print(f'\nYou are now in {os.getcwd()}\n')
    folder_content = os.listdir(ch_folder_path)
    folder_content.sort()
    for book in folder_content:
        print(book)

    ## First level function
    def first_level_navigator():
        nav_option = input("\nSelect an option:\n"
                           "    [c]  change directory inside this folder\n"
                           "    [r]  back to root\n"
                           "    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     ")

        ## First level options
        if nav_option not in ["c", "r"]:
            print("Sorry, no such option,\nplease select a valid option:")
            first_level_navigator()
        if nav_option == "r":
            os.chdir("../")
            print(f'\n{os.listdir()}')
            ## Restart program
            root_folder_navigator()
        if nav_option == "c":
            name_directory = input("\nType the folder name:     ")
            final_pth = ch_folder_path + "/" + name_directory
            final_dir_list = os.listdir(final_pth)
            final_dir_list.sort()
            for el in final_dir_list:
                print(el)

        ## Second level function
        ## Function activation if nav_option == "c"
        def second_level_navigator():
            ## Back to previous folder or exit program
            back_or_exit = input("\nSelect an option:\n"
                                 "    [b]  back to previous folder\n"
                                 "    [r]  back to main folder\n"
                                 "    [e]  exit program\n"
                                 "    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     ")
            if back_or_exit not in ["b", "r", "e"]:
                print("Sorry, no such option,\nplease select a valid option:")
                second_level_navigator()
            if back_or_exit == "b":
                back_pth = os.chdir('./')
                for el in os.listdir(back_pth):
                    print(el)
                ## Restart first level function
                first_level_navigator()
            if back_or_exit == "r":
                os.chdir("../")
                print(f'\n{os.listdir()}')
                ## Restart program
                root_folder_navigator()
            if back_or_exit == "e":
                print("\nGoodbye!")
                exit()

        second_level_navigator()


    first_level_navigator()


root_folder_navigator()
