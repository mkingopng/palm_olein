-- Table: public.land-use-for-vegetable-oil-crops

-- DROP TABLE IF EXISTS public."land-use-for-vegetable-oil-crops";

CREATE TABLE IF NOT EXISTS public."land-use-for-vegetable-oil-crops"
(
    "Entity" character varying COLLATE pg_catalog."default" NOT NULL,
    "Code" character varying COLLATE pg_catalog."default" NOT NULL,
    year date NOT NULL,
    "Crops - Olives - 260 - Area harvested - 5312 - ha" bigint,
    "Crops - Rapeseed - 270 - Area harvested - 5312 - ha" bigint,
    "Crops - Soybeans - 236 - Area harvested - 5312 - ha" bigint,
    "Crops - Safflower seed - 280 - Area harvested - 5312 - ha" bigint,
    "Crops - Sunflower seed - 267 - Area harvested - 5312 - ha" bigint,
    "Crops - Oil palm fruit - 254 - Area harvested - 5312 - ha" bigint,
    "Crops - Coconuts - 249 - Area harvested - 5312 - ha" bigint,
    "Crops - Groundnuts, with shell - 242 - Area harvested - 5312 - " bigint,
    "Crops - Linseed - 333 - Area harvested - 5312 - ha" bigint,
    "Crops - Seed cotton - 328 - Area harvested - 5312 - ha" bigint,
    "Crops - Sesame seed - 289 - Area harvested - 5312 - ha" bigint,
    "Crops - Castor oil seed - 265 - Area harvested - 5312 - ha" bigint,
    "Crops - Karite nuts (sheanuts) - 263 - Area harvested - 5312 - " bigint,
    "Crops - Tung nuts - 275 - Area harvested - 5312 - ha" bigint
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."land-use-for-vegetable-oil-crops"
    OWNER to mkingston;