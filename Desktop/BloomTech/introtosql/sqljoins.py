'''sql intro relating to JOINS'''

#The full syntax to specify an inner join is:

SELECT character_creator_character.name, character_creator_inventory.id
FROM character_creator_character
INNER JOIN character_creator_character ON 
character_creator_character_id = characterreator_character_inventory.charactor.id;

#The query can be made easier by using table aliases and replacing
#  explicit join with an implicit inner join using a where clause:

SELECT character.name, inventory.id
FROM charactorcreator_character AS character,
charactercreator_character_inventory AS inventory 
WHERE character.charecter_id = inventory.character_id;

#returning 898 rows for the included rpg_db.sqlite3 data in this module
#lets load the first 10 rows of data

SELECT character.name, inventory.id
FROM charactorcreator_character AS character,
charactercreator_character_inventory AS inventory 
where character.charecter_id = inventory.character_id
LIMIT 10;

#This will show Character names and all their unique inventory id values 
# - each of these then corresponds to an actual item, but the 
# details of that lives in another table. Fortunately, we can
# get it by just growing our join:

SELECT character.name, item.name
FROM charactercreator_character AS character,
charactercreator_character_inventory AS inventory,
armory_item AS item
WHERE character.character_id = inventory.character_id
AND inventory.item_id = item.item_id
LIMIT 10;

# We’ve successfully joined across three tables, connecting characters to the items they own.

