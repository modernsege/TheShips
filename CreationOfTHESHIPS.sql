create database TheShips;
use TheShips;
create table Abilities (ID int auto_increment, Ability_Name char(50), Description varchar(1000), Type enum('Active', 'Passive'), Cooldown int unsigned, primary key(ID));
create table AbilitiesOfFractions (ID int auto_increment, Fraction_ID int, Ability_ID int, primary key(ID));
create table Effects (ID int auto_increment, Effect char(100), Arguments_Format char(50), Description varchar(1000), primary key(ID));
create table EffectsOfItems (ID int auto_increment, Item_ID int, Effect_ID int, Arguments char(50), primary key(ID));
create table Fractions (ID int auto_increment, Fraction_Name char(50), Description varchar(1000), Gold int, primary key(ID));
create table Items (ID int auto_increment, Item_Name char(50), Description varchar(1000), Price int, Quantity int, Price_Rise_Multiplier double precision(10,4), Price_Rise int, Available boolean, primary key(ID));
create table Profiles (ID int auto_increment, Nickname char(50), Wins int, Defeats int, Login char(30), Encrypted_Password varchar(500), Email char(100), Status enum('Active', 'Inactive', 'Suspended' ,'Banned'), primary key(ID));

create or replace view AbilitiesOfFractionsView as select aof.Fraction_Name, a.Ability_Name, a.Type, a.Description, a.Cooldown, aof.Fraction_ID, aof.Ability_ID from (select f.Fraction_Name, af.Fraction_ID, af.Ability_ID from Fractions f inner join AbilitiesOfFractions af on f.ID = af.Fraction_ID) aof inner join Abilities a on aof.Ability_ID = a.ID;
create or replace view ItemsAndEffectsView as select eoi.Item_Name, e.Effect, eoi.Item_ID, eoi.Effect_ID, eoi.Arguments, e.Arguments_Format from (select i.Item_Name, ei.Item_ID, ei.Effect_ID, ei.Arguments from Items i inner join EffectsOfItems ei on i.ID = ei.Item_ID) eoi inner join Effects e on eoi.Effect_ID = e.ID;

create user 'admin'@'localhost' identified by 'admin';
grant all privileges on theships.* to 'admin'@'localhost';

create user 'guest'@'localhost' identified by 'guest';
grant usage on theships.* to 'guest'@'localhost';


DELIMITER //

create trigger delete_ability
after delete on abilities
for each row
begin
	delete from abilitiesoffractions where ability_ID = old.id;	
end //

create trigger delete_fractions
after delete on fractions
for each row
begin
	delete from abilitiesoffractions where fraction_ID = old.id;	
end //

# test
# git test 2

create trigger delete_effects
after delete on effects
for each row
begin
	delete from effectsofitems where Effect_ID = old.id;
end//

create trigger delete_item
after delete on items
for each row
begin
	delete from effectsofitems where Item_ID = old.id;	
end //

DELIMITER ;



DELIMITER $$
CREATE PROCEDURE update_price_by_inflation (IN inflation integer, IN name_of_item varchar(64))
BEGIN
UPDATE items
set Price = Price * (inflation*0.01 + 1) 
WHERE item_name = name_of_item;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE update_price_by_adding (IN new_price integer, IN name_of_item varchar(64))
BEGIN
UPDATE items
set Price = Price + new_price
WHERE item_name = name_of_item;
END $$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE match_ended (IN winner integer, IN loser integer)
BEGIN
start transaction;
UPDATE profiles
set Wins = Wins + 1
WHERE ID = winner;
UPDATE profiles
set Defeats = Defeats + 1
WHERE ID = loser;
commit;
END $$
DELIMITER ;


create or replace view NamesAndDescriptionsFractionAndAbilities as select fraction_name as name, description from fractions union select ability_name as name, description from abilities;
create or replace view NamesAndDescriptionsItemsAndEffects as  select item_name as name, description from items union select effect as name, description from effects;
create or replace view NamesAndDescriptions as  select name, description from NamesAndDescriptionsFractionAndAbilities union select name, description from NamesAndDescriptionsItemsAndEffects;



