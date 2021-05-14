create database TheShips;
use TheShips;
create table Abilities (ID int auto_increment, Ability_Name char(50), Description varchar(1000), Type enum('Active', 'Passive'), Cooldown int unsigned, primary key(ID));
create table AbilitiesOfFractions (ID int auto_increment, Fraction_ID int, Ability_ID int, primary key(ID));
create table Effects (ID int auto_increment, Effect char(100), Arguments_Format char(50), Description varchar(1000), primary key(ID));
create table EffectsOfItems (ID int auto_increment, Item_ID int, Effect_ID int, Arguments char(50), primary key(ID));
create table Fractions (ID int auto_increment, Fraction_Name char(50), Description varchar(1000), Gold int, primary key(ID));
create table Items (ID int auto_increment, Item_Name char(50), Description varchar(1000), Price int, Quantity int, Price_Rise_Multiplier double precision(10,4), Price_Rise int, Available boolean, primary key(ID));
create table Profiles (ID int auto_increment, Nickname char(50), Wins int, Defeats int, Login char(30), Encrypted_Password varchar(500), Email char(100), primary key(ID));

create or replace view AbilitiesOfFractionsView as select aof.Fraction_Name, a.Ability_Name, a.Type, a.Description, a.Cooldown, aof.Fraction_ID, aof.Ability_ID from (select f.Fraction_Name, af.Fraction_ID, af.Ability_ID from Fractions f inner join AbilitiesOfFractions af on f.ID = af.Fraction_ID) aof inner join Abilities a on aof.Ability_ID = a.ID;
create or replace view ItemsAndEffectsView as select eoi.Item_Name, e.Effect, eoi.Item_ID, eoi.Effect_ID, eoi.Arguments, e.Arguments_Format from (select i.Item_Name, ei.Item_ID, ei.Effect_ID, ei.Arguments from Items i inner join EffectsOfItems ei on i.ID = ei.Item_ID) eoi inner join Effects e on eoi.Effect_ID = e.ID;

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

DELIMITER ;
