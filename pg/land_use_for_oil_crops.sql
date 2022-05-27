-- Table: public.land_use_for_oil_crops

-- DROP TABLE IF EXISTS public.land_use_for_oil_crops;

CREATE TABLE IF NOT EXISTS public.land_use_for_oil_crops
(
    "Entity" character varying COLLATE pg_catalog."default",
    "Code" character varying COLLATE pg_catalog."default",
    "Year" bigint,
    "Crops - Olives - 260 - Area harvested - 5312 - ha" character varying COLLATE pg_catalog."default",
    "Crops - Rapeseed - 270 - Area harvested - 5312 - ha" character varying COLLATE pg_catalog."default",
    "Crops - Soybeans - 236 - Area harvested - 5312 - ha" character varying COLLATE pg_catalog."default",
    "Crops - Safflower seed - 280 - Area harvested - 5312 - ha" character varying COLLATE pg_catalog."default",
    "Crops - Sunflower seed - 267 - Area harvested - 5312 - ha" character varying COLLATE pg_catalog."default",
    "Crops - Oil palm fruit - 254 - Area harvested - 5312 - ha" character varying COLLATE pg_catalog."default",
    "Crops - Coconuts - 249 - Area harvested - 5312 - ha" character varying COLLATE pg_catalog."default",
    "Crops - Groundnuts, with shell - 242 - Area harvested - 5312 - " character varying COLLATE pg_catalog."default",
    "Crops - Linseed - 333 - Area harvested - 5312 - ha" character varying COLLATE pg_catalog."default",
    "Crops - Seed cotton - 328 - Area harvested - 5312 - ha" character varying COLLATE pg_catalog."default",
    "Crops - Sesame seed - 289 - Area harvested - 5312 - ha" character varying COLLATE pg_catalog."default",
    "Crops - Castor oil seed - 265 - Area harvested - 5312 - ha" character varying COLLATE pg_catalog."default",
    "Crops - Karite nuts (sheanuts) - 263 - Area harvested - 5312 - " character varying COLLATE pg_catalog."default",
    "Crops - Tung nuts - 275 - Area harvested - 5312 - ha" character varying COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.land_use_for_oil_crops
    OWNER to postgres;