#!/usr/bin/python3

import os
import time
import datetime
import subprocess

##############################################################################

def main_menu():
    program_ascii_logo_and_menu = """
██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░

███╗░░░███╗██╗░░░██╗░██████╗███████╗
████╗░████║██║░░░██║██╔════╝██╔════╝
██╔████╔██║██║░░░██║╚█████╗░█████╗░░
██║╚██╔╝██║██║░░░██║░╚═══██╗██╔══╝░░
██║░╚═╝░██║╚██████╔╝██████╔╝███████╗
╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░╚══════╝

[ Nuri ACAR ] [ nuriacar.com ]

[ Project Muse ] [ https://muse.jhu.edu/ parser, downloader, archiver. ]

[ Menu ]                                            [ v0.0.2 : 20201208134849 ]
===============================================================================
.
... 1. Download
...... [+] Program can download:
.......... [+] Access granted books
.......... [+] or open access books like in Covid-19 library. 
...... [!] Your IP can be restricted if you do not have a proxychain. :)

... 8. About & Source Code Repository & Version History
... 9. Exit
===============================================================================
"""
    clear_screen()
    print("{}".format(program_ascii_logo_and_menu))

##############################################################################

def swtch_main_menu_option(): # Python has not switch case.
    print("Select an Option!")
    selected_option = get_chck_positive_numeric()

    if selected_option == 9:
        clear_screen()
        print("[ 9. Exit ]")
        prnt_seperator()
        prnt_terminated()
        return False # while loop breaker in main.
    elif selected_option == 1:
        clear_screen()
        print("[ 1. Download ]")
        prnt_seperator()
        book_downloader()
        prnt_hit_enter_to_continue()
    elif selected_option == 8:
        clear_screen()
        print("[ 8. About & Source Code Repository & Version History ]")
        prnt_seperator()
        prnt_about_source_history()
        prnt_hit_enter_to_continue()
    else:
        prnt_out_of_option()
        prnt_hit_enter_to_continue()

###############################################################################

def get_chck_positive_numeric():
    # Returns only positive number. If entry not numeric, 0 or negative, 
    # calls itself till entry become positive.
    str_numeric_entry = input("\n>>> ") # ...reads user entry.

    try:
        int_numeric_entry = int(str_numeric_entry) # If entry is integer,
        if int_numeric_entry > 0: # and positive (must)...
            return int_numeric_entry
        else: # Else, so not positive...
            prnt_entry_must_be_positive_number()

            # Because of function recall inside itself, value become None.
            # So, return is important below!
            # Returns proper value of function call n to function call 1!
            return get_chck_positive_numeric()
    except ValueError: # Else, so entry is not integer.
        prnt_entry_must_be_numeric()

        # Because of function recall inside itself, value become None.
        # So, return is important below!
        # Returns proper value of function call n to function call 1!
        return get_chck_positive_numeric()

###############################################################################

def prnt_about_source_history():
    about_source_history = """[ About ]  http://nuriacar.com/cevizlab/2020/10/13/project_muse.html

[ Source ] https://github.com/nuriacar/project_muse

[ Version History ]
===============================================================================

20200415001835 :        : Start

20200416042603 : v0.0.1 : Done :)
20200416073925 : v0.0.1 : Parsing commands fixed (chaptername error),
                          code beautified.
20201208134849 : v0.0.2 : Program flow and variable names changed.
"""

    print("{}".format(about_source_history))

##############################################################################

