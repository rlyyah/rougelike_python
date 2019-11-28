import helpers


def duel_stracture():
    duel = """

                                                                    ██████╗ ██╗   ██╗███████╗██╗        
                                                                    ██╔══██╗██║   ██║██╔════╝██║     ██╗
                                                                    ██║  ██║██║   ██║█████╗  ██║     ╚═╝
                                                                    ██║  ██║██║   ██║██╔══╝  ██║     ██╗
                                                                    ██████╔╝╚██████╔╝███████╗███████╗╚═╝
                                                                    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝                                       """
    
    rat_warrior = """
                                                                      ,     .         You will newer pass us,
                                                                      (\,;,/)           We will eat you to
                                                                       (o o)\//,              Death !
                                                                        \ /     \,
                                                                        `+'(  (   \    )
                                                                         //  //  \ |_./
                                                                        '~' '~----'       """
    skeleton = """

                                                                                  _.--""-._
                                                      .                         ."         ".
                                                     / \    ,^.         /(     Y             |       )\ 
                                                    /   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
                                                    |        :|    `>   '.     l_..-------.._l      .'
                                                    |      __l;__ .'      "-.__.||_.-'v'-._||`"----"
                                                    \  .-' | |  `              l._       _.'
                                                     \/    | |                   l`^^'^^'j
                                                           | |                _   \_____/     _
                                                           j |               l `--__)-'(__.--' |
                                                           | |               | /`---``-----'"1 |  ,-----.
                                                           | |               )/  `--' '---'   \|-'  ___  `-. 
                                                           | |              //  `-'  '`----'  /  ,-'   I`.  \ 
                                                         _ L |_            //  `-.-.'`-----' /  /  |   |  `. \ 
                                                        '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
                                                        `._;/7(-.......'  /        ) (     |  |            | | |
                                                         `._;l _'--------_/        )-'/     :  |___.    _._./ ;
                                                           | |                 .__ )-'\  __  \  \  I   1   / /
                                                           `-'                /   `-\-(-'   \ \  `.|   | ,' /
                                                                              \__  `-'    __/  `-. `---'',-'
                                                                                   )-._.-- (      `-----'
                                                                                )(  l\ o ('..
                                                                          _..--' _'-' '--'.-. |
                                                                    __,,-'' _,,-''            \ \ 
                                                                   f'. _,,-'                   \ \ 
                                                                  ()--  |                       \ \ 
                                                                    \.  |                       /  \ 
                                                                      \ \                      |._  |
                                                                       \ \                     |  ()|
                                                                        \ \                     \  /
                                                                        ) `-.                   | |
                                                                      // .__)                  | |
                                                                   _.//7'                      | |
                                                                '---'                         j_|
                                                                                            (| |
                                                                                             |  \ 
                                                                                             |lllj
                                                                                              |||||                                                                        
                """

    rat_boss = """
                                                                           ____
                                                               ________   |    |
                                                               \      /   |____|
                                                                \    /   _|____|_   
                                                                 \||/     /  oo`\    
                                                                  ||    .<     ___\*   
                                                                  ||\   /\ \.-.' \    
                                                                  || \ J  `.|`.\/ \  
                                                                  || | | _.|  | | |
                                                                  || /\/\  .'`.|-' /
                                                                  ||/   L   /|o`--'\ 
                                                                  ||    |  /\/\/\   \           
                                                                  ||    J /      `.__\ 
                                                                  ||    |/         /  \     
                                                                  ||     \\      .'`.  `..                                           .'
                                                                  ||    ___)_/\_(____`.  `-._______________________________________.'/
                                                                  ||   (___._/  \_.___) `-.________________________________________.-'
                """
    rat_1 = """

                                                                       __             _,-"~^"-.
                                                                     _// )      _,-"~`         `.
                                                                   ." ( /`"-,-"`                 ;
                                                                  / 6                             ;
                                                                 /           ,             ,-"     ;
                                                                (,__.--.      \           /        ;
                                                                //'   /`-.\   |          |        `._________
                                                                  _.-'_/`  )  )--...,,,___\     \-----------,)
                                                                 ((("~` _.-'.-'           __`-.   )         //
                                                                       ((("`             (((---~"`         //
                                                                                                           ((________________
                                                                                                            `----""""~~~~^^^```"""
    return [duel,[rat_warrior, skeleton, rat_boss, rat_1]]


def print_menu(duel_stracture_items, num_of_option = 1):   
    helpers.clear_screen()
    TITLE = 0
    MONSTERS = 1
    EXIT = 2

    print(f'{duel_stracture_items[TITLE]}')#
    
    print(f'{duel_stracture_items[MONSTERS][num_of_option]}')

    

    
    # print()
    # print('{0:<0}{2:^100}{1:>0}'.format('<-a','d->',duel_structure[MENU_COMPONENTS][num_of_option]))
    # print()
    # print('{:^.centre}'.format(duel_stracture))
    # print(duel_stracture)



print_menu(duel_stracture())