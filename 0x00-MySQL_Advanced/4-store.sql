CREATE TRIGGER decrease_quantity
BEFORE INSERT ON orders
FOR EACH Row
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;