from raw_crud import insert_record, connection_to_server

conn = connection_to_server() #Default localhost i połączenie z bazą TheShips

#Abilities table
insert_record(conn, 'abilities', "1, 'Quartermaster', 'Reduce items cooldown by 2.', 'Active', 5")
insert_record(conn, 'abilities', "2, 'The Dank Engine', 'Transport your chosen ship to other (chosen and available) location', 'Active', 5")
insert_record(conn, 'abilities', "3, 'Berserk', 'Grant your ships additional round of firing.', 'Active', 15")
insert_record(conn, 'abilities', '4, "Piercing Shot", "Fire enormous cannonball that destroy 50% of map\'s width in 1 row.", "Active", 15')
insert_record(conn, 'abilities', "5, 'The Grand Master of Shopping', 'You can buy more items in shop (3x) and the items bought in shop are replanished in every 40 rounds (during battle).', 'Passive', 0")
insert_record(conn, 'abilities', "6, 'Boarder King', 'Your boarder expands by 1 in X and 1 in Y in every ((X+Y)/2(+2*round)) rounds.', 'Passive', 0")
insert_record(conn, 'abilities', "7, 'Viking Rage', 'You can shoot again (max 3 times) if you hit an enemy ship.', 'Passive', 0")
insert_record(conn, 'abilities', "8, 'BOOM', 'If you hit an enemy ship you destroy additional part of the ship.', 'Passive', 0")

#AbilitiesOfFractions table
insert_record(conn, 'AbilitiesOfFractions', "1, 1, 1")
insert_record(conn, 'AbilitiesOfFractions', "2, 1, 5")
insert_record(conn, 'AbilitiesOfFractions', "3, 2, 2")
insert_record(conn, 'AbilitiesOfFractions', "4, 2, 6")
insert_record(conn, 'AbilitiesOfFractions', "5, 3, 3")
insert_record(conn, 'AbilitiesOfFractions', "6, 3, 7")
insert_record(conn, 'AbilitiesOfFractions', "7, 4, 4")
insert_record(conn, 'AbilitiesOfFractions', "8, 4, 8")

#EffectsOfItems table
insert_record(conn, 'EffectsOfItems', "1, 7, 3, '(1)'")
insert_record(conn, 'EffectsOfItems', "2, 2, 2, '(3)'")
insert_record(conn, 'EffectsOfItems', "3, 3, 2, '(4)'")
insert_record(conn, 'EffectsOfItems', "4, 4, 1, '(10,5,5)'")
insert_record(conn, 'EffectsOfItems', "5, 5, 4, '(1)'")
insert_record(conn, 'EffectsOfItems', "6, 6, 3, '(1)'")
insert_record(conn, 'EffectsOfItems', "7, 7, 5, '-'")
insert_record(conn, 'EffectsOfItems', "8, 7, 6, '-'")
insert_record(conn, 'EffectsOfItems', "9, 1, 2, '(2)'")
insert_record(conn, 'EffectsOfItems', "10, 7, 2, '(1)'")

#Items table
insert_record(conn, 'Items', "1, 'Small Bomb', 'Explodes in a small area', 100, 3, 1, 0, true")
insert_record(conn, 'Items', "2, 'Medium Bomb', 'Explodes in a medium area', 200, 2, 1, 0, true")
insert_record(conn, 'Items', "3, 'BIG Bomb', 'Explodes in a BIG area', 300, 1, 1, 0, true")
insert_record(conn, 'Items', "4, 'Shrapnel', 'Shots Z random missiles in the area X*Y', 250, 2, 1, 0, true")
insert_record(conn, 'Items', "5, 'Map Extension X', 'Extends your map by 1 X', 200, 1, 1.2, 0, true")
insert_record(conn, 'Items', "6, 'Map Extension Y', 'Extends your map by 1 Y', 200, 1, 1.2, 0, true")
insert_record(conn, 'Items', "7, 'Sample item 1', 'Sample', 400, 0, 1, 0, true")


#effects table
insert_record(conn, 'effects', '1,"Shoot_var_times_randomly_in_YX_area", "(var, Y, X)", "Shoot [var] times randomly in [Y]x[X] area."')
insert_record(conn, 'effects', '2,"Destroy_in_var_radious", "(var)", "Destroy area in [var] radious."')
insert_record(conn, 'effects', '3,"Increase_friendly_Y_by_var", "(var)", "Extend your map in Y direction by [var]."')
insert_record(conn, 'effects', '4,"Increase_friendly_X_by_var", "(var)", "Extend your map in X direction by [var]."')
insert_record(conn, 'effects', '5,"Sample_effect_1", "", ""')
insert_record(conn, 'effects', '6,"Sample_effect_2", "", ""')

#fractions table
insert_record(conn, 'fractions', '1,"Merchant Federation", "Fraction focused on earnig as much money as it is possible. Good in shopping.", 700')
insert_record(conn, 'fractions', '3,"Vikings", "They can throw their axes faster than sth very fast. U blink u miss it.", 100')
insert_record(conn, 'fractions', '2,"Transport Guild", "Has the fastest ships all over the world. It is able to change their position even in the fires of battle.", 300')
insert_record(conn, 'fractions', '4,"Pirates", "Their cannon shots are more paiful than stepping on the lego with your bare foot.", 200')

#profiles table
insert_record(conn, 'profiles', '1,"Admin", 99999, 0,"admin","jhk2e89sdn10sd5sudas89d82d988sd98sd98209","admino911@gmail.com"')
insert_record(conn, 'profiles', '2,"Casual", 0, 99999,"ordinarycasual07","asmd8a7sd87a89sd7s5d65saf6hg7hs","anonymouse420@gmail.com"')
insert_record(conn, 'profiles', '3,"[EoC]tomek123", 5, 2,"tomq777","asd78sag78hjgcvbn789vc8cx5692jfi","tomeeeeeq172@vp.pl"')
insert_record(conn, 'profiles', '4,"adam2008pl", 2, 5,"adamo123","fggerhgtew43rt2rg112!@#","adamo123@gmail.com"')