def book_downloader():
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:208&min=1&max=637" >> 208_arizona.html;
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:173&min=1&max=351" >> 173_colorado.html;
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:255&min=1&max=2303" >> 255_cornell.html;
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:93&min=1&max=927" >> 93_fordham.html;
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:164&min=1&max=670" >> 164_georgia.html;
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:1&min=1&max=1646" >> 1_johnhopkins.html;
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:6&min=1&max=544" >> 6_mit.html;
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:17&min=1&max=1483" >> 17_nebraska.html;
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:56&min=1&max=1350" >> 56_pennsylvania.html;
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:12&min=1&max=1678" >> 12_northcarolina.html;
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:267&min=1&max=5929" >> 267_princeton.html;
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:76&min=1&max=61" >> 76_texastech.html;
    # curl "https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:183&min=1&max=745" >> 183_temple.html;

    curl_cmd = """curl """
    min_max_text = """&min=1&max="""
    bash_flushout_sign = " >> "
    html_ext = """_booklist.html;"""

    publisher_page_base_link = """https://muse.jhu.edu/search?action=browse&limit=subscription:n&limit=publisher_id:""" # Attention! Head and end of link has a '.

    publisher_id_list = ["208", "173", "255", "93", "164", "1", "6", "17", "56", "12", "267", "76", "183"]

    publisher_name_list = ["arizona", "colorado", "cornell", "fordham", "georgia", "johnhopkins", "mit", "nebraska", "pennsylvania", "northcarolina", "princeton", "texastech", "temple"]

    publisher_book_count_list = ["637", "351", "2303", "927", "670", "1646", "544", "1483", "1350", "1678", "5929", "61", "745"]

    for i in range(len(publisher_name_list)):
        publisher_page_curl_cmd = curl_cmd + "'" + publisher_page_base_link + "{}".format(publisher_id_list[i]) + min_max_text + "{}".format(publisher_book_count_list[i]) + "'" + bash_flushout_sign + "{}".format(publisher_name_list[i]) + html_ext
        os.system(publisher_page_curl_cmd)

        # Do not delete! Necessary while developing!
        # print(publisher_page_curl_cmd)
        # input()

        # Publisher name directory for all book directories and pdfs.
        publisher_mkdir_cmd = """mkdir {};""".format(publisher_name_list[i])
        os.system(publisher_mkdir_cmd)
        
        # Do not delete! Necessary while developing!
        # print(publisher_mkdir_cmd)
        # input()
        
        # Will be used in chapters download.
        cat_cmd = """cat """
        publisher_booklist_html_file = """{}_booklist.html""".format(publisher_name_list[i])
        booklist_html_parser_block = r""" | grep book | sed 's/.*href=\"//' | sed -n 's:.*<span>\(.*\)</span>.*:\1:p' | cut -c 10- | sed 's/....$//' | sed s/\'\>/}/g | cut -c 7- | sed "s/[\"\’–,.:;']//g" | sed 's/[ -]/_/g' | tr '[:upper:]' '[:lower:]' | """
        booklist_html_bookname_parser_block = """cut -d } -f 2"""
        booklist_html_bookid_parser_block = """cut -d } -f 1"""

        publisher_booknames_file = "{}_booknames.txt".format(publisher_name_list[i])
        publisher_bookid_file = "{}_bookids.txt".format(publisher_name_list[i])

        publisher_bookname_list_parser_to_file_cmd = cat_cmd + publisher_booklist_html_file + booklist_html_parser_block + booklist_html_bookname_parser_block + bash_flushout_sign + publisher_booknames_file
        publisher_bookid_list_parser_to_file_cmd = cat_cmd + publisher_booklist_html_file + booklist_html_parser_block + booklist_html_bookid_parser_block + bash_flushout_sign + publisher_bookid_file
        
        os.system(publisher_bookname_list_parser_to_file_cmd)
        os.system(publisher_bookid_list_parser_to_file_cmd)

        # Do not delete! Necessary while developing!
        # print(publisher_bookname_list_parser_to_file_cmd)
        # print(publisher_bookid_list_parser_to_file_cmd)
        # input()

        with open(publisher_booknames_file) as f:
            publisher_bookname_list = f.read().splitlines()
        with open(publisher_bookid_file) as f:
            publisher_bookid_list = f.read().splitlines()

        # Do not delete! Necessary while developing!
        # print(publisher_bookname_list)
        # print(publisher_bookid_list)
        # input()

        about_dir = """000_about"""
        about_publisher_mkdir_cmd = """mkdir {}; mv {} ./{};""".format(about_dir, about_dir, publisher_name_list[i])
        os.system(about_publisher_mkdir_cmd)

        # Do not delete! Necessary while developing!
        # print(about_publisher_mkdir_cmd)
        # input()

        publisher_booklist_archive_dir_mv_cmd = """mv {} {} {} ./{}/{};""".format(publisher_booklist_html_file, publisher_booknames_file, publisher_bookid_file, publisher_name_list[i], about_dir)
        os.system(publisher_booklist_archive_dir_mv_cmd)

        # Do not delete! Necessary while developing!
        # print(publisher_booklist_archive_dir_mv_cmd)
        # input()

        bookpage_base_link = """https://muse.jhu.edu/book/"""

        for j in range(len(publisher_bookname_list)):
            
            book_mkdir_cmd = """mkdir {}; mv {} ./{};""".format(publisher_bookname_list[j], publisher_bookname_list[j], publisher_name_list[i])
            os.system(book_mkdir_cmd)

            # Do not delete! Necessary while developing!
            # print(book_mkdir_cmd)
            # input()

            # attention! head and end of link has a '
            tmp_book_html_file = "{}".format(publisher_bookname_list[j]) + ".html"
            bookpage_curl_cmd = curl_cmd + "'" + bookpage_base_link + "{}".format(publisher_bookid_list[j]) + "'" + bash_flushout_sign + tmp_book_html_file
            os.system(bookpage_curl_cmd)

            # Do not delete! Necessary while developing!
            # print(bookpage_curl_cmd)
            # input()

            # gets chapter id and links
            chapter_html_parser_block = r""" | grep chapter | sed 's/.*href=\"//' | grep \<\/span\>\<\/li\> | sed 's/................$//' | sed s/\"\>/}/g | cut -c 10- | sed "s/[\"\’–,.:;']//g" | sed 's/[ -]/_/g' | tr '[:upper:]' '[:lower:]' | """
            chapter_html_chapter_id_parser_block = """cut -d } -f 1"""

            bookchapter_ids_file = "{}_chapterids.txt".format(publisher_bookname_list[j])

            bookchapter_id_parser_to_file_cmd = cat_cmd + tmp_book_html_file + chapter_html_parser_block + chapter_html_chapter_id_parser_block + bash_flushout_sign + bookchapter_ids_file

            os.system(bookchapter_id_parser_to_file_cmd)

            # Do not delete! Necessary while developing!
            # print(bookchapter_id_parser_to_file_cmd)
            # input()

            with open(bookchapter_ids_file) as f:
                bookchapter_id_list = f.read().splitlines()
            
            # Do not delete! Necessary while developing!
            # print(bookchapter_id_list)
            # input()

            about_book_mkdir_cmd = """mkdir {}; mv {} ./{}/{};""".format(about_dir, about_dir, publisher_name_list[i], publisher_bookname_list[j])
            os.system(about_book_mkdir_cmd)

            bookchapter_archive_dir_mv_cmd = """mv {} {} ./{}/{}/{};""".format(tmp_book_html_file, bookchapter_ids_file, publisher_name_list[i], publisher_bookname_list[j], about_dir)
            os.system(bookchapter_archive_dir_mv_cmd)

            chapterpage_base_link = """https://muse.jhu.edu/chapter/"""

            for k in range(len(bookchapter_id_list)):

                pre_num = k + 1
                str_pre_num = str(pre_num).zfill(2)
                
                temp_bookchapter_id_file = str_pre_num + "_{}".format(bookchapter_id_list[k]) + ".pdf"
                chapter_curl_cmd = curl_cmd + "'" + chapterpage_base_link + "{}".format(bookchapter_id_list[k]) + "/pdf" + "'" + bash_flushout_sign + temp_bookchapter_id_file
                os.system(chapter_curl_cmd)
                
                # Do not delete! Necessary while developing!
                # print(chapter_curl_cmd)
                # input()

                chapter_mv_cmd = """mv {} ./{}/{};""".format(temp_bookchapter_id_file, publisher_name_list[i], publisher_bookname_list[j])

                os.system(chapter_mv_cmd)
                
                # Do not delete! Necessary while developing!
                # print(chapter_mv_cmd)
                # input()

