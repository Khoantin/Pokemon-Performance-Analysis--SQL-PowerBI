CREATE TABLE `poke_table` (
    `Id` INT PRIMARY KEY,
    `Name` VARCHAR(100) NOT NULL,
    `Type1` VARCHAR(50) NOT NULL,
    `Type2` VARCHAR(50),
    `Weight` DECIMAL(8,2),        -- allows weights like 999999.99
    `Height` DECIMAL(6,2),        -- allows heights like 9999.99
    `Hp` INT,
    `Attack` INT,
    `Defense` INT,
    `Sp.Attack` INT,
    `Sp.Defense` INT,
    `Speed` INT,
    `Hidden_ability` VARCHAR(100),
    `Generation` INT,
    `Catch_rate` INT,
    `img_url` VARCHAR(255)
);