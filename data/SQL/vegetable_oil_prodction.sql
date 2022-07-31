CREATE TABLE IF NOT EXISTS public.vegetable_oil_production
(
    domain_code character varying COLLATE pg_catalog."default",
    domain character varying COLLATE pg_catalog."default",
    area_code character varying COLLATE pg_catalog."default",
    area character varying COLLATE pg_catalog."default",
    element_code character varying COLLATE pg_catalog."default",
    element character varying COLLATE pg_catalog."default",
    item_code character varying COLLATE pg_catalog."default",
    item character varying COLLATE pg_catalog."default",
    year character varying COLLATE pg_catalog."default",
    unit character varying COLLATE pg_catalog."default",
    value character varying COLLATE pg_catalog."default",
    flag character varying COLLATE pg_catalog."default",
    flag_description character varying COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.vegetable_oil_production
    OWNER to postgres;