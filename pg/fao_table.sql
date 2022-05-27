-- Table: public.fao_data

-- DROP TABLE IF EXISTS public.fao_data;

CREATE TABLE IF NOT EXISTS public.fao_data
(
    "Domain Code" character varying COLLATE pg_catalog."default",
    "Domain" character varying COLLATE pg_catalog."default",
    "Area Code (FAO)" character varying COLLATE pg_catalog."default",
    "Area" character varying COLLATE pg_catalog."default",
    "Element Code" character varying COLLATE pg_catalog."default",
    "Element" character varying COLLATE pg_catalog."default",
    "Item Code (FAO)" character varying COLLATE pg_catalog."default",
    "Item" character varying COLLATE pg_catalog."default",
    "Year Code" character varying COLLATE pg_catalog."default",
    "Year" character varying COLLATE pg_catalog."default",
    "Unit" character varying COLLATE pg_catalog."default",
    "Value" character varying COLLATE pg_catalog."default",
    "Flag" character varying COLLATE pg_catalog."default",
    "Flag Description" character varying COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.fao_data
    OWNER to mkingston;