###############################################################################
# ScreenCleaner

# function v.1

# def clear_screen():
#     if os.name == "nt":
#         os.system("cls")
#     else:
#         os.system("clear")


# function v.2 (shortest version of v.1)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

###############################################################################

def prnt_seperator():
    print("=" * 79)

###############################################################################

def prnt_hit_enter_to_continue():
    input("\nHit 'Enter' to continue to menu!")
    clear_screen()

###############################################################################

def prnt_newline():
    print("")

###############################################################################

def prnt_terminated():
    print("Terminated!\n") # Double newline! First one is in print() fn!

###############################################################################

def prnt_entry_must_be_numeric():
    print("\nEntry must be numeric!")

###############################################################################

def prnt_entry_must_be_positive_number():
    print("\nEntry must be positive number!")

###############################################################################

def prnt_out_of_option():
    print("\nOut of Option!")

###############################################################################

def get_date_time():
    now = datetime.datetime.now()
    # H:M:S, dd/mm/YY
    dt_string = now.strftime("%H:%M:%S, %A, %d/%m/%Y")
    return dt_string

###############################################################################

def main():
    ##########
    # Gets time now for elapsed time calculation.
    start_time = time.time() # Returns float.
    ##########
    
    # ctrl + c termination and input error handler
    try:
        while True:
            main_menu()
            if os.name == "nt": # Program runs on only *nix systems!
                attention_nt = """
Attention!
This program runs on only *nix systems because of dependencies.
Please, check the source code for details!

"""
                print("{}".format(attention_nt))
                prnt_terminated()
                return False # while loop breaker.
            
            # If OS is not NT, runs the code below!
            while_breaker = swtch_main_menu_option() # 9 Menu Exit.
            if while_breaker == False:
                break
    except KeyboardInterrupt: # If ctrl + c pressed while code is running...
        prnt_newline()
        prnt_newline()
        print("Keyboard Interrupt Termination!")
        prnt_newline()
    except EOFError: # Input Error handler.
        prnt_newline()
        prnt_newline()
        print("Input Error Termination!")
        prnt_newline()
    
    ##########
    # Gets duration time from time 0 till now.
    duration = time.time() - start_time # Returns float. So convert to int.
    
    hours = int(duration / 3600)
    minutes = int((duration / 60) % 60)
    seconds = int(duration % 60)

    prnt_seperator()

    if hours > 0:
        print("[ Done! ] ====> {0} h. {1} m. {2} s."\
            .format(hours, minutes, seconds))
    elif minutes > 0:
        print("[ Done! ] ====> {0} m. {1} s."\
            .format(minutes, seconds))
    else:
        print("[ Done! ] ====> {0} s."\
            .format(seconds))

    ##########

###############################################################################

if __name__ == "__main__":
    main()
